---
type: literature-note
source_url: https://www.hpcwire.com/2026/08/18/whats-hot-now-custom-ai-chips
author: Unknown
tags: [custom-silicon, ai-inference, chip-design, etched]
date_consumed: 2026-08-19
---

## Summary

The AI industry is shifting from standardized GPUs toward custom-built inference silicon as the workload balance moves from training to inference. [[Etched]] raised $700 million at a $21 billion valuation for its transformer-specific Sohu ASIC, joining a wider trend of AMD's Taalas acquisition, Nvidia's Groq acquisition, and OpenAI/Anthropic's own custom-chip efforts.

## Core Concepts

- **[[Application-Specific Integrated Circuit (ASIC)]]**: Chips hard-designed for one workload type (like transformer inference) that trade general-purpose flexibility for dramatic performance gains — Etched's Sohu claims 500,000 tokens/second on Llama 70B, 20x an eight-GPU H100 system.
- **[[Performance-Flexibility Tradeoff]]**: Taalas's HC1 chip hard-wires Llama 3.1-8B weights directly onto silicon for 16,000 tokens/second — nearly 10x the next-fastest chip — but can only run that one model.
- **[[Custom Silicon Race]]**: OpenAI (Jalapeno, with Broadcom/Celestica), Anthropic (in talks with Samsung for 2nm fabrication), and all three major clouds (Google TPU, AWS Trainium, Microsoft Maia) are building proprietary AI chips rather than relying solely on Nvidia.

## Key Takeaways

- **Etched's raise**: $700M at $21B valuation, led by Jane Street (also a customer running an Etched cluster in production); $1B in orders across public and private frontier AI companies and clouds.
- **Nvidia's pivot**: Spent $20B acquiring Groq's assets in December 2025, dropping the DRAM-heavy Rubin CPX GPU roadmap in favor of Groq's low-latency LPU design.
- **AMD's move**: Planned acquisition of Taalas to pair its ASIC with Epyc CPUs and Instinct GPUs in AMD's new Helios rack.
- **Economics driver**: Companies running large fractions of global compute workload gain enough scale to justify eliminating hardware flexibility for throughput gains.

## 🧠 First Principles & Mental Models

- **[[Comparative Advantage]]**: As inference volume dwarfs training volume industry-wide, specializing hardware for the dominant workload (inference) captures more value than staying general-purpose — the same logic that drives economic specialization at any scale.

## 🃏 Review Questions

**Q1**: What is the core claim of this article?
**A**: The AI industry is increasingly investing in custom, workload-specific chips for inference rather than relying solely on general-purpose GPUs, as the industry's compute focus shifts from training to inference.

**Q2**: What specific performance figure illustrates the ASIC advantage?
**A**: Etched claims its Sohu chip generates 500,000 tokens per second on Llama 70B — 20x the throughput of an eight-GPU H100 system — by stripping out support for all non-transformer workloads.

**Q3**: What's the practical risk of this custom-silicon strategy for a company like Etched or Taalas?
**A**: Specialization eliminates programmability — Taalas's chip only runs one specific model — so these companies must continuously redesign hardware as models and market demands change, unlike flexible general-purpose GPUs.
