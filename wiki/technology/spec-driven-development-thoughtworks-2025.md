---
type: literature-note
source_url: https://www.thoughtworks.com/insights/blog/agile-engineering-practices/spec-driven-development-unpacking-2025-new-engineering-practices
alternate_source_url: https://thoughtworks.medium.com/spec-driven-development-d85995a81387
author: Liu Shangqi
tags: [spec-driven-development, ai-assisted-development, context-engineering, software-methodology]
date_consumed: 2026-08-03
---

## Summary

Thoughtworks engineer Liu Shangqi frames [[Spec-Driven Development]] (SDD) as one of 2025's most important emerging engineering practices: using well-crafted software requirement specifications as prompts for [[AI Coding Agents]] to generate executable code. A key debate divides practitioners — whether the spec or the generated code is the authoritative artifact — with the author arguing that executable code remains the source of truth while specs serve as its driver. SDD positions itself between vibe coding (too fast, no discipline) and Waterfall (too slow, long feedback cycles), aiming for shorter and more effective feedback loops.

## Core Concepts

- **[[Spec-Driven Development]]** — a paradigm where software requirement specifications are crafted as prompts for AI coding agents; specs define external behavior (inputs/outputs, preconditions, invariants, interface types, state machines) rather than implementation details.
- **Spec vs. Code as Artifact** — the central debate: some view the spec as the sole source of truth with code as a byproduct; the author's position is that specs *drive* code generation but executable code remains authoritative.
- **[[Context Engineering]]** — specs function as compressed contextual information for AI agents, directly connecting SDD to context engineering practices that improve AI output quality.
- **[[Behavior-Driven Development]] (BDD)** — SDD draws on BDD's Given/When/Then structure and few-shot prompting techniques to structure specs in domain language.
- **[[Vibe Coding]]** — the undisciplined AI-assisted coding practice SDD is explicitly designed to replace; characterized by excessive speed without design rigor.
- **[[Waterfall]]** — SDD's other foil; Waterfall failed through long feedback cycles, not through documentation itself — SDD reintroduces design rigor without the latency.
- **Tooling** — [[Cursor]], [[Claude Code]], and [[Context7]] are cited as platforms that natively support SDD workflows.
- **Spec drift** — a challenge where specs diverge from actual system behavior over time, threatening the reliability of AI-generated code.

## Key Takeaways

- **Spec definition**: more than a PRD — specifies external behavior: I/O, preconditions, invariants, interface types, state machines.
- **Domain language**: good specs use domain terminology and Given/When/Then to reduce AI hallucinations.
- **Context compression**: specs are a structured way to compress context for AI coding agents.
- **Not Waterfall**: SDD shortens feedback loops instead of extending them — design rigor without long cycles.
- **Not vibe coding**: SDD reintroduces discipline that vibe coding sacrifices for speed.
- **Core challenges**: non-deterministic code generation, spec drift, hallucination risk, no consensus on artifact primacy.
- **Semi-structured formatting**: spec formatting style improves LLM reasoning quality, not just human readability.
- **CI/CD dependency**: SDD still requires robust CI/CD practices; non-deterministic code generation makes automated testing non-negotiable.
- **Status**: emerging practice — significant evolution expected through 2026.

## 🧠 First Principles & Mental Models

- **[[Garbage In, Garbage Out]]**: Specs are the input to AI code generation; ambiguous or drifted specs directly degrade generated code quality — making spec clarity the highest-leverage investment in an SDD workflow.
- **[[Feedback Loops]]**: SDD's value proposition is precisely calibrating feedback loop length — avoiding Waterfall's excess latency and vibe coding's absent discipline, landing at "shorter and effective" cycles that keep quality tractable.

## 🃏 Review Questions

**Q1**: What is the central definitional debate within spec-driven development?
**A**: Whether the spec or the generated executable code is the authoritative artifact — some treat code as a byproduct of specs; others (including the author) hold that specs drive generation but code remains the source of truth.

**Q2**: What structural elements make a spec effective for AI code generation?
**A**: Good specs define external behavior via input/output mappings, preconditions, invariants, interface types, and state machines, written in domain language using Given/When/Then structure to minimize AI hallucinations.

**Q3**: How does SDD position itself relative to Waterfall and vibe coding, and what does this imply for adoption?
**A**: SDD reintroduces design rigor (absent in vibe coding) while keeping feedback loops short (unlike Waterfall), making it a disciplined middle path — though its status as an emerging practice means workflow standards and tooling are still maturing.
