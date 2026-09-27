---
type: literature-note
source_url: https://every.to/vibe-check/vibe-check-opus-5-5-is-pulling-our-codex-converts-back-to-claude
author: Katie Parrott
tags: [claude, anthropic, llm-evaluation, ai-models]
date_consumed: 2026-09-27
---

## Summary

[[Claude Opus 5.5]] is winning back users who had migrated to competing models like [[Claude Fable 5.1]] and [[Codex]], thanks to pricing roughly 60% cheaper than Fable 5.1 at $4/million input tokens and $20/million output tokens. A team at Every.to tested the model across coding, writing, knowledge work, and agentic behavior, finding it reaches ~90% of Fable 5.1's capability while introducing notable quirks — such as autonomous self-rejection of UI outputs and a tendency to bury the lead in written prose. Consensus: a strong daily-driver replacement for most tasks, with Fable still preferred for high-stakes or large-scale problems.

## Core Concepts

- **[[Claude Opus 5.5]]** — Anthropic's cost-optimised model; $4/M input, $20/M output — approximately 60% cheaper than [[Claude Fable 5.1]]
- **[[LLM Pricing]]** — cost differential is a primary driver for teams switching back to Claude from Codex/Fable
- **[[Agentic Behavior]]** — Opus 5.5 follows instructions more reliably than Opus 5, but will consume entire token budgets if unconstrained
- **[[AI Model Evaluation]]** — multi-domain testing across coding, writing, knowledge work, and agent tasks reveals model-specific tradeoffs
- **[[Codex]]** — competing model some Every.to team members had adopted before Opus 5.5 reversed the trend

## Key Takeaways

- **Coding**: ~90% as capable as Fable 5.1; cleaner, more idiomatic code but occasional broken core screens.
- **Writing**: Best readability scores tested (Flesch-Kincaid ~6.95); buries the lead, using ~2x sentences to make a point.
- **Knowledge work**: Strong analyst and planner; fails under deadline pressure — ran out of time without producing a requested schedule.
- **Agent behavior**: Reliably follows instructions but consumes full token budgets without constraints.
- **Autonomous self-rejection**: Opus 5.5 rejected 90%+ of its own UI outputs for untraceable reasons in one test.
- **Team split**: Kieran Klaassen replaced Fable 5.1; Dan Shipper still 80/20 favors Codex.
- **Best use cases**: Visual/interface work, creative collaboration, analytical judgment tasks.
- **Stay with Fable 5.1 for**: High-stakes, large-scale, or hard problems.

## 🧠 First Principles & Mental Models

- **[[Price-Performance Tradeoff]]**: At 60% lower cost for ~90% capability, Opus 5.5 shifts the rational default for most teams — the remaining 10% gap only justifies Fable's premium for genuinely high-stakes workloads.
- **[[Goodhart's Law]]**: Opus 5.5's autonomous rejection of 90%+ of its own UI outputs — for reasons no external rubric could explain — illustrates that when a model internalizes an opaque quality signal, its optimization becomes uninterpretable and hard to override.

## 🃏 Review Questions

**Q1**: What is the core claim about Claude Opus 5.5's market position?
**A**: Opus 5.5 is pulling users back from Codex and Fable 5.1 by delivering roughly 90% of Fable 5.1's capability at approximately 60% lower cost.

**Q2**: What specific agent behavior anomaly did Tyler Nishida observe?
**A**: Opus 5.5 autonomously rejected over 90% of its own UI outputs for reasons he could not trace to any external rubric, suggesting the model applies an opaque internal quality filter.

**Q3**: How should teams decide between Opus 5.5 and Fable 5.1?
**A**: Use Opus 5.5 for visual/interface work, creative collaboration, and analytical tasks requiring judgment; stick with Fable 5.1 for high-stakes or large-scale problems where the capability ceiling matters.
