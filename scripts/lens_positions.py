"""Per-layer, per-token J-lens ranks of each item's hidden steps and answer, for layer x position heatmaps.

lens_readout.py reads the lens only at the token before the answer. This reads it at the last
POSITIONS_KEPT tokens of the prompt too, because a hidden step may be computed where its inputs sit
(e.g. "spider" at the "webs" token) rather than at the end. For each tracked word it stores the
vocabulary rank (0 = the lens's top token) of its best single-token spelling at every (layer, position),
plus the lens's own top token there. Ranks are computed on the GPU; full-vocab logits never leave it.

Items need name, prompt, target, intermediates, and optionally start and depth (lens-eval-multihop.json,
or make_ncri_tasks.py output). Needs a GPU; run each dataset with the same model in one go:

    uv sync --group pod
    OMP_NUM_THREADS=8 uv run python scripts/lens_positions.py Qwen/Qwen3.6-27B neuronpedia/jacobian-lens \
        qwen3.6-27b/jlens/Salesforce-wikitext/Qwen3.6-27B_jacobian_lens_n1000.pt \
        data/lens-eval-multihop.json data/brew.json data/chain9.json
"""

import json
import sys
from pathlib import Path

import jlens
import torch
import transformers
from jlens.hooks import ActivationRecorder

POSITIONS_KEPT = 48

model_name, lens_repo, lens_file, *dataset_paths = sys.argv[1:]
tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
device = "cuda" if torch.cuda.is_available() else "cpu"
hf_model = transformers.AutoModelForCausalLM.from_pretrained(model_name, dtype=torch.bfloat16).to(device)
model = jlens.from_hf(hf_model, tokenizer)
lens = jlens.JacobianLens.from_pretrained(lens_repo, filename=lens_file)
layers = lens.source_layers
jacobians = {layer: lens.jacobians[layer].to(device) for layer in layers}


def single_token_ids(word: str) -> list[int]:
    """Ids of the single-token spellings of `word`. The lens can only show a word that is one token."""
    spellings = {word, " " + word, word.capitalize(), " " + word.capitalize()}
    encodings = [tokenizer.encode(spelling, add_special_tokens=False) for spelling in spellings]
    return [ids[0] for ids in encodings if len(ids) == 1]


def tracked_words(item: dict) -> dict[str, str]:
    """word -> role, in reading order: start state, each hidden step, answer."""
    target = item["target"].strip()
    roles = {item["start"]: "start"} if "start" in item else {}
    for index, word in enumerate(item["intermediates"]):
        roles[word] = f"step {index + 1}" if "start" in item else "intermediate"
    roles[target] = "answer"
    return roles


@torch.no_grad()
def read_item(item: dict) -> dict:
    input_ids = model.encode(item["prompt"] + item["target"])
    offsets = tokenizer(item["prompt"] + item["target"], add_special_tokens=False, return_offsets_mapping=True)["offset_mapping"]
    target_tokens = len(offsets) - next(index for index, (_, end) in enumerate(offsets) if end > len(item["prompt"]))
    read_position = input_ids.shape[1] - target_tokens - 1
    positions = list(range(max(0, read_position - POSITIONS_KEPT + 1), read_position + 1))

    final_layer = model.n_layers - 1
    with ActivationRecorder(model.layers, at=sorted({*layers, final_layer})) as recorder:
        model.forward(input_ids)
    model_logits = model.unembed(recorder.activations[final_layer][0, read_position].float()).float()

    words = {word: {"role": role, "ids": single_token_ids(word), "rank": []} for word, role in tracked_words(item).items()}
    top1 = []
    for layer in layers:
        residual = recorder.activations[layer][0, positions].float() @ jacobians[layer].T
        logits = model.unembed(residual).float()  # [positions, vocab]
        top1.append([tokenizer.decode(token_id) for token_id in logits.argmax(-1)])
        for series in words.values():
            if series["ids"]:
                word_logit = logits[:, series["ids"]].max(-1).values
                series["rank"].append((logits > word_logit[:, None]).sum(-1).tolist())

    return {
        **{key: item[key] for key in ("name", "prompt", "target", "intermediates", "start", "depth") if key in item},
        "tokens": [tokenizer.decode(input_ids[0, position]) for position in positions],
        "model_top5": [tokenizer.decode(token_id) for token_id in model_logits.topk(5).indices],
        "words": {word: {"role": series["role"], "rank": series["rank"]} for word, series in words.items() if series["ids"]},
        "lens_top1": top1,
    }


for dataset_path in dataset_paths:
    readouts = []
    for item in json.loads(Path(dataset_path).read_text())["items"]:
        readouts.append(read_item(item))
        verdict = "ok " if readouts[-1]["model_top5"][0].strip() == item["target"].strip() else "BAD"
        print(f"{verdict} {item['name']:32} model says {readouts[-1]['model_top5'][:3]}", flush=True)
    output_path = Path("data/positions") / f"{model_name.split('/')[-1].lower()}" / f"{Path(dataset_path).stem}.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps({"model": model_name, "lens": f"{lens_repo}/{lens_file}", "layers": layers, "items": readouts}))
    print(f"wrote {output_path}", flush=True)
