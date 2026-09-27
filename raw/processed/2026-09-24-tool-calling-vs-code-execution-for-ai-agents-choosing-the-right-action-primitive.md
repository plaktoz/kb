---
source_url: https://machinelearningmastery.com/tool-calling-vs-code-execution-for-ai-agents-choosing-the-right-action-primitive/
author: Shittu Olumide
date: 2026-09-24
---

# Tool Calling vs. Code Execution for AI Agents: Choosing the Right Action Primitive

## Summary

The article examines two fundamental action primitives for AI agents — tool calling and code execution — arguing that the choice between them has real architectural consequences for cost, latency, and accuracy.

## Tool Calling

The model emits special tokens wrapping a JSON payload; the host application pauses generation, executes the call, and feeds results back into the conversation. Every action is discrete and loggable, and the model sees each result directly before deciding next steps. This works well for single, time-sensitive lookups where the model genuinely needs to reason over the returned data.

## Code Execution (Programmatic Tool Calling)

Rather than requesting one action at a time, the model writes a full script that calls tools internally. Only the script's final output returns to the model — intermediate results never enter context. The key enabling mechanism is adding `"allowed_callers": ["code_execution_20250825"]` to a tool's definition.

## Performance Evidence

- Anthropic reported a real workflow dropping from 150,000 tokens to 2,000 — "a 98.7% reduction" — by keeping data inside the execution environment.
- Internal benchmarks showed average token usage falling from ~43,500 to ~27,300 (37% reduction) on complex tasks, while GAIA benchmark accuracy *improved* from 46.5% to 51.2%.
- The CodeAct paper (Wang et al., 2024) found code-executing agents succeeded "up to 20% more often on complex, multi-step tasks."

## Decision Framework

| Factor | Favors Tool Calling | Favors Code Execution |
|---|---|---|
| Call volume | One or a few | Many, with fan-out |
| Result handling | Model reasons over them | Filter, sum, or compare |
| Data sensitivity | Low | High (PII, large payloads) |
| Latency tolerance | Tight | Multi-round-trip workflows |
| Infrastructure | No sandbox available | Sandbox already in place |
| Auditability | Per-action logging needed | Aggregate outcome matters |

## Key Takeaway

Neither primitive replaces the other. Production agents typically use plain tool calling for simple lookups and switch to code execution when tasks require fan-out, aggregation, or handling data too large or sensitive to route through model context. The skill is recognizing, task by task, which the work requires.
