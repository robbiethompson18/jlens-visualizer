# Available pre-fitted J-lenses

Which open-weights models already have a public Jacobian lens, where each lens lives, and which
models can answer the multi-hop questions in one forward pass. Compiled 2026-10-04.

Paper: "Verbalizable Representations Form a Global Workspace in Language Models" (Anthropic, 2026),
https://transformer-circuits.pub/2026/workspace/. Reference code: `anthropics/jacobian-lens`
(installed here as `jlens` via the `pod` dependency group).

## Lens repos on HuggingFace

### `camilablank/workspace-lenses` (linked from Neel Nanda's MATS 12 central doc)

A J-lens and a matched R-lens per model, at `<model>/j-lens/lens.pt` and `<model>/r-lens/lens.pt`.

| Directory            | Model                           | Size      | `d_model` |
| -------------------- | ------------------------------- | --------- | --------- |
| `qwen3.5-4b/`        | `Qwen/Qwen3.5-4B`               | 4B dense  | 2560      |
| `qwen3.5-9b/`        | `Qwen/Qwen3.5-9B`               | 9B dense  | 4096      |
| `qwen3.5-27b/`       | `Qwen/Qwen3.5-27B`              | 27B dense | 5120      |
| `qwen3.6-27b/`       | `Qwen/Qwen3.6-27B`              | 27B dense | 5120      |
| `gemma-3-27b-it/`    | `google/gemma-3-27b-it`         | 27B dense | 5376      |
| `qwen3.6-35b-a3b/`   | `Qwen/Qwen3.6-35B-A3B`          | 35B MoE   | 2048      |
| `qwen3.5-122b-a10b/` | `Qwen/Qwen3.5-122B-A10B`        | 122B MoE  | 3072      |
| `deepseek-v4-flash/` | `deepseek-ai/DeepSeek-V4-Flash` | ~280B MoE | 4096      |

- Fitting recipe (the README calls it paper-faithful): target layer `n_layers - 2`,
  `skip_first = 4`, 25 prompts from `NeelNanda/pile-10k`.
- R-lens: same estimator read through a RelP-modified backward graph. Its claimed advantage is
  cleaner early-layer reads. Post:
  https://www.lesswrong.com/posts/nv8oedrnLXKRzNEL9/r-lens-making-j-lens-more-faithful-on-early-layers
- Template lens (Qwen 3.6 27B only, `qwen3.6-27b/template-lens/`): a multi-token variant. Plain
  J-lens can only show single-token words.
- Loading gotcha: each `lens.pt` has an extra `provenance` key and the README loads it with
  `torch.load(..., weights_only=False)`. `jlens.JacobianLens.load` uses `weights_only=True`, so
  `scripts/lens_readout.py` may need a small change. Not yet tried.
- None of these have been downloaded or run in this repo yet.

### `anicka/jlens-qwen2.5-7b-instruct`

One file, `qwen2.5-7b-instruct_jlens.pt`, for `Qwen/Qwen2.5-7B-Instruct`. Fitted on WikiText-103
with the reference implementation; the model card gives no quality numbers. Layers 0–26. This is the
only lens run in this repo so far (`data/readouts/qwen2.5-7b-instruct.json`).

### `solarkyle/jspace-lenses`

`<model>/lens.pt`, fitted on 100 WikiText-103 prompts in bf16. Models: `gemma-4-e4b-it`,
`gemma-4-12b-it`, `huihui-gemma-4-12b-it-abliterated`, `gemma-4-26b-a4b-it`, `gemma-4-31b-it`,
`qwen3.6-27b`, `gpt-oss-20b`, `mistral-small-24b-instruct-2501`. Not run here yet.

## Related, not J-lenses

Celeste (`ceselder` on HuggingFace) has Qwen 3.6 27B meta-models: an NLA
(`ceselder/qwen3.6-27b-nla-rl`) and the collection `ceselder/qwen-36-27b-good-meta-models`
(skip-lens, oracle lens, modulation lens). Neel's doc cites these for comparing methods.

## Which models answer without reasoning

All 93 items of `data/lens-eval-multihop.json`, asked through OpenRouter in chat format with
reasoning disabled (`scripts/check_no_cot.py`, per-item results in `data/no_cot_results.json`). No
model reasoned silently. Scoring is exact-prefix, so "four" for "4" counts as wrong.

| Model                    | Correct |
| ------------------------ | ------- |
| Gemma 4 31B              | 77/93   |
| Qwen 3.6 27B             | 72/93   |
| Gemma 4 26B-A4B          | 65/93   |
| Mistral Small 24B (2501) | 53/93   |
| Qwen 2.5 7B Instruct     | 42/93   |

- `gpt-oss-20b` cannot be tested this way: its reasoning cannot be disabled.
- In the raw `Fact:` format used for the lens run, Qwen 2.5 7B's top next token is right on 35/93.
- Untested: every `camilablank` model except Qwen 3.6 27B, and Gemma 4 E4B / 12B (not on
  OpenRouter).

## What has been run

Qwen 2.5 7B Instruct with the `anicka` lens, on one RTX 4090 (about 15 GB of VRAM, a few minutes).
Graphs are in `graphs/qwen2.5-7b-instruct/`. On the spider item, "spider" jumps at layer 21 and
peaks at 24, "legs" peaks at 24, and "8" takes over at layer 26. Layers 0–20 decode to punctuation
and junk tokens.

## Suggested next run

Qwen 3.6 27B with the `camilablank` J-lens and R-lens side by side. It answers 72/93 without
reasoning and the R-lens targets the early-layer noise seen above. Needs an 80 GB card (about 54 GB
of weights in bf16) and the loading change noted above.
