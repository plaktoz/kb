# Humans and Agents in Software Engineering Loops

source_url: https://martinfowler.com/articles/exploring-gen-ai/human-agent-loops.html

---

Author: Kief Morris
Published: March 4, 2026
Source: martinfowler.com

This article introduces the concept of "harness engineering" — the practice of designing software systems where AI agents operate within loops that humans can monitor, correct, and guide without being in every individual step.

The core model: "on the loop" rather than "in the loop." Humans set goals, define guardrails, and review outputs periodically — rather than approving every AI action. This enables agentic systems to operate at speed while preserving human accountability.

Key concepts:

**Agentic flywheel**: Iterative loops where agents execute tasks, evaluate results, self-correct, and request human input only at decision points or when confidence is low.

**Harness design principles:**
- Define clear entry/exit criteria for human review
- Instrument loops with observability (logging, artifact snapshots)
- Grade confidence explicitly — agents should signal uncertainty rather than guess silently
- Design for human interruption at any point

**Role of the human in the loop:**
- Not a bottleneck but a governor
- Provides goal-level direction, not step-level supervision
- Reviews artifacts (diffs, summaries, outputs) rather than watching execution

Morris argues that "on the loop" is the right mental model for complex engineering workflows — distinguishing it from fully automated pipelines and from the older "human in the loop" model that requires step-by-step approval.

This framing has particular relevance for software delivery pipelines, CI/CD, infrastructure-as-code, and AI coding assistants.
