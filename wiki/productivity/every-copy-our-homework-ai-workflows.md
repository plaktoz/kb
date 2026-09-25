---
type: literature-note
source_url: https://every.to/context-window/copy-our-homework
author: Every Staff
tags: [ai-workflows, computer-use, token-management, ai-tools]
date_consumed: 2026-09-25
---

## Summary

Every's "Copy Our Homework" compiles the week's best AI workflows and prompts into a "steal these" format, drawing from three recent Context Window issues. The digest covers practical delegation techniques for [[Computer Use]], folder-structure prompts for AI agents, and a taxonomy of token spend strategies — framed as immediately actionable templates rather than conceptual overviews.

## Core Concepts

- **[[Computer Use]] Delegation**: [[Codex]] handles calendar management, customer support chats, and IT troubleshooting; [[Douglas Brundage]]'s four-step deck pattern (design reference slides → draft copy → Codex builds deck → save corrections as rules) is a reusable template.
- **Non-Interruption Signal**: [[Randy Counsman]] uses a 🖥️ emoji in a running note to signal to himself (and others) that [[Codex]] is mid-task and should not be disrupted — a simple social protocol for agentic workflows.
- **Folder Audit Prompt**: A pre-restructuring agent prompt that audits folder structure and maps ownership without moving anything until the user approves — prevents destructive reorganization.
- **[[Kieran Klaassen]]'s Memory Architecture**: One folder per job with all required context inside; separate memory files organized by time scale (daily / weekly / monthly / yearly) — mirrors his Tuin/Erf personal system (see [[show-us-your-folders-tuin-erf-ai-workspace]]).
- **[[Token Spend]] Control**: Capping subagents at five and adding a judge agent with concrete visual targets resolved an unbounded swarm that consumed 4.5 billion tokens on one Blender model.
- **[[Tiered Model Routing]]**: [[Marcus Moretti]]'s pattern — [[Claude Sonnet]] for basic checks, [[Claude Opus]] for scoped changes, [[Fable 5.1]] for large feature planning — matches model cost to task complexity.
- **Post-Experiment Review**: Three questions after any expensive AI run: what did it cost, what value was gained, what was learned. Attributed to [[Arielle Shipper]].

## Key Takeaways

- **Deck workflow**: Design reference → Codex copy draft → Codex builds in Google Slides → corrections as saved rules.
- **Emoji as signal**: 🖥️ emoji flags an active Codex session to prevent mid-task interruptions.
- **Audit before restructuring**: Prompt agent to map folder ownership first; approve before any moves.
- **Memory by time scale**: Daily / weekly / monthly / yearly tiers keep context fresh without losing durability.
- **Cap agent sprawl**: Five-agent limit + judge agent with concrete targets prevents runaway token spend.
- **Route down by default**: Delegate to lower-tier models; escalate only when complexity demands it.
- **Make prompt larger than output**: Front-load your own material to constrain AI invention (see [[13-beliefs-about-ai-writing-mike-taylor]]).
- **Post-run retrospective**: Cost + value + lessons converts expensive failures into institutional learning.

## 🧠 First Principles & Mental Models

- **[[Checklists as Protocols]]**: The 🖥️ emoji signal and the pre-restructuring audit prompt both operationalize checklists — low-cost, high-reliability gates that prevent common failure modes (interrupted sessions, destructive refactors) without requiring judgment each time.
- **[[Feedback Loop Design]]**: The three post-experiment questions (cost / value / lessons) close the loop on expensive AI runs, ensuring each failure pays forward as institutional knowledge rather than just sunk cost.

## 🃏 Review Questions

**Q1**: What is the core purpose of Every's "Copy Our Homework" format?
**A**: It distills the week's three Context Window issues into immediately actionable workflows and prompts — not concepts to understand, but templates to copy and adapt.

**Q2**: How did Randy Counsman's 🖥️ emoji signal solve a practical problem in agentic workflows?
**A**: It provides a visible, non-technical signal that Codex is mid-task, preventing teammates (or himself) from intervening and disrupting the agent's execution.

**Q3**: What structural fix resolved the 4.5-billion-token runaway agent swarm?
**A**: Capping subagents at five, removing a redundant implementer layer, and giving the judge agent a concrete visual target rather than an open-ended success criterion.
