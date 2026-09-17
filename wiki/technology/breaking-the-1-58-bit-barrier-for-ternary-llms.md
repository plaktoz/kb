---
type: literature-note
source_url: https://arxiv.org/abs/2609.16338
author: Evangelos Georganas, Alexander Heinecke, Pradeep Dubey
tags: [ternary-llm, quantization, model-compression, inference-efficiency]
date_consumed: 2026-09-17
---

## Summary

Ternary LLMs encode weights as {-1, 0, +1} symbols, conventionally stored at ~1.585 bits/weight using five-trit-per-byte packing that assumes uniform symbol distribution. The authors measured real weight distributions across 29 ternary models and found zeros often exceed 50% of all weights, motivating a new layout called **BITCOS** that exploits this sparsity. BITCOS achieves as low as 1.485 bits/weight and delivers up to 1.28× faster matrix-vector multiplication on both CPUs and GPUs.

## Core Concepts

- **[[Ternary LLM]]**: Large language models whose weights are constrained to the set {-1, 0, +1}, reducing storage and enabling fast integer arithmetic.
- **[[1-bit / Sub-2-bit Quantization]]**: A family of extreme model compression techniques targeting storage below 2 bits per weight, of which ternary (log₂3 ≈ 1.585 bits) is the current standard.
- **[[BITCOS]]**: The proposed weight layout — a presence bitmap indicating non-zero positions combined with a compacted sign vector — costing `2 − z` bits/weight where `z` is zero density.
- **[[Weight Sparsity]]**: The observation that zeros can comprise over 50% of weights in ternary models, creating an exploitable asymmetry in compression.
- **[[AVX-512]] / [[AVX2]] / Intel Xe2**: CPU and GPU SIMD instruction sets for which the authors wrote optimized BITCOS unpacking kernels.
- **[[Matrix-Vector Multiplication]]**: The dominant compute operation during LLM inference decode, which BITCOS accelerates through denser memory layouts.

## Key Takeaways

- **Baseline assumption flaw**: Standard five-trit packing treats all symbols as equally probable (~1.625 bits/weight).
- **Empirical finding**: Zeros exceed 50% of weights in many ternary models — violating the uniform assumption.
- **BITCOS layout**: Bitmap + sign vector costs `2 − z` bits/weight; lower as zero density grows.
- **Coverage**: Outperforms five-trit packing in 26 of 29 tested ternary models.
- **Best-case compression**: 1.485 bits/weight on the sparsest model tested.
- **MatVec speedup**: Up to 1.28× gain in matrix-vector multiplication.
- **End-to-end decode**: Up to 1.18× faster on CPUs, 1.27× faster on GPUs across 5 platforms.

## 🧠 First Principles & Mental Models

- **[[Goodhart's Law]] / Specification Gaming**: The conventional 1.585-bit figure is a theoretical ceiling derived from log₂3, not a measure of actual entropy in real models — optimizing to that number ignores the true underlying distribution, leaving compression gains on the table.
- **[[Exploiting Asymmetry]]**: BITCOS is a direct application of the first-principles idea that any encoding scheme should match the actual probability distribution of the data (Shannon's source coding theorem) rather than assume uniformity.

## 🃏 Review Questions

**Q1**: What is the core claim of the BITCOS paper?
**A**: Real ternary LLM weight distributions are highly skewed toward zero, so a layout that separates presence from sign achieves sub-1.585 bits/weight and faster inference than standard five-trit packing.

**Q2**: How does BITCOS achieve its storage savings, and what is its cost formula?
**A**: BITCOS stores a presence bitmap (1 bit per weight) plus a compacted sign vector only for non-zero weights, yielding `2 − z` bits/weight where `z` is the fraction of zero weights — the sparser the model, the greater the saving.

**Q3**: How would a practitioner apply these findings?
**A**: Swap the default five-trit packing for BITCOS when deploying ternary models on AVX-512/AVX2 CPUs or Intel Xe2 GPUs to gain up to 1.27× decode throughput at no accuracy cost.
