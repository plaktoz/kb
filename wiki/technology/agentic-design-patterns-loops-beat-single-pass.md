---
type: literature-note
source_url: https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/
author: Andrew Ng
tags: [agentic-ai, loop-engineering, benchmarks, design-patterns]
date_consumed: 2026-07-27
---

## Summary

Andrew Ng argues that agentic workflows — not next-generation foundation models — will drive the most near-term AI progress. The empirical evidence is striking: GPT-3.5 in an agent loop reaches 95.1% on HumanEval, surpassing GPT-4 zero-shot at 67.0%, a gain that dwarfs the model generation gap. The root problem with current LLM use is that it's mostly zero-shot, like "writing an essay without being allowed to backspace."

## Core Concepts

- **[[HumanEval]] benchmark**: standard coding benchmark for measuring LLM capability
- **Four agentic design patterns**: [[Reflection]], [[Tool Use]], [[Planning]], [[Multi-Agent Collaboration]]
- **Zero-shot vs agentic loop**: the fundamental performance gap — single-pass generation vs iterative refinement
- **[[Andrew Ng]]** — founder of DeepLearning.AI, Coursera co-founder; this series introduced agentic patterns to a broad ML audience

## Key Takeaways

- **HumanEval numbers**: GPT-3.5 zero-shot 48.1% → agent loop 95.1%; GPT-4 zero-shot 67.0%
- **Loop > model upgrade**: the agent loop gain (47pp) dwarfs the GPT-3.5→GPT-4 jump (19pp)
- **Zero-shot is the bottleneck**: most current LLM use is constrained to single-pass generation
- **Four patterns summary**: Reflection (self-critique), Tool Use (external APIs), Planning (multi-step strategy), Multi-Agent (divide-debate-refine)
- **Near-term bet**: agentic workflows will drive more progress than the next foundation model generation

## 🧠 First Principles & Mental Models

- **[[Compound Interest]]**: Iterative refinement in loops compounds quality gains — each revision builds on the last, producing non-linear improvement from linear compute investment.
- **[[Constraint Relaxation]]**: The zero-shot constraint (no backspacing) is artificial. Removing it — allowing iteration — is the simplest architectural change with the largest quality impact.
