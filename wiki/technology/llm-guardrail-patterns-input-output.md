---
type: literature-note
source_url: https://developers.openai.com/cookbook/examples/how_to_use_guardrails
author: Unknown
tags: [llm-safety, guardrails, prompt-injection, ai-architecture]
date_consumed: 2026-08-20
---

## Summary
LLM guardrails are application-layer detective controls that intercept and validate inputs before they reach the model and outputs before they reach users. Two main types exist: input guardrails (blocking off-topic requests, jailbreaks, and prompt injection) and output guardrails (checking factual grounding, tone, PII leakage, and toxicity). The key architectural insight is running guardrail checks asynchronously in parallel with the main LLM call to minimize latency impact.

## Core Concepts
- [[Input Guardrails]] — validate user prompts before the LLM sees them; catches [[Prompt Injection]], [[Jailbreaking]], and off-topic queries
- [[Output Guardrails]] — validate LLM responses before delivery; uses [[G-Eval]]-inspired 1–5 scoring by a secondary LLM call
- [[Async Guardrail Pattern]] — run guardrail and main LLM call in parallel; discard main response only if guardrail fails
- [[Layered Detection]] — combine LLM-based guardrails with rules-based checks to reduce shared vulnerabilities
- [[Red-Teaming]] — proactive adversarial testing to discover new attack vectors before production exposure

## Key Takeaways
- **Async execution**: Run guardrail and LLM calls in parallel to avoid adding latency.
- **G-Eval scoring**: Score outputs 1–5; block responses at threshold 3+ on harm scale.
- **Input threats**: Covers off-topic queries, jailbreaks, and prompt injection attempts.
- **Output threats**: Covers PII leakage, toxicity, hallucination, and competitor mentions.
- **Gradual rollout**: Start in annotation-only mode before enabling hard blocking.
- **False positive cost**: Over-refusals degrade UX as much as false negatives risk harm.
- **Shared vulnerability**: LLM-based guardrails can be fooled by the same attacks as the base model.
- **Long context risk**: Jailbreak success rates increase as conversation history grows.

## 🧠 First Principles & Mental Models

**Defense in Depth** — No single guardrail is sufficient; layering LLM-based and rules-based checks mirrors the security principle that multiple independent controls reduce overall failure probability.

**Accuracy-Latency-Cost Triangle** — Guardrail design forces explicit trade-offs: more thorough checks improve safety but increase latency and token cost; the async pattern is the primary lever for escaping this trade-off.

## 🃏 Review Questions

**Q1**: What is the core purpose of application-layer guardrails vs. model training-time safety?
**A**: Application-layer guardrails are configurable, auditable detective controls that can be updated independently of the model, whereas training-time safety is baked in and cannot be changed post-deployment.

**Q2**: How does the async guardrail pattern reduce latency?
**A**: The guardrail check and the main LLM call run concurrently; if the guardrail passes, the LLM response is already ready with no sequential wait, and the response is only discarded if the guardrail fires.

**Q3**: Why should guardrail rollout begin in annotation-only mode?
**A**: Annotation-only mode lets teams measure false positive and false negative rates on real traffic before enabling blocking, preventing premature over-refusals that would harm user experience.
