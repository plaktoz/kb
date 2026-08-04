---
type: literature-note
source_url: https://www.youtube.com/watch?v=Np8UTsHnUV0
author: Johnny Nel (AI for Founders)
tags: [ai-agents, harness-engineering, loop-engineering, graph-engineering, agentic-workflows, done-test, verification]
date_consumed: 2026-08-04
---

## Summary

Every AI agent failure traces back to exactly one of three decisions: (1) what the agent can reach (the harness), (2) how the agent knows it is finished (the done test), or (3) what has to happen before what (ordering/graph). Diagnosing in that order — cheapest and most common first — eliminates most guesswork and prevents wasting time on retries that cannot fix a structural problem.

## Core Concepts

- **[[Harness Engineering]]** — everything that is not the model itself: tools, connectors, permissions, memory files, working conditions; defines which "doors" the agent can open
- **[[Done Test]]** — a short written list of conditions that must be true when the agent returns; every condition must be checkable by someone outside the conversation, not by the agent that produced the output
- **[[Graph Engineering]] / Ordering** — controlling which steps must complete before others run; only matters if something later in the run reads what came before it
- **[[Memory File]] pattern** — a persistent text file the agent writes at the end of each session and reads at the start of the next; prevents re-briefing every morning and records what is blocked
- **[[Tool Overcrowding]]** — having too many connectors switched on forces the agent to choose among unused tools and sends their descriptions on every turn, degrading performance
- **[[Compaction Limitation]]** — Anthropic's internal experiment (November 2025) found that squeezing a conversation smaller was not sufficient for multi-session continuity; a persistent memory file worked better

## The Three Decisions in Diagnostic Order

| # | Decision | Question to Ask | Older Analogue |
|---|----------|-----------------|----------------|
| 1 | **Harness** | Could a competent person do this job with what the agent was given? | OS file permissions |
| 2 | **Done Test** | Could someone outside the conversation tell whether it is finished? | Render return code |
| 3 | **Graph / Ordering** | Does step N need the output of step N-1? | Build dependency graph |

> "The diagnostic order is the part that holds up even when the lines between the three are contested." — Johnny Nel

## Key Takeaways

- **Harness is the most common failure point**: the first question (could it reach what it needed?) stops most failures before reaching the others.
- **Retries only help random failures**: if two attempts fail the same way, the problem lives in the harness — stop retrying and audit what the agent can reach.
- **A wish vs. a test**: "it should read professionally" is a wish; "every figure in the draft appears on the source sheet" is a test. Only tests belong in a done test.
- **A check that only looks for success will wait forever on a job that already failed**: any monitoring check must also fire when the job dies, not only when it finishes.
- **Ordering is the last thing to change**: if the harness is correct and the done test passes cleanly, then ordering becomes worth examining. Build no graph while your process is still changing every few weeks.
- **Tool hygiene matters**: count what is switched on; switch off everything not deliberately turned on for the current job.
- **Persistent memory file beats compaction**: four lines written at the end of a session outperform conversation summarisation for multi-session continuity.

## 🧠 First Principles & Mental Models

- **[[Separation of Concerns]]**: The three-decision framework cleanly separates what the agent knows about (harness), what it produces (done test), and how it sequences work (graph) — mirroring classical software layers.
- **[[Cheapest-First Diagnosis]]**: Checking harness before done test before ordering follows the principle of eliminating the most probable, least costly root cause first — the same heuristic used in system debugging and medicine.
- **[[Autonomy-Oversight Tradeoff]]**: The done-test requirement — that completion criteria be verifiable by an outsider — is a direct design response to the autonomy problem: the AI is the part that can be wrong about its own ending.

## 🃏 Review Questions

**Q1**: What are the three decisions that explain every AI agent failure, and in what order should they be diagnosed?
**A**: (1) Harness — what the agent can reach; (2) Done Test — how it knows it is finished; (3) Graph/Ordering — what must happen before what. Diagnose harness first (cheapest and most common), then done test, then ordering.

**Q2**: What is the rule that distinguishes a done-test condition from a wish?
**A**: Every condition on the done test must be checkable by someone who is not in the conversation — not gradeable only by the agent that produced the output.

**Q3**: Why does a persistent memory file outperform conversation compaction for multi-session agents?
**A**: Compaction shrinks the same conversation but loses completed work and blocked items across sessions. A memory file written at session end and read at session start is durable, human-readable, and session-independent — Anthropic's own internal experiment confirmed compaction alone was not sufficient.

## Links

- [[loop-engineering-agent-loop-design]] — the six loop design elements (trigger, context, action, verification, memory, escalation) that this video's framework maps onto
- [[a-guide-to-context-engineering-for-llms]] — context engineering as the layer below harness engineering
- [[agentic-design-patterns-loops-beat-single-pass]] — empirical support for agent loops and the importance of verification
- [[agentic-engineering-subagents]] — subagent patterns that plug into a well-designed harness
- [[ai-agent-three-failure-modes-harness-done-test-graph]] — this note
