---
type: literature-note
source_url: https://www.youtube.com/watch?v=abvQEhvRI_c
author: Andreas Kollegger & Zaid Zaim (Neo4j), AI Engineer
tags: [context-graphs, decision-aware-agents, knowledge-graph, neo4j, agentic-ai, risk-value-analysis, precedent-learning]
date_consumed: 2026-08-04
---

## Summary

Zaid Zaim and Andreas Kollegger (Neo4j) argue that context engineering for AI agents needs to go beyond knowledge and tools — agents must also have access to policies, rules, and prior decisions to become genuinely decision-aware. The key artefact is a **context graph**: a knowledge graph enriched with the "why" layer (rules, policies, precedent reasoning chains) that explains why a given action is correct in a given context. The talk introduces a five-stage decision-making framework — frame, global-context, risk-value analysis, act/escalate, write-precedent — where the final step is the most important: every decision is written back into the graph and becomes precedent for future agents.

## Core Concepts

- **[[Context Graph]]**: A knowledge graph extended with policies, rules, and recorded reasoning chains; adds the *why* dimension missing from pure knowledge graphs. Distinguishes itself from context engineering in that it encodes not just knowledge and tools but decision rationale.
- **Memory layers in context graphs**:
  - *Short-term*: Recent conversation state and action history.
  - *Long-term*: Generalised entities — people, organisations, things.
  - *Reasoning memory*: Stored reasoning chains and policy decisions that guide future decisions.
- **Agentic graph architecture**: User query → agent checks knowledge cache → if missing, text-to-Cypher tool traverses [[Neo4j]] graph → result returned with richer context.
- **Reference class validation**: Before acting, an agent must determine which group a situation belongs to — the 99% case or the dangerous 1% case (e.g., prescribing drug X that is correct 99% of the time but fatal in a specific population). Statistical reasoning cannot substitute for explicit class membership.
- **Five-stage decision framework**:
  1. **Frame the problem**: Define objective, causality (how did we get here?), and environment (medical, financial, household).
  2. **Global context**: Pull relevant prior decisions for consistency, and hard/soft rules of the organisation.
  3. **Risk-value analysis**: Assess reference class, reversibility, cost of being wrong; identify what is being maximised or minimised.
  4. **Act or escalate**: Propose options with pros/cons; if the agent lacks authority or certainty, escalate to a higher-privilege agent or a human-in-the-loop.
  5. **Write precedent**: Record the full reasoning chain, what was considered and rejected, and the decision itself back into the context graph.
- **Compartmentalised agent roles**: The risk-value analysis agent only proposes options; a separate agent decides whether to act based on authority. Separation prevents premature commitment.
- **Human-in-the-loop escalation**: An authority check governs when an agent defers to a human — triggered by insufficient certainty or insufficient authority.

## Key Takeaways

- **Graphs give agents the "why"**: Knowledge and tools alone produce agents that know *what* to do on average but cannot handle edge cases; policies and rules in the context graph close that gap.
- **Reference class is the hardest step**: Most AI engineering mistakes stem from applying the average-case rule to an instance that belongs in the 1% class — making class membership explicit is the fix.
- **Precedent compounds value**: Every decision written back into the graph becomes training data for future agents, turning each successful decision into a reusable asset.
- **Reversibility changes risk calculus**: Whether a decision can be undone should explicitly change how much analysis is performed before acting.
- **Domain specificity is unavoidable**: The framework is general, but every step requires domain-specific instantiation — there is no fully generalisable agent decision procedure.
- **Parallel to human organisations**: MBA-style decision frameworks transfer directly to agent design; what is implicit for humans must be made explicit for agents.

## Related Notes

- [[knowledge-graph]] — foundational context on knowledge graphs and their structure
- [[graph-rag-implementation-neo4j-langchain]] — Neo4j-based retrieval pipeline implementation
- [[rag-graphrag-context-engineering-ai-performance]] — context engineering as a discipline; GraphRAG for precision retrieval
- [[graph-algorithms-ai-applications-practitioners-guide]] — practical graph algorithms (PPR, shortest path, subgraph matching) for AI applications
- [[microsoft-graphrag]] — Microsoft Research's GraphRAG community detection approach

## First Principles & Mental Models

- **[[Explicit vs Implicit Knowledge]]**: The central engineering challenge of agentic AI is making implicit human decision knowledge explicit — this talk operationalises that principle as a structured five-stage workflow written into a graph.
- **[[Separation of Concerns]]**: Decomposing decision-making into framing, analysis, acting, and precedent-writing keeps each sub-agent focused and auditable, preventing reasoning from becoming entangled with action.

## Review Questions

**Q1**: What is a context graph and how does it differ from a standard knowledge graph?
**A**: A context graph is a knowledge graph augmented with policies, rules, and recorded reasoning chains — it captures not just what entities exist and how they relate, but *why* an agent should act in a certain way, giving it the missing "why" layer.

**Q2**: What is reference class validation and why does it matter in risk-value analysis?
**A**: Reference class validation is determining whether a given instance belongs to the common case (99%) or the edge case (1%) before deciding what to do — because the statistically optimal action in the common class may be fatal in the edge class, average-case statistical reasoning is insufficient.

**Q3**: Why is writing the reasoning chain back into the graph (step 5) described as the most important part of the framework?
**A**: Because every recorded decision becomes precedent — future agents can retrieve prior reasoning, decisions, and the rules that applied, making the system self-improving and consistent over time rather than repeating costly deliberation from scratch.
