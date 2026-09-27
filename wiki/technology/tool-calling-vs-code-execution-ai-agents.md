---
type: literature-note
source_url: https://machinelearningmastery.com/tool-calling-vs-code-execution-for-ai-agents-choosing-the-right-action-primitive/
author: Shittu Olumide
tags: [ai-agents, tool-calling, code-execution, agentic-architecture]
date_consumed: 2026-09-27
---

## Summary

Tool calling and code execution are two fundamental action primitives for AI agents, each with real architectural consequences for cost, latency, and accuracy. Tool calling emits discrete JSON requests that feed results back into model context one at a time, while code execution lets the model write a full script that runs all tool calls internally and returns only the final output. The choice between them depends on call volume, data sensitivity, and whether the model needs to reason over intermediate results.

## Core Concepts

- **[[Tool Calling]]**: Model emits special tokens wrapping a JSON payload; the host pauses generation, executes the call, and returns results directly into context. Ideal for single, time-sensitive lookups where the model must reason over the returned data.
- **[[Code Execution]]** (programmatic tool calling): Model writes a full script that invokes tools internally; only the script's final output enters model context. Enabled by adding `"allowed_callers": ["code_execution_20250825"]` to a tool's definition.
- **[[AI Agents]]**: Autonomous systems that select and invoke tools or scripts to complete multi-step tasks — the choice of action primitive shapes their performance and cost profile.
- **[[CodeAct]]** (Wang et al., 2024): Research paper demonstrating that code-executing agents succeed up to 20% more often on complex, multi-step tasks than discrete tool-calling agents.
- **[[GAIA Benchmark]]**: Evaluation suite for general AI assistants; switching to code execution improved accuracy from 46.5% to 51.2% in internal benchmarks cited in the article.

## Key Takeaways

- **Token efficiency**: Code execution kept a real workflow at 2,000 tokens vs. 150,000 — a 98.7% reduction.
- **Accuracy gain**: GAIA benchmark accuracy improved from 46.5% to 51.2% with code execution.
- **CodeAct finding**: Code-executing agents succeed up to 20% more often on complex tasks.
- **Use tool calling when**: call volume is low, model needs to reason over each result, or per-action auditability is required.
- **Use code execution when**: many fan-out calls needed, data is large/sensitive (PII), or latency from multiple round-trips is unacceptable.
- **Production agents** typically combine both — plain tool calling for simple lookups, code execution for aggregation or large payloads.
- **Prerequisite**: code execution requires a sandbox environment to be in place.

## 🧠 First Principles & Mental Models

- **[[Separation of Concerns]]**: Code execution isolates intermediate data inside the execution environment rather than routing it through model context — the model stays focused on final reasoning, not bookkeeping over raw intermediate results.
- **[[Batch Processing vs. Stream Processing]]**: Tool calling is stream-style (one result at a time, model reacts to each); code execution is batch-style (all operations run, model sees only the aggregate). The right choice mirrors the classic data-engineering trade-off between latency and throughput.

## 🃏 Review Questions

**Q1**: What is the central architectural argument of the article?
**A**: The choice between tool calling and code execution has real consequences for cost, latency, and accuracy — neither primitive universally replaces the other, and production agents should select per task.

**Q2**: What specific performance evidence supports preferring code execution on complex tasks?
**A**: Anthropic reported a 98.7% token reduction on one real workflow; internal benchmarks showed a 37% average token reduction and a GAIA accuracy improvement from 46.5% to 51.2%; the CodeAct paper found code-executing agents succeed up to 20% more often on multi-step tasks.

**Q3**: How would you decide which primitive to use when designing an agent action?
**A**: Use tool calling for single or few calls where the model needs to reason over each result and per-action logging matters; use code execution when tasks require fan-out, aggregation, or handling data too large or sensitive to pass through model context.
