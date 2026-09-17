---
source_url: https://arxiv.org/abs/2609.16338
author: Evangelos Georganas, Alexander Heinecke, Pradeep Dubey
date: 2026-09-14
---

# Breaking the 1.58-bit Barrier for Ternary LLMs

Ternary LLMs encode weights as symbols from {-1, 0, +1}, with storage conventionally referenced to log₂3 ≈ 1.585 bits per weight. The standard deployment method packs five ternary weights per byte, effectively treating all three symbols as equally probable at ~1.625 bits/weight.

The authors measured actual weight distributions across 29 ternary models and found zeros can comprise over half of all weights. This asymmetry motivated **BITCOS**, a new layout combining a presence bitmap with a compacted sign vector, costing `2 - z` bits per weight (where `z` = zero density).

## Key Results

- Outperforms five-trit packing in 26 of 29 tested models
- Achieves as low as **1.485 bits/weight** on the sparsest model
- Optimized unpacking for AVX-512, AVX2, and Intel Xe2 GPUs
- Up to **1.28× gain** in matrix-vector multiplication
- End-to-end decode throughput improvements: up to **1.18×** on CPUs, **1.27×** on GPUs across 5 platforms
