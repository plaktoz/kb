---
type: literature-note
source_url: https://www.anthropic.com/claude-opus-5-5
author: Anthropic
tags: [anthropic, claude, ai-models, llm-pricing]
date_consumed: 2026-09-23
---

## Summary

[[Anthropic]] released [[Claude Opus 5.5]], the first model in their 5.5 family, delivering performance comparable to [[Claude Fable 5.1]] on most tasks at 40% lower cost than [[Claude Opus 5]]. The model leads benchmarks in agentic coding, computer use, and knowledge work while introducing stronger safety guarantees — approximately 85% fewer containment boundary violations than its predecessor. It also ships with redesigned communication defaults that prioritize clarity and user-defined writing rules.

## Core Concepts

- **[[Claude Opus 5.5]]** — new cost-optimised flagship from [[Anthropic]]; sits below Opus 5 in price but matches [[Claude Fable 5.1]] on most evals
- **[[Agentic Coding]]** — benchmark category where Opus 5.5 leads; demonstrated by a 680,000-line code migration completed in under one day
- **[[Containment Boundaries]]** — safety constraint layer; Opus 5.5 violates these ~85% less often than Opus 5
- **[[Preserved Thinking]]** — anti-distillation measure shipped with Opus 5.5 to prevent model weights from being reproduced via output sampling
- **[[LLM Pricing]]** — output tokens priced at $20/1M (vs. $25 for Opus 5); cache reads at $0.20/1M (vs. $0.50)
- **[[Multi-Cloud AI Deployment]]** — available on [[AWS]], [[Google Cloud]], [[Microsoft Azure]], and the Claude Platform

## Key Takeaways

- **Cost reduction**: Opus 5.5 is 40% cheaper than Opus 5 across all token types.
- **Agentic coding**: Completed a 680,000-line migration in under one day.
- **Reliability**: Cut web-app load times successfully 39 out of 40 attempts.
- **Safety**: Best scores on Anthropic's ~2,000-scenario behavioral audit.
- **Anti-distillation**: Ships with "preserved thinking" measures against model distillation.
- **Communication**: Redesigned to lead with key info and follow user writing rules.
- **Biology & cybersecurity safeguards**: Match those of Fable 5.1 at launch.
- **Model ID**: `claude-opus-5-5` on all supported cloud platforms.

## 🧠 First Principles & Mental Models

- **[[Pareto Efficiency]]**: Opus 5.5 achieves Fable 5.1 parity at lower cost — moving one dimension (price) without sacrificing the other (capability) is the hallmark of a Pareto improvement, which drives real adoption.
- **[[Safety as Differentiator]]**: Anthropic's emphasis on behavioural audits and containment metrics reflects a deliberate positioning strategy — safety scores become a competitive moat when enterprise buyers treat risk as a first-class procurement criterion.

## 🃏 Review Questions

**Q1**: What is the core claim about Claude Opus 5.5's performance relative to its predecessor and cost?
**A**: Opus 5.5 matches Claude Fable 5.1 on most tasks while costing 40% less than Opus 5, making it the most cost-efficient high-capability model in Anthropic's lineup.

**Q2**: What specific benchmark or task demonstrates Opus 5.5's agentic coding capability?
**A**: The model completed a 680,000-line code migration in under one day and successfully reduced web-app load times in 39 out of 40 attempts without behaviour-altering side effects.

**Q3**: How does the "preserved thinking" feature affect downstream use of Claude Opus 5.5?
**A**: "Preserved thinking" is an anti-distillation measure that prevents third parties from reproducing Anthropic's model weights by training on Opus 5.5's outputs, protecting Anthropic's IP in deployment.
