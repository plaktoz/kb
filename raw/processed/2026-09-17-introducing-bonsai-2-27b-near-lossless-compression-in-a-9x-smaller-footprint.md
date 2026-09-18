---
source_url: https://prismml.com/news/bonsai-2-27b
author: PrismML
date: 2026-09-17
---

# Introducing Bonsai 2 27B: Near-Lossless Compression in a 9x Smaller Footprint

PrismML has released Ternary Bonsai 2 27B, built on Qwen3.8 27B, achieving 1.76 effective bits per weight in a 5.9GB footprint — over 9x smaller than full-precision while retaining 98.2% of aggregate benchmark performance.

## Key Specifications

- Ternary weights {−1, 0, +1} with FP16 group-wise scaling
- 262K-token context window
- Multimodal (text + image)
- Apache 2.0 license

## Benchmark Performance

- Aggregate score: 83.9 vs. full-precision Qwen3.8 27B's 85.4
- Up to 143 tokens/sec on RTX 5090
- 46.8 tokens/sec on M5 Max
- 0.714 mWh/token on RTX 4090 — 40% more energy-efficient than an 8B model running in full-precision

Versus the prior Bonsai 27B generation, capability retention improved from ~95% to over 98%, which PrismML characterizes as "practically lossless."

The model runs on NVIDIA GPUs (CUDA) and Apple devices (MLX). Full details are available in their whitepaper on GitHub.
