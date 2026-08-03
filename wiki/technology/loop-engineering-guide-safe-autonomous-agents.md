---
type: literature-note
source_url: https://loopengineering.run
author: Loop Engineering
tags: [loop-engineering, ai-agents, agentic-workflows, automation]
date_consumed: 2026-08-03
---

## Summary

Loop engineering is the practice of designing automated systems that orchestrate coding agents repeatedly on a schedule, sitting atop prompt, context, and harness engineering as a fourth distinct layer. The core shift is from manual prompting to building a system that discovers work, assigns it to agents, verifies outputs via an independent evaluator, and repeats. Five moves — discovery, handoff, verification, persistence, and scheduling — must all be present or the system breaks.

## Core Concepts

- **[[Loop Engineering]]** — fourth layer of the agentic stack; handles scheduling, coordination, and safe repetition across agent runs
- **[[Four-Layer Agentic Stack]]** — (1) [[Prompt Engineering]] single instruction/response; (2) [[Context Engineering]] window management; (3) [[Harness Engineering]] tools, permissions, done condition; (4) [[Loop Engineering]] repetition and coordination
- **[[Five Loop Moves]]** — Discovery, Handoff, Verification, Persistence, Scheduling; removing any one breaks the loop
- **[[Verification Separation]]** — the agent that generates a change must not grade its own output; a separate evaluator sub-agent or human gate is required
- **[[Generator-Evaluator Pattern]]** — split writer from critic sub-agents to prevent self-grading bias; directly implements verification separation
- **[[Worktrees]]** — isolated execution environments for each agent run, preventing state contamination between tasks
- **[[Durable State]]** — on-disk persistence of results, logs, and run state enabling safe resumption and rollback
- **[[Cognitive Surrender]]** — risk where humans stop reviewing agent outputs because the loop "seems to work"; mitigated by explicit human decision points
- **[[Comprehension Rot]]** — gradual loss of human understanding of the codebase as agents make changes without explanatory summaries

## Key Takeaways

- **Stack layer**: loop engineering sits above harness; without it you still prompt manually
- **Five moves are mandatory**: skip any one and the system is not a loop — it is a script
- **Independent evaluator is non-negotiable**: "the agent that generated the change should not grade its own homework"
- **Six production primitives**: scheduling, [[Worktrees]], [[Skills]], connectors/MCP, generator+evaluator sub-agents, durable state
- **Key risks**: verification debt, comprehension rot, cognitive surrender, token blowout
- **Safety principle**: scope all destructive permissions explicitly and emit observable run summaries
- **Deployment order**: start read-only → add write access after proven value → tighten evaluator before scaling
- **Tool-agnostic architecture**: design loops portable across [[Claude Code]], Codex, Grok, etc.

## 🧠 First Principles & Mental Models

- **[[Separation of Concerns]]**: Splitting generator from evaluator is the same principle that separates author from editor — conflating them degrades quality, and the architectural rule applies at the agent level just as it does in human workflows.
- **[[Defense in Depth]]**: The starter checklist (discovery source, state file, independent evaluator, isolation, token cap, human review point) mirrors layered security — no single guardrail is sufficient; safety emerges from the stack of overlapping controls.

## 🃏 Review Questions

**Q1**: What distinguishes loop engineering from harness engineering?
**A**: Harness engineering covers tools, permissions, and a done condition for a single run; loop engineering adds scheduling, coordination, and safe repetition so the system discovers and processes work automatically over time.

**Q2**: Why must the verifying agent be separate from the generating agent?
**A**: The guide states "the agent that generated the change should not grade its own homework" — a generator is optimistically biased toward its own output, so an independent evaluator is needed to catch errors before merge.

**Q3**: What is the recommended rollout sequence before scaling a production loop?
**A**: Start read-only, add write access only after the loop proves value, then tighten the evaluator before scaling — this limits blast radius while you validate correctness at each stage.
