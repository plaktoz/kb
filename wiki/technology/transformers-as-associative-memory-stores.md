---
type: literature-note
source_url: https://alexwang.ai/posts/associative-memory/
author: Alex Wang
tags: [transformers, associative-memory, self-attention, mlp]
date_consumed: 2026-10-17
---

## Summary

Alex Wang derives the full transformer architecture — linear layers, MLPs, and self-attention — from a single memory-retrieval primitive: the associative memory store. By measuring interference-to-signal ratio, he shows that each successive layer design is a principled upgrade in memory capacity, culminating in self-attention's exponential capacity (~1.2 million memories for 64-dimensional keys) compared to a linear layer's ~64.

## Core Concepts

- **[[Associative Memory]]** — A memory store that retrieves a value when queried with a similar key; the unifying lens for all transformer layers
- **Outer-product memory store** — Accumulates memories as outer products of keys and values; capacity ≈ key dimension ($d_k$); the linear layer gradient update is exactly this store
- **Interference-to-signal ratio** — The ratio of noise from other stored memories to the target signal during recall; sets capacity limits for each architecture
- **Optimal linear store** — Adds covariance whitening via least-squares regression; doubles capacity to $2d_k$ by canceling redundancy
- **[[MLP]] as nonlinear memory** — Rows and columns of the two weight matrices are keys and values; applying ReLU/squared-ReLU gates suppress low-similarity keys, boosting capacity to $2d_k^2/3 \approx 2700$ for $d_k=64$
- **[[Self-Attention]] as non-parametric memory** — Uses the exponential (softmax) to suppress interference with effectively unbounded capacity (~$e^{2\beta}$); keys/values come from context tokens, not trained weights
- **[[Scalable-Softmax]] / [[LogN-Scaling]]** — Raising the attention temperature $\beta$ with $\log M$ as context grows maintains recall quality at any context length
- **[[Alex Wang]]** — Author; AI researcher; also cited work on [[Test-Time Regression]]

## Key Takeaways

- **Capacity ladder**: Linear ~64 → optimal linear ~128 → ReLU MLP ~128 → squared ReLU ~2,700 → self-attention ~1.2M memories (for $d_k=64$).
- **Gradient descent = memory write**: A linear layer trained by SGD is updating an outer-product memory store one batch at a time.
- **ReLU's role**: Zeros out negative-similarity keys, halving interference variance ($\sqrt{2}$ capacity gain).
- **Squared ReLU**: Shrinks each interference term from $1/\sqrt{d_k}$ to $1/d_k$, giving ~40× capacity over linear.
- **Self-attention is non-parametric**: Number of stored memories equals context length; growing context = growing memory store.
- **Long-context scaling**: $\log M$ attention scaling lets memory capacity scale with context without saturation.
- **~3.6 bits/param**: Estimates from Morris et al. suggest GPT-style models memorize ~3.6 bits per parameter; 2 bits of factual knowledge per parameter (Allen-Zhu & Li).

## 🧠 Core Principles

**T1. Better recall requires suppressing interference, not just adding capacity.** Each architectural upgrade is fundamentally an interference-reduction strategy; the exponential in softmax is its limit case, suppressing all but the closest key. · *model:* [[Signal vs. Noise]]
→ explains: Capacity ladder, Self-attention is non-parametric

**T2. Inductive biases encode priors about which memories matter.** ReLU zeros negative similarities; softmax exponentially concentrates weight on the best match — each nonlinearity is a prior that trading-off recall breadth for recall precision.
→ explains: ReLU's role, Squared ReLU

## 🃏 Review Questions

**Q1**: What is the core claim of this article about transformer layers?
**A**: Every standard transformer layer (linear, MLP, self-attention) can be understood as a key-value associative memory store; the differences between them reflect successive improvements in how much interference is suppressed during recall.

**Q2**: Why does squaring the ReLU activation dramatically increase MLP memory capacity?
**A**: A squared ReLU shrinks each interference term from approximately $1/\sqrt{d_k}$ to $1/d_k$, reducing the noise that other stored memories add during recall and boosting capacity from ~128 to ~2,700 memories for 64-dimensional keys.

**Q3**: What makes self-attention's capacity effectively unbounded, and what is the practical challenge?
**A**: The softmax's exponential weighting function suppresses all but the most similar key with exponentially increasing sharpness, giving capacity of order $e^{2\sqrt{d_k}} \approx 1.2M$; the practical challenge is that as context grows ($M$ increases), the temperature $\beta$ must be raised (log-scaled) to maintain recall quality.
