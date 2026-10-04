"""Small derived data files for the blog post's Altair charts (the post's chart scripts read only these).

Writes to <out_dir>:
- brew_accuracy.json: no-CoT brew accuracy by number of stirs per OpenRouter model (data/no_cot_brew.json),
  dropping models that reasoned silently on most items.
- heatmap_mean.json: over the two-stir brew items Gemma-4-31B-it gets right, the median rank among the
  10 colours of the start colour, the colour after stir 1 and the answer, at every layer and every token
  of the items' last two lines (they share one template, so positions line up).
The stir-state medians come from plot_stir_states.py (graphs/brew_stir_states.json).

    uv run python scripts/export_blog_data.py ~/repos/personal-website/posts/jlens-multistep/charts/data
"""

import gzip
import json
import re
import shutil
import statistics
import sys
from pathlib import Path

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
two_stir = [item for item in readout["items"] if item["depth"] == 2 and item["model_top5"][0].strip() == item["target"].strip()]
# Each item's last two lines share one template, so token positions line up across items.
tails = []
for item in two_stir:
    first = next(index for index in range(len(item["tokens"])) if "".join(item["tokens"][index:]).startswith("The potion starts"))
    tails.append((item, first))
assert len({len(item["tokens"]) - first for item, first in tails}) == 1, "templates do not line up"
template, template_first = tails[0]
stirs = re.search(r"one at a time: (\w+), then (\w+)\.", "".join(template["tokens"]))
assert stirs
slots = {template["start"]: "‹start›", stirs.group(1): "‹stir 1›", stirs.group(2): "‹stir 2›"}
tokens = [slots.get(token.strip(), token.strip()) for token in template["tokens"][template_first:]]
roles = {
    "start": lambda item: item["start"],
    "after stir 1": lambda item: item["intermediates"][0],
    "answer": lambda item: item["target"].strip(),
}
heatmap = {
    "model": readout["model"],
    "n_items": len(tails),
    "layers": readout["layers"],
    "tokens": tokens,
    "rank": {
        role: [
            [
                statistics.median(item["words"][pick(item)]["alphabet_rank"][layer][first + offset] + 1 for item, first in tails)
                for offset in range(len(tokens))
            ]
            for layer in range(len(readout["layers"]))
        ]
        for role, pick in roles.items()
    },
}
(out_dir / "heatmap_mean.json").write_text(json.dumps(heatmap))
shutil.copy("graphs/brew_stir_states.json", out_dir / "stir_states.json")
print(f"wrote brew_accuracy.json, heatmap_mean.json, stir_states.json to {out_dir}")
