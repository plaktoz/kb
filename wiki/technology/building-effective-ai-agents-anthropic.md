---
type: literature-note
source_url: https://www.anthropic.com/engineering/building-effective-agents
author: Erik S. and Barry Zhang (Anthropic)
tags: [agentic-ai, loop-engineering, tool-use, workflow-patterns]
date_consumed: 2026-07-27
---

## Summary

Anthropic distinguishes workflows (predefined code paths) from agents (LLMs that dynamically direct their own processes) and argues that the simplest solution that works should always be preferred. The core agentic loop receives a task, plans and acts via tools, gathers ground truth from the environment at each step, and terminates when done or blocked. The article emphasizes that tool documentation is as important as architecture — treated like a docstring for a junior developer.

## Core Concepts

- [[Agentic Loop]] — the fundamental cycle of receive → plan → act → observe → continue or terminate
- [[Workflow Patterns]]: [[Prompt Chaining]], [[Routing]], [[Parallelization]], [[Orchestrator-Workers]], [[Evaluator-Optimizer]]
- [[Agent-Computer Interface (ACI)]] — design principles for tool documentation and format
- [[Human Checkpoints]] — placed at irreversible actions and unresolvable blockers within the loop
- [[Anthropic]] engineering guidance on production-ready agent systems

## Key Takeaways

- **Single LLM call first**: optimize the simplest approach before adding complexity
- **Prompt chaining**: fixed subtask sequences with verification gates; trades latency for accuracy
- **Routing**: classifies input → specialized downstream path or model tier
- **Parallelization**: sectioning (independent subtasks) or voting (multiple runs for consensus)
- **Orchestrator-workers**: orchestrator dynamically decomposes tasks — suited to unpredictable structure
- **Eval-act cycle**: generator + evaluator in a loop; works when feedback can be clearly articulated
- **Agentic loop agents**: best for open-ended, multi-step tasks in trusted, reversible environments
- **Tool docs matter**: absolute paths, minimal formatting overhead, thorough edge-case documentation
- **Transparency principle**: show planning steps explicitly; never hide reasoning from operators
- **Failure mode taxonomy (Chip Huyen)**: planning failures (invalid tool calls, wrong params, wrong goal, false completion belief), tool failures (wrong output, NL→command translation errors, missing tools), efficiency failures (unnecessary sequential steps when parallel is possible) ← `[[agents-agentic-loops-chip-huyen]]`
- **Per-action oversight principle**: set automation level per action type based on reversibility and consequence — not per system as a whole; write actions (email, DB writes, financial APIs) require stricter gates than read actions ← `[[agents-agentic-loops-chip-huyen]]`
- **Planning-as-search discipline**: decouple plan generation → validation → execution; conflating them is the source of most agent planning failures ← `[[agents-agentic-loops-chip-huyen]]`

## 🧠 First Principles & Mental Models

- **[[Occam's Razor]]**: Anthropic's "start simple, add complexity only when measurably beneficial" is exactly this — every added layer must earn its complexity cost, not just feel more sophisticated.
- **[[Feedback Loops]]**: The eval-act cycle makes the feedback loop explicit — quality improves not from smarter generation but from grounded, iterated critique.

## Weekly Connections

### 2026-W31
- Chip Huyen's per-action oversight extends Anthropic's human checkpoint model: oversight should be calibrated to reversibility of each action type rather than set system-wide — the same principle expressed at different granularities ← `[[agents-agentic-loops-chip-huyen]]`
- The three-way failure taxonomy (planning/tool/efficiency) gives practitioners a diagnostic framework for the production agent failures Anthropic describes as motivating human checkpoints ← `[[agents-agentic-loops-chip-huyen]]`
