---
type: literature-note
source_url: https://www.youtube.com/watch?v=S_oN3vlzpMw
author: Ras Mic (via Greg Isenberg)
tags: [ai-agents, claude-code, context-windows, skills]
date_consumed: 2026-07-29
---

## Summary

Ras Mic argues that current frontier models (e.g., Opus 4.6, GPT 5.4) are exceptionally capable, and the real differentiator is the quality of context built around them. He makes a strong case for using [[Agent Skills]] instead of agent.md files, leveraging [[Progressive Disclosure]] to save thousands of tokens per session. His core methodology is to walk through a workflow with the agent step by step, achieve a successful run, and only then codify it as a skill — then recursively refine through failure loops.

## Core Concepts

- **[[Context Window]]**: The total token budget for an agent session, comprising the system prompt, CLAUDE.md/agent.md files, tools, codebase, and conversation history. Hard limit ~250,000 tokens; hitting it triggers compaction and performance degradation.
- **[[Agent Skills]]**: Modular instruction files where only the name and description (~53 tokens) live in context; the full body is fetched only when the skill is invoked — vastly more efficient than monolithic agent.md files.
- **[[Progressive Disclosure]]**: Design principle where costly information is loaded lazily into context on demand, not upfront on every turn.
- **[[Token Efficiency]]**: Optimizing context usage to preserve model performance throughout long sessions.
- **[[Recursive Skill Refinement]]**: A feedback loop — run workflow, identify failure, fix it, then instruct the agent to update the skill so the error is documented and avoided next time.
- **[[Claude Code]]** / **[[OpenClaw]]**: Agentic coding harnesses that implement the skills/context pattern described.
- **[[Sub-agents]]**: Delegated agents managed by a primary agent; Ras Mic advocates building foundational single-agent skills before adding sub-agents.

## Key Takeaways

- **Model quality is solved**: Focus shifts fully to context and harness design.
- **Skip agent.md**: 95% of users burn tokens unnecessarily; only use for proprietary per-turn data.
- **Skills use progressive disclosure**: ~53 tokens per skill in context vs. thousands for agent.md lines.
- **Build skills from successful runs**: Walk through the workflow live, then ask the agent to write the skill.
- **Recursive refinement**: Feed each failure back and have the agent update the skill file.
- **Scale deliberately**: Start with one agent and proven skills before adding sub-agents.
- **Don't download random skills**: Security risk; also lacks your specific workflow context.

## 🧠 First Principles & Mental Models

- **[[Experiential Learning]]**: Ras Mic's methodology mirrors pedagogical research — agents that "do" a workflow before being given a procedure retain far more behavioral fidelity than those given abstract instructions upfront.
- **[[Lean Manufacturing]] / Pull vs. Push**: Progressive disclosure applies a pull-based information model to token management — context is fetched on demand rather than pushed in bulk, eliminating waste.
