# Lesson Plan: Guardrails — AI/LLM and Software/System Implementation

*Source: `research/guardrails-implementation/report.md`*
*Each lesson → one HTML file in `lessons/`, one reference doc in `reference/`*

---

## Module 1 — Foundations: What Are Guardrails?
*Establishes the shared mental model and threat landscape before splitting into the two implementation tracks.*

### Lesson 1: The Guardrail Mental Model
**File:** `lessons/0001-guardrail-mental-model.html`
**Key concepts:** funnel-and-filter model · defense in depth · fail-safe vs. fail-open · specificity over breadth
**Source paper:** Report §1 — core concepts and three unifying principles
**Skill:** Draw the funnel-and-filter diagram for a system of your choice (LLM chatbot or REST API); label where each of the three principles applies
**Reference doc:** `reference/mental-models.html`

### Lesson 2: What Guardrails Defend Against — OWASP Top 10 for LLMs
**File:** `lessons/0002-owasp-top-10-llm.html`
**Key concepts:** prompt injection · insecure output handling · excessive agency · sensitive information disclosure · supply chain vulnerabilities
**Source paper:** https://owasp.org/www-project-top-10-for-large-language-model-applications/ — 10 highest-risk LLM vulnerabilities with mitigation guidance
**Skill:** For each of the 10 OWASP risks, write one sentence naming the guardrail type that mitigates it (input filter, output filter, rate limit, etc.)
**Reference doc:** `reference/owasp-llm-top10.html`

---

## Module 2 — AI/LLM Guardrails
*Moves from the threat taxonomy into concrete attack techniques, then to the input and output guardrail patterns that defend against them.*

### Lesson 3: Adversarial Prompting — Injection, Leaking, and Jailbreaking
**File:** `lessons/0003-adversarial-prompting.html`
**Key concepts:** prompt injection · prompt leaking · jailbreaking (DAN, Waluigi, GPT-4 Simulator) · parameterization defense · adversarial detector LLM
**Source paper:** https://www.promptingguide.ai/risks/adversarial — attack taxonomy and defense techniques for LLM prompts
**Skill:** Write a system prompt for a customer support chatbot that includes defensive instructions against at least two of the attack types covered
**Reference doc:** `reference/adversarial-attacks.html`

### Lesson 4: Advanced Attack Techniques and Defense Strategies
**File:** `lessons/0004-advanced-attacks-defenses.html`
**Key concepts:** token manipulation (TextFooler, BERT-Attack) · GCG adversarial suffixes · perplexity filtering · paraphrasing defense · no single defense is robust
**Source paper:** https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/ — comprehensive survey of adversarial attack methods and defense strategies
**Skill:** For each defense strategy (perplexity filtering, paraphrasing, adversarial training, retokenization), write one sentence on when you would and would not use it in a production system
**Reference doc:** *(extend existing adversarial-attacks.html)*

### Lesson 5: Input Guardrails — Topical Filtering and Jailbreak Detection
**File:** `lessons/0005-input-guardrails.html`
**Key concepts:** topical guardrail · secondary LLM call pattern · allowed/not_allowed response schema · async execution for latency · jailbreak detection
**Source paper:** https://developers.openai.com/cookbook/examples/how_to_use_guardrails — input/output guardrail patterns with async execution and G-Eval
**Skill:** Write pseudocode for an async input guardrail that runs a secondary LLM check in parallel with the main call, returning the guardrail response if triggered
**Reference doc:** `reference/input-output-guardrails.html`

### Lesson 6: Output Guardrails — Filtering, Scoring, and Production Content Filters
**File:** `lessons/0006-output-guardrails.html`
**Key concepts:** G-Eval output scoring · harm category classification · annotate-only vs. block mode · PII detection · groundedness detection · finish_reason: content_filter
**Source paper:** https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/content-filter — Azure OpenAI's multi-layer content filtering system with categories, severity levels, and API scenarios
**Skill:** Design an output guardrail policy for a medical information chatbot: list the harm categories to filter, the severity threshold for each, and whether to annotate-only or block
**Reference doc:** *(extend existing input-output-guardrails.html)*

---

## Module 3 — Software/System Guardrails
*Covers the defensive patterns every backend service needs — especially relevant for the infrastructure wrapping LLM API calls.*

### Lesson 7: The Circuit Breaker Pattern
**File:** `lessons/0007-circuit-breaker.html`
**Key concepts:** Closed → Open → Half-Open state machine · failure threshold · reset timeout · cascading failure prevention · fallback strategies
**Source paper:** https://martinfowler.com/bliki/CircuitBreaker.html — the foundational pattern description by Martin Fowler
**Skill:** Draw the state machine for a circuit breaker; then write pseudocode wrapping an LLM API call with a circuit breaker that opens after 3 consecutive failures and retries after 30 seconds
**Reference doc:** `reference/software-guardrail-patterns.html`

### Lesson 8: Timeouts, Retries, and Exponential Backoff with Jitter
**File:** `lessons/0008-timeouts-retries-backoff.html`
**Key concepts:** connection vs. read timeout · idempotent operations · retry budget · exponential backoff formula · full jitter · thundering herd problem
**Source paper:** https://builder.aws.com/content/3EumjoZascWd1oZiEgL8ORlv3qE/timeouts-retries-and-backoff-with-jitter — AWS builder's library guide on layering these three defensive patterns
**Skill:** Calculate the backoff values for 4 retry attempts using `min(cap=32s, base=1s * 2^attempt)` with full jitter; then write the combined timeout+retry+backoff pseudocode for an LLM API call
**Reference doc:** *(extend existing software-guardrail-patterns.html)*

### Lesson 9: Rate Limiting — Algorithms and When to Use Each
**File:** `lessons/0009-rate-limiting.html`
**Key concepts:** Fixed Window Counter · Token Bucket · Leaky Bucket · Sliding Window Log · Sliding Window Counter · HTTP 429 · limit/window/identifier triad
**Source paper:** https://blog.bytebytego.com/p/rate-limiting-fundamentals — algorithm taxonomy with use-case guidance
**Skill:** For a public AI API with free and paid tiers, choose one rate-limiting algorithm per tier and justify the choice; then describe what happens when a free-tier user exceeds their limit mid-stream
**Reference doc:** *(extend existing software-guardrail-patterns.html)*

---

## Module 4 — Tools, Libraries, and Integration
*Bridges concepts to code — covers the main Python libraries and assembles everything into a production-ready 6-layer stack.*

### Lesson 10: Guardrails AI — Guards, Validators, and the Hub
**File:** `lessons/0010-guardrails-ai-library.html`
**Key concepts:** Guard · Validator · OnFailAction · Guardrails Hub · guardrails start (REST service) · Pydantic structured output
**Source paper:** https://github.com/guardrails-ai/guardrails — open-source library README with code examples
**Skill:** Write a Guard that combines ToxicLanguage (threshold 0.5) and a RegexMatch validator, and describe what happens when the Guard raises an exception vs. when it filters
**Reference doc:** `reference/guardrails-tools.html`

### Lesson 11: NeMo Guardrails and Pydantic — Programmable Rails and Boundary Validation
**File:** `lessons/0011-nemo-pydantic.html`
**Key concepts:** Colang conversational flows · YAML rails configuration · LLMRails API · Pydantic BaseModel · strict vs. lax mode · ValidationError · boundary enforcement layer
**Source paper:** https://docs.nvidia.com/nemo/guardrails/ + https://pydantic.dev/docs/validation/latest/get-started/ — NeMo's programmable rails and Pydantic's type-driven validation
**Skill:** Write a Pydantic model for a chatbot request (message, user_id, session_token) with at least one custom validator; then sketch the NeMo YAML config that would add a topic rail limiting the chatbot to cooking topics
**Reference doc:** *(extend existing guardrails-tools.html)*

### Lesson 12: End-to-End — Building a Guardrailed AI Backend Service
**File:** `lessons/0012-end-to-end-guardrailed-service.html`
**Key concepts:** 6-layer guardrail stack · integration sequencing · which layer catches which failure mode · latency budget per layer · graceful degradation
**Source paper:** Report §5 — synthesized 6-layer guardrail architecture (Pydantic → Rate limit → LLM input guard → LLM output guard → Circuit breaker → Retry with backoff)
**Skill:** Given a scenario (e.g., a legal document summarizer API), map each of the 6 layers to a specific implementation choice and describe what each layer catches that the others miss
**Reference doc:** `reference/end-to-end-stack.html`

---

## Suggested Teaching Order

Work through modules in sequence — Module 1 builds the conceptual frame; Module 2 fills it with AI-specific attack/defense knowledge; Module 3 layers in the software resilience patterns; Module 4 wires everything into working code. Don't skip Module 3 before Module 4 — the 6-layer stack in Lesson 12 depends on understanding Circuit Breaker and Rate Limiting from Module 3.

---

## Reference Documents to Build

| File | Contents |
|------|----------|
| `reference/mental-models.html` | Funnel-and-filter diagram, defense-in-depth principle, fail-safe vs. fail-open decision guide |
| `reference/owasp-llm-top10.html` | Full OWASP Top 10 LLM risks with guardrail mapping table |
| `reference/adversarial-attacks.html` | Attack taxonomy (injection, leaking, jailbreaking, token manipulation, GCG) with defense strategy comparison table |
| `reference/input-output-guardrails.html` | Input guardrail patterns (secondary LLM, async), output patterns (G-Eval, content filter), latency tradeoff guide |
| `reference/software-guardrail-patterns.html` | Circuit breaker state machine, timeout/retry/backoff formulas, rate limiting algorithm comparison table |
| `reference/guardrails-tools.html` | Guardrails AI Guard/Validator code examples, NeMo YAML config skeleton, Pydantic BaseModel template |
| `reference/end-to-end-stack.html` | 6-layer guardrail stack diagram with per-layer tool choices and failure mode coverage |
