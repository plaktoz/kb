---
type: literature-note
source_url: https://poloclub.github.io/transformer-explainer/
author: Aeree Cho, Grace C. Kim, Alexander Karpekov, Alec Helbling, Jay Wang, Seongmin Lee, Benjamin Hoover, Polo Chau
tags: [transformer, gpt-2, attention-mechanism, neural-networks]
date_consumed: 2026-09-22
---

## Summary

The Transformer, introduced in the 2017 "Attention is All You Need" paper, is the architecture underpinning models like GPT, Llama, and Gemini, and operates via next-token prediction. This interactive explainer walks through GPT-2 (small) to show exactly how embeddings, multi-head self-attention, and MLP layers transform input tokens into output probability distributions. Sampling parameters — temperature, top-k, and top-p — then control how the final token is drawn from that distribution.

## Core Concepts

- **[[Transformer Architecture]]** — the neural network design powering modern LLMs, built from stacked identical blocks
- **[[Next-Token Prediction]]** — the fundamental task: given a prompt, predict the most likely following token
- **[[Tokenization]] & [[Positional Encoding]]** — text is split into subwords mapped to 768-dimensional vectors; positional encodings inject sequence order
- **[[Multi-Head Self-Attention]]** — tokens are projected into [[Query]], [[Key]], and [[Value]] matrices; attention scores capture inter-token relationships; GPT-2 uses 12 parallel attention heads whose outputs are concatenated
- **[[MLP Layer]]** — per-token feedforward network: expands 768 → 3,072 dimensions via [[GELU]] activation, then compresses back to 768
- **[[Softmax]]** — final projection into 50,257-dimensional logit space (one per vocabulary token), converted to a probability distribution
- **Sampling Controls**: [[Temperature]], [[Top-k Sampling]], [[Top-p Sampling (Nucleus Sampling)]]
- **Stabilization Techniques**: [[Layer Normalization]], [[Dropout]], [[Residual Connections]]
- **[[GPT-2]]** — 12 stacked transformer blocks, vocabulary of 50,257 tokens; used as the live in-browser demo model (via ONNX Runtime)
- **[[Andrej Karpathy]]** — nanoGPT implementation that the interactive tool is based on
- **[[Georgia Institute of Technology]]** — research team behind the Transformer Explainer tool

## Key Takeaways

- **Embedding**: tokens → 768-dim vectors + positional encodings before entering blocks.
- **Multi-Head Attention**: 12 parallel heads compute Q/K/V scores, then concatenate results.
- **MLP Expansion**: 768 → 3,072 (4×) via GELU, then back to 768 per token.
- **Output**: 50,257 logits → softmax probability distribution for next-token sampling.
- **Temperature < 1**: sharpens distribution; Temperature > 1: flattens it.
- **Top-k**: restricts candidates to k highest-probability tokens.
- **Top-p (nucleus)**: selects smallest token set exceeding cumulative probability p.
- **Residual connections** prevent vanishing gradients across 12 stacked blocks.
- **Live demo** runs real GPT-2 inference in-browser via ONNX Runtime + Svelte + D3.js.

## 🧠 First Principles & Mental Models

- **[[Abstraction Layers]]**: Each of the 12 transformer blocks is an identical repeating unit — the same operation stacked to progressively refine token representations, illustrating how compositional depth creates emergent capability from simple primitives.
- **[[Signal-to-Noise Ratio]]**: Temperature, top-k, and top-p are all mechanisms for controlling the randomness-versus-determinism tradeoff in sampling — a direct application of tuning signal vs. noise to desired output quality.

## 🃏 Review Questions

**Q1**: What is the fundamental task the Transformer is trained to perform, and how does it produce output?
**A**: The Transformer performs next-token prediction: given an input prompt, it produces a probability distribution over the full vocabulary (50,257 tokens for GPT-2) via a softmax layer, and samples the next token from that distribution.

**Q2**: What do the Query, Key, and Value matrices in multi-head self-attention represent, and how many heads does GPT-2 (small) use?
**A**: Q, K, V are learned linear projections of each token's representation; attention scores computed from Q and K weight how much each token attends to others, with V holding the actual content aggregated. GPT-2 small uses 12 parallel attention heads whose outputs are concatenated.

**Q3**: How does the temperature sampling parameter affect generated text, and when would you lower it?
**A**: Temperature below 1 sharpens the probability distribution, making high-probability tokens even more likely and output more deterministic/focused; you would lower it when you want factual, consistent, or precise completions rather than creative variation.
