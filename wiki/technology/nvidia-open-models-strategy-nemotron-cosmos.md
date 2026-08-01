---
type: literature-note
source_url: https://blog.bytebytego.com/p/how-nvidia-builds-open-models-for
author: ByteByteGo / Bryan Catanzaro (interview)
tags: [nvidia, open-source-ai, llm-architecture, physical-ai]
date_consumed: 2026-08-01
---

## Summary

NVIDIA is the world's largest publisher of open AI models, spanning language, robotics, autonomous vehicles, drug discovery, and climate forecasting. Its competitive edge comes from co-designing models and hardware together — training in 4-bit precision on Blackwell-class GPUs from day one — and using a reusable hybrid architecture (Mamba + Transformer + MoE) across all model families. The open-source strategy is deliberate: releasing models, data, and training recipes keeps NVIDIA's researchers honest, grows the ecosystem, and ultimately drives demand for the GPUs that power it all.

## Core Concepts

- **[[Nemotron]]** — NVIDIA's flagship reasoning model family (Nano, Super, Ultra); uses hybrid Mamba-Transformer architecture; 100M+ total downloads on Hugging Face.
- **[[Cosmos]]** — NVIDIA's world model for physical AI; generates physically plausible video, reasons about motion/causality; unified in 2026 as Cosmos 3 with a 4B-parameter Edge variant.
- **[[Isaac GR00T]]** — Open foundation model for humanoid robots (vision-language-action); uses Cosmos as reasoning backbone; enables locomanipulation and step-by-step planning.
- **[[Alpamayo]]** — Open reasoning model for self-driving; shares Cosmos backbone; exposes chain-of-cause-and-effect for developer inspection.
- **[[Mamba (SSM)]]** — State space model that reads sequences in linear time with fixed-size memory; efficient for long contexts but weaker at pinpoint recall.
- **[[Transformer Attention]]** — Quadratic-cost mechanism that lets every token attend to every other; powerful recall but expensive on long inputs.
- **[[Hybrid Architecture (Mamba + Attention)]]** — Most layers are Mamba (efficiency), a few are full attention (recall precision); NVIDIA published this design in 2024; later adopted by Qwen and Kimi teams.
- **[[Mixture of Experts (MoE)]]** — Routes each token to only a subset of expert layers, keeping per-token compute low while total model capacity stays high.
- **[[NVFP4 Training]]** — 4-bit pretraining format co-designed with Blackwell GPU hardware; reduces memory and data movement, translating speed into capability compounding.
- **[[Reinforcement Learning from Environments]]** — Post-training stage where models practice across >1M rollouts; diversity of environments identified as the real bottleneck for capability.
- **[[BioNeMo]]** — Open model family for biology and drug discovery with an autonomous agent toolkit.
- **[[Earth-2]]** — Open models and frameworks for professional-grade weather and climate AI.
- **[[CUDA Unified Foundation]]** — Cultural and architectural precedent: one programmable substrate, everything built on top; took 10+ years to become industry standard.
- **[[OpenMDW License]]** — Linux Foundation community license for open AI models; adopted by NVIDIA to reduce friction and signal genuine openness.

## Key Takeaways

- **Largest open AI publisher**: NVIDIA's models span language, robotics, AVs, biotech, quantum, and climate.
- **Speed = capability**: faster models train on more data, post-train across more environments, and reason longer at inference.
- **Hybrid architecture**: Mamba layers (linear cost) + attention layers (exact recall) + MoE (large capacity, low per-token cost).
- **Hardware-model co-design**: NVFP4 pretraining was only viable because Blackwell was being built for it simultaneously.
- **RL environment diversity**: identified as the real bottleneck — more environments, not more data or compute.
- **Open means more than weights**: NVIDIA releases training data, post-training datasets, RL environments, and recipes.
- **Reusable foundation**: Cosmos Reason reused inside GR00T; Nemotron backbone shared across all three sizes — "be as lazy as possible."
- **Volunteer culture**: teams choose what to work on; collaboration rewarded with resources, not mandated from the top.
- **Business rationale**: NVIDIA grows when AI grows; open models expand the developer ecosystem = future GPU customers.
- **Nemotron + Cosmos Coalitions**: new program to bring partners in during model development, not just at release.

## 🧠 First Principles & Mental Models

- **[[Platform Strategy]]**: By releasing models, data, and tooling freely, NVIDIA turns AI developers into GPU customers — the same logic that made CUDA dominant: own the platform layer, profit from the infrastructure layer beneath it.
- **[[Compounding Returns]]**: Speed gains at pretraining compound through post-training and inference — a faster model is cheaper to RL-train across more environments, which yields a more capable model, which justifies more investment. NVIDIA explicitly designs this flywheel in.
- **[[Lazy Evaluation / Reuse Principle]]**: Building one unified foundation (Cosmos as reasoning backbone, shared hybrid architecture) and reusing it across robotics, AVs, and language avoids the combinatorial cost of parallel reinvention — Bryan calls this "being as lazy as possible," which is first-principles resource allocation.
