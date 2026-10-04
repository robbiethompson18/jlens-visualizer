"""Draw the per-layer J-lens graphs from a lens_readout.py JSON.

One PNG per multi-hop item, plus overview.png with every item the model answers correctly.
X is layer, Y is the J-lens logit of each word at the token just before the answer. Lines are
the two prompt words the lens surfaces most strongly, then the hidden intermediate(s), then the answer.

    uv run python scripts/plot_readout.py data/readouts/qwen2.5-7b-instruct.json
"""

import json
import math
import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.axes import Axes

# Categorical slots from the dataviz skill's validated palette. Colour follows the word's role,
# so the answer and the intermediate keep their colour in every panel.
ROLE_COLORS = {"prompt": ["#2a78d6", "#1baf7a"], "intermediate": ["#eb6834", "#e87ba4", "#008300"], "target": ["#eda100"]}
SURFACE, INK, MUTED_INK, GRID = "#fcfcfb", "#1a1a19", "#6b6a63", "#e6e5df"

readout = json.loads(Path(sys.argv[1]).read_text())
layers = readout["layers"]


def words_to_plot(item: dict) -> list[tuple[str, str]]:
    """(word, colour) for the prompt words the lens surfaces most, then intermediates, then the answer."""
    late_layers = slice(len(layers) // 2, None)  # early layers mostly surface filler like "the"
    by_role = {role: [word for word, series in item["words"].items() if series["role"] == role] for role in ROLE_COLORS}
    by_role["prompt"].sort(key=lambda word: min(item["words"][word]["jlens"]["rank"][late_layers]))
    return [pair for role, colors in ROLE_COLORS.items() for pair in zip(by_role[role], colors)]


def is_correct(item: dict) -> bool:
    return item["model_top5"][0].strip().lower() == item["target"].lower()


def plot_item(ax: Axes, item: dict, *, compact: bool) -> None:
    series = [(word, color, item["words"][word]["jlens"]["logit"]) for word, color in words_to_plot(item)]
    for word, color, logits in series:
        ax.plot(layers, logits, color=color, linewidth=2, label=word, solid_capstyle="round")
    ax.margins(y=0.2)
    # Label each line at its peak, in ink, so identity never rests on color alone.
    # Lift a label that would land on an earlier one.
    label_height = (ax.get_ylim()[1] - ax.get_ylim()[0]) * (0.1 if compact else 0.06)
    placed: list[tuple[int, float]] = []
    for word, _, logits in sorted(series, key=lambda entry: max(entry[2])):
        peak = max(range(len(layers)), key=lambda index: logits[index])
        y = logits[peak]
        while any(abs(layers[peak] - x) < 5 and abs(y - other_y) < label_height for x, other_y in placed):
            y += label_height
        placed.append((layers[peak], y))
        ax.annotate(
            word, (layers[peak], y), xytext=(0, 4), textcoords="offset points",
            ha="center", color=INK, fontsize=8 if compact else 10, fontweight="bold",
        )  # fmt: skip
    ax.set_facecolor(SURFACE)
    ax.grid(axis="y", color=GRID, linewidth=1)
    ax.set_axisbelow(True)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(GRID)
    ax.tick_params(colors=MUTED_INK, length=0, labelsize=7 if compact else 9)
    title = item["name"] if compact else item["prompt"].removeprefix("Fact: ").strip() + " …"
    ax.set_title(title, color=INK, fontsize=9 if compact else 12, loc="left", wrap=True)


output_dir = Path("graphs") / Path(sys.argv[1]).stem
output_dir.mkdir(parents=True, exist_ok=True)
model_label = readout["model"].split("/")[-1]

for item in readout["items"]:
    fig, ax = plt.subplots(figsize=(8, 4.5), facecolor=SURFACE)
    plot_item(ax, item, compact=False)
    verdict = "correct" if is_correct(item) else f"wrong, answer is {item['target']}"
    ax.set_xlabel(f"layer ({model_label}; its top next token is {item['model_top5'][0].strip()!r}: {verdict})", color=MUTED_INK, fontsize=9)
    ax.set_ylabel("J-lens logit", color=MUTED_INK, fontsize=9)
    ax.legend(frameon=False, fontsize=9, labelcolor=INK, loc="upper left")
    fig.tight_layout()
    fig.savefig(output_dir / f"{item['name']}.png", dpi=150)
    plt.close(fig)

correct_items = [item for item in readout["items"] if is_correct(item)]
columns = 5
rows = math.ceil(len(correct_items) / columns)
fig, axes = plt.subplots(rows, columns, figsize=(columns * 3.6, rows * 2.5), facecolor=SURFACE, squeeze=False)
for ax, item in zip(axes.flat, correct_items):
    plot_item(ax, item, compact=True)
for ax in axes.flat[len(correct_items) :]:
    ax.set_visible(False)
fig.suptitle(
    f"J-lens logit by layer, {model_label}: the {len(correct_items)} of {len(readout['items'])} multi-hop questions it answers correctly",
    color=INK, fontsize=14, x=0.01, ha="left",
)  # fmt: skip
fig.tight_layout(rect=(0, 0, 1, 0.985))
fig.savefig(output_dir / "overview.png", dpi=110)
print(f"wrote {len(readout['items'])} graphs and overview.png ({len(correct_items)} correct items) to {output_dir}")
