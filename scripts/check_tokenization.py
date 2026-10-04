"""Which multi-hop items have single-token intermediates and targets?

The J-lens reads out one vocabulary token at a time, so a word only gets its own clean line on the
graph if it is a single token. Checks each word bare and with a leading space, since either form
can be the one the model is disposed to say next.

    uv run --with tokenizers python scripts/check_tokenization.py Qwen/Qwen2.5-7B-Instruct
"""

import json
import sys
from pathlib import Path

from tokenizers import Tokenizer

tokenizer = Tokenizer.from_pretrained(sys.argv[1])
items = json.loads(Path("data/lens-eval-multihop.json").read_text())["items"]


def token_count(word: str) -> int:
    return min(len(tokenizer.encode(form, add_special_tokens=False).ids) for form in (word, " " + word))


clean_items = 0
for item in items:
    counts = {word: token_count(word) for word in [*item["intermediates"], item["target"]]}
    is_clean = all(count == 1 for count in counts.values())
    clean_items += is_clean
    if not is_clean:
        print(f"{item['name']:32} {counts}")
print(f"\n{clean_items}/{len(items)} items have every intermediate and the target as a single token")
