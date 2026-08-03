---
type: literature-note
source_url: https://brooker.co.za/blog/2026/04/09/waterfall-vs-spec.html
author: Marc Brooker
tags: [spec-driven-development, ai-agents, software-methodology, abstraction]
date_consumed: 2026-08-03
---

## Summary

Marc Brooker argues that [[Spec-Driven Development]] (as implemented in tools like [[Kiro]]) is routinely mischaracterized as a return to [[Waterfall]] methodology. The key distinction: specs are not exhaustive upfront designs but *elevated*, living artifacts that sit above implementation and evolve iteratively — making the specification itself the primary thing being iterated on, not the code. Because implementation is increasingly AI-generated downstream of the spec, humans shift their energy to refining requirements and resolving trade-offs in the outer loop.

## Core Concepts

- **[[Spec-Driven Development]]** — a methodology where specifications are the primary iterated artifact; code is generated downstream, increasingly by AI agents.
- **Specs as elevated artifacts** — specs are explicit statements of requirements and key design decisions, intentionally abstracted above implementation; they are neither code nor exhaustive upfront blueprints.
- **[[Waterfall]] misconception** — the "specs = waterfall" criticism conflates upfront documentation with iterative specification; Agile principles accept that requirements are dynamic, conflicting, and incomplete.
- **Specification formats** — specs can use free-form language, structured formats ([[RFC2119]], [[EARS]]), or formal methods ([[TLA+]], [[Lean 4]]) depending on precision needs.
- **AI agents and autonomous work** — specs give AI agents a "map" rather than turn-by-turn prompts, enabling extended autonomous operation and producing higher-quality, better-tested code.
- **Human outer loop** — humans remain essential for refining specs, navigating trade-offs, and resolving conflicting requirements; the inner loop (implementation) is increasingly delegated to AI.
- **Abstraction progression** — software history is a march toward higher abstraction: switches → gates → instructions → code → specs; spec-driven development is the next step in this sequence.

## Key Takeaways

- **Specs iterate, not freeze**: the spec is the living artifact; code is generated output.
- **Waterfall's flaw is late feedback**, not documentation — specs with fast iteration cycles avoid this.
- **AI agents need a map**: specs provide goal context for autonomous multi-step AI work.
- **Higher spec quality → better AI output**: clear specs produce higher-quality, better-tested code.
- **Humans own the outer loop**: trade-off navigation and requirement resolution remain human responsibilities.
- **Multiple spec formats**: RFC2119, EARS, TLA+, Lean 4 each offer different precision/expressiveness tradeoffs.
- **Historical abstraction trend**: specs are the latest step in software's centuries-long abstraction ladder.

## 🧠 First Principles & Mental Models

- **[[Abstraction Ladder]]**: Every major productivity leap in software (assembly → HLL → frameworks → specs) raises the floor of what humans touch directly; spec-driven development is precisely this pattern applied at the requirements layer, not just the code layer.
- **[[Inner Loop / Outer Loop]]**: Brooker's framing maps cleanly onto control-theory loops — AI handles the fast inner loop (code generation), while humans govern the slower outer loop (spec refinement and trade-off resolution), matching each agent to the timescale it handles best.

## 🃏 Review Questions

**Q1**: What is Brooker's core rebuttal to the claim that spec-driven development is just waterfall?
**A**: Specs are elevated, living artifacts iterated continuously — it is the *specification* that is being refined, not a frozen upfront document; this is the opposite of Waterfall's late-feedback, big-design-upfront model.

**Q2**: How do specs change the way AI agents operate compared to prompt-by-prompt instructions?
**A**: Specs give AI agents a "map" of the broader goal, enabling extended autonomous work rather than step-by-step direction; this produces higher-quality and better-tested code because the agent understands full context.

**Q3**: What role does Brooker assign to humans in a spec-driven, AI-assisted development workflow?
**A**: Humans own the outer loop — refining specs, navigating trade-offs, and resolving conflicting requirements — while the inner loop of code generation is delegated to AI agents.
