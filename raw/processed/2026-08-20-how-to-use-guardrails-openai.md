---
source_url: https://developers.openai.com/cookbook/examples/how_to_use_guardrails
author: Unknown
date: 2026-08-20
---

# How to Use Guardrails

This guide demonstrates implementing LLM guardrails — "detective controls that aim to steer your application" — covering two main types: input guardrails and output guardrails.

## What Are Guardrails?

Guardrails are detective controls that intercept and validate LLM inputs and outputs. They sit in the application layer, between users and the LLM, to enforce policies and prevent harm. Unlike training-time safety measures, application-layer guardrails are configurable, auditable, and can be updated independently of the model.

## Input Guardrails

Input guardrails intercept problematic content before it reaches the LLM:

- **Off-topic questions** — Block requests outside the application's intended scope
- **Jailbreaking attempts** — Detect prompts designed to bypass safety measures
- **Prompt injection** — Catch attempts to override system instructions with injected user content

**Async design pattern:** Run guardrail checks in parallel with the main LLM call. If the guardrail passes, the LLM response is already ready. If the guardrail fails, the response is discarded. This minimizes added latency.

## Output Guardrails

Output guardrails validate LLM responses before they are delivered to users:

**G-Eval-inspired scoring:** Content is graded 1–5 against defined criteria by a secondary LLM evaluation call. Responses scoring 3 or above on a harm scale are blocked before delivery.

Common output checks include:
- Factual accuracy / grounding verification
- Tone and policy compliance
- PII or sensitive data leakage
- Competitor mentions
- Toxic language

## Key Design Trade-offs

| Dimension | Consideration |
|---|---|
| Accuracy vs. latency | More thorough checks take longer |
| Accuracy vs. cost | LLM-based guardrails consume tokens |
| False positives | Degrade user experience through unhelpful over-refusals |
| False negatives | Risk business harm by letting harmful content through |

Async execution helps scale guardrails without hurting responsiveness, but adds architectural complexity.

## Known Limitations

- LLM-based guardrails share vulnerabilities with the base model — they can be fooled by the same attacks
- Long conversations increase jailbreak risk as context grows
- Overly strict guardrails cause unhelpful over-refusals that frustrate legitimate users

## Recommended Approach

1. **Gradual rollout** — Start with annotation-only mode before enabling blocking
2. **Active monitoring** — Track both false positives and false negatives over time
3. **Layered detection** — Combine LLM-based guardrails with traditional rules-based detection
4. **Regular red-teaming** — Proactively test for new attack vectors

The combination of async execution, layered detection, and continuous monitoring provides the best balance of safety, performance, and user experience.
