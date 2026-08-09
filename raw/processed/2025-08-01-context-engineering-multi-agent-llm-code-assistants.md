---
source_url: https://arxiv.org/html/2508.08322v1
author: Muhammad Haseeb
date: 2025-08-01
---

# Context Engineering for Multi-Agent LLM Code Assistants Using Elicit, NotebookLM, ChatGPT, and Claude Code

This paper proposes a multi-stage workflow for improving LLM-based code assistants on complex, real-world repositories. The core argument is that single-agent approaches with static context windows produce incomplete or hallucinated solutions; structured, layered context injection combined with specialized sub-agents dramatically improves results.

## Methodology (4 Components)

1. **Intent Translator (GPT-5):** Converts ambiguous user requests into structured task specifications with explicit step-by-step breakdowns.

2. **Semantic Retrieval (Elicit):** Queries academic papers and documentation semantically, fetching top 3–5 relevant results (e.g., API guides, algorithm descriptions).

3. **Knowledge Synthesis (NotebookLM):** Condenses retrieved documents into bullet points or Q&A summaries, maintaining "high signal-to-noise ratio in the context."

4. **Claude Code Multi-Agent System:** Orchestrator-worker architecture with specialized sub-agents:
   - Backend architect
   - Frontend specialist
   - DevOps engineer
   - Code reviewer

   Each agent operates with an **isolated context window**, sharing only a common `CLAUDE.md` base file.

## Agent Orchestration Flow

The system cycles through: **Plan → Retrieve Context → Delegate → Edit/Implement → Run Tests → Review → Integrate/PR**

Failures trigger re-delegation to the responsible agent with error output attached.

## Results (RainMakerz Next.js codebase, ~180K lines)

| Metric | Multi-Agent System | Single-Agent Baseline |
|---|---|---|
| Single-shot success (5 tasks) | 4/5 (80%) | 2/5 (40%) |
| Token usage per task | ~100K | ~10–20K (but ~50K with retries) |

**Key finding:** The multi-agent system avoided hallucinated function names. Where the baseline invented a non-existent `refreshToken()` call, the multi-agent approach correctly used the existing `renewSession()` function drawn from retrieved context.

## Comparison to Prior Work

| System | Benchmark | Success Rate |
|---|---|---|
| MASAI | SWE-Bench Lite | 28.33% |
| HyperAgent | SWE-Bench Verified | 31.4% |
| DARS | SWE-Bench Lite | 47% pass@1 |
| This work | Custom (5 tasks) | 80% first-attempt |

Direct benchmark comparison is limited by the small, qualitative evaluation sample.

## Limitations

- Irrelevant Elicit retrievals can inject noise that "confused the Planner agent"
- Orchestration follows a fixed sequence; cannot dynamically re-plan mid-task
- Heavily dependent on an existing test suite for correctness validation
- Token costs are 3–5× higher than single-agent approaches
- Multi-agent debugging is difficult without trajectory visualization tools (e.g., SeaView)

## Key Takeaway

The paper demonstrates that providing LLMs with "not just more information, but the *right* information in the right form" — combined with role-decomposed agents — yields substantially better autonomous coding outcomes than monolithic prompt-based approaches.
