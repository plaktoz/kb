---
type: literature-note
source_url: https://machinelearningmastery.com/agent-or-workflow-a-practical-test-for-knowing-when-you-actually-need-an-ai-agent/
author: Kanwal Mehreen
tags: [ai-agents, agentic-ai, llm-workflow, system-design]
date_consumed: 2026-09-27
---

## Summary

The article cuts through the overuse of "agent" in AI discourse by offering a single diagnostic question: can you draw a complete flowchart of the task before the LLM ever runs? If yes, build a [[Workflow]]; if the next step depends on runtime discoveries, consider a true [[AI Agent]]. A five-point checklist operationalizes this test, biasing practitioners toward the simpler, cheaper, and more reliable workflow unless genuine runtime adaptability is required.

## Core Concepts

- **[[AI Agent]]**: A system where the [[LLM]] decides at runtime what to do next — choosing tools, order of operations, and stopping conditions based on intermediate discoveries.
- **[[Workflow]]**: A system where control flow is fixed at design time; steps, branches, and logic are predetermined even if LLMs are used within individual steps.
- **[[Flowchart Test]]**: The core decision heuristic — if the full execution path can be drawn before runtime, it's a workflow regardless of how many LLM calls it makes.
- **[[Runtime Adaptability]]**: The defining property of agents; the model must be able to redirect the execution path mid-task based on what it discovers.
- **[[LLM Chaining]]**: Connecting LLM calls sequentially in a predetermined pipeline — this is still a workflow, not an agent, even though it uses multiple model calls.
- **[[Kanwal Mehreen]]**: Author covering practical AI engineering and ML system design.

## Key Takeaways

- **The flowchart test**: "Can you draw a complete flowchart before the LLM runs?" — yes = workflow.
- **Complexity ≠ agency**: A sophisticated multi-step pipeline is still a workflow if steps are predetermined.
- **Five workflow signals**: fixed steps, low input variability, tight cost/latency budgets, compliance traceability, or an untried embedded-LLM workflow.
- **Default to workflow**: always try a workflow with embedded LLM judgment before reaching for an agent.
- **Agents earn their complexity**: use only when the model genuinely needs to decide next steps from runtime output.
- **Identical execution paths**: compliance or audit requirements favor workflows over agents.

## 🧠 First Principles & Mental Models

- **[[Occam's Razor]]**: The flowchart test is a direct application — prefer the simpler deterministic structure (workflow) until the problem provably requires the more complex adaptive one (agent), because complexity should not be introduced without necessity.
- **[[Premature Optimization Fallacy]]**: Reaching for agents before exhausting workflow solutions mirrors the classic engineering mistake of over-engineering for flexibility you haven't yet needed — the article's "try a workflow first" rule encodes exactly this principle.

## 🃏 Review Questions

**Q1**: What is the single diagnostic question that separates a workflow from an agent?
**A**: "Can you draw a complete flowchart of the task before the LLM ever runs?" If yes, build a workflow; if the next step depends on what the model discovers at runtime, consider an agent.

**Q2**: What are two of the five checklist signals that indicate a workflow is the right choice?
**A**: Any two of: major steps can be listed before runtime; input variability is low enough for a maintainable decision tree; volume/cost/latency constraints are tight; identical execution paths are required for compliance; or a workflow with embedded LLM judgment hasn't been tried yet.

**Q3**: How should a practitioner apply the agent-vs-workflow framework when starting a new AI task?
**A**: Default to a workflow with embedded LLM judgment first; only escalate to a true agent if the task genuinely requires the model to redirect its own execution path based on intermediate discoveries.
