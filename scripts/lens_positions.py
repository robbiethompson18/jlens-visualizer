"""Per-layer, per-token J-lens ranks of each item's hidden steps and answer, for layer x position heatmaps.

lens_readout.py reads the lens only at the token before the answer. This reads it at every token of
the item's own problem too (everything after the last blank line, so a 1-shot example is skipped),
because a hidden step may be computed where its inputs sit (e.g. "spider" at the "webs" token) rather
than at the end. For each tracked word it stores, at every (layer, position), the vocabulary rank
(0 = the lens's top token, capped at RANK_CAP) of its best single-token spelling, and, when the dataset
has an answer `alphabet`, its rank among those candidates only (0 = the lens prefers it over every other
colour / digit). Full-vocab rank cannot separate digits: wherever a number is due, all of them rank high.
Ranks are computed on the GPU; full-vocab logits never leave it. Output is gzipped JSON.

Items need name, prompt, target, intermediates, and optionally start, depth and lookups
(lens-eval-multihop.json, or make_ncri_tasks.py output). Needs a GPU; run each dataset in one go:

    uv sync --group pod
    OMP_NUM_THREADS=8 uv run python scripts/lens_positions.py Qwen/Qwen3.6-27B neuronpedia/jacobian-lens \
        qwen3.6-27b/jlens/Salesforce-wikitext/Qwen3.6-27B_jacobian_lens_n1000.pt \
        data/lens-eval-multihop.json data/brew.json data/chain9.json
"""

import gzip
import json
import sys
from pathlib import Path

import jlens
import torch
import transformers
from jlens.hooks import ActivationRecorder

RANK_CAP = 10_000  # plots treat everything past 10^4 as "not there"; capping keeps the files small

model_name, lens_repo, lens_file, *dataset_paths = sys.argv[1:]
tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
device = "cuda" if torch.cuda.is_available() else "cpu"


def load_model() -> torch.nn.Module:
    """Text-only class first; multimodal checkpoints it can't map fully (Gemma 4) load as image-text-to-text."""
    try:
        hf_model, info = transformers.AutoModelForCausalLM.from_pretrained(model_name, dtype=torch.bfloat16, output_loading_info=True)
        if not info["missing_keys"]:
            return hf_model
        print(f"AutoModelForCausalLM left {len(info['missing_keys'])} weights unloaded; retrying as image-text-to-text", flush=True)
    except ValueError as error:
        print(f"AutoModelForCausalLM failed ({error}); retrying as image-text-to-text", flush=True)
    return transformers.AutoModelForImageTextToText.from_pretrained(model_name, dtype=torch.bfloat16)


hf_model = load_model().to(device)
model = jlens.from_hf(hf_model, tokenizer)
lens = jlens.JacobianLens.from_pretrained(lens_repo, filename=lens_file)
layers = lens.source_layers
jacobians = {layer: lens.jacobians[layer].to(device) for layer in layers}


def single_token_ids(word: str) -> list[int]:
    """Ids of the single-token spellings of `word`. The lens can only show a word that is one token."""
    spellings = {word, " " + word, word.capitalize(), " " + word.capitalize()}
    encodings = [tokenizer.encode(spelling, add_special_tokens=False) for spelling in spellings]
    return [ids[0] for ids in encodings if len(ids) == 1]


def alphabet_ids(alphabet: list[str]) -> list[list[int]]:
    return [single_token_ids(word) for word in alphabet]


def tracked_words(item: dict) -> dict[str, str]:
    """word -> role, in reading order: start state, each hidden step, answer."""
    target = item["target"].strip()
    roles = {item["start"]: "start"} if "start" in item else {}
    for index, word in enumerate(item["intermediates"]):
        roles[word] = f"step {index + 1}" if "start" in item else "intermediate"
    roles[target] = "answer"
    return roles


@torch.no_grad()
def read_item(item: dict, alphabet: list[list[int]]) -> dict:
    text = item["prompt"] + item["target"]
    input_ids = model.encode(text)
    offsets = tokenizer(text, add_special_tokens=False, return_offsets_mapping=True)["offset_mapping"]
    special_tokens = input_ids.shape[1] - len(offsets)  # a BOS the model's encode() may prepend
    target_tokens = len(offsets) - next(index for index, (_, end) in enumerate(offsets) if end > len(item["prompt"]))
    read_position = input_ids.shape[1] - target_tokens - 1
    problem_start = item["prompt"].rfind("\n\n") + 2 if "\n\n" in item["prompt"] else 0
    first_position = special_tokens + next(index for index, (start, _) in enumerate(offsets) if start >= problem_start)
    positions = list(range(first_position, read_position + 1))

    final_layer = model.n_layers - 1
    with ActivationRecorder(model.layers, at=sorted({*layers, final_layer})) as recorder:
        model.forward(input_ids)
    model_logits = model.unembed(recorder.activations[final_layer][0, read_position].float()).float()

    words = {
        word: {"role": role, "ids": single_token_ids(word), "rank": [], "alphabet_rank": []} for word, role in tracked_words(item).items()
    }
    for layer in layers:
        residual = recorder.activations[layer][0, positions].float() @ jacobians[layer].T
        logits = model.unembed(residual).float()  # [positions, vocab]
        if alphabet:
            alphabet_logits = torch.stack([logits[:, ids].max(-1).values for ids in alphabet], dim=-1)  # [positions, alphabet]
        for series in words.values():
            if series["ids"]:
                word_logit = logits[:, series["ids"]].max(-1).values
                series["rank"].append((logits > word_logit[:, None]).sum(-1).clamp(max=RANK_CAP).tolist())
                if alphabet:
                    series["alphabet_rank"].append((alphabet_logits > word_logit[:, None]).sum(-1).tolist())

    return {
        **{key: item[key] for key in ("name", "prompt", "target", "intermediates", "start", "depth", "lookups") if key in item},
        "tokens": [tokenizer.decode(input_ids[0, position]) for position in positions],
        "model_top5": [tokenizer.decode(token_id) for token_id in model_logits.topk(5).indices],
        "words": {
            word: {key: series[key] for key in ("role", "rank", "alphabet_rank") if series[key] or key == "role"}
            for word, series in words.items()
            if series["ids"]
        },
    }


for dataset_path in dataset_paths:
    dataset = json.loads(Path(dataset_path).read_text())
    alphabet = alphabet_ids(dataset.get("alphabet", []))
    readouts = []
    for item in dataset["items"]:
        readouts.append(read_item(item, alphabet))
        verdict = "ok " if readouts[-1]["model_top5"][0].strip() == item["target"].strip() else "BAD"
        print(f"{verdict} {item['name']:32} model says {readouts[-1]['model_top5'][:3]}", flush=True)
    output_path = Path("data/positions") / f"{model_name.split('/')[-1].lower()}" / f"{Path(dataset_path).stem}.json.gz"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    lens_name = f"{lens_repo}/{lens_file}"
    readout = {"model": model_name, "lens": lens_name, "layers": layers, "alphabet": dataset.get("alphabet"), "items": readouts}
    output_path.write_bytes(gzip.compress(json.dumps(readout).encode()))
    print(f"wrote {output_path}", flush=True)
