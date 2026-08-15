---
source_url: https://thebcms.com/blog/spec-driven-development/
author: Unknown
date: 2026-08-03
---

# Spec-Driven Development (SDD): The Definitive 2026 Guide

Spec-driven development (SDD) is a methodology where a versioned, structured specification serves as the primary artifact — code is derived output, not the source of truth.

## Core Problem It Solves

AI coding agents suffer from three failure modes: intent drift from vague prompts, context decay as codebases grow, and unverifiable output without explicit criteria.

## The 4-Phase Loop

1. **Specify** – Write user stories and acceptance criteria
2. **Plan** – Translate spec into architecture and technical choices
3. **Tasks** – Break the plan into atomic, independently shippable units
4. **Implement** – Agent executes tasks, verified against the spec

Human review occurs at each phase boundary.

## EARS Notation

Five patterns make requirements AI-parseable:

- **Ubiquitous** – always-true rules
- **Event-driven** – WHEN [trigger] THE system SHALL [response]
- **State-driven** – WHILE [state] THE system SHALL [behavior]
- **Unwanted behavior** – IF [condition] THEN THE system SHALL [response]
- **Optional features** – WHERE [feature enabled] THE system SHALL [behavior]

## Key Tools

| Tool | Best For |
|------|----------|
| GitHub Spec Kit | Model-agnostic, portable |
| AWS Kiro | AWS-integrated teams |
| Claude Code + cc-sdd | Terminal-first solo devs |
| Cursor Plan Mode | IDE-first teams |
| Tessl | Regulated industries |

## SDD vs. Related Methodologies

- **vs. TDD:** TDD writes failing tests first; SDD treats the spec itself as primary, with tests generated *from* it
- **vs. BDD:** SDD is broader — it encompasses architecture, constraints, and NFRs, not just behavior scenarios
- **vs. Waterfall:** The spec is a living, versioned document that evolves continuously alongside code

## Practical Guidance

- Store specs in the repo (e.g., `specs/NNN-feature-name/`)
- Write a "constitution" first — project-wide rules as ubiquitous EARS statements
- Keep individual specs to 1–3 pages; split if larger
- "Spec the negative space" — out-of-scope notes are as important as requirements
- Vibe coding remains useful for prototypes; SDD is for production systems
