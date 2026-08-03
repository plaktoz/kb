---
type: literature-note
source_url: https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html
author: Kief Morris
tags: [ai-agents, software-engineering, human-in-the-loop, harness-engineering]
date_consumed: 2026-08-03
---

## Summary

[[Kief Morris]] argues against both extremes of AI-assisted development — pure vibe coding with no oversight and micromanaging every agent output. Instead, he proposes "humans on the loop": engineers who build and maintain the harness (specs, quality checks, workflow guidance) that governs agent behavior rather than inspecting individual artefacts. This framing, published on [[Martin Fowler]]'s site, introduces a nested loop model and an agentic flywheel toward self-improving systems.

## Core Concepts

- **The "why" loop vs. the "how" loop** — the why loop iterates on ideas to produce working software (always human-owned); the how loop handles the mechanics of building via code, tests, specs, and tooling
- **Three stances toward AI agents**:
  - *Humans outside* — vibe coding; agents run the how loop entirely without oversight
  - *Humans in* — humans inspect and gate every agent output; creates bottlenecks
  - *Humans on* — humans build and maintain the **harness** that guides agents
- **[[Harness Engineering]]** — the collection of specs, quality checks, and workflow guidance controlling agent behavior; the leverage point for on-the-loop humans
- **[[Agentic Flywheel]]** — escalating improvement cycle: agents evaluate loop performance → recommend harness improvements → humans review → low-risk changes progressively automated → production signals feed richer inputs
- **Internal code quality** — still matters under AI not for developer experience, but because clean codebases let LLMs "work faster and spiral less," reducing cost

## Key Takeaways

- **On vs. in the loop**: in-the-loop humans fix bad artefacts; on-the-loop humans fix the system that produced them.
- **Harness is the leverage point**: improving specs, evals, and checks scales better than reviewing each output.
- **Three stances**: outside (pure vibe coding), in (bottleneck), on (scalable governance).
- **Why/how split**: humans always own the why loop; the how loop is where agents operate.
- **Flywheel outcome**: potential for anti-fragile systems that continuously improve themselves.
- **LLM code quality**: clean internal code reduces agent spiral time and token cost.

## 🧠 First Principles & Mental Models

- **[[Systems Thinking]]**: Morris's core move is shifting attention from individual artefact quality to the system producing artefacts — a classic leverage-point reframe that unlocks scalable improvement.
- **[[Goodhart's Law]]**: Fixing individual outputs (in-the-loop) is optimizing the proxy; fixing the harness targets the underlying generative process — exactly what avoids the metric-gaming trap at scale.

## 🃏 Review Questions

**Q1**: What is the central argument of Morris's "on the loop" model?
**A**: Rather than inspecting every agent-generated artefact, humans should improve the harness — the specs, checks, and guidance that shape agent behavior — so the system itself produces better outputs.

**Q2**: How does the agentic flywheel work?
**A**: Agents evaluate their own loop performance using tests and evals, recommend harness improvements, humans review and progressively automate approval of low-risk changes, and production data feeds richer signals back — creating a self-reinforcing improvement cycle.

**Q3**: Why does internal code quality still matter in an AI-assisted workflow?
**A**: Cleaner codebases allow LLMs to work faster and spiral less, directly reducing the time and cost of agentic code generation even when no human reads the internal code.
