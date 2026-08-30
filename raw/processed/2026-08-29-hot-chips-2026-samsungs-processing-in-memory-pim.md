---
source_url: https://chipsandcheese.com/p/hot-chips-2026-samsungs-processing
author: Chester Lam
date: 2026-08-29
---

# Hot Chips 2026: Samsung's Processing-in-Memory (PIM)

Samsung presented their LPDDR5X-PIM chip at Hot Chips 2026, integrating MAC compute units directly inside standard LPDDR5X-9600 memory while maintaining compatibility with existing memory controllers.

## Architecture

Each of the chip's 16 banks gets its own PIM block, enabling internal bandwidth of 614 GB/s — compared to just 76.8 GB/s via the normal external interface. Each PIM block contains a MAC tree, register files for activations and scale factors, and a 64-instruction register file. Supported formats include INT8, FP8, and 4-bit weights, with package-wide throughput reaching 2.4 TOPS at 4-bit precision.

## Interface Design

Samsung repurposes reserved row addresses as mode-switching triggers — no new hardware interface required. Special rows toggle between single-bank (normal) and multi-bank (PIM) modes. Activation values broadcast across all 16 banks simultaneously via write commands, while read commands trigger computation rather than data retrieval. An Address Align Mode handles memory controller reordering.

## Software Challenges

The approach creates serious complications:

- **Multitasking conflicts:** PIM mode changes affect the entire memory channel, so concurrent non-PIM accesses can corrupt computation state. Channel isolation is likely required, sacrificing bandwidth for non-PIM workloads.
- **Cache incompatibility:** Samsung recommends marking PIM memory uncacheable, which severely degrades CPU performance.
- **Speculative execution hazards:** Prefetchers and out-of-order loads can inadvertently trigger PIM computations, corrupting VRF state.
- **OS complexity:** Context-switching a PIM thread requires saving all per-bank register state across 16 banks — a substantial burden.

## Proposed Improvements

A cleaner path forward would include dedicated compute commands in the DRAM interface, cache-coherency integration via read-for-ownership requests, and new CPU instructions (e.g., a block MAC operation) that transparently delegate to in-memory compute when beneficial — avoiding the need for reserved uncacheable memory regions and thread serialization.
