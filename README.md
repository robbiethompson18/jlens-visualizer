# jlens-visualizer

Per-layer J-lens (Jacobian lens) logit graphs for multi-hop prompts like "the number of legs on the
animal that spins webs is". Does the hidden intermediate (`spider`) light up in the middle layers
before the answer (`8`)?

## Reports

- [Qwen3.6-27B](graphs/qwen3.6-27b/README.md) (Neuronpedia lens), 60/93 correct
- [Qwen2.5-7B-Instruct](graphs/qwen2.5-7b-instruct/README.md) (anicka lens), 35/93 correct
