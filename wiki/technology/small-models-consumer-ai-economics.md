---
type: literature-note
source_url: https://calv.info/small-models-have-arrived
author: Calvin French-Owen
tags: [small-models, consumer-ai, inference-cost, llm-economics]
date_consumed: 2026-08-28
---

## Summary

Cheap, fast small models like gpt-5.6-luna (~$0.10 per complex task) are now viable for consumer AI products that were previously unworkable at $1+ per run. The shift unlocks a new wave of consumer AI companies by making per-request inference costs compatible with subscription pricing. Most organizational and personal work (~95%) falls into "token spewer" territory — high-volume, fast, good-enough tasks — rather than rare frontier-level reasoning.

## Core Concepts

- **[[Small Language Models]]**: Compact inference models that trade some capability ceiling for dramatically lower cost and higher throughput (~100 tokens/second).
- **[[Consumer AI Economics]]**: Traditional consumer apps rely on cheap infrastructure + viral growth + ads; AI inference costs disrupt this until per-task cost falls below ~$0.10.
- **[[Token Spewer Work]]**: Term coined by [[Peter Reinhardt]] (Segment, Charm Industrial) for high-volume, routine, fast-turnaround tasks that represent ~95% of real organizational work.
- **[[IQ 180 Work]]**: Reinhardt's term for rare, breakthrough-level problem solving that genuinely requires frontier models.
- **[[Inference Cost Curve]]**: The ongoing drop in per-token pricing that determines which AI use cases become economically viable.
- **[[Prompt Injection]]**: Security risk that must be solved in tooling before small models can be safely deployed at consumer scale.

## Key Takeaways

- **Cost threshold**: $1/run is unworkable for consumer apps; $0.10/run opens the market.
- **Speed**: gpt-5.6-luna runs at ~100 tokens/second, enabling responsive UX.
- **Work taxonomy**: ~95% of work is "token spewer" (fast/cheap/good-enough), not frontier-level reasoning.
- **Frontier models remain essential** for novel discovery and deep engineering.
- **Ecosystem gap**: Safety, permissions, and [[Prompt Injection]] tooling must catch up before full consumer deployment.
- **Benchmark test**: Personalized daily news aggregator from HN, Reddit, Twitter = ~$0.10 with luna vs ~$1 with Sonnet-class.

## 🧠 First Principles & Mental Models

- **[[Price Elasticity of Demand]]**: As inference cost drops 10x, demand for AI-powered consumer products expands non-linearly — use cases that were economically impossible suddenly become viable at scale, mirroring historical patterns in cloud storage and compute.
- **[[Pareto Principle]]**: Reinhardt's 95/5 split — most work is routine and fast, only a small fraction requires peak capability — suggests that optimizing the commodity tier unlocks disproportionate value relative to improving the frontier tier.

## 🃏 Review Questions

**Q1**: What is the core claim about small models and consumer AI?
**A**: Small models have become cheap enough (~$0.10 per complex task) to make consumer AI products economically viable, unlocking a category that was previously blocked by high per-request inference costs.

**Q2**: What is the "token spewer" vs "IQ 180" distinction, and what percentage of work is each?
**A**: "Token spewer" work is high-volume, fast, good-enough blocking-and-tackling; "IQ 180" is rare breakthrough-level problem solving. Peter Reinhardt estimates ~95% of his own work is token spewer.

**Q3**: What ecosystem gaps still need to close before small models can be widely deployed at consumer scale?
**A**: Tooling around safety, permissions, and prompt injection must mature before small models can be safely rolled out to broad consumer audiences.
