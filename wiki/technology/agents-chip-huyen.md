---
type: literature-note
source_url: https://huyenchip.com/2025/01/07/agents.html
author: Chip Huyen
tags: [ai-agents, agentic-ai, llm-tooling, planning]
date_consumed: 2026-08-01
---

## Summary

Chip Huyen's primer on AI agents defines an agent as any system that perceives and acts on its environment, with tools expanding its capabilities across read and write operations. Planning is framed as a search problem, with patterns like [[ReAct]] and [[Reflexion]] guiding how agents reason and self-correct in agentic loops. The piece emphasizes that robust agent design requires careful failure taxonomy, human oversight for high-risk write actions, and systematic evaluation of plan quality.

## Core Concepts

- **[[AI Agent]]**: A system characterized by its environment and available actions; tools unlock knowledge augmentation, capability extension, and write operations.
- **[[Tool Use]]**: Three categories — knowledge augmentation (search, SQL, retrieval), capability extension (code interpreters, calculators), and write actions (APIs, database modifications).
- **[[Agentic Loop]]**: The repeated cycle of reasoning and action that drives an agent toward a goal until completion.
- **[[ReAct Pattern]]**: Interleaves reasoning and action as "Thought → Act → Observation"; foundational control loop for LLM agents.
- **[[Reflexion]]**: Extends ReAct with explicit self-critique after failures to improve subsequent attempts.
- **[[Planning as Search]]**: Treating plan generation as path evaluation over a goal space; plans can be validated before execution using heuristics or AI judges.
- **[[Human-in-the-Loop]]**: Humans can intervene to provide, validate, or approve plans — especially critical for irreversible write actions.
- **[[Control Flow]]**: Complex plans use sequential, parallel, if-statement (routing), and for-loop structures.
- **[[Chip Huyen]]**: Author and ML practitioner known for practical AI engineering writing.

## Key Takeaways

- **Tool Taxonomy**: Agents use tools for perception, capability, or world-modifying write actions.
- **Decoupled Planning**: Generate and validate a plan before execution to catch errors early.
- **ReAct Loop**: Thought → Act → Observation cycles until task is complete.
- **Write Action Caution**: High-risk operations (DB writes, bank transfers) require human approval gates.
- **Failure Modes**: Planning, tool, and efficiency failures each have distinct root causes.
- **Evaluation Dataset**: Measure plan validity ratio, invalid tool calls, wrong parameters per task.
- **Ablation Studies**: Identify dispensable tools; analyze tool-call distribution for usage patterns.
- **Parallel Execution**: Sequential steps where parallelism is possible are an efficiency failure.

## 🧠 First Principles & Mental Models

- **[[Separation of Concerns]]**: Decoupling planning from execution mirrors the software engineering principle that distinct responsibilities should be isolated — validating a plan before acting prevents compounded errors mid-task.
- **[[Principle of Least Privilege]]**: Limiting write-action authority to reliable agents only mirrors security thinking — an unreliable AI should no more initiate a bank transfer than an untrusted intern should touch production.
