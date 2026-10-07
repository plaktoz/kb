---
type: literature-note
source_url: https://venturebeat.com/technology/mistral-debuts-large-4-le-chonk-a-1-trillion-parameter-text-output-model-with-high-benchmarks-planned-for-open-weights-release
author: Carl Franzen
tags: [mistral, open-weight-models, mixture-of-experts, sovereign-ai]
date_consumed: 2026-10-07
---

## Summary

[[Mistral]] has launched a public preview of Mistral Large 4 (ML4, codename "Le Chonk"), a one-trillion-parameter sparse multimodal-input, text-output model with 49 billion active parameters, with weights due on Oct. 27 under a custom license. Mistral pitches it as the strongest [[Open-Weight Models|open-weight model]] built outside China, targeting coding, cybersecurity, finance, manufacturing and visual grounding. Preliminary benchmarks look competitive but are only partly verifiable, and the release reflects Mistral's bet that weights will commoditize while value shifts to a [[Sovereign AI]] enterprise stack.

## Core Concepts

- **[[Mistral Large 4]] (ML4 / "Le Chonk")**: 1T total parameters, 49B active, using a [[Mixture of Experts]] sparse architecture; trained from scratch in roughly two months on 4,000 [[Nvidia]] Grace Blackwell GPUs in Mistral's own European data centers, across more than 160 languages.
- **Staged open-weight rollout**: A roughly three-week preview with developers, cybersecurity leaders and government authorities, during which [[Reinforcement Learning]] continues on the final checkpoint before weights go public.
- **Meme origin**: The viral, fictional "Le Chaton Fat" model (June) was amplified by CEO [[Arthur Mensch]] and investor [[Marc Andreessen]]; co-founder [[Guillaume Lample]] calls ML4 an initial version of that idea, with larger models to come.
- **Open weights for cybersecurity**: Mistral argues closed providers' safety systems may refuse legitimate dual-use defensive requests, so open weights give security teams more control.
- **Benchmark claims vs. independent sources**: Covers [[DeepSWE]], Harvey's Legal Agent Benchmark (via [[Vals.ai]]), Finch, Dense200 and DIOR-RSVG; compares against [[Reflection AI]] Beam, Qwen 3.8 Max, [[DeepSeek]] V4 Pro, GLM-5.3 and [[Kimi K3]].
- **Full-stack business strategy**: Products, customization, inference infrastructure and Mistral Compute, sold to more than 125 enterprises including Airbus, [[ASML]] and HSBC.

## Key Takeaways

- **Scale**: 1T parameters, 49B active; Large 3 was 675B/41B on 3,000 H200s.
- **Release date**: Weights publish Oct. 27 under a custom Mistral license; no API pricing given.
- **Coding**: 62% on DeepSWE v1.1 vs. GLM-5.3 61%, DeepSeek V4 Pro 57%, Beam 44%.
- **Leaderboard caveat**: Best-config DeepSWE shows GLM-5.3/Kimi K3 ~69%, frontier closed models ~74%.
- **Legal**: 15% on Harvey's benchmark, ahead of Kimi K3 (12.92%) if methodology matches.
- **Finance**: 67% on Finch, tied with DeepSeek V4 Pro; results not independently located.
- **Visual grounding**: 42% Dense200, 73% DIOR-RSVG; competitor scores unverified in public sources.
- **Funding**: €3B Series D at a post-money valuation above €21B (roughly $24B per Reuters).
- **Team growth**: Lample scaled the science team from 3 to roughly 300 researchers.
- **Provisional ranking**: ML4 is not yet in Artificial Analysis or DeepSWE leaderboards.

## 🧠 First Principles & Mental Models

- **[[Commoditize Your Complement]]**: Mistral releases flagship weights because it expects models to commoditize, and it captures value in the deployment, infrastructure and customization layers around them.

## 🃏 Review Questions

**Q1**: What is Mistral's central strategic claim for Mistral Large 4?
**A**: Not that it beats every closed model, but that it is the strongest open-weight model built outside China and competitive with the best Chinese open systems.

**Q2**: How does ML4's architecture balance size and inference cost?
**A**: It is sparse: it holds one trillion parameters in total but activates only 49 billion during inference, increasing capacity while running just a fraction of the network.

**Q3**: How should an enterprise read ML4's preview benchmarks?
**A**: Treat them as provisional, since several competitor scores can't be independently verified and best-configuration leaderboards rank other models higher. The real test comes after Oct. 27, when outsiders can evaluate the released weights on their own hardware.
