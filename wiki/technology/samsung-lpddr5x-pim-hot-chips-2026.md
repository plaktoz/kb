---
type: literature-note
source_url: https://chipsandcheese.com/p/hot-chips-2026-samsungs-processing
author: Chester Lam
tags: [processing-in-memory, semiconductor, memory-architecture, ai-hardware]
date_consumed: 2026-08-30
---

## Summary

Samsung presented their LPDDR5X-PIM chip at Hot Chips 2026, integrating MAC compute units directly inside standard LPDDR5X-9600 memory banks while preserving compatibility with existing memory controllers. The design achieves 614 GB/s internal bandwidth and 2.4 TOPS throughput at 4-bit precision by placing a PIM block in each of 16 banks, sidestepping the memory wall bottleneck. However, the approach introduces significant software and OS-level complications around multitasking, cache coherency, and speculative execution.

## Core Concepts

- **[[Processing-in-Memory]] (PIM)**: Moving compute directly into DRAM to exploit the vast internal bandwidth that never leaves the chip package.
- **[[LPDDR5X]] Interface Repurposing**: Samsung uses reserved row addresses as mode-switch triggers — no new hardware interface required — toggling between normal single-bank mode and PIM multi-bank mode.
- **MAC Tree Architecture**: Each of the 16 banks contains a multiply-accumulate tree, register files for activations and scale factors, and a 64-instruction register file.
- **Supported Precision Formats**: [[INT8]], [[FP8]], and 4-bit weights — targeting AI inference workloads where reduced precision is acceptable.
- **[[Memory Wall]] Problem**: The fundamental bottleneck of moving data between CPU/GPU and DRAM; PIM attacks this by bringing compute to the data.
- **[[Address Align Mode]]**: A Samsung mechanism to handle memory controller reordering when operating in PIM mode.

## Key Takeaways

- **Internal vs. External Bandwidth**: 614 GB/s internally vs. 76.8 GB/s through the normal external interface — 8x advantage.
- **Throughput**: 2.4 TOPS at 4-bit precision across the full package.
- **Mode Switching Mechanism**: Reserved row addresses toggle between normal and PIM modes — no new hardware interface needed.
- **Broadcast Writes**: Activation values are broadcast to all 16 banks simultaneously via write commands; read commands trigger computation.
- **Multitasking Risk**: PIM mode affects the entire memory channel, so concurrent non-PIM accesses can corrupt computation state.
- **Cache Incompatibility**: Samsung recommends marking PIM memory uncacheable, severely degrading CPU performance for affected regions.
- **Speculative Execution Hazard**: Prefetchers and out-of-order loads can inadvertently trigger PIM computations, corrupting register file state.
- **OS Overhead**: Context-switching a PIM thread requires saving per-bank register state across all 16 banks.
- **Proposed Fix**: Dedicated DRAM compute commands, cache-coherency via read-for-ownership, and new CPU block-MAC instructions would cleanly resolve most integration issues.

## 🧠 First Principles & Mental Models

- **[[Law of the Bottleneck]]**: System throughput is constrained by its slowest stage; moving compute inside DRAM directly attacks the memory bandwidth bottleneck rather than widening an external bus that still cannot match internal bandwidth.
- **[[Leaky Abstraction]]**: Samsung's hack of repurposing reserved row addresses to trigger PIM mode is a classic leaky abstraction — it works until another layer (OS scheduler, CPU prefetcher, cache subsystem) assumes the abstraction holds and corrupts state accordingly.

## 🃏 Review Questions

**Q1**: What is the central claim of Samsung's LPDDR5X-PIM design?
**A**: By embedding MAC compute units directly inside each of 16 DRAM banks, Samsung achieves 614 GB/s internal bandwidth — 8x the external interface — while remaining compatible with existing memory controllers.

**Q2**: How does Samsung trigger PIM mode without a new hardware interface, and what risks does this create?
**A**: Reserved row addresses are repurposed as mode-switch triggers; however, this means prefetchers and out-of-order CPU loads can inadvertently activate PIM computations, corrupting vector register file state.

**Q3**: What would a cleaner long-term architecture look like, according to the article?
**A**: Dedicated compute commands in the DRAM interface, cache-coherency integration via read-for-ownership requests, and new CPU block-MAC instructions would allow transparent delegation to in-memory compute without requiring uncacheable memory regions or thread serialization.
