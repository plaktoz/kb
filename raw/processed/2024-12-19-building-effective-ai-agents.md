# Building Effective AI Agents

source_url: https://www.anthropic.com/engineering/building-effective-agents

---

Authors: Erik S. and Barry Zhang
Published: December 19, 2024

Anthropic distinguishes between two agentic system types: Workflows (LLMs orchestrated via predefined code paths) and Agents (LLMs that dynamically direct their own processes and tool usage).

## Workflow Patterns

**Prompt Chaining**: Sequential LLM calls where each step processes prior output. Intermediate "gates" verify progress. Best for tasks cleanly divisible into fixed subtasks, trading latency for accuracy.

**Routing**: Classifies input, then directs it to specialized downstream tasks. Useful for separating customer query types or routing simpler questions to lighter models (e.g., Haiku) and harder ones to more capable models.

**Parallelization**: Two variants — Sectioning (independent subtasks run simultaneously) and Voting (same task run multiple times for consensus). Effective when subtasks are independent or when higher confidence requires multiple perspectives.

**Orchestrator-Workers**: A central LLM dynamically decomposes tasks and delegates to worker LLMs. Unlike parallelization, subtasks aren't predefined — the orchestrator determines them per input. Suited for complex coding or multi-source research.

**Evaluator-Optimizer (Eval-Act Cycle)**: One LLM generates; another evaluates and feeds back in a loop. Works well when "LLM responses can be demonstrably improved when a human articulates their feedback."

## Agent Architecture

Agents operate in an agentic loop:
1. Receive task (via command or dialogue)
2. Plan and act independently using tools
3. Gather ground truth from the environment at each step (tool results, code execution)
4. Pause for human input at checkpoints or blockers
5. Terminate on completion or hitting stopping conditions

Agents are "typically just LLMs using tools based on environmental feedback in a loop."

## Tool Design (Agent-Computer Interface)

Key guidance:
- Give the model enough tokens to reason before committing
- Keep formats close to naturally occurring internet text
- Avoid formatting overhead (e.g., line-count tracking, JSON string escaping)
- Use absolute rather than relative filepaths to reduce errors
- Write tool documentation like a thorough docstring for a junior developer

## Three Core Principles

1. Maintain simplicity in agent design
2. Prioritize transparency — show planning steps explicitly
3. Invest heavily in tool documentation and testing

## When to Use Each Pattern

| Pattern | Use When |
|---|---|
| Single LLM call | Most cases — optimize this first |
| Prompt chaining | Fixed subtask sequences |
| Routing | Distinct input categories |
| Parallelization | Independent subtasks or consensus needed |
| Orchestrator-workers | Unpredictable subtask structure |
| Evaluator-optimizer | Clear criteria + iterative refinement adds value |
| Full agents | Open-ended, multi-step, trusted environments |

The overarching recommendation: start simple, measure performance, and add complexity only when it demonstrably improves outcomes.
