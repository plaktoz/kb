# Experience Memory Graph (EMG): Graph-Based Error Correction for AI Agents

## Core Idea

EMG replaces the costly "fail, reflect, retry" loop in AI agents with a deterministic, math-based error correction mechanism. Rather than asking the LLM to verbally diagnose its own failures, EMG:

1. Represents both the **failed agent path** and the **expert (successful) path** as directed decision graphs.
2. Applies the **Fused Gromov-Wasserstein (FGW) algorithm** to mathematically compute the structural difference between the two graphs.
3. Stores the computed correction as a reusable **experience memory** — a set of discrete edit operations (delete, add, rename) expressed in natural language.
4. At test time, retrieves the closest correction pattern from the database via **cosine similarity** and injects it into the agent's context as a skill-like instruction.

## Why Graphs Instead of Text

Traditional reflection loops depend on the LLM's ability to self-diagnose — unreliable for small models (4B–8B parameters). Graphs provide a **mathematical, deterministic basis** for comparing behavioral trajectories:

- Nodes = agent actions (e.g., "pick up apple")
- Edges = environmental observations / state transitions
- Graph structure captures **causal position**, not just semantic similarity

The FGW algorithm handles non-isomorphic graphs: failed and expert graphs rarely have the same size or topology, yet FGW finds the minimum-cost alignment by jointly optimizing node content similarity (Wasserstein term) and structural compatibility (Gromov term).

## How the Correction Is Derived

The aligned transport map (a probability matrix) identifies:
- **Common subgraph** (green): steps that already match — keep as-is.
- **Delete operations**: nodes/edges in the failed graph with no match in the expert graph.
- **Add operations**: nodes/edges present in the expert graph but absent in the failed graph.
- **Rename operations**: structurally matched nodes whose action labels differ (e.g., "put on table" → "put on shelf").

These three edit types are then translated back into **natural language correction rules** and stored in a vector database.

## Training vs. Test Time

| Phase | What happens |
|-------|-------------|
| **Training** | Graph matching runs offline; FGW computes corrections; results stored as text in a vector DB |
| **Test** | Zero graph math — task description is embedded, top-K similar corrections retrieved via cosine similarity, injected into agent prompt |

This asymmetry is why EMG works well with small models: all heavy math runs offline.

## MemoHarness + EMG Combination

The paper proposes pairing two complementary systems:
- **MemoHarness** — RAG-based control layer that dynamically configures the agent's memory and tools around the LLM kernel ([[loop-engineering-agent-loop-design]])
- **EMG** — graph-matching inside the agent's procedural memory to ensure the correct action sequence without costly reflection loops

MemoHarness fixes *system configuration failures*; EMG fixes *internal decision failures* (the agent had the right tools but pressed the wrong button).

## Performance

On 4B-parameter models, EMG achieved ~40% average task success vs ~20s for reflection-based baselines. Time cost was near-zero compared to reflection loops that took ~4x longer for equivalent success rates.

## Limitations

- Does not guarantee the globally optimal correction path — depends on quality of training examples.
- Unseen tasks at test time rely entirely on similarity retrieval; no online graph construction occurs.
- The retrieval step reverts to standard RAG with cosine similarity — a known bottleneck that well-understood pre-2024 methods already solve.
- At test time, the LLM still has to correctly apply a correction learned from a different task — a transfer gap the paper does not fully address.

## Source

- Paper: *Experience Memory Graph: One-Shot Error Correction for Agents* (arXiv:2607.13884), UESTC Chengdu, July 2026
- Video: [From LOOPS to GRAPHS: AI Agents Learn Graph-Based Error Corrections](https://www.youtube.com/watch?v=yC9cd3gKaIc) — Discover AI

## Related Notes

- [[loop-engineering-agent-loop-design]]
- [[graph-theory]]
- [[rag-evolution-simple-retrieval-to-agentic-ai]]
- [[graph-engineering-verification-anthropic-agents]]
- [[agentic-design-patterns-reflection]]
