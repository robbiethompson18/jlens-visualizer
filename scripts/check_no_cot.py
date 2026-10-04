"""Which items can each model answer in one forward pass?

Asks every item of a dataset (default data/lens-eval-multihop.json) via OpenRouter with reasoning
disabled. An item only makes a meaningful J-lens graph on a model that gets it right without chain of
thought. Models default to MODELS. Writes per-item results to data/no_cot_results.json for the default
dataset, else data/no_cot_<dataset>.json, and prints accuracy per depth when items have one.

    uv run python scripts/check_no_cot.py
    uv run python scripts/check_no_cot.py data/brew.json google/gemma-4-31b-it moonshotai/kimi-k3
"""

import json
import os
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from pathlib import Path

# OpenRouter ids of models with a public pre-fitted Jacobian lens
# (anicka/jlens-qwen2.5-7b-instruct, solarkyle/jspace-lenses and neuronpedia/jacobian-lens on HuggingFace).
# openai/gpt-oss-20b also has a lens but its reasoning cannot be disabled.
MODELS = [
    "qwen/qwen-2.5-7b-instruct",
    "qwen/qwen3.6-27b",
    "qwen/qwen3-32b",
    "google/gemma-4-26b-a4b-it",
    "google/gemma-4-31b-it",
    "mistralai/mistral-small-24b-instruct-2501",
    "meta-llama/llama-3.3-70b-instruct",
]

INSTRUCTION = "Complete the sentence with only the next word or number, nothing else.\n\n"
# More output tokens than this means the provider reasoned silently and stripped the text.
MAX_HONEST_COMPLETION_TOKENS = 8


def ask(model: str, prompt: str) -> dict:
    body = {
        "model": model,
        "messages": [{"role": "user", "content": INSTRUCTION + prompt.strip()}],
        "reasoning": {"enabled": False},
        "temperature": 0,
        "max_tokens": 200,
    }
    request = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {os.environ['OPENROUTER_API_KEY']}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            payload = json.load(response)
    except (urllib.error.URLError, TimeoutError) as error:
        return {"error": str(error)}
    if "error" in payload:
        return {"error": payload["error"]["message"]}
    message = payload["choices"][0]["message"]
    return {
        "answer": message["content"] or "",
        "reasoned": bool(message.get("reasoning")) or payload["usage"]["completion_tokens"] > MAX_HONEST_COMPLETION_TOKENS,
    }


def is_correct(answer: str, target: str) -> bool:
    """NCRI-style items ask for an 'Answer: X' envelope; multi-hop items are bare completions."""
    return answer.split("Answer:")[-1].strip(" \"'.*").lower().startswith(target.strip().lower())


dataset_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/lens-eval-multihop.json")
models = sys.argv[2:] or MODELS
items = json.loads(dataset_path.read_text())["items"]
results: dict[str, dict[str, dict]] = {}
for model in models:
    with ThreadPoolExecutor(max_workers=8) as pool:
        responses = list(pool.map(partial(ask, model), [item["prompt"] for item in items]))
    results[model] = {item["name"]: response for item, response in zip(items, responses)}
    errors = sum("error" in response for response in responses)
    reasoned = sum(response.get("reasoned", False) for response in responses)
    wrong = [
        (item["name"], item["target"], response["answer"])
        for item, response in zip(items, responses)
        if "error" not in response and not is_correct(response["answer"], item["target"])
    ]
    print(f"{model}: {len(items) - errors - len(wrong)}/{len(items)} correct, {errors} errors, {reasoned} reasoned")
    if "depth" in items[0]:
        wrong_names = {name for name, _, _ in wrong}
        for depth in sorted({item["depth"] for item in items}):
            at_depth = [item for item in items if item["depth"] == depth]
            correct = sum(item["name"] not in wrong_names and "error" not in results[model][item["name"]] for item in at_depth)
            print(f"    depth {depth}: {correct}/{len(at_depth)}")
    else:
        for name, target, answer in wrong:
            print(f"    {name:32} want={target!r} got={answer[:40]!r}")

output_name = "no_cot_results.json" if dataset_path.name == "lens-eval-multihop.json" else f"no_cot_{dataset_path.stem}.json"
Path("data", output_name).write_text(json.dumps(results, indent=1))
