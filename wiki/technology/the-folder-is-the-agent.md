---
type: literature-note
source_url: https://every.to/source-code/the-folder-is-the-agent-rerun
author: Kieran Klaassen
tags: [ai-agents, claude-md, context-engineering, software-engineering]
date_consumed: 2026-09-07
---

## Summary

Kieran Klaassen, sole engineer behind Every's AI email assistant [[Cora]], discovered after three months of failed agent-swarm experiments that a project folder populated with a [[CLAUDE.md]], skill definitions, and institutional knowledge is itself the agent. The same generalist model becomes a specialist purely through accumulated context — no new model needed. He now operates 44 such folders spanning multiple projects, each conferring a distinct persona on the underlying LLM.

## Core Concepts

- **[[Folder-as-Agent Pattern]]**: A directory containing [[CLAUDE.md]], conventions, architecture docs, runbooks, and sub-agent skill files transforms a generalist [[Large Language Model]] into a context-specific specialist.
- **[[Context Engineering]]**: The discipline of curating what goes into a model's context window to shape its behavior — Klaassen's core insight is that this curation lives at the filesystem level, not the prompt level.
- **Persona Isolation via Folders**: `~/cora/` behaves as a [[Rails]] engineer; `~/cora-agent/` behaves as an ops engineer with access to logs, databases, and incident history — same model, radically different agent.
- **Dispatch Layer**: A Ruby daemon using file-based messaging coordinates work. Two commands drive most activity: `/hey` (morning status across projects) and `/orchestrate` (breaks tasks into subtasks and spawns workers in the appropriate folder).
- **[[Agent Orchestration]] Pitfalls**: Encoding crashes from em dashes and curly quotes, context drift, duplicate work across agents, and silent stalls were all encountered before a reliable system emerged.

## Key Takeaways

- **Folder = Agent**: Project folder + [[CLAUDE.md]] + skills = specialist agent, no fine-tuning required.
- **Context is identity**: Same model, different folder → different agent persona entirely.
- **44 folders**: Klaassen operates this pattern at scale across multiple concurrent projects.
- **Two-folder split**: Separate Rails-engineer and ops-engineer folders for the same product prevent context contamination.
- **File-based messaging**: Ruby daemon dispatches work via filesystem; avoids complex RPC.
- **"You can't vibe orchestrate"**: Build the folder, use it, trust it — *then* automate.
- **Failure modes**: Em dash encoding crashes, context drift, duplicate work, silent stalls all real risks.

## 🧠 First Principles & Mental Models

- **[[Specialization via Constraints]]**: Removing degrees of freedom (narrowing context) increases expertise — Klaassen's folders operationalize this by injecting domain constraints at the filesystem level rather than the model level.
- **[[Conway's Law]]** (inverted): The structure of the agent mirrors the structure of the system it maintains — ops folder reflects ops concerns, Rails folder reflects app concerns, keeping cognitive boundaries clean.

## 🃏 Review Questions

**Q1**: What is the central claim of "the folder is the agent"?
**A**: A project folder containing a CLAUDE.md, skill definitions, and institutional knowledge is sufficient to transform a generalist LLM into a domain specialist — the folder *is* the agent.

**Q2**: How does Klaassen use two folders for the same product (Cora), and why?
**A**: `~/cora/` is configured as a Rails engineer and `~/cora-agent/` as an ops engineer with access to logs and incident history; the same underlying model takes on distinct personas because the accumulated context differs.

**Q3**: What is the practical lesson from his orchestration failures?
**A**: "You can't vibe orchestrate" — you must build the folder, use it manually, and trust it before handing it to automation; skipping that grounding phase leads to silent stalls, context drift, and encoding crashes.
