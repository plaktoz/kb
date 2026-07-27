# LLM Powered Autonomous Agents

source_url: https://lilianweng.github.io/posts/2023-06-23-agent/

---

Author: Lilian Weng
Date: June 23, 2023

The article examines how large language models can serve as central controllers in autonomous agent systems. Three core components define these systems: Planning, Memory, and Tool Use.

## Planning & Task Decomposition

Agents must break complex tasks into manageable steps. Key approaches:
- **Chain of Thought (CoT)**: Instructs models to reason step-by-step, converting large tasks into smaller ones
- **Tree of Thoughts**: Extends CoT by branching into multiple reasoning paths, searchable via BFS or DFS
- **LLM+P**: Outsources planning to classical planners using PDDL as an intermediary language

## ReAct & Self-Reflection

**ReAct** (Yao et al., 2023) merges reasoning with action by prompting the model in a repeating format: "Thought: ... Action: ... Observation: ..." This loop allows the model to interact with environments (e.g., search APIs) while generating natural-language reasoning traces.

**Reflexion** (Shinn & Labash, 2023) extends this with dynamic memory — after each action, the agent evaluates its trajectory and may restart if it detects inefficiency or hallucination (defined as repeated identical actions producing identical observations).

**Chain of Hindsight (CoH)** trains models on sequences of past outputs annotated with feedback, encouraging progressive self-improvement.

**Algorithm Distillation (AD)** applies similar logic to RL: feeding multi-episode learning histories into a model so it can predict increasingly better actions.

## Memory Architecture

| Human Memory | Agent Equivalent |
|---|---|
| Sensory | Embedding representations of raw inputs |
| Short-term | In-context learning (limited by context window) |
| Long-term | External vector stores with fast retrieval |

For long-term memory, MIPS (Maximum Inner Product Search) via approximate nearest neighbor algorithms (LSH, ANNOY, HNSW, FAISS, ScaNN) enables fast retrieval from large knowledge stores.

## Tool Use

Agents extend their capabilities by calling external APIs. Notable frameworks:
- **MRKL**: Routes queries from a general LLM to specialized "expert" modules (neural or symbolic)
- **Toolformer / TALM**: Fine-tune models to learn when and how to invoke tools
- **HuggingGPT**: Uses ChatGPT as a task planner to coordinate models on HuggingFace
- **API-Bank**: A benchmark assessing tool-use across three levels — calling, retrieving, and multi-step planning with APIs

## Identified Challenges

1. **Finite context length** restricts historical awareness and communication bandwidth
2. **Long-term planning difficulty** — LLMs struggle to adapt when unexpected errors arise mid-plan
3. **Natural language interface fragility** — formatting errors and occasional non-compliance require significant output-parsing code

## Eval-Act Cycles

The planning loop across these systems generally follows: observe → reflect → plan → act → evaluate, with self-reflection or external reward signals closing the loop. Reflexion and ReAct most explicitly implement this cycle.
