---
type: literature-note
source_url: https://jyn.dev/tokens-too-cheap-to-meter/
author: jyn
tags: [ai-inference, token-cost, llm-economics, compute-efficiency]
date_consumed: 2026-09-24
---

## Summary

AI inference costs are collapsing across hardware, software, and model architecture simultaneously, yielding roughly 2.5 orders of magnitude cost reduction per task over the past year. The author argues this cost implosion is not just about cheaper compute but about the emergence of cheap *intelligence*, fundamentally reshaping what software is worth building and how value accrues. When token costs fall below the cost of conventional tool calls like grep or HTML parsing, the economics of software development itself change.

## Core Concepts

- **[[AI Inference Cost Collapse]]**: Multi-dimensional compression — hardware efficiency, inference engine optimization, and model architecture improvements — compounding simultaneously to drive costs down ~2.5 orders of magnitude per task in one year.
- **[[GPU Energy Efficiency]]**: GPU efficiency doubles roughly every two years (continuous since the [[Moore's Law]] era of the 1960s), independent of model improvements.
- **[[vLLM]]**: Inference engine that improved ~40% in energy efficiency over just 15 months through software-only optimization.
- **[[Mixture-of-Experts]] (MoE)**: Model architecture allowing ~7x smaller models to achieve equivalent benchmark performance by routing inputs to specialized sub-networks.
- **[[Mamba-Transformer Hybrid]]**: Architecture combining state-space models with transformers, reducing RAM requirements by ~5x and enabling more capable local inference.
- **[[Software Moat Erosion]]**: When intelligence is cheap, differentiation via code-based features erodes; operational excellence and security become the primary value drivers.
- **[[LLM-as-Unix-Pipe]]**: Emerging pattern of embedding cheap classifiers directly into CLI pipelines — e.g. a classifier priced at $42/billion tokens enabling AI-native shell tooling.

## Key Takeaways

- **Cost trajectory**: ~2.5 orders of magnitude per-task cost reduction in the past year alone.
- **Hardware**: GPU energy efficiency doubles every ~2 years, an independent compounding factor.
- **Software**: vLLM achieved 40% energy efficiency gain in 15 months via software only.
- **MoE**: Models can be 7x smaller while matching larger model benchmark performance.
- **Mamba hybrids**: ~5x RAM reduction enables richer local/edge inference.
- **Below tool-call costs**: Token costs approaching or below cost of grep, HTML parsing, builds.
- **Value shift**: Software moats weaken; security and operational reliability become key differentiators.
- **New user option**: Beyond use/don't use/switch — users can now ask an LLM to build the tool.
- **Binding constraint shifts**: From raw token volume to quality and access.

## 🧠 First Principles & Mental Models

- **[[Jevons Paradox]]**: As inference efficiency improves and costs fall, total AI usage expands faster than efficiency gains — cheap intelligence will be consumed in ever-larger quantities, not merely substituted for existing tool calls.
- **[[Commoditization of Complements]]**: When a key input (intelligence) becomes nearly free, value shifts to adjacent layers — in this case, from model capability to security, reliability, and operational trust. Joel Spolsky's principle explains why software moats built on feature complexity will erode fastest.

## 🃏 Review Questions

**Q1**: What is the core claim about AI inference costs in the article?
**A**: Inference costs are collapsing across hardware, software, and model architecture simultaneously, yielding roughly 2.5 orders of magnitude per-task cost reduction over the past year — representing the arrival of cheap *intelligence*, not merely cheap compute.

**Q2**: What specific architectural and software improvements are driving the cost collapse?
**A**: Mixture-of-Experts enables ~7x smaller models at equivalent performance; Mamba-Transformer hybrids cut RAM requirements by ~5x; and inference engines like vLLM improved 40% in energy efficiency through software optimization alone over 15 months.

**Q3**: What does it mean for software development when token costs fall below conventional tool-call costs?
**A**: Software moats based on coded features erode, since LLMs can replicate them cheaply; operational excellence and security become the primary value drivers, and users gain the option to have an LLM build any missing tool rather than waiting for a vendor.
