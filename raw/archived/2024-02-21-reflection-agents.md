# Reflection Agents

source_url: https://www.langchain.com/blog/reflection-agents

---

Author: Ankush Gola
Date: February 21, 2024

Reflection as a prompting strategy improves agent quality by prompting LLMs to critique their own past actions. This moves from "System 1" (reactive) toward "System 2" (methodical) thinking. The tradeoff: extra compute time in exchange for better output quality — suited for knowledge-intensive tasks over low-latency ones.

## Three Architectures

### 1. Basic Reflection

Two chained LLM calls: a generator and a reflector. The reflector plays a teacher role, offering critique. The loop runs a fixed number of iterations. State is managed as a list of messages via LangGraph's MessageGraph. Limitation: reflection isn't grounded externally, so improvement may be marginal.

### 2. Reflexion (Shinn et al.)

An actor agent that explicitly critiques responses and grounds feedback in external data (e.g., search/citations). The agent is forced to enumerate missing or superfluous content. The loop: draft → execute tools → revise, repeating up to MAX_ITERATIONS. Weakness: it follows one fixed trajectory, so early errors can compound.

### 3. Language Agent Tree Search (LATS) (Zhou et al.)

Combines reflection, evaluation, and Monte Carlo Tree Search. The four steps:
1. **Select** — pick best next action using Upper Confidence Bound (UCT)
2. **Expand & Simulate** — generate N parallel candidate actions
3. **Reflect & Evaluate** — score outcomes via reflection or external feedback
4. **Backpropagate** — update root trajectory scores

LATS is well-suited for code generation (e.g., unit test scoring) and unifies reasoning patterns from Reflexion, Tree of Thoughts, and plan-and-execute architectures.

## Key Takeaway

All three approaches trade latency for quality. Saving trajectories enables future model improvement — either as memory or fine-tuning data.
