---
type: literature-note
source_url: https://www.youtube.com/watch?v=S_oN3vlzpMw
author: Greg Isenberg (host), Ras Mic (guest)
tags: [ai-agents, claude-code, skills, context-window]
date_consumed: 2026-08-01
---

## Summary

Ras Mic explains that current LLMs (Opus 4.6, GPT 5.4) are exceptionally capable, making the quality of context the primary differentiator between useful output and slop. He argues that 95% of users should skip agent.md/CLAUDE.md files entirely because they burn tokens on every turn, and instead build custom skills that use progressive disclosure to load only a name and description into context until needed. The best way to create a skill is to walk through the workflow step-by-step with the agent, complete a successful run, then instruct the agent to write the skill from that real context — and recursively refine it by feeding failures back until the agent executes flawlessly.

## Core Concepts

- **[[Context Window]]**: The complete token budget consumed by an agent on each turn — composed of system prompt, agent.md files, skill listings, tools, the codebase, and the conversation history. Hard limit ~250,000 tokens; hitting it triggers compaction and performance degradation.
- **[[Progressive Disclosure]] (Skills)**: [[Claude Code]] skills load only their name and description (~53 tokens) into context at all times. The full instructions are fetched only when the agent determines the skill is relevant — vastly cheaper than agent.md files that repeat thousands of tokens every turn.
- **[[Skill Creation Methodology]]**: Do not write skills upfront. Walk through the workflow with the agent interactively, correct mistakes in real time, complete a successful run, then ask the agent to "review what you just did and create the skill." This grounds the skill in actual execution context.
- **[[Recursive Skill Improvement]]**: After a skill is created, each failure is an opportunity — identify the error, fix it with the agent, then instruct the agent to update the skill so the same mistake is documented and avoided. After ~5 iterations, complex multi-source workflows run reliably.
- **[[Scaling for Productivity]]**: Start with a single [[AI Agent]] and build reliable skills before adding sub-agents. Jumping to multi-agent architectures prematurely optimizes for appearance rather than actual productivity.
- **[[Token Efficiency]]**: Stripping unnecessary context (agent.md, redundant instructions) and replacing it with on-demand skills is the primary lever for sustained agent performance over long sessions.

## Key Takeaways

- **Model quality is solved**: Opus 4.6 and GPT 5.4 are good enough — context quality is what matters now.
- **Skip agent.md**: 95% of users don't need it; use it only for proprietary or per-turn-required information.
- **Skills beat CLAUDE.md**: ~53 tokens per skill in context vs. 7,000+ tokens for a 1,000-line CLAUDE.md file.
- **Walk before you codify**: Run the workflow interactively first; never write a skill before a successful run exists.
- **Feed failures forward**: When the agent fails, identify the error, fix it, then update the skill file immediately.
- **Sub-agents come last**: Build one agent with solid skills before scaling to multi-agent architectures.
- **Code is context**: For coding projects, the codebase itself provides sufficient context — no stack-specific agent.md needed.
- **Don't download third-party skills**: They lack your specific run context and introduce attack-vector risk.

## First Principles & Mental Models

- **[[Mimicry Without Understanding]]**: LLMs predict the most probable next token — they don't reason. Giving an agent an underspecified task yields sycophantic confirmation because there's nothing concrete to mimic. Providing a step-by-step successful run gives the model a high-quality pattern to replicate reliably.
- **[[Experiential Learning]]**: Ras Mic's skill-building process mirrors how humans acquire procedural knowledge — guidance, failure, correction, repetition, then codification. Asking the agent to write the skill *after* a successful run is the equivalent of "write the SOP once you understand the job."
