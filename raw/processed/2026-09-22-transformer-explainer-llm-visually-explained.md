---
source_url: https://poloclub.github.io/transformer-explainer/
author: Aeree Cho, Grace C. Kim, Alexander Karpekov, Alec Helbling, Jay Wang, Seongmin Lee, Benjamin Hoover, Polo Chau
date: 2026-09-22
---

# Transformer Explainer: LLM Transformer Model Visually Explained

The Transformer is a neural network architecture introduced in the 2017 paper "Attention is All You Need," now powering models like GPT, Llama, and Gemini. It operates on **next-token prediction**: given a prompt, what token most likely follows?

## Three Core Components

### 1. Embedding
Input text is tokenized (split into words/subwords), converted to numerical vectors, and combined with positional encodings. GPT-2 (small) uses a vocabulary of 50,257 tokens, each represented as a 768-dimensional vector.

### 2. Transformer Block (12 stacked blocks in GPT-2 small)
- **Multi-Head Self-Attention:** Tokens are transformed into Query, Key, and Value matrices. Attention scores determine inter-token relationships. GPT-2 uses 12 parallel attention heads, then concatenates their outputs.
- **MLP Layer:** Expands token representations from 768 → 3,072 dimensions (via GELU activation), then compresses back to 768, enriching representational capacity per token independently.

### 3. Output Probabilities
Final layers project representations into a 50,257-dimensional space (one logit per vocabulary token), then apply softmax to produce a probability distribution for next-token sampling.

## Sampling Controls
- **Temperature:** Values below 1 sharpen predictions; above 1 introduce more variation
- **Top-k:** Restricts candidates to the k highest-probability tokens
- **Top-p:** Selects the smallest token set whose cumulative probability exceeds threshold p

## Auxiliary Features
- **Layer Normalization** – stabilizes training
- **Dropout** – reduces overfitting
- **Residual Connections** – prevents vanishing gradients in deep networks

The interactive tool runs a live GPT-2 model in-browser (via ONNX Runtime), built with Svelte and D3.js, based on Andrej Karpathy's nanoGPT implementation. Created by researchers at Georgia Institute of Technology.
