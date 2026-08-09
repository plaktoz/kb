# Context Engineering for Coding Agents

**Source:** https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html
**Author:** Birgitta Böckeler (Distinguished Engineer, Thoughtworks)
**Date:** 05 February 2026

---

## Overview

Context engineering has become central to coding agent workflows. A concise definition: *"Context engineering is curating what the model sees so that you get a better result."*

---

## What Is Context?

### Reusable Prompts

Two main categories:

- **Instructions** – Tell the agent to do something (e.g., "Write an E2E test in the following way…")
- **Guidance** – General conventions to follow (e.g., "Always write independent tests")

### Context Interfaces

Descriptions of how the LLM can retrieve additional context:

- **Tools** – Built-in capabilities (bash, file search, etc.)
- **MCP Servers** – Custom programs exposing data sources/actions
- **Skills** – On-demand resources the LLM loads when relevant

---

## Key Dimensions

### Who Loads Context?

| Loader | Example | Trade-off |
|--------|---------|-----------|
| LLM | Skills | Non-deterministic |
| Human | Slash commands | Less automation |
| Agent software | Hooks | Deterministic |

### Size Management

Effectiveness drops with too much context. Build rules files **gradually**. Tools like Claude Code's `/context` command provide transparency about what's consuming space.

---

## Claude Code Features (as of January 2026)

### CLAUDE.md
- **Type:** Guidance, always loaded at session start
- **Use for:** Project-wide conventions ("we use yarn, not npm")

### Rules
- **Type:** Guidance, path-scoped
- **Use for:** Modular guidance loaded only for relevant files (e.g., bash style rules for `**/*.sh`)

### Slash Commands *(deprecated, superseded by Skills)*
- **Type:** Instructions, human-triggered
- **Use for:** Common tasks like `/code-review`, `/prep-commit`

### Skills
- **Type:** Guidance/instructions/docs/scripts, lazy-loaded
- **Use for:** Resources only needed situationally (JIRA access, API integration docs, React conventions)

### Subagents
- **Type:** Instructions + isolated context window
- **Use for:** Parallel tasks, alternate models, scoped tool access, orchestrated workflows
- Foundational for swarm experiments

### MCP Servers
- **Type:** External program integration
- **Use for:** API access, browser automation, local knowledge bases

### Hooks
- **Type:** Scripts triggered by lifecycle events
- **Use for:** Deterministic actions (run prettier after every JS file edit, custom notifications, logging)

### Plugins
- **Type:** Distribution mechanism
- **Use for:** Sharing commands, skills, and hooks across teams

---

## Sharing Context Configurations

Challenges include:
- Context must match between sharer and receiver
- Risk of overengineering by copying instructions blindly
- Contradictory instructions can silently degrade agent behavior

---

## Caution: Illusion of Control

Context engineering improves *probability* of good results but cannot *guarantee* behavior. Phrases like "ensure it does X" or "prevent hallucinations" overstate what's achievable — LLM execution remains probabilistic, and appropriate human oversight is still necessary.
