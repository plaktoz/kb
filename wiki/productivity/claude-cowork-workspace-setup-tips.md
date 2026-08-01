---
type: literature-note
source_url: https://www.youtube.com/watch?v=4wvLHFgnQZQ
author: Jeff Su
tags: [claude, cowork, workspace, productivity, memory-management, obsidian]
date_consumed: 2026-08-02
---

## Summary

After five months of daily Claude Co-Work use, Jeff Su distills five foundational setup decisions that prevent compounding inefficiencies: using Obsidian as a markdown editor, keeping the root `claude.md` under 300 lines, structuring `memory.md` with clear sections and a 150-line ceiling, migrating Claude Projects into Co-Work workstations, and distinguishing workstations from skills by whether it is a "place you work" or "a thing you do."

## Core Concepts

- **[[Claude Co-Work]]**: Agentic Claude desktop feature that reads a folder of markdown files as a persistent workspace, routing tasks to specialized workstations.
- **[[Obsidian]]**: Free markdown editor used here purely as a lens to read and edit `.md` files without touching code — no Obsidian features needed beyond file rendering.
- **[[claude.md]]**: Root instruction file loaded on every session; governs tone, rules, routing map, and references to on-demand files.
- **[[memory.md]]**: Root context file loaded each session; stores active projects, scheduled tasks, and persistent facts — distinct from `claude.md` which holds behavioral rules.
- **[[Workstation]]**: A Co-Work folder dedicated to an ongoing area of work (e.g., newsletter, email), carrying its own `claude.md` and `memory.md`.
- **[[Claude Skill]]**: A repeatable checklist-driven process that runs autonomously and returns a predictable output format — no human decisions required mid-run.
- **[[PARA Method]]**: Tiago Forte's Projects / Areas / Resources / Archive framework; recommended for organizing files inside Co-Work by actionability rather than type.

## Key Takeaways

- **Obsidian as viewer**: Install Obsidian, point it at the Co-Work folder, and use it to read and edit `.md` files legibly. No learning curve beyond file editing. Enable "show all file types" to see PDFs and images in the sidebar.
- **300-line rule**: Keep root `claude.md` between 200–250 lines (300 absolute max). Cutting from 600 to 250 lines reduced token usage by ~25%. Test: Does Co-Work need this every session? If not, relocate it to a reference file and add a one-line pointer.
- **claw.md vs memory.md test**: If an entry uses prescriptive language ("always", "never", "before X do Y"), it belongs in `claude.md`. If it records a changeable fact, it goes in `memory.md`.
- **Memory diet**: Structure root `memory.md` with three sections — active projects, scheduled tasks, core facts. Set a 150-line ceiling with a rule to compress and archive, never raise the ceiling.
- **Archive.md pattern**: Active memory is a whiteboard; `archive.md` is the filing cabinet. Co-Work reads `archive.md` only on demand ("what happened with X three months ago?"), so it costs zero tokens per session.
- **Per-workstation memory**: Create a separate `memory.md` per workstation and project so root memory stays under 100 lines despite months of use.
- **Project transplant**: Migrate Claude Projects into Co-Work: project instructions → workstation `claude.md`; project memory → `memory.md`; knowledge files → resources folder. Co-Work also auto-updates the routing map.
- **Workstation vs. skill test**: Workstation = an ongoing area with accumulated context and voice. Skill = a repeatable process with a predictable, automatable output format. Apply both together: the workstation holds the newsletter workflow (human decisions required); a newsletter subject-line skill runs autonomously on the finalized draft.

## 🧠 First Principles & Mental Models

- **[[Token Economics]]**: Every line in files loaded at session start has a per-session token cost. Treating `claude.md` and `memory.md` as expensive real estate — and externalizing anything not needed every session — is a direct application of cost-minimization to context windows.
- **[[MECE Principle]]**: The governance rule Jeff adds to his workspace — instructions must be "mutually exclusive and collectively exhaustive" — ensures no rule overlap or gap, preventing conflicting instructions as the workspace grows.
- **[[Compounding Systems]]**: Each improvement to the workspace (tighter rules, better routing, richer memory) raises the baseline quality of every future session. This is why migrating from Claude Projects to Co-Work is framed as unlocking compounding: changes persist and build, rather than resetting per chat.

## Related Notes

- [[claude-ai-full-tutorial-basics-to-agentic-2026]] — three-tier overview of Co-Work's place in the broader Claude ecosystem
- [[andrej-karpathy-llm-wiki-obsidian-codeex]] — Karpathy's use of Obsidian + Claude Code for a personal knowledge base
- [[llm-wiki-knowledge-base-obsidian-claude-code]] — parallel vault + Claude Code workflow
- [[claude-deep-work-planning]] — using Claude for pre-block deep work planning
