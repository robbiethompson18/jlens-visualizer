"""Graphs, layer x position heatmaps and a Markdown report from a lens_positions.py JSON.

Per item, one PNG: on top, each tracked word's J-lens rank at the token before the answer by layer (log
scale, rank 1 at the top; thin line raw, thick line EWMA with a 2-layer halflife); below, one heatmap per
word, layer x prompt token, darker = higher rank. Plus summary.png: per depth, the median rank of each role
over the items the model gets right. README.md in the output directory shows it all, one item at a time.

    uv run python scripts/plot_positions.py data/positions/qwen3.6-27b/brew.json
"""

import json
import statistics
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# Categorical slots from the dataviz skill's validated palette, by role in reading order.
ROLE_COLORS = {"start": "#2a78d6", "intermediate": "#eb6834", "step 1": "#eb6834", "step 2": "#e87ba4", "answer": "#eda100"}
SURFACE, INK, MUTED_INK, GRID = "#fcfcfb", "#1a1a19", "#6b6a63", "#e6e5df"
MAX_LOG_RANK = 4  # ranks past 10^4 all render as "not there"
EWMA_HALFLIFE = 2

readout_path = Path(sys.argv[1])
readout = json.loads(readout_path.read_text())
layers = readout["layers"]
model_label = readout["model"].split("/")[-1]
output_dir = Path("graphs") / model_label.lower() / readout_path.stem
output_dir.mkdir(parents=True, exist_ok=True)


def is_correct(item: dict) -> bool:
    return item["model_top5"][0].strip() == item["target"].strip()


def ewma(values: np.ndarray) -> np.ndarray:
    alpha = 1 - 0.5 ** (1 / EWMA_HALFLIFE)
    smoothed = np.empty_like(values)
    smoothed[0] = values[0]
    for index in range(1, len(values)):
        smoothed[index] = alpha * values[index] + (1 - alpha) * smoothed[index - 1]
    return smoothed


def style(ax: plt.Axes) -> None:
    ax.set_facecolor(SURFACE)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.spines["left"].set_color(GRID)
    ax.spines["bottom"].set_color(GRID)
    ax.tick_params(colors=MUTED_INK, labelsize=8)


def setup_rank_axis(ax: plt.Axes) -> None:
    ax.set_yscale("log")
    ax.set_ylim(10**MAX_LOG_RANK * 3, 0.8)
    ax.set_yticks([1, 10, 100, 1000, 10000], ["1", "10", "100", "1k", "10k"])
    ax.grid(axis="y", color=GRID, linewidth=1)
    ax.set_ylabel("rank in J-lens readout\n(1 = top token)", color=MUTED_INK, fontsize=9)
    style(ax)


def plot_item(item: dict) -> None:
    words = list(item["words"].items())
    fig = plt.figure(figsize=(12, 3.4 + 2.3 * len(words)), facecolor=SURFACE)
    grid = fig.add_gridspec(1 + len(words), 1, height_ratios=[1.5] + [1] * len(words), hspace=0.55)

    ax = fig.add_subplot(grid[0])
    for word, series in words:
        ranks = np.array([layer_ranks[-1] for layer_ranks in series["rank"]], dtype=float) + 1
        color = ROLE_COLORS[series["role"]]
        ax.plot(layers, ranks, color=color, linewidth=0.8, alpha=0.45)
        ax.plot(layers, 10 ** ewma(np.log10(ranks)), color=color, linewidth=2.2, label=f"{word.strip()} ({series['role']})")
    setup_rank_axis(ax)
    if words:
        ax.legend(frameon=False, fontsize=9, labelcolor=INK, loc="upper left", bbox_to_anchor=(1.01, 1))
    verdict = "correct" if is_correct(item) else f"wrong, answer is {item['target'].strip()}"
    ax.set_title(
        f"{item['name']}: rank at the token before the answer ({model_label} says {item['model_top5'][0].strip()!r}: {verdict})",
        color=INK, fontsize=11, loc="left",
    )  # fmt: skip

    token_labels = [token.replace("\n", "⏎") for token in item["tokens"]]
    for row, (word, series) in enumerate(words, start=1):
        ax = fig.add_subplot(grid[row])
        colormap = LinearSegmentedColormap.from_list(series["role"], [ROLE_COLORS[series["role"]], "#ffffff"])
        log_ranks = np.log10(np.array(series["rank"], dtype=float) + 1)  # [layer, position]
        image = ax.imshow(log_ranks, aspect="auto", origin="lower", cmap=colormap, vmin=0, vmax=MAX_LOG_RANK, interpolation="nearest")
        ax.set_yticks(range(0, len(layers), 10), [layers[index] for index in range(0, len(layers), 10)])
        ax.set_xticks(range(len(token_labels)), token_labels, rotation=90, fontsize=7)
        ax.set_ylabel("layer", color=MUTED_INK, fontsize=9)
        ax.set_title(f'"{word.strip()}" ({series["role"]}): rank by layer and token', color=INK, fontsize=10, loc="left")
        style(ax)
        bar = fig.colorbar(image, ax=ax, pad=0.01, fraction=0.03, ticks=range(MAX_LOG_RANK + 1))
        bar.ax.set_yticklabels(["1", "10", "100", "1k", "10k+"], fontsize=7, color=MUTED_INK)
    fig.savefig(output_dir / f"{item['name']}.png", dpi=90, bbox_inches="tight")
    plt.close(fig)


def plot_summary(correct_items: list[dict]) -> Path:
    """Median rank by layer of each role at the token before the answer, one panel per depth."""
    depths = sorted({item.get("depth", 0) for item in correct_items})
    fig, axes = plt.subplots(1, len(depths), figsize=(max(9, 5.5 * len(depths)), 4), facecolor=SURFACE, squeeze=False)
    for ax, depth in zip(axes[0], depths):
        items = [item for item in correct_items if item.get("depth", 0) == depth]
        roles = list(dict.fromkeys(series["role"] for item in items for series in item["words"].values()))
        for role in roles:
            role_series = [series for item in items for series in item["words"].values() if series["role"] == role]
            per_item = [[layer_ranks[-1] + 1 for layer_ranks in series["rank"]] for series in role_series]
            medians = [statistics.median(ranks[index] for ranks in per_item) for index in range(len(layers))]
            ax.plot(layers, medians, color=ROLE_COLORS[role], linewidth=2.2, label=f"{role} (n={len(per_item)})")
        setup_rank_axis(ax)
        ax.set_title(f"depth {depth}" if depth else "all correct items", color=INK, fontsize=11, loc="left")
        ax.set_xlabel("layer", color=MUTED_INK, fontsize=9)
        ax.legend(frameon=False, fontsize=8, labelcolor=INK, loc="lower left")
    title = f"{readout_path.stem}, {model_label}: median J-lens rank at the token before the answer"
    fig.suptitle(title, color=INK, fontsize=12, x=0.01, ha="left")
    fig.tight_layout()
    path = output_dir / "summary.png"
    fig.savefig(path, dpi=100)
    plt.close(fig)
    return path


def question(item: dict) -> str:
    """The item's own problem, without the 1-shot example before it."""
    return item["prompt"].split("\n\n")[-1].removesuffix("Answer:").removesuffix("Answer: ").strip()


def item_section(item: dict) -> str:
    trajectory = " → ".join([*([item["start"]] if "start" in item else []), *item["intermediates"], item["target"].strip()])
    mark = "✅" if is_correct(item) else "❌"
    top5 = ", ".join(f"`{token.strip()}`" for token in item["model_top5"])
    body = question(item).replace("\n", "  \n")
    return f"""---

![{item["name"]}]({item["name"]}.png)

{body}

**Answer:** **{item["target"].strip()}** · **Hidden trajectory:** {trajectory}

**{model_label}:** {mark} top 5: {top5}
"""


correct_items = [item for item in readout["items"] if is_correct(item)]
wrong_items = [item for item in readout["items"] if not is_correct(item)]
for item in readout["items"]:
    plot_item(item)
if correct_items:
    plot_summary(correct_items)

depths = sorted({item.get("depth", 0) for item in readout["items"]})
accuracy_rows = "\n".join(
    f"| {depth or 'all'} | {sum(is_correct(i) for i in readout['items'] if i.get('depth', 0) == depth)}"
    f"/{sum(i.get('depth', 0) == depth for i in readout['items'])} |"
    for depth in depths
)
report = f"""# {readout_path.stem}: J-lens by layer and token, {model_label}

Lens: `{readout["lens"]}`. Each item's graph shows, on top, the J-lens rank of every tracked word at the
token before the answer (log scale, rank 1 at the top; thin = raw, thick = EWMA with a {EWMA_HALFLIFE}-layer
halflife). Below it, one heatmap per word: rank at every layer (y) and each of the last prompt tokens (x),
darker = closer to the lens's top token. Correct items first.

| depth | correct |
| --- | --- |
{accuracy_rows}

## Summary: median rank over correct items

![summary](summary.png)

## Answered correctly ({len(correct_items)})

{"".join(item_section(item) for item in correct_items)}
## Answered wrong ({len(wrong_items)})

{"".join(item_section(item) for item in wrong_items)}"""
(output_dir / "README.md").write_text(report)
print(f"wrote {len(readout['items'])} item graphs, summary.png and README.md to {output_dir}")
