# Mission: Guardrails — AI/LLM and Software/System Implementation

## Why
Building AI-powered apps and backend services without guardrails means shipping systems that can be manipulated, abused, or silently broken by adversarial input, API instability, or unexpected model behavior. This course gives you the threat models, patterns, and tools to ship AI services that fail safely, enforce boundaries, and remain predictable under pressure.

## Success looks like
- You can name the OWASP Top 10 LLM risks and map each to a concrete guardrail type
- You can implement an input guardrail that blocks prompt injection and off-topic requests using a secondary LLM call
- You can implement an output guardrail that validates schema and detects toxicity/PII before surfacing a response
- You can wire a Circuit Breaker, retry-with-backoff, and rate limiter around an LLM API call in Python
- You can choose the right guardrail tool (Guardrails AI, NeMo Guardrails, Pydantic) for a given scenario and explain why
- You can describe the 6-layer guardrail stack for a production AI backend service from input to output

## Constraints
- Learning from research sources — no access to proprietary systems
- Self-paced, one lesson at a time
- Examples are Python-first (but patterns are language-agnostic)

## Out of scope
- Fine-tuning or RLHF for safety alignment
- Red-teaming methodology (attack techniques covered only as background for defense)
- Infrastructure-level security (network, IAM, secrets management)
- Specific LLM model benchmarks or safety evaluations
