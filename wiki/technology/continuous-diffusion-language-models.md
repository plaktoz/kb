---
type: literature-note
source_url: https://sander.ai/2026/08/24/continuous-dlms.html
author: Sander Dieleman
tags: [diffusion-models, language-models, nlp, generative-ai]
date_consumed: 2026-08-31
---

## Summary

Sander Dieleman surveys the full arc of continuous diffusion language models (CDLMs), from their emergence in 2022 through near-extinction in 2023 and their strong comeback in 2025–2026. The primary driver of the revival is a distillability advantage: continuous methods support trajectory-based step distillation far more naturally than discrete approaches, enabling fewer sampling steps and faster inference. Several recent papers argue that continuous methods now scale competitively with discrete diffusion models.

## Core Concepts

- **[[Continuous Diffusion Language Models]] (CDLMs)** — models that embed discrete tokens in continuous space and apply Gaussian noise, as opposed to discrete diffusion models that corrupt token identities directly
- **[[Discrete Diffusion Models]]** — earlier dominant paradigm (D3PM, multinomial diffusion, SUNDAE); structurally limited in few-step generation because simultaneously sampled tokens are assumed conditionally independent
- **[[Diffusion-LM]] / CDCD / SED** — early 2022 continuous approaches that pioneered the embedding-then-noise pipeline
- **[[Flow Maps]]** — described as "essentially the integral of a diffusion model"; the conceptual bridge that inspired the 2025–2026 wave (Categorical Flow Maps, LangFlow, RePlaid)
- **[[Self-Conditioning]]** — passing prior denoiser predictions forward as input to the next denoising step; yields large performance gains at the cost of breaking strict statelessness
- **[[Step Distillation]]** — compressing a multi-step diffusion trajectory into fewer steps via knowledge distillation; structurally easier in continuous space
- **[[Generative Perplexity]] (GenPPL)** — the dominant evaluation metric for diffusion LMs, but easily gamed and biased toward autoregressive surrogates
- **[[Sander Dieleman]]** — researcher at DeepMind known for work on generative audio and continuous diffusion approaches

## Key Takeaways

- **2021–2022 emergence**: Discrete diffusion (D3PM) came first; continuous methods (Diffusion-LM, CDCD) followed.
- **2023 near-extinction**: Continuous methods measured ~64x less training-efficient than discrete; field largely abandoned them.
- **2025–2026 revival**: Hybrid bridging models (CADD, CCDD, CANDI) and flow map frameworks reignited continuous research.
- **Core advantage**: Continuous methods distill multi-step trajectories more naturally than discrete methods.
- **Discrete ceiling**: Simultaneous token independence assumption limits few-step quality in discrete diffusion.
- **Open problem**: No consensus recipe; evaluation via GenPPL remains weak and gameable.
- **Latent diffusion for language** (sentence/paragraph-level) remains promising but technically difficult.

## 🧠 First Principles & Mental Models

- **[[Technological Revival Cycle]]**: CDLMs illustrate how a technique abandoned for efficiency reasons can return when the bottleneck shifts — the distillability constraint only became critical once fast inference and post-training steering were paramount, reversing the cost-benefit calculus entirely.
- **[[Goodhart's Law]]**: GenPPL as an evaluation metric is easily optimized against without genuine improvement in language quality — models can game the surrogate metric without actually generating better text, a textbook case of the metric becoming the target.

## 🃏 Review Questions

**Q1**: What is the central argument for why continuous diffusion language models have revived after near-extinction in 2023?
**A**: The primary driver is a distillability advantage — continuous methods support trajectory-based step distillation more naturally, enabling fewer sampling steps and unlocking post-training and steering capabilities critical to modern LLMs.

**Q2**: What structural limitation makes discrete diffusion models harder to distill into fewer steps?
**A**: Discrete diffusion assumes that simultaneously sampled tokens are conditionally independent, which creates a structural ceiling on few-step generation quality that continuous methods do not face.

**Q3**: How should practitioners interpret the current state of evaluation for diffusion language models?
**A**: With caution — generative perplexity (GenPPL), the dominant metric, is easily gamed and biased toward autoregressive surrogates, meaning benchmark improvements may not reflect genuine gains in text quality.
