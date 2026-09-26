# Lesson Plan: Jev AI (TypeSafe AI)

*Source: `research/jev-ai/report.md`*
*Each lesson → one HTML file in `lessons/`, one reference doc in `reference/`*

---

## Module 1 — Why Jev Exists
*Foundations first: understand the problem Jev solves before touching the API. Without this, the design decisions feel arbitrary.*

### Lesson 1: The LLM Reliability Problem
**File:** `lessons/0001-llm-reliability-problem.html`
**Key concepts:** RLHF · mode dropping · overconfidence · hallucination · human-in-the-loop bottleneck
**Source paper:** https://typesafe.ai/blog/ai-too-good-to-be-true-too-bad-to-be-useful-typesafe-ai — LLMs simultaneously overpromise (general intelligence) and underdeliver (unreliable for production automation)
**Skill:** List 3 real automation tasks you've wanted to automate and identify which RLHF failure mode (overconfidence, mode dropping, hallucination) would most likely break each one
**Reference doc:** `reference/rlhf-vs-rlcd.html`

### Lesson 2: The Bitterest Lesson — Picking the Right Task
**File:** `lessons/0002-bitterest-lesson-ml-hierarchy.html`
**Key concepts:** ML hierarchy (task > data > compute > algorithms) · task selection · InstructGPT example · optimization objective
**Source paper:** https://typesafe.ai/blog/bitterest-lesson — GPT-2-scale models trained on the right task outperformed GPT-3 on instruction-following
**Skill:** For each layer of the ML hierarchy, write one sentence explaining what "getting it wrong" looks like in a real system you've built or used
**Reference doc:** `reference/rlhf-vs-rlcd.html` *(extend existing)*

### Lesson 3: System One Models — A New Category
**File:** `lessons/0003-system-one-models.html`
**Key concepts:** System One (Kahneman) · RLCD · machine-native intelligence · 99% machine-to-machine · Jevons Paradox
**Source paper:** https://typesafe.ai/blog/introducing-system-one-models-and-jev — RLCD trains for calibrated probabilities on structured tasks; 193.6× faster, 444.6× cheaper than frontier LLMs
**Skill:** Draw (on paper or in text) a diagram of a workflow you know — mark each decision point as either "System One" (fast, typed judgment) or "System Two" (reasoning needed)
**Reference doc:** `reference/rlhf-vs-rlcd.html` *(extend existing)*

---

## Module 2 — The Jev API
*Move from concepts to hands-on: learn the three primitives and call the API for the first time.*

### Lesson 4: The Three Primitives — Choice, Score, Noul
**File:** `lessons/0004-three-primitives.html`
**Key concepts:** Choice · Score · Noul · parallel evaluation · atomic question design · context-rot
**Source paper:** https://docs.typesafe.ai/ — all primitives evaluated in parallel and in isolation; adding questions has minimal latency impact
**Skill:** Given a support ticket "I was charged twice and my account is locked", write out 3 questions you'd ask Jev — one Choice, one Score, one Noul — with your criteria
**Reference doc:** `reference/primitives-cheatsheet.html`

### Lesson 5: Your First API Call — Python Quickstart
**File:** `lessons/0005-python-quickstart.html`
**Key concepts:** TypeSafeClient · system_one() · TYPESAFE_API_KEY · answer access · context manager
**Source paper:** https://docs.typesafe.ai/introduction/quickstart + https://github.com/typesafe-ai/typesafe-sdk-python — `pip install typesafe-sdk`; reads env var automatically
**Skill:** Write (but don't run) a complete Python script that classifies a support message into billing/technical/account and prints the result with its confidence score
**Reference doc:** `reference/primitives-cheatsheet.html` *(extend existing)*

### Lesson 6: The JavaScript/TypeScript SDK
**File:** `lessons/0006-javascript-sdk.html`
**Key concepts:** @typesafe-ai/sdk · choice() / score() / noul() helpers · type inference · ESM/CJS/TS declarations
**Source paper:** https://github.com/typesafe-ai/typesafe-sdk-js — answer types inferred from question definitions automatically; Node.js ≥ 20
**Skill:** Rewrite your Lesson 5 Python script as TypeScript — note the syntax differences (camelCase, helper functions, type inference) in a short list
**Reference doc:** `reference/primitives-cheatsheet.html` *(extend existing)*

---

## Module 3 — Reliability and Patterns
*Go deeper: confidence scores are the killer feature. Learn how to use them to build systems that are trustworthy, not just fast.*

### Lesson 7: Confidence Scores — The Killer Feature
**File:** `lessons/0007-confidence-scores.html`
**Key concepts:** probability distribution · confidence formula · three behavioral tiers · risk-scaled thresholds · raw probabilities
**Source paper:** https://docs.typesafe.ai/confidence — formula: `(n × max_prob − 1) / (n − 1)`; thresholds should scale with consequence severity
**Skill:** For your Lesson 5/6 classifier, write pseudocode for three confidence tiers: auto-route (high), flag for review (medium), reject (low) — choose threshold numbers and justify them
**Reference doc:** `reference/confidence-guide.html`

### Lesson 8: The Four Architectural Patterns
**File:** `lessons/0008-architectural-patterns.html`
**Key concepts:** Speculative Fan-Out · Confidence-Gated Routing · Composite Scoring · Intent Routing · atomic decision composition
**Source paper:** https://docs.typesafe.ai/patterns — four patterns covering cost, speed, reliability, and safety trade-offs
**Skill:** Pick one pattern and sketch a mini-system design (in text or diagram) that uses it — include: the state, the questions, the confidence threshold, and the routing logic
**Reference doc:** `reference/confidence-guide.html` *(extend existing)*

### Lesson 9: Jev vs. LLM Structured Outputs
**File:** `lessons/0009-jev-vs-llm.html`
**Key concepts:** JSON mode · function calling · token-by-token generation · system-one-adapter-python · benchmark caveats
**Source paper:** https://typesafe.ai/blog/introducing-system-one-models-and-jev — LLM structured outputs constrain format only, not generation; TypeSafe adapter lets you compare both on same task
**Skill:** Write a 3-row comparison table: Jev vs. OpenAI function calling vs. Claude tool use — columns: latency, cost, confidence support, type safety
**Reference doc:** `reference/rlhf-vs-rlcd.html` *(extend existing)*

---

## Module 4 — Weekend Project
*Apply everything: build, run, and extend the support ticket router end-to-end.*

### Lesson 10: Build the Support Ticket Router (Part 1 — Classify)
**File:** `lessons/0010-ticket-router-part1.html`
**Key concepts:** project setup · state design · Choice + Score + Noul in one call · reading responses
**Source paper:** https://github.com/typesafe-ai/typesafe-sdk-python — quickstart project: support ticket router
**Skill:** Set up the project, get your API key, and get the classifier running against at least 4 test tickets — paste your output
**Reference doc:** `reference/primitives-cheatsheet.html` *(extend existing)*

### Lesson 11: Build the Support Ticket Router (Part 2 — Confidence Gates)
**File:** `lessons/0011-ticket-router-part2.html`
**Key concepts:** confidence threshold tuning · three-tier routing · risk tolerance · test with edge cases
**Source paper:** https://docs.typesafe.ai/confidence — start conservative, test, adjust
**Skill:** Run your router at three confidence thresholds (0.6, 0.8, 0.95) and record what changes — which tickets flip from auto-route to human review? Why?
**Reference doc:** `reference/confidence-guide.html` *(extend existing)*

### Lesson 12: Extend and Reflect
**File:** `lessons/0012-extend-and-reflect.html`
**Key concepts:** extension patterns · system-one-adapter-python · Speculative Fan-Out · what Jev is bad at
**Source paper:** https://typesafe.ai/blog/introducing-system-one-models-and-jev — well-suited tasks: classification, routing, scoring; not suited for reasoning, generation, explanation
**Skill:** Add one extension to your router (JSON output, stdin input, escalation logic, or LLM comparison) and write a one-paragraph retrospective: what surprised you, what would you use Jev for next?
**Reference doc:** *(all reference docs)*

---

## Suggested Teaching Order

Follow Module 1 → 2 → 3 → 4 linearly. Module 1 provides essential conceptual grounding — skipping it makes Module 3 (confidence) harder to motivate. Lessons 5 and 6 can be done in either order depending on language preference. Lessons 10–12 must be done sequentially as they build on each other.

---

## Reference Documents to Build

| File | Contents |
|------|----------|
| `reference/rlhf-vs-rlcd.html` | Side-by-side comparison of RLHF, RLVR, RLCD; mode dropping explained; why calibration matters for automation |
| `reference/primitives-cheatsheet.html` | Quick-reference for Choice, Score, Noul — syntax in Python and JS, when to use each, example criteria patterns |
| `reference/confidence-guide.html` | Confidence formula, three tiers, risk-scaling thresholds, raw probabilities, code examples |
