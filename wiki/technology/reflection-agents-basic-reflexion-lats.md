---
type: literature-note
source_url: https://www.langchain.com/blog/reflection-agents
author: Ankush Gola (LangChain)
tags: [reflection-loop, lats, reflexion, agentic-ai]
date_consumed: 2026-07-27
---

## Summary

Reflection as a prompting strategy prompts LLMs to critique their own past actions, shifting from reactive (System 1) toward methodical (System 2) thinking at the cost of added latency. The article presents three reflection architectures of increasing sophistication: Basic Reflection (fixed iterations), [[Reflexion]] (externally-grounded critique loop), and [[LATS]] (Monte Carlo Tree Search over candidate action paths). All three trade latency for quality and generate trajectory data reusable for fine-tuning.

## Core Concepts

- **Basic Reflection**: generator LLM + reflector LLM chained in a fixed iteration loop via [[LangGraph]] MessageGraph
- **[[Reflexion]]** (Shinn et al.): actor agent grounds critique in external evidence (search/citations); loops as draft → execute tools → revise up to MAX_ITERATIONS; single trajectory
- **[[LATS]] (Language Agent Tree Search)** (Zhou et al.): combines reflection, evaluation, and [[Monte Carlo Tree Search]]
  - Select via UCT (Upper Confidence Bound)
  - Expand N parallel candidate actions
  - Reflect and evaluate outcomes
  - Backpropagate scores to root
- **System 1 vs System 2 thinking**: reflection moves agent behavior from fast/reactive toward slow/deliberate
- **Trajectory reuse**: saved reflection trajectories become fine-tuning data or episodic memory
- **[[LangChain]]** / [[LangGraph]] implementation context

## Key Takeaways

- **Basic reflection limitation**: not grounded externally → marginal improvement only
- **Reflexion limitation**: single trajectory — early errors can compound without backtracking
- **LATS solves both**: tree search enables backtracking; parallel expansion prevents early lock-in
- **LATS is best for code**: unit test scoring provides objective external evaluation signal
- **Latency tradeoff**: all three approaches are unsuitable for low-latency production use cases
- **Trajectory data is valuable**: reflection runs generate labeled training examples automatically
- **LATS unifies**: [[Reflexion]] + [[Tree of Thoughts]] + plan-and-execute in one architecture

## 🧠 First Principles & Mental Models

- **[[Iterate Don't Predict]]**: Reflection loops embody this — instead of trying to generate perfect output in one shot, accept imperfection and improve iteratively. The question isn't "how smart is the model?" but "how many revision cycles can we afford?"
- **[[Explore-Exploit Tradeoff]]**: LATS makes this explicit via UCT — the UCB formula balances exploring new candidate actions against exploiting the currently best-scoring trajectory, which is exactly the explore-exploit dilemma formalized.
