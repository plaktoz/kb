---
type: literature-note
source_url: https://eiln.github.io/posts/ane-dma.html
author: Eileen Yoon
tags: [apple-silicon, neural-engine, hardware-bug, llm-inference]
date_consumed: 2026-09-13
---

## Summary

An RTL bug in the [[Apple M3]] Neural Engine ([[ANE]]) causes a speculative prefetch ring to misfire when DRAM weight transfer sizes are exact multiples of 1 MiB, dropping throughput from a nominal 45–60 GB/s to just 17–19 GB/s. The root cause is 14-bit head/tail address arithmetic in the kernel [[DMA]] engine that aliases a full-lap transfer as an empty one, starving the prefetch pipeline. A software workaround — splitting 1 MiB transfers into non-multiple chunks — restores near-nominal bandwidth and more than doubles token throughput for affected [[ANEMLL]] models.

## Core Concepts

- **[[Apple Neural Engine]] (ANE)**: Apple's dedicated ML accelerator; M3 variant has 16 cores and a 64 KiB per-core kernel memory (KMem).
- **[[DRAM]] Weight Streaming**: Single-token decode bottleneck dominated by weight reads; benchmark task is `X[1,D] × W[D,N] = Y[1,N]`.
- **RTL Prefetch Ring Bug**: The ANE DMA engine uses a 14-bit ring pointer for speculative prefetch credits. A transfer of exactly 0x4000 lines (1 MiB at 64 bytes/line) makes `end_ptr == rd_ptr` in 14-bit arithmetic, signaling "empty" instead of "full lap," and collapses credit to zero.
- **Credit Function**: `credit(x) = min(x, 256)` — bandwidth recovers linearly within ±256 lines (~16 KiB, one [[Apple Silicon]] VM page) of each 0x4000 boundary.
- **[[ANEMLL]]**: Open-source project running LLMs on the ANE; 7 of 15 models have projection dimensions that hit the 1 MiB multiple trigger.
- **Software Fix**: Split kernel tasks so no individual transfer is a 1 MiB multiple. Two 0x2000-line tasks yield 45.52 GB/s vs. 17.25 GB/s for one 0x4000-line task.

## Key Takeaways

- **Throughput collapse**: Affected transfers drop from ~45–60 GB/s to 17–19 GB/s — a ~200% hit.
- **Trigger condition**: Any `D × N` product equaling 1 MiB per ANE core causes collapse.
- **FFT confirmation**: Sweeping D reveals throughput notches with a dominant 2048-element harmonic.
- **DRAM contention ruled out**: Address scrambling and core-count variation both failed to explain the collapse.
- **Root cause**: 14-bit modular arithmetic aliases full-lap DMA transfers as zero-length.
- **Proper fix**: Compute `distance = transfer_lines - issued_lines` in 32-bit space to avoid aliasing.
- **Llama 3.2 1B**: 10.0 → 24.3 tokens/s after software fix (2.4×).
- **Qwen3-8B**: 1.36 → 2.97 tokens/s after software fix (2.2×).
- **Affected models**: Llama 3.1 8B, DeepSeek, DeepHermes 8B/3B, Qwen3-8B, Gemma 3 4B.

## 🧠 First Principles & Mental Models

- **[[Off-by-One Error]]**: The 14-bit ring pointer is a textbook off-by-one at the boundary — the design cannot distinguish "zero remaining" from "exactly one full lap remaining," which is the canonical fencepost problem at scale.
- **[[Abstraction Leak]]**: The 14-bit choice was motivated by Apple Silicon's 16 KiB page size (page offset fits in addr[13:0]), but this hardware convenience leaked an implicit assumption — no single transfer spans an exact multiple of the ring capacity — into the architectural correctness contract.

## 🃏 Review Questions

**Q1**: What is the core finding of the Apple M3 ANE throughput investigation?
**A**: An RTL bug in the M3 Neural Engine's DMA prefetch ring causes DRAM weight streaming throughput to collapse from 45–60 GB/s to 17–19 GB/s whenever a transfer is an exact multiple of 1 MiB.

**Q2**: Why does 14-bit address arithmetic in the prefetch ring produce the throttle?
**A**: A 1 MiB transfer spans exactly 0x4000 cache lines; in 14-bit arithmetic `end_ptr - rd_ptr` equals zero (full lap aliases to empty), so the prefetch engine issues zero credits and stalls the pipeline.

**Q3**: How can software work around this hardware bug, and what are the practical gains?
**A**: Splitting any 1 MiB-multiple kernel transfer into smaller non-multiple chunks avoids the buggy boundary; for ANEMLL models this more than doubles token throughput (e.g., Llama 3.2 1B: 10 → 24.3 tokens/s).
