# Agents

source_url: https://huyenchip.com/2025/01/07/agents.html

---

Author: Chip Huyen
Date: January 7, 2025

## Agent Design Fundamentals

An agent is anything perceiving and acting upon its environment, characterized by two elements: the environment it operates in and its available actions. Tools expand what agents can do — enabling both read-only perception and write actions that modify the world.

Three tool categories:
- **Knowledge augmentation**: web browsing, SQL executors, retrieval systems
- **Capability extension**: calculators, code interpreters, translators, multimodal converters
- **Write actions**: email APIs, database modifications, financial transactions

## Agentic Loops & Planning

Planning is fundamentally a search problem — evaluating paths toward a goal. A key design principle is decoupling planning from execution: generate a plan, validate it, then execute. Validation can use heuristics (e.g., eliminating plans with unavailable tools) or AI judges.

The ReAct pattern interleaves reasoning and action: "Thought → Act → Observation," cycling until task completion. Reflexion extends this with explicit self-critique after failures.

Control flows in complex plans include sequential, parallel, if-statement (routing), and for-loop structures.

## Human Oversight

Humans can intervene at any stage — providing plans, validating them, or approving risky operations like database updates or code merges. The key principle: "you need to clearly define the level of automation an agent can have for each action."

Write actions receive particular caution: "just as you shouldn't give an intern the authority to delete your production database, you shouldn't allow an unreliable AI to initiate bank transfers."

## Failure Modes

**Planning failures:**
- Invalid tool calls (hallucinated function names)
- Valid tools with wrong parameters or incorrect values
- Goal failures — solving the wrong task or ignoring constraints
- Reflection errors — agent incorrectly believes a task is complete

**Tool failures:**
- Incorrect tool outputs (e.g., wrong SQL, wrong image captions)
- Translation errors when converting natural-language plans to executable commands
- Missing tools for certain domains

**Efficiency failures:**
- Excessive steps or cost per task
- Unnecessarily slow sequential execution when parallel execution is possible

## Evaluation Approach

Create a planning dataset of (task, tool inventory) tuples and measure:
- Ratio of valid plans generated
- Average plans needed to reach a valid one
- Frequency of invalid tool calls, wrong parameters, incorrect values

Ablation studies help identify dispensable tools; tool-call distribution analysis reveals usage patterns.
