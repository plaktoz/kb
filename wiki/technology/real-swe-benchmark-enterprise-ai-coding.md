---
type: literature-note
source_url: https://withspecific.com/benchmarks/real-swe
author: Specific Labs
tags: [ai-coding, benchmarks, software-engineering, enterprise-ai]
date_consumed: 2026-09-13
---

## Summary

Specific Labs introduced Real-SWE, a benchmark evaluating frontier AI models on private, real-world enterprise codebases licensed from actual companies — not synthetic or public tasks. The benchmark uses "native harnesses" mirroring how enterprise engineers actually work, with tasks drawn from production systems involving genuine business consequences. Results show all models struggle significantly, with even the top performer ([[Fable 5.1]]) resolving only 38.8% of tasks, and 6 of 10 tasks having resolution rates below 15%.

## Core Concepts

- **[[Real-SWE Benchmark]]** — Evaluation framework using private enterprise codebases to test AI coding agents on tasks that are "natively out of distribution" and unavailable on the public internet.
- **[[Native Harnesses]]** — Task execution environments that mirror how enterprise engineers actually work (e.g. [[Claude Code]], [[Codex CLI]], [[Gemini CLI]]), rather than standardized scaffolding.
- **[[Pass@1 Resolution Rate]]** — Primary metric: percentage of tasks solved correctly on the first attempt, averaged over 8 runs per task.
- **[[Missed Requirements Failure Mode]]** — The most common failure across models; the AI omits required behaviors rather than implementing them incorrectly.
- **[[Fable 5.1]]** (Anthropic) — Top-ranked model at 38.8% resolution rate, using [[Claude Code]] as its harness.
- **[[GPT-6 Astra]]** (OpenAI) — Second-ranked at 33.8%, using [[Codex CLI]].
- **[[Gemini 3.8 Flash]]** (Google) — Third-ranked at 31.2% at ~$2.50/rollout, offering strong cost-efficiency relative to performance.

## Key Takeaways

- **Top Model**: [[Fable 5.1]] leads at 38.8% resolution rate using [[Claude Code]].
- **Cost Efficiency**: [[Gemini 3.8 Flash]] scores 31.2% at ~$2.50/rollout vs. Fable's $6.96.
- **Task Complexity**: Median reference solution touches 11 files vs. 6 in competing benchmarks.
- **Hardest Task**: "Analytics stream reducer" had 0% resolution rate across all models.
- **Time Not Bottleneck**: Short rollouts (<10 min) failed 71.4% vs. 73.4% for longer ones.
- **Top Failure Mode**: "Missed requirement" — e.g. Grok 4.6 shows this in 67.2% of failures.
- **Integration Errors**: [[Gemini 3.8 Flash]] suffers integration errors in 49.1% of failed runs.
- **Regression Risk**: Models frequently break existing behavior while attempting fixes.

## 🧠 First Principles & Mental Models

- **[[Goodhart's Law]]**: Public benchmarks like SWE-bench have become optimization targets — models trained to score well on public data fail when the distribution shifts to genuinely private enterprise code, exposing the gap between benchmark performance and real capability.
- **[[Out-of-Distribution Generalization]]**: Real-SWE's "natively out of distribution" design principle exposes that frontier models' coding skills are partially pattern-matched to public repositories rather than grounded in deep software reasoning.

## 🃏 Review Questions

**Q1**: What makes Real-SWE different from existing coding benchmarks like SWE-bench?
**A**: Real-SWE uses private, real-world enterprise codebases licensed from actual companies, with tasks involving genuine business consequences — none of the tasks appear anywhere on the public internet, making them truly out-of-distribution for all models.

**Q2**: What is the most common failure mode across models, and what is a notable per-model example?
**A**: "Missed requirement" is the most common failure — the model omits required behaviors entirely. Grok 4.6 shows this in 67.2% of its failed runs, while Gemini 3.8 Flash has integration errors (correct idea, wrong wiring) in 49.1% of its failures.

**Q3**: What does the cost-vs-performance tradeoff suggest for enterprise AI adoption decisions?
**A**: Higher cost does not guarantee better results — Gemini 3.8 Flash achieves 31.2% resolution at ~$2.50/rollout compared to the top model's 38.8% at ~$6.96/rollout, suggesting teams should evaluate cost-efficiency rather than assuming the most expensive model is best.
