"""Small derived data files for the blog post's Altair charts (the post's chart scripts read only these).

Writes to <out_dir>:
- brew_accuracy.json: no-CoT brew accuracy by number of stirs per OpenRouter model (data/no_cot_brew.json),
  dropping models that reasoned silently on most items.
- heatmap_item.json: one Gemma-4-31B-it brew item's rank among the 10 colours at every layer and every
  token of its last two lines, for the start colour, the colour after stir 1 and the answer.
The stir-state medians come from plot_stir_states.py (graphs/brew_stir_states.json).

    uv run python scripts/export_blog_data.py ~/repos/personal-website/posts/jlens-multistep/charts/data
"""

import gzip
import json
import shutil
import sys
from pathlib import Path

HEATMAP_ITEM = "brew-d2-03"  # the clearest of Gemma's 16 correct two-stir items (see the post)

out_dir = Path(sys.argv[1])
out_dir.mkdir(parents=True, exist_ok=True)

items = {item["name"]: item for item in json.loads(Path("data/brew.json").read_text())["items"]}
no_cot = json.loads(Path("data/no_cot_brew.json").read_text())
accuracy = []
for model, responses in no_cot.items():
    if sum(response.get("reasoned", False) for response in responses.values()) > len(responses) / 2:
        continue
    for depth in sorted({item["depth"] for item in items.values()}):
        names = [name for name, item in items.items() if item["depth"] == depth]
        answers = [responses[name]["answer"].split("Answer:")[-1].strip(" \"'.*").lower() for name in names]
        correct = sum(answer.startswith(items[name]["target"].strip()) for answer, name in zip(answers, names))
        accuracy.append({"model": model.split("/")[-1], "stirs": depth, "correct": correct, "n": len(names)})
(out_dir / "brew_accuracy.json").write_text(json.dumps(accuracy, indent=1))

readout = json.loads(gzip.decompress(Path("data/positions/gemma-4-31b-it/brew.json.gz").read_bytes()))
item = next(item for item in readout["items"] if item["name"] == HEATMAP_ITEM)
first = next(index for index in range(len(item["tokens"])) if "".join(item["tokens"][index:]).startswith("The potion starts"))
heatmap = {
    "model": readout["model"],
    "layers": readout["layers"],
    "tokens": item["tokens"][first:],
    "trajectory": [item["start"], *item["intermediates"], item["target"].strip()],
    "rank": {
        word: [layer_ranks[first:] for layer_ranks in item["words"][word]["alphabet_rank"]]
        for word in [item["start"], *item["intermediates"], item["target"].strip()]
    },
}
(out_dir / "heatmap_item.json").write_text(json.dumps(heatmap))
shutil.copy("graphs/brew_stir_states.json", out_dir / "stir_states.json")
print(f"wrote brew_accuracy.json, heatmap_item.json, stir_states.json to {out_dir}")
