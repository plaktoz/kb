---
type: literature-note
source_url: https://blog.bytebytego.com/p/how-nvidia-builds-open-models-for
author: ByteByteGo
tags: [nvidia, open-models, hybrid-architecture, physical-ai]
date_consumed: 2026-07-29
---

## Summary
NVIDIA is the largest publisher of open AI models, spanning reasoning models ([[Nemotron]]), world models for robots and self-driving cars ([[Cosmos]]), humanoid robot foundation models ([[Isaac GR00T]]), and domain models for drug discovery, quantum computing, and weather forecasting. Its models combine a [[Hybrid Mamba-Attention Architecture]] with [[Mixture of Experts]] and 4-bit ([[NVFP4]]) training co-designed with its Blackwell GPUs to be both fast and capable. NVIDIA open-sources data, training recipes, and RL environments — not just weights — because it needs deep AI understanding to design future chips and because ecosystem growth drives GPU demand.

## Core Concepts
- **[[Nemotron]]** — NVIDIA's reasoning LLM family (Nano/Super/Ultra sizes), now in its third generation.
- **[[Cosmos]]** — NVIDIA's open world-model family for physical AI; predicts next world state from current state and action, used as a shared reasoning backbone.
- **[[Isaac GR00T]]** — vision-language-action foundation model line for humanoid robots, built on Cosmos as its reasoning core.
- **[[Alpamayo]]** — reasoning-based self-driving model family, also built on Cosmos, exposing its chain of cause-and-effect per decision.
- **[[Hybrid Mamba-Attention Architecture]]** — most layers use [[Mamba]] (state space model, linear cost, constant memory) for cheap long-context processing, with a few full-attention layers retained for precise recall.
- **[[Mixture of Experts]] (MoE)** — routes each token to only a few expert sub-layers, giving large capacity at low per-token cost.
- **[[NVFP4]]** — 4-bit number format NVIDIA pretrains its larger models in, co-designed with Blackwell GPU hardware for speed and lower power.
- **[[BioNeMo]]**, **[[Earth-2]]**, **[[Ising]]** — domain-specific open model/tooling lines for biology, climate, and quantum computing.

## Key Takeaways
- "The fastest model is the smartest model" — speed compounds into more training data, more RL rollouts, and cheaper long-thinking at inference.
- Open in NVIDIA's sense includes datasets, RL environments, and recipes, not just downloadable weights.
- NVIDIA open-sources partly for self-honesty: private models are easy to fool yourself about.
- Real bottleneck for better models is diversity of RL training environments, not data or compute alone.
- A unified backbone (CUDA-style "build once, reuse everywhere") lets one team's component (e.g., Cosmos Reason) power robotics, driving, and language efforts.
- NVIDIA moved to the community OpenMDW license to reduce adoption friction.

## 🧠 First Principles & Mental Models
- **[[Unification as Leverage]]**: NVIDIA's CUDA-derived instinct — build one reusable foundation instead of parallel stacks — explains why Cosmos Reason transfers directly into GR00T and Alpamayo without being rebuilt for each domain.
