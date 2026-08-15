# Context Engineering for Multi-Agent LLM Code Assistants

**Source:** https://arxiv.org/html/2508.08322v1
**Author:** Muhammad Haseeb (Virginia Tech)
**Date:** August 2025

---

## Abstract

The paper proposes a workflow combining multiple AI tools to address LLM limitations in complex, multi-file codebases:

- **GPT-5** as Intent Translator
- **Elicit** for semantic literature retrieval
- **NotebookLM** for document synthesis
- **Claude Code** multi-agent system for generation and validation

The system outperforms single-agent baselines on a ~180K-line Next.js codebase.

---

## 1. Introduction

Single-agent LLMs struggle with repository-level tasks due to:
- Limited context windows
- Hallucinations with unfamiliar APIs
- Missing cross-file coordination

The authors note that "a default Claude Code agent with a basic CLAUDE.md prompt often produced incomplete or incorrect solutions for non-trivial features."

Prior art cited for motivation:
- **MASAI**: 28.3% resolution on SWE-Bench Lite via modular sub-agents
- **HyperAgent**: 31.4% on SWE-Bench Verified using Planner/Navigator/Editor/Executor roles
- **AllianceCoder**: ~20% higher pass@1 via API description retrieval

---

## 2. Related Work

### LLM-based Coding Agents
HyperAgent and MASAI demonstrated that specialized sub-agents outperform monolithic approaches on benchmarks like SWE-Bench.

### Planning and Iterative Refinement
- **CodePlan**: High-level pseudocode plans improve multi-step reasoning
- **DARS**: Dynamic action re-sampling achieved 47% pass@1 on SWE-Bench Lite

### Retrieval-Augmented Code Generation
AllianceCoder found that providing API documentation yields gains, while blindly retrieving similar code can sometimes hurt performance.

### Agent Tooling and Debugging
**SeaView** was proposed to visualize agent trajectories — highlighting the need for better debugging interfaces in long agentic sessions.

---

## 3. Methodology: Context Engineering Workflow

The pipeline flows as:
> User Request → Intent Translator → Semantic Retrieval → Knowledge Synthesis → Claude Orchestrator → Sub-Agents + VectorDB + MCP Tools → Repository/CI/CD

### Intent Translation (GPT-5)
Converts ambiguous user queries into structured task specs. Example: *"Add a calendar view"* becomes an explicit list of UI, API, and test steps.

### Semantic Literature Retrieval (Elicit)
Queries academic papers and documentation using semantic search (not just keyword matching). Top k=3–5 results fetched as text/PDF.

### Knowledge Synthesis (NotebookLM)
Distills retrieved documents into bullet points and Q&A pairs. The authors found that "structuring external knowledge as a list of key bullet points...makes it much easier to integrate into the code-writing prompt."

### Repository Context Retrieval
- Vector DB built with ChromaDB or Zilliz
- Code chunked by function/class via AST parser (tree-sitter)
- Combines semantic search with lexical tools (grep)

---

## 4. System Architecture and Agent Orchestration

### 4.1 Claude Multi-Agent Design

Hub-and-spoke pattern: a central "Manager" Claude coordinates specialist sub-agents defined via YAML/Markdown files in `.claude/agents/`.

**Example agent config:**
```yaml
name: backend-architect
description: Design RESTful APIs, microservice boundaries,
and database schemas
model: sonnet
tools: Read, Write, Edit, Bash

You are a senior backend architect specializing in scalable
system design
```

Each sub-agent has an **isolated context window**, receiving only task-relevant information plus shared `CLAUDE.md` project context.

**Context layers (L1–L5):**
1. Task Specification (Intent Translator output)
2. External Knowledge (Elicit & NotebookLM)
3. Project Memory (CLAUDE.md, internal docs)
4. Retrieved Code Context (Vector DB, grep)
5. Execution Artifacts (diffs, logs, test results)

### 4.2 Agent Orchestration Flow

Sequential steps with feedback loops:

1. **Planning** — Planner agent produces concrete implementation steps
2. **Task Delegation** — Orchestrator routes steps to frontend/backend/devops agents
3. **Iterative Coding & Validation** — Agents edit code; test failures trigger corrections
4. **Code Review** — Dedicated reviewer checks type safety, performance, security
5. **Output/Deployment** — Diff consolidated; optionally pushed via GitHub Actions

---

## 5. Results

Evaluated on 5 tasks in the RainMakerz codebase (Next.js, ~180K LOC).

| Metric | Multi-Agent System | Single-Agent Baseline |
|--------|-------------------|----------------------|
| Single-shot success rate | 80% (4/5 tasks) | 40% (2/5 tasks) |
| Avg. token usage | ~100K | ~10–20K (but ~50K with debugging) |
| Context adherence | High — no hallucinated functions | Low — invented non-existent APIs |

### Case Study: CustomBlock Feature
The system successfully implemented a new pitch-deck block spanning React component, TypeScript types, and registry updates. An initial test failure (missing serialization whitelist entry) was caught and fixed automatically. The baseline missed registry and type definition updates entirely.

### Notable Findings
- Baseline invented a non-existent `getEvents()` API; the multi-agent system used the actual `renewSession()` function
- Token overhead (~3–5× more) is justified by autonomous task completion

---

## 6. Discussion

### Effect of Context Engineering
Each component contributed measurably. The Elicit-retrieved debounce explanation, for instance, led to a correct implementation where the baseline applied a superficial fix.

### Lessons on Multi-Agent Orchestration
- Clearly delineated responsibilities prevent both gaps and overlaps
- A file-lock mechanism was needed to prevent concurrent edits
- The reviewer agent caught issues (null pointer risks, security concerns) that coding agents missed

### Limitations
- Irrelevant Elicit results can introduce noise and confuse the Planner
- Orchestration follows a rigid sequence; dynamic re-planning is not yet supported
- Sparse test suites reduce the system's ability to verify correctness
- Multi-agent error tracing is difficult without tooling like SeaView

### Future Work
- Scaling to diverse stacks (Java, Python data science)
- Learning from past sessions via fine-tuning or RL
- Graph-based code representations for smarter planning
- Structured human-in-the-loop intervention points

---

## 7. Conclusion

The paper demonstrates that "the right information in the right form" matters more than simply providing more context. The multi-agent, context-layered approach moves toward autonomous software development by combining planning, retrieval, synthesis, and role-decomposed execution.

---

## References

1. Bui et al. (2024). HyperAgent. arXiv:2409.16299
2. Arora et al. (2024). MASAI. arXiv:2406.11638
3. Wen et al. (2025). CodePlan. ICLR 2025
4. Aggarwal et al. (2025). DARS. arXiv:2503.14269
5. Gu et al. (2025). AllianceCoder. arXiv:2503.20589
6. Bula et al. (2025). SeaView. arXiv:2504.08696
7. Anthropic (2025). How we built our multi-agent research system. Engineering Blog
