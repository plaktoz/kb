# Agentic Design Patterns Part 1: Why Loops Beat Single-Pass

source_url: https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/

---

Author: Andrew Ng
Date: March 20, 2024

## The Core Problem with Zero-Shot LLMs

Current LLM usage is mostly zero-shot — the model generates output in one pass, like writing an essay "straight through with no backspacing allowed." Despite this constraint, results are surprisingly good, but iterative approaches perform far better.

## Benchmark Evidence

On the HumanEval coding benchmark:
- GPT-3.5 (zero-shot): 48.1%
- GPT-4 (zero-shot): 67.0%
- GPT-3.5 (agent loop): up to 95.1%

The jump from agent workflows dwarfs the GPT-3.5 → GPT-4 improvement. Agentic workflows may drive more near-term AI progress than next-generation foundation models.

## The Four Agentic Design Patterns

1. **Reflection** — The LLM reviews its own output to identify improvements
2. **Tool Use** — The LLM accesses web search, code execution, or other external functions
3. **Planning** — The LLM constructs and executes a multi-step strategy toward a goal
4. **Multi-Agent Collaboration** — Multiple agents divide tasks, debate, and jointly refine solutions

Each pattern is explored in subsequent parts of the series.
