---
type: literature-note
source_url: https://docs.typesafe.ai/patterns
author: Unknown
tags: [jev, system-design, architectural-patterns, ai-automation]
date_consumed: 2026-09-26
---

## Summary

TypeSafe documents four architectural patterns for building reliable AI systems with [[Jev]]: Speculative Fan-Out (ask many questions in one call), Confidence-Gated Routing (use confidence as a safety axis), Composite Scoring (merge dimensions into one score), and Intent Routing (classify and route user intent). Each pattern is designed around the principle that atomic decisions compose into complex system behavior.

## Core Concepts

- **[[Speculative Fan-Out]]** — send many questions in a single Jev call including speculative ones; code decides which answers to use; benefits: cost and speed (all parallel, one API call)
- **[[Confidence-Gated Routing]]** — use confidence as a second decision axis alongside the answer itself; enables systems that act autonomously when certain and escalate when uncertain; benefits: reliability and safety
- **[[Composite Scoring]]** — combine several independent dimensions (e.g. urgency, sentiment, topic) into a single weighted score in code; benefits: cost, reliability, speed
- **[[Intent Routing]]** — classify a user's intent and direct traffic to the appropriate handler; benefits: cost and speed
- **Atomic decision composition** — key mental model: complex system behavior emerges from discrete, single-purpose decisions combined with deterministic code

## Key Takeaways

- **4 patterns**: Speculative Fan-Out, Confidence-Gated Routing, Composite Scoring, Intent Routing
- **Fan-out is cheap**: multiple questions in one call cost almost nothing extra (parallel evaluation)
- **Confidence = second axis**: don't just route on *what* Jev answers — also route on *how confident* it is
- **Composite scoring**: combine dimensions with custom weights in code, not in a prompt
- **Intent routing**: the most common pattern — classify then dispatch

## 🧠 First Principles & Mental Models

- **[[Separation of Concerns]]**: Each pattern separates the AI judgment layer (Jev) from the routing/combination logic (your code), keeping both simple and independently testable.
- **[[Compositionality]]**: Complex, multi-factor decisions are built by composing simple independent judgments — the same principle underlying functional programming and circuit design.

## 🃏 Review Questions

**Q1**: What is Speculative Fan-Out and why is it cost-effective?
**A**: Send many questions — including ones you may not need — in a single Jev call and let your code decide which answers to use. It's cost-effective because all questions are evaluated in parallel with minimal overhead, so asking 10 questions costs almost the same as asking 1.

**Q2**: How does Confidence-Gated Routing add safety beyond simple intent classification?
**A**: It uses confidence as a second decision axis — the system acts automatically on high-confidence answers but routes low-confidence ones to humans or a fallback, preventing wrong auto-routes on uncertain cases.

**Q3**: When would you choose Composite Scoring over a single Score question?
**A**: When the target dimension is multi-factorial (e.g. "overall quality" depends on accuracy, clarity, and tone separately). Composite Scoring evaluates each dimension independently and combines them with a custom formula in code, making the weights adjustable without rewriting prompts.
