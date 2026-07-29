---
type: literature-note
source_url: https://simonwillison.net/guides/agentic-engineering-patterns/interactive-explanations/
author: Simon Willison
tags: [agentic-engineering, cognitive-debt, interactive-explanations, coding-agents]
date_consumed: 2026-07-29
---

## Summary

Losing track of how agent-written code actually works creates [[Cognitive Debt]] that compounds like technical debt once the code becomes a black box. [[Simon Willison]] argues one of the best repayment tools is asking a coding agent to build an **interactive or animated explanation** of its own code — illustrated by generating an animated visualization of an "Archimedean spiral placement" word-cloud algorithm that made the mechanism click in a way a written walkthrough hadn't.

## Core Concepts

- **[[Cognitive Debt]]** — the accumulating cost of not understanding code an agent wrote on your behalf, which eventually slows feature planning the same way technical debt slows implementation
- **[[Linear Walkthrough]]** — a written, sequential explanation of a codebase's structure, useful but sometimes insufficient for building real intuition about *how* an algorithm behaves
- **[[Animated Explanation]]** — having an agent generate a visual, interactive artifact that demonstrates a process step by step, going beyond static prose

## Key Takeaways

- **Not all code needs deep understanding**: simple, guessable logic (fetch-and-output) doesn't require the same scrutiny as core application logic
- **A written walkthrough alone can fall short** for building genuine intuition about non-obvious algorithms
- **Animation succeeded where prose didn't**: watching the word-cloud placement algorithm animate made the underlying spiral-search logic obvious at a glance
- **Agents can be asked to explain themselves**: a capable coding agent can generate its own interactive documentation, not just the code
