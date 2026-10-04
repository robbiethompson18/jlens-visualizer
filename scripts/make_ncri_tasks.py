"""Generate fresh brew and chain-9 items in the format of Neel Nanda's nocot-bench (NCRI).

Text format, instruction and 1-shot layout copy github.com/neelnanda-io/nocot-bench (MIT), but the
items are new draws from our own seed, so none of the sealed benchmark items end up in this public repo.
Every state along an item's trajectory is distinct, so each step gets its own line on a lens graph.
Each item also records `lookups`, the prompt line that computes each step (so plots can mark it), and
each file records its answer `alphabet`, so a word can be ranked against the other possible answers.

- brew: a 10-colour x 3-ingredient rewrite table, a start colour, then 1-3 stirs. Colours are single
  Qwen tokens. Intermediates = the colour after each stir but the last.
- chain9: NCRI's `chain` (serial non-affine integer updates, wrapped into a range) shrunk from 1..20 to
  1..9, because Qwen splits multi-digit numbers into one token per digit. Not the sealed bank.

    uv run python scripts/make_ncri_tasks.py
"""

import json
import random
from collections.abc import Callable
from pathlib import Path

COLORS = ["red", "blue", "green", "gold", "black", "white", "pink", "gray", "purple", "brown"]
INGREDIENTS = ["ash", "bark", "chalk", "clay", "moss", "salt"]
BREW_INSTRUCTION = (
    "You will be shown the color-change rules for a potion and the sequence of ingredients stirred in. "
    "Answer immediately using the format 'Answer: [ANSWER]' where [ANSWER] is a single color word, nothing else."
)
CHAIN_INSTRUCTION = (
    "You will be shown a starting number and a list of steps. "
    "Answer immediately using the format 'Answer: [ANSWER]' where [ANSWER] is a single number, nothing else."
)
MOD = 9
ITEMS_PER_DEPTH = 20
DEPTHS = [1, 2, 3]


def brew_item(rng: random.Random, depth: int) -> tuple[str, list[str], list[str]]:
    """Problem text, the colour trajectory [start, after stir 1, ..., final], and the rule line each stir reads."""
    while True:
        ingredients = sorted(rng.sample(INGREDIENTS, 3))
        rules = {color: {ing: rng.choice([c for c in COLORS if c != color]) for ing in ingredients} for color in COLORS}
        states = [rng.choice(COLORS)]
        stirs = [rng.choice(ingredients) for _ in range(depth)]
        for stir in stirs:
            states.append(rules[states[-1]][stir])
        if len(set(states)) == len(states):
            break
    rule_line = {
        color: f"A {color} potion turns {rules[color][ingredients[0]]} with {ingredients[0]}, "
        f"{rules[color][ingredients[1]]} with {ingredients[1]}, and {rules[color][ingredients[2]]} with {ingredients[2]}."
        for color in COLORS
    }
    rule_lines = [rule_line[color] for color in rng.sample(COLORS, len(COLORS))]
    problem = "\n".join(
        [
            "A potion changes color each time an ingredient is stirred in. The rules:",
            *rule_lines,
            f"The potion starts out {states[0]}. You stir in, one at a time: {', then '.join(stirs)}.",
            "What color is the potion at the end?",
        ]
    )
    return problem, states, [rule_line[state] for state in states[:-1]]


def chain_step(rng: random.Random) -> tuple[str, Callable[[int], int]]:
    """A non-affine update rule over 1..MOD, as (text, function)."""
    kind = rng.choice(["halve", "parity", "threshold"])
    if kind == "halve":
        return "Halve it, rounding up.", lambda v: (v + 1) // 2
    if kind == "parity":
        k = rng.randint(1, MOD - 1)
        return f"If it is even, halve it; if it is odd, add {k}.", lambda v, k=k: v // 2 if v % 2 == 0 else v + k
    k = rng.randint(1, 4)
    return f"If it is bigger than 5, subtract {k}; otherwise double it.", lambda v, k=k: v - k if v > 5 else 2 * v


def chain_item(rng: random.Random, depth: int) -> tuple[str, list[str], list[str]]:
    """Problem text, the number trajectory [start, after step 1, ..., final] as strings, and each step's line."""
    while True:
        states = [rng.randint(1, MOD)]
        step_texts = []
        for _ in range(depth):
            text, apply = chain_step(rng)
            step_texts.append(text)
            states.append((apply(states[-1]) - 1) % MOD + 1)
        if len(set(states)) == len(states):
            break
    problem = "\n".join(
        [
            (
                f"Start with the number {states[0]} and apply the steps in order. After every step, "
                f"if the number is bigger than {MOD}, subtract {MOD}; if it is smaller than 1, add {MOD}."
            ),
            *step_texts,
            "What is the final number?",
        ]
    )
    return problem, [str(state) for state in states], step_texts


def build(task: str, make_item, instruction: str, target_prefix: str, alphabet: list[str]) -> None:
    """Writes data/<task>.json in lens-eval-multihop.json's shape: name, prompt, target, intermediates.

    The answer is read at the token before it, so a colour (single token with its leading space) goes
    in the target, while a digit's leading space is its own Qwen token and stays in the prompt.
    """
    rng = random.Random(f"jlens-visualizer|{task}")
    shot_problem, shot_states, _ = make_item(rng, 2)
    shot = f"{instruction}\n\n{shot_problem}\nAnswer: {shot_states[-1]}\n\n"
    items = []
    for depth in DEPTHS:
        for index in range(ITEMS_PER_DEPTH):
            problem, states, lookups = make_item(rng, depth)
            items.append(
                {
                    "name": f"{task}-d{depth}-{index:02d}",
                    "prompt": f"{shot}{problem}\nAnswer:{target_prefix}",
                    "target": states[-1] if target_prefix else " " + states[-1],
                    "start": states[0],
                    "intermediates": states[1:-1],
                    "lookups": lookups,
                    "depth": depth,
                }
            )
    path = Path(f"data/{task}.json")
    path.write_text(json.dumps({"alphabet": alphabet, "items": items}, indent=1))
    print(f"wrote {len(items)} items to {path}")


build("brew", brew_item, BREW_INSTRUCTION, target_prefix="", alphabet=COLORS)
build("chain9", chain_item, CHAIN_INSTRUCTION, target_prefix=" ", alphabet=[str(n) for n in range(1, MOD + 1)])
