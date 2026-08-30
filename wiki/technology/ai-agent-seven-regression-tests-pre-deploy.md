---
type: literature-note
source_url: https://machinelearningmastery.com/7-regression-tests-every-ai-agent-should-pass-before-deploy/
author: Vinod Chugani
tags: [ai-agents, testing, ci-cd, regression-testing]
date_consumed: 2026-08-29
---

## Summary

Most AI agent failures originate in the orchestration layer's state management, not model intelligence. The article presents seven binary pass/fail regression tests suited for CI/CD pipelines, grounded in the distinction between "state" (deterministic execution records) and "memory" (probabilistic retrieved context). Passing all seven is a minimum bar before any agent deployment.

## Core Concepts

- **[[Regression Testing for AI Agents]]** — binary pass/fail checks targeting orchestration-layer failure modes, not model quality; designed to slot into [[CI/CD Pipeline]] automation
- **[[State vs. Memory in Agents]]** — "state" is deterministic (execution records, serialized data); "memory" is probabilistic (retrieved context); conflating them causes brittle test design
- **[[Tool Idempotency]]** — identical tool-call payloads must produce exactly one write, regardless of retry count; idempotency keys should derive from operation identity, not step ID or message position
- **[[Prompt Injection Resistance]]** — adversarial payloads embedded in user input *and* indirect vectors (e.g., retrieved documents); assertions must target the tool-call trace and side effects, not output prose
- **[[Structured Output Adherence]]** — goes beyond schema syntax; failure modes include truncation (check `finish_reason`), refusals mishandled as transient errors, semantic invalidity, and model-version skew from aliases
- **[[Bounded Orchestration]]** — preventing non-termination requires a triple budget: max steps, max token cost, and wall-clock timeout; step count alone misses a single hanging step
- **[[RAG Grounding Test]]** — use a synthetic fact contradicting common knowledge; test both directions: agent should prefer correct retrieved context over stale parametric recall, but also resist obviously wrong retrieved facts
- **[[State Rehydration]]** — serialize agent state mid-workflow, destroy the in-memory object, and rehydrate in a new process; two failure points are version skew in serialization schemas and mid-tool-call resumption needing idempotency key infrastructure

## Key Takeaways

- **Root cause is orchestration, not intelligence**: most failures stem from state management, not the model itself.
- **Binary pass/fail design**: tests must be deterministic enough for automated CI/CD gates.
- **Context Loss**: query a fact from turn one after filling ~80% of prompt budget; retrieval success ≠ summarization success.
- **Idempotency keys from operation identity**: step ID or message position are unstable keys — derive from what the operation *does*.
- **Prose refusal masks harmful tool calls**: "an agent can produce a polite refusal in prose while still emitting a harmful tool call underneath."
- **Triple budget for non-termination**: max steps + max token cost + wall-clock timeout — any single budget leaves a gap.
- **RAG grounding is bidirectional**: the agent must adopt correct retrieved facts *and* resist incorrect ones.
- **Explicit out-of-scope**: cost/latency regression, API schema drift, PII leakage in traces, and embedding-space skew are not covered.

## 🧠 First Principles & Mental Models

- **[[Separation of Concerns]]**: Distinguishing state (deterministic) from memory (probabilistic) is the foundational design move — tests that conflate the two will produce flaky, untrustworthy results.
- **[[Defense in Depth]]**: The seven tests cover independent failure surfaces (retrieval, side effects, injection, output schema, loops, grounding, persistence) — no single test catches all modes; layered coverage is the only defense.

## 🃏 Review Questions

**Q1**: What is the article's core claim about where AI agent failures originate?
**A**: Most failures come from orchestration-layer state management problems, not from model intelligence — the model is rarely the broken part.

**Q2**: Why must prompt-injection assertions target the tool-call trace rather than output prose?
**A**: An agent can emit a polite textual refusal while simultaneously issuing a harmful tool call underneath; only inspecting the tool-call trace and side effects catches this.

**Q3**: How should a practitioner apply the RAG grounding test, and why must it be bidirectional?
**A**: Inject a synthetic fact that contradicts common knowledge, then verify the agent adopts the correct retrieved fact over stale training data; also verify it resists a clearly wrong retrieved fact — one-directional tests miss half the failure surface.

## Links

- [[ai-agent-three-failure-modes-harness-done-test-graph]] — complementary diagnostic framework (harness, done test, graph) that precedes formal regression testing
- [[agentic-manual-testing]] — manual testing by agents as a complement to automated regression suites
- [[agentic-design-patterns-reflection]] — reflection loops as a runtime mechanism that regression tests can validate
