"""Bundle a model's per-item J-lens graphs into one Markdown report that GitHub renders (phone included).

One section per question: the graph, then the full question, the hidden step, what the model
predicted, and which OpenRouter models answer it without chain of thought. Items the model gets
right come first. Run plot_readout.py first; the report links to its PNGs by relative path.

    uv run python scripts/build_report.py data/readouts/qwen2.5-7b-instruct.json
"""

import json
import sys
from pathlib import Path

readout = json.loads(Path(sys.argv[1]).read_text())
no_cot = json.loads(Path("data/no_cot_results.json").read_text())
items = {item["name"]: item for item in json.loads(Path("data/lens-eval-multihop.json").read_text())["items"]}
graph_dir = Path("graphs") / Path(sys.argv[1]).stem
model_label = readout["model"].split("/")[-1]


def is_correct(answer: str, target: str) -> bool:
    """Same rule as check_no_cot.py."""
    return answer.strip(" \"'.").lower().startswith(target.lower())


def mark(correct: bool) -> str:
    return "✅" if correct else "❌"


def percent_row(label: str, correct: int) -> str:
    total = len(readout["items"])
    return f"| {label} | {correct}/{total} | {100 * correct / total:.0f}% |"


def section(readout_item: dict) -> str:
    item = items[readout_item["name"]]
    prediction = readout_item["model_top5"][0].strip()
    top5 = ", ".join(f"`{token.strip()}`" for token in readout_item["model_top5"])
    chain = " → ".join([*item["intermediates"], item["target"]])
    no_cot_lines = "\n".join(
        f"- {mark(is_correct(no_cot[model][item['name']]['answer'], item['target']))} {model.split('/')[-1]}: "
        f"`{no_cot[model][item['name']]['answer'].strip()[:40]}`"
        for model in no_cot
    )
    return f"""---

![J-lens graph for {item["name"]}]({item["name"]}.png)

### {item["prompt"].strip()} **{item["target"]}**

**Hidden reasoning:** {chain}

**{model_label} (this graph):** {mark(is_correct(prediction, item["target"]))} predicts `{prediction}`; top 5: {top5}

<details><summary>No-CoT answers via OpenRouter</summary>

{no_cot_lines}

</details>
"""


graph_correct = [item for item in readout["items"] if is_correct(item["model_top5"][0].strip(), item["target"])]
graph_wrong = [item for item in readout["items"] if item not in graph_correct]
summary_rows = [percent_row(f"{model_label}, raw prompt, local forward pass (the graphs)", len(graph_correct))]
for model in no_cot:
    no_cot_correct = sum(is_correct(no_cot[model][name]["answer"], items[name]["target"]) for name in items)
    summary_rows.append(percent_row(f"{model.split('/')[-1]}, no-CoT via OpenRouter (chat + next-word instruction)", no_cot_correct))
summary_table = "\n".join(summary_rows)

page = f"""# J-lens readouts on multi-hop questions: {model_label}

Each graph shows, per layer, the J-lens logit of the answer, the hidden intermediate (never written in the prompt), and the two
prompt words the lens surfaces most, all read at the token just before the answer. Questions {model_label} answers correctly
come first ({len(graph_correct)}), then the ones it gets wrong ({len(graph_wrong)}).

## Correct %

| model | correct | % |
| --- | --- | --- |
{summary_table}

## Answered correctly

{"".join(section(item) for item in graph_correct)}
## Answered wrong

{"".join(section(item) for item in graph_wrong)}"""

output_path = graph_dir / "README.md"
output_path.write_text(page)
print(f"wrote {output_path}")
