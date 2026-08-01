---
type: literature-note
source_url: https://www.langchain.com/blog/reflection-agents
author: Ankush Gola
tags: [reflection-agents, lats, reflexion, agentic-ai]
date_consumed: 2026-08-01
---

## Summary

Reflection as a prompting strategy improves LLM agent quality by having agents critique their own past actions, shifting from "System 1" reactive responses toward "System 2" methodical reasoning. LangChain presents three architectures — Basic Reflection, Reflexion, and LATS — each increasing in sophistication and compute cost. All three trade latency for output quality, making them best suited for knowledge-intensive tasks rather than low-latency applications.

## Core Concepts

- **Basic Reflection**: Two chained LLM calls — a generator and a reflector acting as a teacher — running for a fixed number of iterations via [[LangGraph]] MessageGraph; limited by lack of external grounding
- **[[Reflexion]]**: Actor agent that grounds critique in external data (search, citations); loop is draft → execute tools → revise up to MAX_ITERATIONS; prone to error compounding from a single fixed trajectory
- **[[Language Agent Tree Search]] (LATS)**: Combines reflection with [[Monte Carlo Tree Search]] — Select (UCT), Expand & Simulate, Reflect & Evaluate, Backpropagate; explores multiple trajectories rather than one
- **System 1 → System 2 thinking**: Reflection architectures convert reactive LLM outputs into deliberate, iterative reasoning
- **Trajectory saving**: Completed reflection loops can serve as memory or fine-tuning data for future model improvement

## Key Takeaways

- **Basic Reflection**: simplest setup; limited gains without external feedback grounding
- **Reflexion grounding**: forces enumeration of missing/superfluous content via external tools
- **Reflexion weakness**: single trajectory means early errors compound across iterations
- **LATS advantage**: parallel candidate exploration avoids single-trajectory failure mode
- **LATS use case**: strongest for code generation — unit test scoring as external evaluator
- **LATS unifies**: [[Reflexion]], [[Tree of Thoughts]], and plan-and-execute patterns in one framework
- **Universal tradeoff**: all three architectures exchange latency for output quality

## 🧠 First Principles & Mental Models

- **[[System 1 vs System 2 Thinking]]**: Reflection architectures are an explicit engineering attempt to force LLMs out of fast, associative response patterns and into the slower, iterative checking loop — the article names this directly as the design motivation.
- **[[Exploration vs Exploitation]]**: LATS instantiates this tradeoff via UCT scoring — it balances exploiting high-scoring known trajectories against exploring new candidate paths, which is why it outperforms single-trajectory Reflexion on complex tasks.
