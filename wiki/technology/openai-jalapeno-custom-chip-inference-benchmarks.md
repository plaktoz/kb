---
type: literature-note
source_url: https://the-decoder.com/openais-first-custom-chip-jalapeno-reportedly-beats-nvidias-blackwell-and-rubin-in-inference-benchmarks/
author: Matthias Bastian
tags: [ai-chips, inference, openai, nvidia]
date_consumed: 2026-08-29
---

## Summary

OpenAI unveiled benchmark results for its first custom inference chip, "[[Jalapeño]]," at the Hot Chips conference, claiming it beats [[Nvidia]]'s Blackwell and even the newer Vera Rubin platform on throughput per watt and latency. The chip, co-developed with [[Broadcom]], handles inference only and is not tuned specifically to OpenAI's own models. Despite being a first-generation design built in roughly nine months, SemiAnalysis says the results suggest Nvidia's "CUDA moat" may be weakening.

## Core Concepts

- **[[Jalapeño]]**: OpenAI's first in-house AI inference accelerator, developed with [[Broadcom]], targeting general-purpose LLM inference rather than training or OpenAI-specific models.
- **[[Nvidia Blackwell]]** and **[[Nvidia Vera Rubin]]**: The current and next-generation Nvidia GPU platforms used as the competitive baseline; Vera Rubin is considered the fairer comparison since both it and Jalapeño use HBM4 memory.
- **[[InferenceX Benchmark]]**: A public benchmark from [[SemiAnalysis]] used to test Jalapeño against commercial systems, with some runs verified on-site by SemiAnalysis.
- **[[CUDA Moat]]**: Nvidia's long-standing software ecosystem advantage, which [[SemiAnalysis]] suggests may be eroding given how quickly OpenAI brought up new models on its own silicon.
- **[[Speculative Decoding]]** and **[[Multi-Token Prediction]]**: Inference optimization techniques that some comparison systems used but Jalapeño did not, implying further headroom for Jalapeño's performance.

## Key Takeaways

- Jalapeño delivers **1.5x–1.9x** more AI work per watt at peak throughput across three tested models.
- End-to-end latency is **1.7x–3.6x** lower than the best commercial systems tested.
- Interactive workload performance is **2.1x–4.1x** higher than competitors.
- At matched decoding speed, Jalapeño reaches **54x–104x** token throughput per kilowatt versus the best available accelerator.
- Tested models: **GPT-OSS 120B** (~1,400 tokens/sec/user), **Deepseek R1 670B** (~700 tokens/sec/request), and **Kimi K2.5 1T**.
- Jalapeño beats **Vera Rubin** on output tokens per megawatt, despite Rubin using multi-token prediction and Jalapeño not using it yet.
- Total cost of ownership per token is roughly even between Jalapeño and Vera Rubin.
- Design-to-fabrication took about **9 months**; the full development cycle was **16 months**, starting mid-2024.
- OpenAI used its own AI models during chip development — older models aided design, newer ones sped up programming.
- Jalapeño hasn't shipped beyond engineering samples, while Rubin systems are already shipping to customers.
- OpenAI CFO **Sarah Friar** frames Jalapeño as complementary to existing partnerships with Nvidia, AMD, AWS, Cerebras, and CoreWeave, not a replacement.

## 🧠 First Principles & Mental Models

- **[[Moat Erosion]]**: A durable competitive advantage (Nvidia's CUDA software ecosystem) weakens once a well-resourced competitor can replicate the outcome through a different path — here, OpenAI using its own AI models to compress chip design time undercuts the assumption that only Nvidia's tooling maturity enables fast, competitive silicon.

## 🃏 Review Questions

**Q1**: What is the core claim of the article?
**A**: OpenAI's first custom inference chip, Jalapeño, reportedly outperforms Nvidia's Blackwell and even its newer Vera Rubin platform on throughput per watt and latency, despite being a first-generation design.

**Q2**: What specific evidence supports Jalapeño's performance claims?
**A**: On SemiAnalysis's InferenceX benchmark, Jalapeño showed 1.5x–1.9x better performance per watt, 1.7x–3.6x lower latency, and 54x–104x higher token throughput per kilowatt at matched decoding speed across GPT-OSS 120B, Deepseek R1 670B, and Kimi K2.5 1T.

**Q3**: What is the broader implication of Jalapeño's results?
**A**: SemiAnalysis argues it signals Nvidia's "CUDA moat" may no longer hold, since OpenAI could bring up competitive silicon quickly using its own AI models — though Jalapeño remains at the engineering-sample stage and untested against newer large models like Deepseek V4 Pro and Kimi K3.
