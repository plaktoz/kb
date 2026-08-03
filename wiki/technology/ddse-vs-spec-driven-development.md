---
type: literature-note
source_url: https://huggingface.co/blog/mrmanna/ddse-vs-sdd
author: Mahmudur R Manna
tags: [software-engineering, ai-development, decision-records, spec-driven]
date_consumed: 2026-08-03
---

## Summary

Decision-Driven Software Engineering (DDSE) uses a typed hierarchy of Technical Decision Records (TDRs) stored in-repo with CI/CD enforcement and machine-parsable AI context blocks as its source of truth. Spec-Driven Development (SDD), exemplified by GitHub's Spec Kit, treats written specs as truth and converts them into agent-executable plans for tools like Copilot, Claude Code, and Gemini CLI. DDSE targets enterprise-scale governance and parallel delivery; SDD excels in speed-first prototyping and small teams.

## Core Concepts

- **[[Decision-Driven Software Engineering]] (DDSE)**: An engineering methodology where [[Technical Decision Records]] (TDRs) form a typed, in-repo hierarchy enforced by CI/CD; each TDR embeds constraints, verification commands, and machine-parsable AI context blocks.
- **[[Spec-Driven Development]] (SDD)**: A methodology using a written spec as the authoritative source of truth, which is converted into agent-executable plans and tasks consumed by [[AI Coding Agents]] such as [[GitHub Copilot]], [[Claude Code]], and [[Gemini CLI]].
- **[[Contract Decision Records]] (CDR)**: A DDSE primitive providing mock servers, TypeScript type generation, and contract tests to enable parallel front-end/back-end delivery — with no equivalent in SDD.
- **[[Technical Decision Records]] (TDR)**: The core artifact of DDSE; machine-parsable records annotated with decision-to-code traceability requirements and stored directly in the repository.
- **AI Alignment**: DDSE embeds constraints and verification commands into each TDR; SDD's alignment is contingent on spec clarity and individual agent behavior.
- **Governance**: DDSE prescribes authority matrices and CI-enforced compliance; SDD governance is largely team-defined and implicit.

## Key Takeaways

- **DDSE Source of Truth**: TDRs stored in-repo, CI/CD-enforced, with machine-parsable AI context blocks.
- **SDD Source of Truth**: Written spec converted into agent-executable plans for [[AI Coding Agents]].
- **Contract Primitive Gap**: DDSE's CDR enables parallel team delivery; SDD lacks a standardized equivalent.
- **Traceability**: DDSE mandates decision-to-code annotations; SDD's traceability is implicit.
- **Use SDD When**: Prototyping, small teams, or contained subsystems — "low activation energy" for early delivery.
- **Use DDSE When**: Enterprise scale, audit requirements, parallel teams, or AI-accelerated development needing provable governance.
- **Core Framing**: "Decisions run the enterprise" — DDSE positions itself as the sustainable-agility-at-scale model.

## 🧠 First Principles & Mental Models

- **[[Explicit vs. Implicit Contracts]]**: DDSE makes architectural decisions machine-readable and CI-enforced, embodying the principle that implicit contracts eventually become liabilities — especially when AI agents must interpret ambiguous intent at scale.
- **[[Conways Law]]**: DDSE's authority matrices and parallel-delivery CDRs directly address the tendency for software architecture to mirror team communication structures, enforcing deliberate coordination rather than accidental coupling.

## 🃏 Review Questions

**Q1**: What is the fundamental difference in "source of truth" between DDSE and SDD?
**A**: DDSE uses a typed hierarchy of TDRs stored in-repo with CI/CD enforcement as its source of truth, while SDD treats the written spec itself as truth, converting it into agent-executable tasks.

**Q2**: What specific DDSE primitive enables parallel front-end/back-end delivery, and what does it provide?
**A**: Contract Decision Records (CDRs) provide mock servers, TypeScript type generation, and contract tests, enabling parallel team delivery — a capability SDD has no standardized equivalent for.

**Q3**: In what scenarios should a team prefer SDD over DDSE?
**A**: SDD is preferred for prototyping, small teams, and contained subsystems where "low activation energy" for early delivery matters more than governance overhead.
