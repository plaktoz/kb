---
type: literature-note
source_url: https://code.visualstudio.com/docs/agents/guides/context-engineering-guide
author: Unknown
tags: [context-engineering, vscode, github-copilot, ai-agents]
date_consumed: 2026-08-09
---

## Summary

Context engineering in VS Code is a three-step systematic workflow for giving AI agents targeted project information to improve generated code quality. The approach separates concerns across project-wide context, planning, and implementation phases — each handled by a dedicated agent or prompt configuration. A well-tuned setup reduces back-and-forth corrections and helps the AI make more consistent, architecturally aligned decisions.

## Core Concepts

- **[[Context Engineering]]**: Systematic approach to curating the information AI agents receive, distinct from ad-hoc prompting.
- **[[GitHub Copilot]]**: The AI agent in VS Code that consumes context files and follows project-specific instructions.
- **`.github/copilot-instructions.md`**: The always-included context file automatically loaded in all chat interactions — equivalent to [[CLAUDE.md]] in [[Claude Code]].
- **Custom Planning Agent** (`.github/agents/plan.agent.md`): A read-only agent configured to produce structured implementation plans before coding begins.
- **TDD Implementation Agent**: A dedicated agent enforcing test-first development patterns during the implementation phase.
- **[[Progressive Context Building]]**: Adding detail gradually rather than overwhelming the model with an upfront context dump.
- **Agent Handoffs**: Structured transitions between planning, coding, and review agents using configured handoff prompts.

## Key Takeaways

- **Step 1 — Project-wide context**: Create `PRODUCT.md`, `ARCHITECTURE.md`, `CONTRIBUTING.md`; reference them in `.github/copilot-instructions.md`.
- **Step 2 — Planning**: Use a `plan-template.md` and a custom planning agent with read-only tools.
- **Step 3 — Implementation**: Reference the saved plan in a new chat; use a TDD agent for structured code generation.
- **Start small**: Only add rules to instructions when the agent repeatedly makes the same mistakes.
- **Separate concerns**: Distinct agents for planning, coding, and review prevent context pollution.
- **Avoid context dumping**: Excessive unfocused information dilutes agent focus and wastes tokens.
- **Watch token costs**: Larger context and deeper agent chains increase credit consumption.
- **Version your setup**: Track instruction files and agent configs via git for reproducibility.

## 🧠 First Principles & Mental Models

- **[[Signal-to-Noise Ratio]]**: The entire workflow is designed to maximize relevant signal — each layer (product docs, architecture, contributing guidelines) is loaded purposefully rather than dumped wholesale, keeping the agent focused on what matters.
- **[[Separation of Concerns]]**: Dedicating separate agents to planning, coding, and review mirrors a classic software design principle — isolating responsibilities reduces compounding errors across the pipeline.

## 🃏 Review Questions

**Q1**: What is the core claim of VS Code's context engineering guide?
**A**: Context engineering is a systematic three-step workflow — curating project-wide context, creating an implementation plan, and generating code — that reduces back-and-forth corrections and improves AI code quality.

**Q2**: What file is automatically included in all VS Code Copilot chat interactions, and what should it contain?
**A**: `.github/copilot-instructions.md` is auto-included in every chat session; it should reference project documentation files and only contain rules that address repeated agent mistakes, starting small to avoid noise.

**Q3**: How should this workflow be applied when building a new feature in a VS Code project?
**A**: First invoke the planning agent to produce a structured `plan.md` with architecture, tasks, and open questions; then reference that plan in a new chat with the implementation (or TDD) agent to generate code aligned with the existing architecture.
