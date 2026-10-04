# jlens-visualizer

Per-layer J-lens (Jacobian lens) logit graphs for multi-hop prompts like "the number of legs on the
animal that spins webs is". Does the hidden intermediate (`spider`) light up in the middle layers
before the answer (`8`)?

## Reports

Layer x token heatmaps (rank of each hidden step and the answer at every layer and prompt token),
all on Qwen3.6-27B with the Neuronpedia lens:

- [Multi-hop facts](graphs/qwen3.6-27b/lens-eval-multihop/README.md), 60/93 correct
- [brew](graphs/qwen3.6-27b/brew/README.md) (NCRI potion-colour lookup table): 20/20 at 1 stir, 4/20
  at 2, 0/20 at 3
- [chain-9](graphs/qwen3.6-27b/chain9/README.md) (NCRI serial arithmetic, shrunk to 1..9): 15/20 at
  1 step, 6/20 at 2, 1/20 at 3

Final-token-only line graphs (older):

- [Qwen3.6-27B](graphs/qwen3.6-27b/README.md), 60/93 correct
- [Qwen2.5-7B-Instruct](graphs/qwen2.5-7b-instruct/README.md), 35/93 correct

## Findings so far

- **The bridge entity shows up early at the tokens that define it.** On `spider-legs`, "spider" is
  rank ~1-10 at the `spins` / `webs` tokens from about layer 5 to 25, but at the final token only
  from about layer 38. Caveat: `webs` is lexically tied to "spider", so this may be association, not
  a computed hop.
- **At the final token the bridge and the answer rise together, late.** Median rank of both crosses
  top-100 around layer 50 of 63 (multi-hop, brew).
- **Qwen3.6-27B does one brew lookup per forward pass.** On 2-stir items, 10 of 16 wrong answers are
  the last stir applied to the start colour (chance ~2/16). On 3-stir items, 7 of 20 stop after the
  first stir and 7 apply the last stir to the start.
- **Full-vocab rank cannot tell digits apart.** On chain-9 every digit rises together wherever a
  number is due, so per-digit rank is uninformative. Next step: rank among the 9 digits only.
