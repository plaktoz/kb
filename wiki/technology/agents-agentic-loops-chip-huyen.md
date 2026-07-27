---
type: literature-note
source_url: https://huyenchip.com/2025/01/07/agents.html
author: Chip Huyen
tags: [agentic-ai, loop-engineering, human-oversight, failure-modes]
date_consumed: 2026-07-27
---

## Summary

Chip Huyen frames agents as environment + actions pairs, with tools expanding both perception and write capabilities. Planning is treated as a search problem — decouple plan generation from execution, validate before acting. The article provides the clearest taxonomy of agentic failure modes (planning, tool, efficiency) and introduces the principle that oversight levels should be set per action type, not per system.

## Core Concepts

- **Agent definition**: anything perceiving and acting on an environment — defined by its environment and available actions
- **Tool categories**: [[Knowledge Augmentation]] (search, SQL, retrieval), [[Capability Extension]] (calculators, code interpreters), [[Write Actions]] (email, database, financial APIs)
- **[[ReAct]] pattern**: Thought → Act → Observation, cycling until complete
- **[[Reflexion]]**: adds explicit self-critique after failures
- **Planning as search**: evaluate paths toward a goal; decouple plan generation from validation from execution
- **Severity-based oversight**: set automation level per action based on reversibility and consequence
- **[[Chip Huyen]]** — author of *Designing Machine Learning Systems*

## Key Takeaways

- **Decouple plan steps**: generate plan → validate (heuristics or AI judge) → execute — never conflate
- **Control flow types**: sequential, parallel, if-statement (routing), for-loop — same primitives as code
- **Write action gate**: "don't give an intern authority to delete production DB; don't give unreliable AI bank transfers"
- **Per-action oversight**: define automation level for each action type, not the system as a whole
- **Planning failures**: invalid tool calls, wrong params, wrong values, wrong goal, false completion belief
- **Tool failures**: wrong output, translation errors (NL → execution command), missing tools
- **Efficiency failures**: too many steps, unnecessary sequential execution when parallel is possible
- **Eval dataset**: (task, tool inventory) tuples — measure valid plan ratio, avg plans to validity, tool-call distribution

## 🧠 First Principles & Mental Models

- **[[Principle of Least Privilege]]**: The per-action oversight model is exactly this security principle applied to AI — grant only the minimum authority required for each action type, and scale up only when trust is earned through demonstrated reliability.
- **[[Separation of Concerns]]**: Decoupling planning from validation from execution prevents a common failure mode where a flawed plan is executed before it can be checked — each stage has a single responsibility.
