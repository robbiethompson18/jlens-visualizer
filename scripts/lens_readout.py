"""Per-layer J-lens readouts for every multi-hop item, saved as JSON for plot_readout.py.

For each item, runs one forward pass and reads the lens at the token just before the answer
(the same position the paper's multihop eval uses). Records, per layer, the logit / log-prob /
rank of the answer, the hidden intermediates, and every word of the prompt, for both the J-lens
and the plain logit lens.

Needs a GPU with ~20 GB for a 7B model:

    uv sync --group pod
    uv run python scripts/lens_readout.py Qwen/Qwen2.5-7B-Instruct \
        anicka/jlens-qwen2.5-7b-instruct qwen2.5-7b-instruct_jlens.pt

On a shared cloud GPU host set OMP_NUM_THREADS=8: torch otherwise spawns a CPU thread per host core
and the per-word log-softmax bookkeeping below crawls (Qwen3.6-27B: stalled for 5+ min vs ~2 min total).
"""

import json
import re
import sys
from pathlib import Path

import jlens
import torch
import transformers

model_name, lens_repo, lens_file = sys.argv[1:4]

tokenizer = transformers.AutoTokenizer.from_pretrained(model_name)
device = "cuda" if torch.cuda.is_available() else "cpu"
hf_model = transformers.AutoModelForCausalLM.from_pretrained(model_name, dtype=torch.bfloat16).to(device)
model = jlens.from_hf(hf_model, tokenizer)
lens = jlens.JacobianLens.from_pretrained(lens_repo, filename=lens_file)
layers = lens.source_layers


def single_token_ids(word: str) -> list[int]:
    """Ids of the single-token spellings of `word`. The lens can only show a word that is one token."""
    spellings = {word, " " + word, word.capitalize(), " " + word.capitalize()}
    encodings = [tokenizer.encode(spelling, add_special_tokens=False) for spelling in spellings]
    return [ids[0] for ids in encodings if len(ids) == 1]


def tokens_from_target(prompt: str, target: str) -> int:
    """How many trailing tokens of prompt+target belong to the target."""
    offsets = tokenizer(prompt + target, add_special_tokens=False, return_offsets_mapping=True)["offset_mapping"]
    target_start = next(index for index, (_, end) in enumerate(offsets) if end > len(prompt))
    return len(offsets) - target_start


def track(logits_by_layer: dict[int, torch.Tensor], token_ids: list[int]) -> dict[str, list[float]]:
    """Best spelling per layer: highest logit, and its log-prob and rank (0 = top)."""
    logit, logprob, rank = [], [], []
    for layer in layers:
        layer_logits = logits_by_layer[layer][0]
        best = max(token_ids, key=lambda token_id: layer_logits[token_id].item())
        logit.append(layer_logits[best].item())
        logprob.append(torch.log_softmax(layer_logits, dim=-1)[best].item())
        rank.append(int((layer_logits > layer_logits[best]).sum()))
    return {"logit": logit, "logprob": logprob, "rank": rank}


items = json.loads(Path("data/lens-eval-multihop.json").read_text())["items"]
readouts = []
for item in items:
    prompt, target = item["prompt"], item["target"]
    # The model is causal, so the appended target cannot affect the position before it.
    position = -tokens_from_target(prompt, target) - 1
    jacobian_logits, model_logits, input_ids = lens.apply(model, prompt + target, positions=[position])
    plain_logits, _, _ = lens.apply(model, prompt + target, positions=[position], use_jacobian=False)

    prompt_words = sorted({word.lower() for word in re.findall(r"[A-Za-z]{3,}", prompt)} - {"fact"})
    words = {"target": [target], "intermediate": item["intermediates"], "prompt": prompt_words}
    tracked = {}
    for role, role_words in words.items():
        for word in role_words:
            token_ids = single_token_ids(word)
            if token_ids and word not in tracked:
                tracked[word] = {
                    "role": role,
                    "jlens": track(jacobian_logits, token_ids),
                    "logit_lens": track(plain_logits, token_ids),
                }

    readouts.append(
        {
            "name": item["name"],
            "prompt": prompt,
            "target": target,
            "readout_token": tokenizer.decode(input_ids[0, position]),
            "model_top5": [tokenizer.decode(token_id) for token_id in model_logits[0].topk(5).indices],
            "jlens_top5_by_layer": [[tokenizer.decode(t) for t in jacobian_logits[layer][0].topk(5).indices] for layer in layers],
            "words": tracked,
        }
    )
    print(f"{item['name']:32} reads at {readouts[-1]['readout_token']!r:8} model says {readouts[-1]['model_top5'][:3]}", flush=True)

output_path = Path("data/readouts") / f"{model_name.split('/')[-1].lower()}.json"
output_path.parent.mkdir(exist_ok=True)
output_path.write_text(json.dumps({"model": model_name, "lens": f"{lens_repo}/{lens_file}", "layers": layers, "items": readouts}))
print(f"wrote {output_path}")
