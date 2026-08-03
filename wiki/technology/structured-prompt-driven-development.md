---
type: literature-note
source_url: https://martinfowler.com/articles/structured-prompt-driven/
author: Wei Zhang, Jessie Jie Xia
tags: [ai-assisted-development, prompt-engineering, software-methodology, thoughtworks]
date_consumed: 2026-08-03
---

## Summary

Structured-Prompt-Driven Development (SPDD) is a Thoughtworks engineering method that treats prompts as first-class delivery artifacts — version-controlled, reviewed, and reused alongside code. Individual AI speed gains don't automatically translate to team-level throughput; SPDD addresses this by making AI-generated changes governable through the REASONS Canvas, a structured seven-part prompt template. The core operating principle is "when reality diverges, fix the prompt first — then update the code."

## Core Concepts

- **[[Structured-Prompt-Driven Development]] (SPDD)** — a [[Thoughtworks]]-developed method where prompts are first-class artifacts, enabling deterministic, traceable, and reviewable AI-assisted code generation at team scale.
- **REASONS Canvas** — a seven-part structured prompt template: Requirements, Entities, Approach, Structure, Operations, Norms, Safeguards; serves as the canonical implementation blueprint for each story.
- **`openspdd` CLI** — toolchain implementing the SPDD workflow via slash commands: `/spdd-story`, `/spdd-analysis`, `/spdd-reasons-canvas`, `/spdd-generate`, `/spdd-prompt-update`, `/spdd-sync`.
- **Prompt-first change management** — logic corrections flow requirements → prompt → code; refactoring flows code → prompt (via `/spdd-sync`), creating a two-track code review discipline.
- **[[Spec-Driven Development]]** — SPDD is a specific instantiation of the broader spec/prompt-as-source-of-truth family, comparable to [[DDSE]] and [[AI Unified Process]].
- **INVEST principle** — user stories produced by `/spdd-story` conform to Independent, Negotiable, Valuable, Estimable, Small, Testable criteria.

## Key Takeaways

- **Team throughput gap**: AI speed gains are individual; SPDD makes them team-scale and governable.
- **REASONS Canvas**: 7-part template — Requirements, Entities, Approach, Structure, Operations, Norms, Safeguards.
- **Prompt-first rule**: when behavior needs to change, update the canvas before changing code.
- **Two-track reviews**: logic fix → prompt first; refactor → code first, then sync canvas.
- **Three core skills**: Abstraction First (design before generate), Alignment (explicit scope), Iterative Review (engineering loop, not one-shot).
- **Best fit**: scaled/standardized delivery and high-compliance constraints (★★★★★); poor fit for hotfixes or exploratory spikes.
- **Cost**: requires senior expertise upfront and automation tooling to avoid throughput ceilings.
- **Core framing**: "The real competition is engineer cognitive bandwidth — how clearly we can think, frame problems, and make decisions."

## 🧠 First Principles & Mental Models

- **[[Garbage In, Garbage Out]]**: Ambiguous requirements fed to AI scale failure; the REASONS Canvas forces clarity at the prompt layer so generated code inherits precision rather than ambiguity.
- **[[Feedback Loops]]**: SPDD's prompt-first correction policy keeps the feedback loop tight — divergence between spec and reality is caught at the canvas level, not after code has propagated downstream.

## 🃏 Review Questions

**Q1**: What problem does SPDD solve that plain AI-assisted coding does not?
**A**: Individual AI speed gains don't translate to team throughput — SPDD makes AI-generated changes governable, reviewable, and traceable by treating prompts as version-controlled delivery artifacts.

**Q2**: How does the REASONS Canvas structure an implementation prompt, and what governs change management?
**A**: The canvas has seven sections (Requirements, Entities, Approach, Structure, Operations, Norms, Safeguards); the change rule is prompt-first for logic corrections and code-first (then sync) for pure refactoring.

**Q3**: When is SPDD a poor fit, and what does that reveal about its underlying assumptions?
**A**: SPDD rates poorly for hotfixes, exploratory spikes, and poorly defined domains — it assumes enough domain clarity to populate the REASONS Canvas upfront, making it unsuitable where requirements are inherently emergent.
