"""Bundle a model's per-item J-lens graphs into one self-contained HTML page.

One section per question: the graph, then the full question, the hidden step, what the model
predicted, and which OpenRouter models answer it without chain of thought. Items the model gets
right come first. Run plot_readout.py first.

    uv run python scripts/build_report.py data/readouts/qwen2.5-7b-instruct.json
"""

import base64
import html
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
    return '<span class="ok">✓</span>' if correct else '<span class="bad">✗</span>'


def percent_row(label: str, correct: int) -> str:
    total = len(readout["items"])
    return f"<tr><td>{html.escape(label)}</td><td>{correct}/{total}</td><td>{100 * correct / total:.0f}%</td></tr>"


def section(readout_item: dict) -> str:
    item = items[readout_item["name"]]
    image = base64.b64encode((graph_dir / f"{item['name']}.png").read_bytes()).decode()
    prediction = readout_item["model_top5"][0].strip()
    top5 = ", ".join(f"<code>{html.escape(token.strip())}</code>" for token in readout_item["model_top5"])
    chain = " → ".join(html.escape(word) for word in [*item["intermediates"], item["target"]])
    no_cot_cells = "".join(
        f"<li>{mark(is_correct(no_cot[model][item['name']]['answer'], item['target']))} {html.escape(model.split('/')[-1])}: "
        f"<code>{html.escape(no_cot[model][item['name']]['answer'].strip()[:40])}</code></li>"
        for model in no_cot
    )
    return f"""
<section id="{item["name"]}">
  <img src="data:image/png;base64,{image}" alt="J-lens graph for {item["name"]}">
  <p class="question">{html.escape(item["prompt"].strip())} <b>{html.escape(item["target"])}</b></p>
  <p><span class="label">Hidden reasoning</span> {chain}</p>
  <p><span class="label">{html.escape(model_label)} (this graph)</span> {mark(is_correct(prediction, item["target"]))}
     predicts <code>{html.escape(prediction)}</code>; top 5: {top5}</p>
  <details><summary>No-CoT answers via OpenRouter (chat template + "next word only" instruction)</summary><ul>{no_cot_cells}</ul></details>
  <p class="name">{item["name"]}</p>
</section>"""


graph_correct = [item for item in readout["items"] if is_correct(item["model_top5"][0].strip(), item["target"])]
graph_wrong = [item for item in readout["items"] if item not in graph_correct]
summary_rows = percent_row(f"{model_label}, raw prompt, local forward pass (the graphs)", len(graph_correct))
for model in no_cot:
    no_cot_correct = sum(is_correct(no_cot[model][name]["answer"], items[name]["target"]) for name in items)
    summary_rows += percent_row(f"{model.split('/')[-1]}, no-CoT via OpenRouter", no_cot_correct)

page = f"""<!doctype html>
<html><head><meta charset="utf-8"><title>J-lens multi-hop: {html.escape(model_label)}</title>
<style>
  body {{ font: 16px/1.5 system-ui, sans-serif; color: #1a1a19; background: #fcfcfb; }}
  body {{ max-width: 1000px; margin: 2rem auto; padding: 0 1rem; }}
  img {{ width: 100%; }}
  section {{ border-top: 1px solid #e6e5df; padding: 2rem 0; }}
  .question {{ font-size: 1.25rem; margin: .5rem 0; }}
  .label {{ color: #6b6a63; font-size: .85rem; text-transform: uppercase; letter-spacing: .04em; margin-right: .5rem; }}
  .name {{ color: #6b6a63; font-size: .8rem; }}
  .ok {{ color: #1baf7a; font-weight: bold; }} .bad {{ color: #d03b3b; font-weight: bold; }}
  table {{ border-collapse: collapse; }} td {{ padding: .2rem 1rem .2rem 0; }}
  ul {{ list-style: none; padding-left: 0; }}
</style></head><body>
<h1>J-lens readouts on multi-hop questions: {html.escape(model_label)}</h1>
<p>Each graph shows, per layer, the J-lens logit of the answer, the hidden intermediate (never written in the prompt), and the two
prompt words the lens surfaces most, all read at the token just before the answer. Questions {html.escape(model_label)} answers
correctly come first ({len(graph_correct)}), then the ones it gets wrong ({len(graph_wrong)}).</p>
<h2>Correct %</h2>
<table>{summary_rows}</table>
<h2>Answered correctly</h2>
{"".join(section(item) for item in graph_correct)}
<h2>Answered wrong</h2>
{"".join(section(item) for item in graph_wrong)}
</body></html>
"""

output_path = graph_dir / "report.html"
output_path.write_text(page)
print(f"wrote {output_path} ({output_path.stat().st_size / 1e6:.1f} MB)")
