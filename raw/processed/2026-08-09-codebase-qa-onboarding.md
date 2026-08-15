# Agent-Powered Codebase Q&A and Onboarding

Source: https://agentpatterns.ai/workflows/codebase-qa-onboarding/

---

## Overview
A structured workflow for using AI agents to explore unfamiliar codebases, generate architecture docs, and accelerate developer onboarding.

---

## The Problem

Program comprehension is among the highest-friction activities in software engineering. Knowledge is scattered across files, commit history, and documentation that quickly drifts from reality. Agents with codebase search tools act as "always-available guides that search the whole codebase" — but their answers aren't always correct, so verification remains essential.

---

## The Workflow

1. **Bootstrap an instruction file** — Run `/init` to generate a `CLAUDE.md` covering build steps, architecture, and conventions
2. **Safe exploration via Plan Mode** — Read-only agent exploration; no unintended changes
3. **Progressive Q&A** — Move from architecture-level to implementation-level questions
4. **Generate architecture documentation** — Produce `docs/architecture.md` with Mermaid diagrams
5. **Feed findings back** — Update instruction files with discoveries; each session compounds into faster future ramp-ups

---

## Progressive Q&A Scope

| Scope | Example Questions |
|-------|------------------|
| Architecture | Main services and how they communicate |
| Data model | Core domain entities and definitions |
| Conventions | Test frameworks, file locations |
| Build & deploy | CI/CD workflows, build scripts |
| Specific flows | End-to-end code path traces |

---

## Knowledge Tiers

Distribute knowledge across three tiers:
- **Hot** — Instruction file, loaded every session
- **Warm** — `docs/` directory, searched on demand
- **Cold** — External knowledge base via MCP or retrieval tools

---

## Key Risk: Comprehension Debt

Over-reliance on agents risks "comprehension debt" — understanding less of your own codebase over time. Mitigations include verifying cited code directly, occasionally implementing features without agent help, and treating generated docs as a starting point rather than a substitute.

---

## Key Takeaways

- Bootstrap `CLAUDE.md` or `AGENTS.md` as the entry point for every session and new team member
- Use Plan Mode for safe, read-only initial exploration
- Verify cited files rather than trusting summaries blindly
- Agents should **accelerate** understanding, not **replace** it
