---
type: literature-note
source_url: https://thebcms.com/blog/spec-driven-development/
author: Unknown
tags: [spec-driven-development, ai-coding-agents, ears-notation, software-methodology]
date_consumed: 2026-08-03
---

## Summary

Spec-Driven Development (SDD) treats a versioned, structured specification as the primary artifact — code is derived output, not the source of truth. In the context of AI coding agents, SDD directly addresses three failure modes: intent drift from vague prompts, context decay as codebases grow, and unverifiable output without explicit acceptance criteria. The methodology is structured around a 4-phase loop (Specify → Plan → Tasks → Implement) with human review at each phase boundary.

## Core Concepts

- **[[Spec-Driven Development]]** — the specification is the primary artifact; code is generated from it, not the other way around.
- **[[EARS Notation]]** — Easy Approach to Requirements Syntax; five structured patterns that make requirements AI-parseable: Ubiquitous, Event-driven, State-driven, Unwanted behavior, and Optional features.
- **[[AI Coding Agents]]** — autonomous code-generation systems that benefit from SDD because they require unambiguous, structured input to produce verifiable output.
- **[[Intent Drift]]** — a failure mode where AI agents diverge from original intent due to vague or evolving prompts; SDD mitigates this by anchoring every task to a versioned spec.
- **[[Context Decay]]** — degraded AI performance as codebase complexity grows; SDD counters this by making the spec the persistent source of truth rather than relying on model context.
- **[[Acceptance Criteria]]** — explicit, testable conditions generated from the spec that define when an implementation task is complete.
- **[[Living Specification]]** — a spec that evolves continuously alongside the codebase, version-controlled in the repository alongside code.
- **[[Test-Driven Development]] (TDD)** — related methodology; TDD writes failing tests first, whereas SDD treats the spec as primary with tests generated from it.
- **[[Behavior-Driven Development]] (BDD)** — related methodology covering behavior scenarios; SDD is broader, encompassing architecture, constraints, and non-functional requirements (NFRs).

## Key Takeaways

- **Spec is truth**: code is derived output; the spec is the primary artifact.
- **3 AI agent failure modes**: intent drift, context decay, unverifiable output.
- **4-Phase SDD loop**: Specify → Plan → Tasks → Implement; human review at each boundary.
- **EARS Event-driven pattern**: WHEN [trigger] THE system SHALL [response].
- **EARS State-driven pattern**: WHILE [state] THE system SHALL [behavior].
- **EARS Unwanted behavior pattern**: IF [condition] THEN THE system SHALL [response].
- **SDD vs. TDD**: tests are generated *from* the spec, not written first independently.
- **SDD vs. BDD**: SDD is broader — covers architecture, NFRs, and constraints beyond behavior.
- **SDD vs. Waterfall**: the spec is a living, versioned document, not a frozen upfront design.
- **Tooling landscape (2026)**: GitHub Spec Kit (model-agnostic), AWS Kiro (AWS teams), Claude Code + cc-sdd (terminal-first), Cursor Plan Mode (IDE-first), Tessl (regulated industries).
- **Practical rule**: store specs in the repo under `specs/NNN-feature-name/`; keep each spec to 1–3 pages.
- **"Spec the negative space"**: out-of-scope notes are as important as requirements.
- **Prototypes vs. production**: vibe coding is fine for prototypes; SDD is for production systems.

## 🧠 First Principles & Mental Models

- **[[Garbage In, Garbage Out]]**: AI coding agents amplify whatever the spec says — vague specs produce unreliable code at scale, making specification quality the highest-leverage investment in an AI-assisted workflow.
- **[[Separation of Concerns]]**: SDD cleanly separates *what* the system must do (the spec) from *how* it does it (code), letting the spec evolve independently of implementation choices and keeping AI agents focused on one decision layer at a time.

## 🃏 Review Questions

**Q1**: What is the central claim of Spec-Driven Development, and how does it differ from conventional coding practice?
**A**: The specification is the primary artifact and source of truth; code is derived output generated from it, reversing the conventional assumption that code is canonical and docs are secondary.

**Q2**: What are the five EARS notation patterns, and why do they make requirements more useful for AI coding agents?
**A**: Ubiquitous, Event-driven (WHEN/SHALL), State-driven (WHILE/SHALL), Unwanted behavior (IF/THEN/SHALL), and Optional features (WHERE/SHALL) — their structured syntax removes ambiguity, giving agents unambiguous, parseable criteria to implement and verify against.

**Q3**: How should a team store and scope SDD specs in practice, and when should they use SDD versus vibe coding?
**A**: Store specs in the repo under `specs/NNN-feature-name/`, keep individual specs to 1–3 pages, and include out-of-scope notes as explicitly as requirements; use vibe coding for throwaway prototypes and SDD for production systems where verifiability matters.
