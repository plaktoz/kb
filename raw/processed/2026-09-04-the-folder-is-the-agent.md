---
source_url: https://every.to/source-code/the-folder-is-the-agent-rerun
author: Kieran Klaassen
date: 2026-09-04
---

# The Folder Is the Agent

Klaassen, sole engineer behind Every's AI email assistant Cora, spent three months attempting agent swarm coordination before discovering a simpler insight: "a folder" with accumulated context *is* the agent.

**Core concept:** A project folder containing a CLAUDE.md, skill definitions, and institutional knowledge transforms a generalist model into a specialist. He now operates 44 such folders across multiple projects.

**His folder structure includes:**
- Conventions (Rails patterns, deploy workflows)
- Architecture docs and system designs
- Runbooks and incident investigations
- Specialized sub-agents for review, planning, and component creation

Two distinct folders demonstrate the principle: `~/cora/` acts as a Rails engineer; `~/cora-agent/` acts as an ops engineer with access to logs, databases, and incident history — same model, different context, different agent.

**Dispatch layer:** He built a Ruby daemon using file-based messaging. Two commands drive most work:
- `/hey` — morning status briefing across all projects
- `/orchestrate` — breaks tasks into subtasks, spawns workers in appropriate folders

**Key failures encountered:**
- Encoding crashes from em dashes/curly quotes in prompts
- Context drift and duplicate work across agents
- Silent agent stalls

**Central lesson:** "You can't vibe orchestrate." Build the folder, use it, trust it — *then* hand it to automation.
