---
type: literature-note
source_url: https://techcrunch.com/2026/08/14/kog-is-going-deeper-to-squeeze-more-inference-out-of-gpus
author: Anna Heim
tags: [ai-inference, gpu-optimization, startups, llm-serving]
date_consumed: 2026-08-15
---

## Summary
French startup Kog is betting that conventional GPUs (Nvidia H200, AMD MI300X) still have far more inference performance to unlock through deep, low-level software optimization rather than purpose-built inference chips. Its tech preview demoed 3,000 tokens/second single-request decoding on a small 2B-parameter open-sourced model (Laneformer 2B), and the company is now racing to prove the same approach scales to large LLMs.

## Core Concepts
- **[[Inference Optimization]]**: Squeezing more throughput/speed out of existing hardware via low-level software engineering (down to assembly/binary) rather than new silicon — Kog's core bet, akin to Stanford's Hazy Research lab.
- **[[GPU Memory Bandwidth]]**: Delalleau argues newer GPUs' growing memory bandwidth is underused for decoding — the "GPUs aren't suited for decoding" view is a misconception he's setting out to disprove.
- **[[Single-Request Decoding]]**: The specific bottleneck Kog targets — fast token generation for one request at a time, as opposed to batched throughput optimization.
- **[[Kog Inference Engine (KIE)]]**: Kog's product, targeting software engineers (e.g., Claude Code users frustrated by wait times) and design partners building prompt-to-app/game tools.

## Key Takeaways
- Kog's demo hit 3,000 TPS but only on a small, purpose-built 2B model — scaling the same 30x-faster claim to full-size LLMs is the company's next, unproven leap.
- 200 tangible business leads came in after Kog's May Hacker News front-page demo, signaling real market pain around inference latency/cost.
- Competitor ZML (also French) takes a different tack — hardware-agnostic software bypassing Nvidia's CUDA entirely, rather than deep single-vendor optimization.
- Kog is backed by France's Bpifrance and French Tech 2030, tying its success to European semiconductor/AI sovereignty ambitions.
- Founder Gaël Delalleau's background in solid-state physics and offensive cybersecurity shapes Kog's reverse-engineering-first culture.

## 🃏 Review Questions
**Q1**: What is Kog's core technical bet, and how does it differ from Cerebras's approach?
**A**: Kog bets that conventional, already-owned datacenter GPUs (not purpose-built inference chips like Cerebras's) still have large untapped inference performance, unlockable through deep low-level software optimization.

**Q2**: What is the key unproven leap in Kog's roadmap as of August 2026?
**A**: Its impressive 3,000 TPS demo used a small, purpose-built 2B-parameter model (Laneformer 2B) — the company has not yet shown its 30x-speed claim holds for full-size large language models.

**Q3**: Why might software engineers specifically be an early target customer for Kog?
**A**: Because they already experience painful multi-hour wait times in AI-assisted coding workflows (e.g., Claude Code), and Anthropic itself charges a premium for faster "Fast Mode" — showing speed has clear monetizable value.
