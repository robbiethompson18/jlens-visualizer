"""Is the potion's colour after each stir readable at that stir's token? One panel per model.

For every brew item and every stir k, takes the J-lens rank among the 10 colours of the colour the potion
has after stir k, at the token of stir k's ingredient (no colour word is written there, so a high rank is
computed, not echoed), averaged over the last quarter of layers. Control: the item's other trajectory
colours at the same token. Writes graphs/brew_stir_states.png.

    uv run python scripts/plot_stir_states.py gemma-4-31b-it qwen3.6-27b
"""

import gzip
import json
import re
import statistics
import sys
from pathlib import Path

import matplotlib.pyplot as plt

PRODUCED, CONTROL = "#eb6834", "#8a8984"
SURFACE, INK, MUTED_INK, GRID = "#fcfcfb", "#1a1a19", "#6b6a63", "#e6e5df"
CHANCE = 5.5


def stir_positions(item: dict) -> list[int]:
    """Token index of each stirred ingredient in 'You stir in, one at a time: ash, then clay.'"""
    text = "".join(item["tokens"])
    token_starts = [0]
    for token in item["tokens"]:
        token_starts.append(token_starts[-1] + len(token))
    stirs = re.search(r"one at a time: (.*)\.", text)
    assert stirs, f"{item['name']}: no stir list"
    positions = []
    for word in re.finditer(r"\w+", stirs.group(1)):
        if word.group() == "then":
            continue
        start, end = stirs.start(1) + word.start(), stirs.start(1) + word.end()
        positions.append(
            [index for index in range(len(item["tokens"])) if token_starts[index] < end and token_starts[index + 1] > start][-1]
        )
    return positions


def stir_state_ranks(model: str) -> tuple[dict, dict]:
    """(depth, stir) -> median rank of the produced colour, and of the other trajectory colours."""
    readout = json.loads(gzip.decompress(Path(f"data/positions/{model}/brew.json.gz").read_bytes()))
    late_layers = range(int(0.75 * len(readout["layers"])), len(readout["layers"]))
    produced, control = {}, {}
    for item in readout["items"]:
        trajectory = [item["start"], *item["intermediates"], item["target"].strip()]
        for stir, position in enumerate(stir_positions(item), start=1):
            for index, colour in enumerate(trajectory):
                rank = statistics.mean(item["words"][colour]["alphabet_rank"][layer][position] + 1 for layer in late_layers)
                (produced if index == stir else control).setdefault((item["depth"], stir), []).append(rank)
    return (
        {key: statistics.median(ranks) for key, ranks in produced.items()},
        {key: statistics.median(ranks) for key, ranks in control.items()},
    )


def accuracy(model: str) -> dict[int, str]:
    readout = json.loads(gzip.decompress(Path(f"data/positions/{model}/brew.json.gz").read_bytes()))
    by_depth: dict[int, list[bool]] = {}
    for item in readout["items"]:
        by_depth.setdefault(item["depth"], []).append(item["model_top5"][0].strip() == item["target"].strip())
    return {depth: f"{sum(results)}/{len(results)}" for depth, results in by_depth.items()}


models = sys.argv[1:]
fig, axes = plt.subplots(1, len(models), figsize=(6 * len(models), 4.2), facecolor=SURFACE, sharey=True, squeeze=False)
for ax, model in zip(axes[0], models):
    produced, control = stir_state_ranks(model)
    keys = sorted(produced)
    x = range(len(keys))
    ax.axhline(CHANCE, color=GRID, linewidth=1.5, linestyle="--")
    ax.text(len(keys) - 0.5, CHANCE - 0.15, "chance", color=MUTED_INK, fontsize=8, ha="right")
    ax.scatter(x, [control[key] for key in keys], color=CONTROL, s=40, label="other colours on the trajectory (control)", zorder=3)
    ax.scatter(x, [produced[key] for key in keys], color=PRODUCED, s=60, label="colour after this stir", zorder=4)
    correct = accuracy(model)
    ax.set_xticks(list(x), [f"stir {stir}\nof {depth}" for depth, stir in keys], fontsize=8)
    ax.set_ylim(10, 0.5)
    ax.set_yticks(range(1, 11))
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.set_facecolor(SURFACE)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.tick_params(colors=MUTED_INK)
    accuracy_line = " · ".join(f"{depth} stir{'s' * (depth > 1)}: {correct[depth]}" for depth in sorted(correct))
    ax.set_title(f"{model}\ncorrect at {accuracy_line}", color=INK, fontsize=11, loc="left")
axes[0][0].set_ylabel(
    "rank among the 10 colours at the stir's token\n(median over items, last quarter of layers)", color=MUTED_INK, fontsize=9
)
axes[0][-1].legend(frameon=False, fontsize=8, labelcolor=INK, loc="lower right")
fig.suptitle("brew: is the colour after each stir readable at that stir's token?", color=INK, fontsize=13, x=0.01, ha="left")
fig.tight_layout()
fig.savefig("graphs/brew_stir_states.png", dpi=110)
print("wrote graphs/brew_stir_states.png")
