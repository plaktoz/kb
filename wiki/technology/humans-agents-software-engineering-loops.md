---
type: literature-note
source_url: https://martinfowler.com/articles/exploring-gen-ai/human-agent-loops.html
author: Kief Morris
tags: [ai-agents, software-engineering, human-in-the-loop, agentic-systems]
date_consumed: 2026-07-27
---

## Summary

This [[Martin Fowler]] article by [[Kief Morris]] introduces "harness engineering" — designing AI agent systems where humans govern goals and review outputs rather than approving each step. The key model shift is "on the loop" versus "in the loop": humans set direction and intervene at decision points, while agents execute autonomously within defined guardrails. This framing has direct applicability to software delivery pipelines, CI/CD, and AI coding assistants.

## Core Concepts

- **[[Harness Engineering]]** — designing the scaffolding around AI agents: guardrails, observability, human intervention points
- **"On the loop" vs "in the loop"** — humans as governors of the system rather than step-by-step approvers
- **[[Agentic Flywheel]]** — iterative loop where agents execute, self-evaluate, and escalate only when confidence is low
- **[[Human-Agent Collaboration]]** — role of humans: goal-setting, artifact review, exception handling; not operational supervision

## Key Takeaways

- **"On the loop"**: humans review artifacts and set goals — they don't supervise each agent action
- **Harness design**: instrument loops with observability; define clear entry/exit criteria for human review
- **Confidence signaling**: agents should explicitly flag uncertainty rather than guessing silently
- **Flywheel model**: agents execute → evaluate → self-correct → escalate at decision points only
- **Design for interruption**: humans should be able to pause the loop at any point
