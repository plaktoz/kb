---
type: literature-note
source_url: https://every.to/context-window/why-you-should-burn-more-tokens
author: Laura Entis
tags: [ai-experimentation, token-spending, llm-workflows, team-culture]
date_consumed: 2026-09-18
---

## Summary

Every CEO Dan Shipper uses more than 3x as many tokens as the next-highest employee and treats low token usage as a warning sign that people aren't experimenting boldly enough. The team's philosophy frames high token spend not as waste but as deliberate experimentation, evaluated with three post-run questions: what did it cost, what did it produce, and what was learned. Each team member tunes their model selection to task complexity, dynamically routing routine work to cheaper models and complex features to frontier models.

## Core Concepts

- **[[Token Spend as Signal]]**: Low token usage at [[Every]] is seen as a potential failure of ambition — a signal people aren't pushing limits.
- **[[Deliberate AI Experimentation]]**: High-cost runs are acceptable when they generate learning; the key metric is cost-per-insight, not cost-per-output.
- **[[Multi-Agent Cost Control]]**: [[Randy Counsman]] burned ~4.5 billion tokens with an unbounded [[Codex]] multi-agent setup; recovered by capping agents (5-agent limit), removing redundant layers, and adding concrete visual targets.
- **[[Tiered Model Routing]]**: [[Marcus Moretti]] routes by task complexity — routine work to [[Claude Sonnet]], scoped objectives to [[Claude Opus]], complex features to [[Fable 5.1]].
- **[[Ambiguous Task Targets]]**: Open-ended prompts like "keep improving until done extremely well" cause runaway agent loops; concrete targets for judge agents prevent this.
- **[[Claude Code Max]]**: Weekly usage limits that teams work within by deliberately matching model tier to task scope.

## Key Takeaways

- **CEO leads by example**: Dan Shipper consumes 3x more tokens than any other employee.
- **Low usage as red flag**: Minimal token spend signals insufficient experimentation, not good discipline.
- **Post-run retrospective**: Ask cost, output, and learning after every expensive run.
- **Unbounded agents are risky**: No cap + vague success criteria = billions of wasted tokens.
- **Fix ambiguous targets first**: Add concrete visual benchmarks before re-running agent pipelines.
- **Route down by default**: Delegate to lower models and let the agent decide when to escalate.
- **Team model diversity**: Different roles favor different models — Sol, Fable 5.1, Grok 4.6 subagents, Claude.

## 🧠 First Principles & Mental Models

- **[[Jevons Paradox]]**: Cheaper models encourage more total usage; Every leans into this deliberately — the goal is maximum learning throughput, not minimum cost per token.
- **[[Feedback Loop Design]]**: The three post-run questions (cost / output / learning) create a closed feedback loop that converts expensive failures into institutional knowledge rather than sunk costs.

## 🃏 Review Questions

**Q1**: What is Every's core philosophy about high token spend?
**A**: High token usage signals bold experimentation; low usage is the warning sign — it suggests people aren't pushing limits enough.

**Q2**: What went wrong with Randy Counsman's 3D face model attempt, and how was it fixed?
**A**: An unbounded multi-agent Codex setup with a vague "extremely well" success target burned ~4.5 billion tokens; the fix was capping agents at 5, removing a redundant implementer layer, and adding concrete visual targets for the judge agent.

**Q3**: How does Marcus Moretti manage token costs while staying within Claude Code Max limits?
**A**: He routes by task complexity — Sonnet for routine work, Opus for scoped objectives, Fable 5.1 for complex features — and instructs agents to delegate downward using their own judgment.
