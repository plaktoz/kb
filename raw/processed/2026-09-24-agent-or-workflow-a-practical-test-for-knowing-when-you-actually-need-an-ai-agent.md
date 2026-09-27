---
source_url: https://machinelearningmastery.com/agent-or-workflow-a-practical-test-for-knowing-when-you-actually-need-an-ai-agent/
author: Kanwal Mehreen
date: 2026-09-24
---

# Agent or Workflow? A Practical Test for Knowing When You Actually Need an AI Agent

The article addresses the overuse of the term "agent" in AI and offers a framework for deciding between workflows and agents.

**Workflow** — a system where control flow is fixed at design time. Steps, branches, and logic are predetermined. LLMs may be used within steps, but the overall path is set in advance.

**Agent** — a system where the LLM decides at runtime what to do next, choosing tools, order of operations, and when to stop based on intermediate discoveries.

## The Core Test

> "Can you draw a complete flowchart of the task before the LLM ever runs?"

If yes → build a workflow. If the next step depends on runtime discoveries → consider an agent.

## Five-Point Checklist

1. Can major steps and branches be listed before runtime? → Workflow
2. Is input variability low enough for a maintainable decision tree? → Workflow
3. Are volume, cost, or latency constraints tight? → Workflow
4. Are identical execution paths required for compliance? → Workflow
5. Have you already tried a workflow with embedded LLM judgment? → Start there first

## Key Insight

Complexity doesn't define the category. A workflow can be sophisticated; a simple system can still be agentic if the model controls what happens next.
