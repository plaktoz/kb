---
type: literature-note
source_url: https://www.techtarget.com/it-strategy/news/366651622/AI-makes-workers-faster-and-reviewers-busier
author: David Linthicum
tags: [ai-productivity, verification-cost, workflow-handoffs, cio-strategy]
date_consumed: 2026-10-06
---

## Summary

[[David Linthicum]] argues that enterprises measure the person using AI rather than the system absorbing AI's output, so they miss the review, verification and exception work that faster generation pushes downstream. AI can make one task cheaper and faster while moving the cost to legal, compliance, QA or senior staff, often the most expensive people in the process. CIOs should therefore measure what happens at the next handoff, not just how much faster a task became.

## Core Concepts

- **"AI moves work. It does not always remove it."**: Linthicum's core thesis; faster output at one step can create more work at the next.
- **[[Trust Gate]]**: Every business-relevant AI output eventually reaches a point where someone or something must decide if it is good enough to use, and that is where work reappears.
- **Task-boundary measurement failure**: Metrics like a rising count of "AI-assisted work products" stop at generation and ignore downstream cost.
- **Downstream effort shift**: Users get faster while reviewers get busier. Development throughput floods [[Quality Assurance|QA]], front-office output creates compliance work, and support closes more tickets while repeat contacts rise.
- **Ownership doesn't transfer**: AI may draft a contract clause, recommend a supplier or summarize a call, but legal, procurement and account management still own the risk, consequence and relationship.
- **[[Verification Cost]]**: Checking sources, testing code, reviewing security, reconciling data, getting approvals and handling exceptions are a real part of AI's cost, not free overhead.
- **Routine vs exception cases**: AI looks strongest on the routine case, while enterprise cost often shows up in the exceptions.
- **Handoff metrics**: Acceptance without material correction, review time, rework, exception rates, escalations and queue time before output becomes an approved decision.

## Key Takeaways

- **Incomplete success story**: One CIO briefing tracked AI usage but not downstream review.
- **Example volume gain**: Sales ops tripled account summaries ahead of quarterly reviews.
- **Real acceleration**: Linthicum's architecture vetting dropped from days to hours per candidate.
- **Hidden queue**: Doubling claims summaries can slow legal review through added validation.
- **Relocation, not transformation**: Throughput gains often just create a queue elsewhere.
- **Expensive absorbers**: Shifted work often lands on the costliest experts in the process.
- **Distrust generation-only claims**: Error rates, rework and expert hours must be counted.
- **Key question**: "What happened at the next handoff?"
- **Map validation ownership**: Know who validates output and whether downstream teams can absorb volume.
- **Core paradox**: AI can make a worker faster and the enterprise slower.

Related: [[workplace-ai-damages-productivity-trust]], [[invisible-burden-ai-developer-productivity-harness-2026]], [[ai-coding-ci-bottleneck-linear-rework]], [[why-ai-is-booming-but-productivity-isnt]], [[ai-productivity-paradox-pc-revolution-parallel]], [[gallup-ajqs-ai-benefits-unevenly-distributed-2026]], [[ai-workplace-adoption]]

## 🧠 First Principles & Mental Models

- **[[Theory of Constraints]]**: Speeding up generation, which isn't the bottleneck, only grows the queue at the real constraint (review and verification), so the overall system gets no faster.
- **[[Second-Order Thinking]]**: Linthicum's question "what happened after those work products were created?" asks about the downstream effects that first-order speed metrics hide.

## 🃏 Review Questions

**Q1**: What is Linthicum's central argument about AI productivity in enterprises?
**A**: AI often moves work instead of removing it. Faster generation by one worker can create more review, verification and exception work downstream, so measuring only the AI user can show a win while the enterprise absorbs the cost elsewhere.

**Q2**: What is a "trust gate," and why does work reappear there?
**A**: A trust gate is the point where someone or something must decide whether AI-generated output is good enough to use. More generated volume means more checking, correction and exception handling at that gate, often by expensive senior staff.

**Q3**: Which metrics should a CIO track to tell whether AI actually removed work?
**A**: Track how much AI output is accepted without material correction, plus review time, rework, exception rates, escalations and queue time before output becomes an approved decision, release or customer response.
