---
type: literature-note
source_url: https://claude.com/blog/getting-started-with-loops
author: Delba de Oliveira and Michael Segner
tags: [loop-engineering, claude-code, agentic-workflows, ai-agents]
date_consumed: 2026-08-03
---

## Summary

The Claude Code team defines loops as agents repeating cycles of work until a stop condition is met, and classifies them along four axes: trigger mechanism, stop condition, primitive used, and task type. Four canonical loop types — turn-based, goal-based, time-based, and proactive — form a spectrum from human-initiated, short-horizon work to fully autonomous, event-driven long-running processes. Quality and cost discipline scales with loop autonomy: cleaner codebases, second-agent review, and right-sized models reduce waste at higher autonomy levels.

## Core Concepts

- **[[Loop Engineering]]** — structuring [[AI Agents]] to repeat cycles of work until a defined stop condition is met, rather than responding to a single prompt
- **[[Turn-Based Loop]]** — user-prompted; [[Claude Code]] stops when it judges the task complete or needs context; best for exploratory, shorter tasks with human in the loop
- **[[Goal-Based Loop]] (`/goal`)** — user defines explicit success criteria and a turn cap; an [[Evaluator Model]] checks the stop condition before allowing termination; best for deterministic criteria like test pass rates
- **[[Time-Based Loop]] (`/loop`, `/schedule`)** — triggered on an interval; `/loop` runs locally, `/schedule` moves execution to the cloud; suited for polling or recurring work
- **[[Proactive Loop]]** — event- or schedule-driven with no real-time human involvement; combines `/schedule`, `/goal`, skills, dynamic workflows, and auto mode for well-defined recurring work
- **[[Evaluator Model]]** — a second agent that verifies whether the goal-based stop condition is actually satisfied before the primary agent terminates
- **[[SKILL.md]]** — configuration file where quantitative verification criteria are encoded to improve turn-based loop quality

## Key Takeaways

- **Four loop axes**: trigger, stop condition, primitive used, task type classify every loop type.
- **Turn-based**: exploratory; add quantitative checks to SKILL.md for quality.
- **Goal-based**: evaluator model enforces deterministic stop conditions.
- **Time-based**: `/loop` is local; `/schedule` moves recurring work to the cloud.
- **Proactive**: fully autonomous; combines schedule + goal + skills + auto mode.
- **Quality levers**: clean codebase, self-verification tools, second-agent code review.
- **Cost levers**: match model size to task complexity; pilot before large runs.
- **Monitoring**: use `/usage`, `/goal`, and `/workflows` to track token consumption.

## 🧠 First Principles & Mental Models

- **[[Autonomy-Oversight Tradeoff]]**: Each loop type trades human oversight for operational throughput — the more autonomous the loop, the stronger the upfront spec and verification tooling must be to compensate for reduced human correction opportunities.
- **[[Evaluator-Generator Pattern]]**: Goal-based loops instantiate the classic generator/evaluator split — one agent produces work, a second independently judges whether success criteria are met — preventing the primary agent from rationalizing early termination.

## 🃏 Review Questions

**Q1**: What is the core definition of a "loop" as used by the Claude Code team?
**A**: Loops are agents repeating cycles of work until a stop condition is met, classified by trigger mechanism, stop condition, primitive used, and task type.

**Q2**: How does a goal-based loop prevent the agent from terminating prematurely?
**A**: An evaluator model checks the user-defined success condition before allowing the agent to stop, ensuring deterministic criteria like test pass rates are genuinely satisfied.

**Q3**: When should you use a proactive loop instead of a time-based loop?
**A**: Use a proactive loop for long-running, well-defined recurring work that requires no real-time human involvement, combining `/schedule`, `/goal`, skills, and auto mode together.
