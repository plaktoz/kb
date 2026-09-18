---
type: literature-note
source_url: https://prismml.com/news/bonsai-2-27b
author: PrismML
tags: [model-compression, ternary-llm, inference-efficiency, quantization]
date_consumed: 2026-09-18
---

## Summary

PrismML released Ternary Bonsai 2 27B, a model built on [[Qwen3]] 27B that achieves 1.76 effective bits per weight in a 5.9 GB footprint — over 9x smaller than full-precision while retaining 98.2% of aggregate benchmark performance. PrismML describes this retention rate as "practically lossless," a significant improvement over the prior Bonsai 27B generation which achieved roughly 95% capability retention.

## Core Concepts

- **[[Ternary LLM]]**: Weights constrained to {−1, 0, +1} with FP16 group-wise scaling, enabling extreme storage reduction and fast integer arithmetic during inference.
- **[[1-bit / Sub-2-bit Quantization]]**: The compression family Bonsai 2 represents — 1.76 bits/weight sits well below the conventional 1.585-bit ternary ceiling, achieved through sparsity exploitation.
- **[[Qwen3]]**: The base model family (Qwen3.8 27B) on which Bonsai 2 27B is built, providing the pre-trained weights subsequently compressed.
- **[[Near-Lossless Compression]]**: PrismML's framing of 98.2% benchmark retention — a threshold above which capability degradation becomes negligible for practical use.
- **[[MLX]]**: Apple's machine learning framework enabling Bonsai 2 to run efficiently on Apple Silicon (M5 Max demonstrated at 46.8 tokens/sec).
- **[[Model Footprint]]**: At 5.9 GB the model fits in VRAM on consumer-grade hardware, unlocking local deployment that a full-precision 27B model cannot support.

## Key Takeaways

- **Size**: 5.9 GB footprint, 9x smaller than full-precision Qwen3.8 27B.
- **Accuracy retention**: 98.2% aggregate benchmark score (83.9 vs. 85.4 full-precision).
- **Generation-over-generation**: Capability retention improved from ~95% (Bonsai 1) to 98.2% (Bonsai 2).
- **Speed — NVIDIA**: Up to 143 tokens/sec on RTX 5090.
- **Speed — Apple**: 46.8 tokens/sec on M5 Max.
- **Energy efficiency**: 0.714 mWh/token on RTX 4090 — 40% more efficient than an 8B full-precision model.
- **Context**: 262K-token context window retained from the base model.
- **Modalities**: Multimodal (text + image).
- **License**: Apache 2.0 — permissive commercial use.
- **Platforms**: CUDA (NVIDIA) and MLX (Apple).

## 🧠 First Principles & Mental Models

- **[[Pareto Principle]]**: Bonsai 2 captures 98.2% of capability at 11% of the storage cost — a clear example of diminishing returns in precision, where the last few percentage points of accuracy demand exponentially more bits per weight.
- **[[Efficiency Frontier]]**: The jump from ~95% to 98.2% retention between generations while holding the compression ratio roughly constant illustrates that the frontier between size and capability is not fixed — better training and calibration routines push it outward.

## 🃏 Review Questions

**Q1**: What is the core claim of Bonsai 2 27B?
**A**: Ternary weight compression at 1.76 bits/weight can shrink a 27B model to 5.9 GB while retaining 98.2% of full-precision benchmark performance — a point PrismML characterizes as "practically lossless."

**Q2**: How does Bonsai 2's energy efficiency compare to running a smaller full-precision model?
**A**: At 0.714 mWh/token on an RTX 4090, Bonsai 2 27B is 40% more energy-efficient than an 8B model running in full FP16 precision, meaning more capable doesn't have to mean more power-hungry.

**Q3**: What practical deployment scenario does Bonsai 2 enable that full-precision 27B does not?
**A**: The 5.9 GB footprint allows the model to run locally on consumer NVIDIA GPUs and Apple Silicon devices (via MLX), bringing 27B-class capability to hardware that cannot hold a full-precision model in VRAM.
