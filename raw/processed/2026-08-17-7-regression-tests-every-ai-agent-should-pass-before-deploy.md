---
source_url: https://machinelearningmastery.com/7-regression-tests-every-ai-agent-should-pass-before-deploy/
author: Vinod Chugani
date: 2026-08-17
---

# 7 Regression Tests Every AI Agent Should Pass Before Deploy

The article argues that most agent failures stem from orchestration-layer state management problems, not model intelligence. It distinguishes "state" (deterministic execution records) from "memory" (probabilistic retrieved context), then presents seven binary pass/fail regression tests suited for CI/CD pipelines.

## The 7 Tests

1. **Context Loss & Retrieval Degradation** – Tests whether critical facts from early conversation turns survive context eviction. Feed ~80% of your prompt budget in history, then query a fact from turn one. Warns against conflating retrieval success with summarization success.

2. **Tool Execution Idempotency** – Fires the same tool-call payload three times; passes only if exactly one write registers. Idempotency keys should derive from operation identity, not step ID or message position.

3. **Prompt Injection Resistance** – Injects adversarial payloads via user input *and* indirect vectors (e.g., retrieved documents). Assert on the tool-call trace and side effects, not output prose — "an agent can produce a polite refusal in prose while still emitting a harmful tool call underneath."

4. **Structured Output Adherence** – Goes beyond syntax checks. Key failure modes: truncation mid-output (check `finish_reason`), refusals mishandled as transient errors, semantic invalidity, and model-version skew from aliases.

5. **Non-Termination & Bounded Orchestration** – Distinguishes livelock (cycling without progress) from true deadlock. Set a triple budget: max steps, max token cost, and wall-clock timeout. A step count alone won't catch a single hanging step.

6. **RAG Grounding vs. Parametric Recall** – Introduces a synthetic fact contradicting common knowledge. Tests *both* directions: the agent should adopt correct retrieved facts over stale training data, but also resist obviously wrong retrieved information.

7. **State Rehydration & Consistency** – Serializes agent state mid-workflow, destroys the in-memory object, and rehydrates in a new process. Two common failure points: version skew between serialization schemas, and mid-tool-call resumption requiring idempotency key infrastructure.

## What These Tests Don't Cover

Cost/latency regression, upstream API schema drift, PII leakage in traces, and embedding space skew from new encoder versions are explicitly out of scope.
