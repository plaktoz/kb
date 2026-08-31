---
source_url: https://sander.ai/2026/08/24/continuous-dlms.html
author: Sander Dieleman
date: 2026-08-24
---

# Continuous Diffusion Language Models

Sander Dieleman surveys the history and recent revival of continuous diffusion language models (CDLMs), tracing the field from 2021 through 2026.

## Historical Arc

- **2021:** First discrete diffusion models for language (D3PM, multinomial diffusion, SUNDAE)
- **2022:** Continuous approaches emerged — Diffusion-LM, CDCD, SED — embedding discrete tokens in continuous space before applying Gaussian noise
- **Late 2023:** Continuous methods went nearly extinct; discrete diffusion dominated, partly due to a measured "64x less efficient" training gap for continuous models

## Core Technical Ingredients for CDLMs

1. **Embedding strategies** — explicit (one-hot), pre-trained (BERT), or jointly learned
2. **Loss functions** — MSE, cross-entropy, or likelihood-based bounds
3. **Noise schedules** — adaptive schedules that linearize entropy across diffusion time
4. **Self-conditioning** — passing prior denoiser predictions forward, yielding large performance gains despite breaking statelessness assumptions

## The 2025–2026 Comeback

Hybrid methods (CADD, CCDD, CANDI) bridged discrete and continuous approaches. Then flow maps — described as "essentially the integral of a diffusion model" — inspired a wave of purely continuous work: Categorical Flow Maps, LangFlow, RePlaid, and others. Several papers argue continuous methods now scale competitively with discrete ones.

## Why Now?

The primary driver is a **distillability advantage**: continuous methods support trajectory-based step distillation more naturally. Fewer sampling steps enable faster inference and unlock post-training/steering capabilities critical to modern LLMs. Discrete diffusion faces a structural ceiling — "simultaneously sampled tokens are assumed to be conditionally independent," limiting few-step quality.

## Open Issues

- No consensus recipe among continuous approaches
- Evaluation methodology remains weak; generative perplexity (GenPPL) is easily gamed and biased toward autoregressive surrogates
- Latent diffusion for language (sentence/paragraph-level representations) remains promising but difficult

## Key Takeaway

> "The distillability advantage is probably the main reason why CDLMs are back with a vengeance today."
