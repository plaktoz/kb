---
source_url: https://loopengineering.run
author: Loop Engineering
date: 2026-08-03
---

# Loop Engineering Guide: Build Safe Autonomous Agent Loops

## Summary

Loop engineering is the practice of designing automated systems that orchestrate coding agents repeatedly — rather than prompting manually each time. It sits atop prompt, context, and harness engineering as a fourth layer.

## Core Concept

The fundamental shift: instead of manually prompting an agent and waiting, you design a system that "discovers work, assigns it to agents, verifies the output, saves state, and runs again on a schedule."

### The Four-Layer Stack

1. **Prompt engineering** — one instruction, one response
2. **Context engineering** — managing the model's window
3. **Harness engineering** — tools, permissions, and a done condition for one run
4. **Loop engineering** — scheduling, coordination, and safe repetition

## The Five Moves

Every loop requires all five; removing any breaks the system:

- **Discovery** — finds work autonomously from CI, issues, queues, etc.
- **Handoff** — packages a bounded task with context and an isolated workspace
- **Verification** — a *separate* agent checks results; "the agent that generated the change should not grade its own homework"
- **Persistence** — durable recording of results, logs, and state
- **Scheduling** — triggers that make it repeat automatically

## Six Production Primitives

- Automations/scheduling (cron, webhooks, CI)
- Worktrees for isolated execution
- Skills (reusable triage logic)
- Connectors/MCP integrations
- Generator + evaluator sub-agents (split writer from critic)
- Durable state/memory on disk

## Key Risks

| Risk | Guardrail |
|---|---|
| Verification debt | Independent evaluator + human gate before merge |
| Comprehension rot | Review summaries; require explanatory state updates |
| Cognitive surrender | Explicit human decision points |
| Token blowout | Budget caps, retry limits, timeout rules |

## Safety Principles

- Scope all tool/branch/destructive permissions explicitly
- Emit observable run summaries and artifacts
- Track success rate, review edits, and rollback frequency
- Architecture should be tool-agnostic (portable across Claude Code, Codex, Grok, etc.)

## Starter Checklist

Before deploying a loop, define:
1. Discovery source
2. State file location
3. Independent evaluator
4. Agent isolation method
5. Token/retry cap
6. Exact human review point

> Recommended approach: "Start read-only, add write access after it proves value, then tighten the evaluator before scaling."
