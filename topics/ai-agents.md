---
type: topic-file
topic: ai-agents
sources: [building-effective-ai-agents-anthropic, llm-powered-autonomous-agents-lilian-weng, agents-agentic-loops-chip-huyen, human-in-the-loop-ai, human-in-the-loop-autonomy-spectrum, agentic-design-patterns-loops-beat-single-pass, the-anatomy-of-an-ai-agent]
last_updated: 2026-08-01
---

# AI Agents

AI agents are LLM-powered systems that perceive an environment and take actions within it — the fundamental shift from language model as answerer to language model as actor, capable of running multi-step tasks with tools, memory, and self-correction.

## What an Agent Is

[[the-anatomy-of-an-ai-agent]] offers the clearest structural definition: an agent is a while-loop built from six parts — a brain (the LLM), a planning layer, tools, memory, the loop itself, and guardrails. Chip Huyen in [[agents-agentic-loops-chip-huyen]] frames it even more precisely: an agent is defined by its environment and its available actions. What separates an agent from a prompted model is the write-action capability — the ability to act on the world (send email, commit code, call an API), not merely generate text about it. [[building-effective-ai-agents-anthropic]] draws a useful further distinction between workflows (predefined code paths with fixed sequencing) and true agents (LLMs dynamically directing their own process); the choice between them is a question of how much runtime judgment the task requires.

## Loops Beat Zero-Shot

The most important empirical finding about agentic systems is [[agentic-design-patterns-loops-beat-single-pass]]'s benchmark result: GPT-3.5 in an agent loop achieves 95.1% on HumanEval, surpassing GPT-4 zero-shot at 67.0%. The loop gain of 47 percentage points dwarfs the model-generation improvement of 19 points. Andrew Ng's framing — that most current LLM use is zero-shot, like "writing an essay without backspace" — explains why the shift to iteration produces such large gains with no model change. The principle generalizes: quality in agentic systems comes from grounded iteration, not from a smarter single pass.

## Planning Architecture

[[llm-powered-autonomous-agents-lilian-weng]] provides the canonical three-component decomposition of any agent: Planning, Memory, and Tool Use. Each can evolve independently, which is why this framing has remained durable despite rapid architectural change. Planning methods range from Chain of Thought and Tree of Thoughts (decomposition strategies) to ReAct (Thought → Action → Observation cycles) and Reflexion (dynamic memory with trajectory restart on detected failure). [[agents-agentic-loops-chip-huyen]] adds a crucial operational principle: treat planning as a search problem, and decouple plan generation from validation from execution — conflating them produces the majority of agent planning failures. [[building-effective-ai-agents-anthropic]] maps five higher-level workflow patterns — Prompt Chaining, Routing, Parallelization, Orchestrator-Workers, and Evaluator-Optimizer — as the practical building blocks for structuring multi-step tasks, with the recommendation to start from the simplest pattern that works before adding complexity.

## Memory and Context

Lilian Weng's memory taxonomy maps human memory types onto agent equivalents: sensory memory becomes embeddings, short-term memory is the context window, and long-term memory is a vector store accessed via semantic search ([[llm-powered-autonomous-agents-lilian-weng]]). The context window's finiteness is the primary constraint in production agents — it limits historical awareness, forces hard choices about what to retain, and is the root cause of the long-horizon replanning failures where early errors compound undetected. [[building-effective-ai-agents-anthropic]] notes that tool documentation quality is as important as architecture — treated like a docstring for a junior developer, with absolute paths, edge cases, and minimal formatting overhead.

## Human Oversight Design

[[human-in-the-loop-autonomy-spectrum]] and [[human-in-the-loop-ai]] describe a three-level autonomy spectrum: Human-in-the-Loop (active per-decision participation), Human-on-the-Loop (autonomous operation with monitoring and override capability), and Human-out-of-the-Loop (full automation). The exception-based model is identified as the most scalable oversight pattern — handle routine cases automatically, route only low-confidence and novel cases to humans. [[agents-agentic-loops-chip-huyen]] sharpens this into a per-action principle: set the automation level per action type based on reversibility and consequence, not per system. Write actions — email sends, database writes, financial API calls — require a stricter gate than read actions, independent of how reliable the rest of the agent is. [[building-effective-ai-agents-anthropic]] anchors human checkpoints specifically at irreversible actions and unresolvable blockers, consistent with this logic.

## Failure Modes

[[agents-agentic-loops-chip-huyen]] provides the most practical failure taxonomy: planning failures (invalid tool calls, wrong parameters, wrong goal interpretation, false completion belief), tool failures (wrong output, natural language to execution command translation errors, missing tools), and efficiency failures (unnecessary sequential execution when parallel is possible, too many steps). [[llm-powered-autonomous-agents-lilian-weng]] adds interface fragility — formatting non-compliance requiring significant output-parsing defensive code — and the long-horizon replanning problem, where early errors that can't be "remembered" compound undetected into late-stage task failure. Alert fatigue is the organizational analog: too many human reviews degrades the quality of oversight ([[human-in-the-loop-autonomy-spectrum]]), which means the routing threshold is a calibration decision with real quality consequences.

## Weekly Updates

### 2026-W31
- Added: [[building-effective-ai-agents-anthropic]], [[llm-powered-autonomous-agents-lilian-weng]], [[agents-agentic-loops-chip-huyen]], [[human-in-the-loop-ai]], [[human-in-the-loop-autonomy-spectrum]], [[agentic-design-patterns-loops-beat-single-pass]], [[the-anatomy-of-an-ai-agent]]
