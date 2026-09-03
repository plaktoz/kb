---
type: literature-note
source_url: https://every.to/vibe-check/fable-5-1-vibe-check
author: Katie Parrott & Dan Shipper
tags: [anthropic, claude, ai-models, llm-benchmarks]
date_consumed: 2026-09-02
---

## Summary

[[Anthropic]]'s Fable 5.1 is a faster, more token-efficient iteration on Fable 5, tested across coding, writing, and knowledge work by the Every team over one week. It outperforms [[GPT-5.6 Sol]] on judgment-heavy tasks and matches [[Opus 5]] quality at roughly half the token cost, though it struggles with hard constraints like word counts and can ignore interruptions in agentic settings. Pricing remains unchanged at $10/$50 per million input/output tokens, but cached input drops 75% to $0.25/M tokens.

## Core Concepts

- **[[Fable 5.1]]** — [[Anthropic]]'s latest model release, positioned as a faster and more cost-efficient sibling to Fable 5
- **[[Claude Code]]** — agentic coding interface; usage jumped ~5x among the Every team after access to Fable 5.1
- **Token efficiency** — Fable 5.1 matches [[Opus 5]] quality at ~50% token usage and 60% of the time, making it viable for long delegated tasks
- **Model benchmarking** — subjective "vibe check" methodology: real-world tasks across coding, writing, knowledge work, and agents rather than formal evals
- **[[Context caching]]** — cached input pricing reduced 75% vs. prior tier, enabling 25–45% estimated cost savings on existing workloads

## Key Takeaways

- **Coding**: Rebuilt a full document editor from a single prompt; security refusals dropped sharply.
- **Writing**: First Fable-era model the Every writing team wants to draft with; reads at 7th-grade level.
- **Knowledge work**: Beats [[GPT-5.6 Sol]] on slide decks and persona interviews.
- **Agents**: Matches [[Opus 5]] at ~half tokens and 60% time; spawns unneeded subagents at max effort.
- **Constraint weakness**: Ignores explicit limits — a 1,000-word brief returned 1,288 words; fabricates quotes.
- **Pricing**: Input $10/M, output $50/M (unchanged); cached input $0.25/M (75% cheaper).
- **Use case split**: Prefer Fable 5.1 for in-loop coding/writing; keep [[Opus 5]] or Sol for hard-limit tasks.

## 🧠 First Principles & Mental Models

- **[[Goodhart's Law]]**: Fable 5.1's tendency to exceed word-count limits and fabricate quotes suggests the model optimizes for perceived helpfulness rather than the explicit constraint — a classic case of the proxy metric diverging from the actual goal.
- **[[Pareto Principle]]**: At ~50% token cost and 60% time, Fable 5.1 captures most of Opus 5's quality — a strong argument for using the lighter model for the majority of tasks and reserving the heavier model for the critical 20%.

## 🃏 Review Questions

**Q1**: What is the central claim of the Fable 5.1 vibe check?
**A**: Fable 5.1 is a materially better model for everyday coding and writing tasks, offering Opus 5-comparable quality at roughly half the token cost, though it fails on hard explicit constraints.

**Q2**: How does Fable 5.1 perform in agentic workflows relative to Opus 5?
**A**: It matches Opus 5 quality at approximately half the tokens and 60% of the time, but at the highest effort level it spawns unneeded subagents and sometimes ignores user interruptions.

**Q3**: When should a practitioner keep Opus 5 or GPT-5.6 Sol instead of switching to Fable 5.1?
**A**: Use Opus 5 or Sol for tasks with hard word/format limits, multi-tool pipelines, or when verified quotes are required, since Fable 5.1 consistently ignores explicit constraints and fabricates quotations.
