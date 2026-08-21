# Lesson Plan: Building an LLM Evaluation Pipeline

*Source: `research/llm-evaluation-pipeline/report.md`*
*Each lesson → one HTML file in `lessons/`, one reference doc in `reference/`*

---

## Module 1 — Foundations
*Why evaluation exists: establishing the mental model before any specific technique is introduced.*

### Lesson 1: Why LLM Products Fail Without Evals
**File:** `lessons/0001-why-evals-matter.html`
**Key concepts:** eval infrastructure · product quality · unit tests vs. A/B testing · investment compounding
**Source paper:** https://hamel.dev/blog/posts/evals/ — three-tier eval architecture (unit tests → human/model eval → A/B testing); most teams over-invest in prompt tweaking while skipping eval infrastructure
**Skill:** List the three eval tiers and, for a hypothetical LLM feature (e.g., a document Q&A bot), write one concrete test for each tier — what it checks, when it runs, and what failure looks like
**Reference doc:** `reference/eval-tiers.html`

### Lesson 2: The Eval Landscape — Three Approaches, One Decision
**File:** `lessons/0002-eval-landscape.html`
**Key concepts:** deterministic evals · semantic metrics · LLM-as-judge · held-out dataset · combining tiers
**Source paper:** https://www.evidentlyai.com/llm-guide/llm-evaluation + https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation — practical overview of all three eval families with guidance on when to combine them
**Skill:** Given three different LLM tasks (classify sentiment, generate a SQL query, write a product description), choose one eval approach for each and write a one-sentence justification
**Reference doc:** `reference/eval-landscape.html`

### Lesson 3: Eval-Driven Development — Task-Specific Over Generic
**File:** `lessons/0003-eval-driven-development.html`
**Key concepts:** eval-driven development · off-the-shelf benchmarks · task-specific test sets · guardrail layers (structural, syntactic, safety, input)
**Source paper:** https://eugeneyan.com/writing/llm-patterns/ — standard benchmarks (MMLU, BLEU) have poor correlation with human judgment; task-specific eval sets are essential; four guardrail layers
**Skill:** Pick a real or hypothetical LLM application and design a minimal eval set: define the task, write 3 test cases with expected outputs, and identify which guardrail layer each check belongs to
**Reference doc:** `reference/guardrail-layers.html`

---

## Module 2 — Deterministic & Semantic Evals
*The cheapest, fastest eval methods — when they're enough and when they're not.*

### Lesson 4: Deterministic Checks — When Exact Rules Are Enough
**File:** `lessons/0004-deterministic-evals.html`
**Key concepts:** exact match · schema validation · regex checks · constraint verification · first-pass filters
**Source paper:** https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation — deterministic scorers (BLEU, ROUGE, METEOR, Levenshtein) are fast but semantics-blind; exact match works only for classification labels and tool call correctness; layering pattern
**Skill:** Write three Python assert statements that could serve as unit tests for an LLM output: one for JSON schema validation, one for keyword presence, one for response length constraint
**Reference doc:** `reference/deterministic-checks.html`

### Lesson 5: Execution-Based Eval — pass@k and the Limits of Text Matching
**File:** `lessons/0005-execution-based-eval.html`
**Key concepts:** pass@k · unit test execution · functional correctness · benchmark validity · normalization bugs
**Source paper:** https://arxiv.org/abs/2107.03374 — HumanEval: Codex 28.8% pass@1 but 70.2% pass@100; https://huggingface.co/blog/open-llm-leaderboard-drop — stop token and normalization bugs caused better models to score worse
**Skill:** Given a code generation task (e.g., "write a function that finds the Nth Fibonacci number"), write 3 unit tests that would form the basis of a pass@k evaluation — cover the happy path, an edge case, and a boundary condition
**Reference doc:** `reference/pass-at-k.html`

### Lesson 6: Semantic Metrics — BERTScore, ROUGE/BLEU, and Their Limits
**File:** `lessons/0006-semantic-metrics.html`
**Key concepts:** cosine similarity · BERTScore · MoverScore · ROUGE · BLEU · contextual bias · NLI classifiers · middle-tier tradeoffs
**Source paper:** https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation (semantic section) + https://www.evidentlyai.com/llm-guide/llm-evaluation — embedding-based scorers sit between statistical n-grams and LLM judges; ROUGE/BLEU miss paraphrases; BERTScore uses contextual embeddings for better semantic alignment
**Skill:** For each of three LLM outputs (a one-word classification, a paragraph summary, a customer support reply), choose one semantic metric that best fits and explain why the others would be weaker choices
**Reference doc:** `reference/semantic-metrics.html`

---

## Module 3 — LLM-as-a-Judge
*Using LLMs to grade LLMs: patterns, biases, rubric design, and implementation.*

### Lesson 7: Judge Patterns — Direct, Pairwise, and Reference-Based
**File:** `lessons/0007-judge-patterns.html`
**Key concepts:** direct scoring · pairwise comparison · reference-based eval · bias taxonomy · PoLL (panel of LLM judges) · cost optimization
**Source paper:** https://eugeneyan.com/writing/llm-evaluators/ — three judge types; position bias, verbosity bias, self-enhancement bias; PoLL matches GPT-4 at 1/7 cost; LLM-human correlation 0.3–0.6
**Skill:** Write a direct-scoring judge prompt for evaluating "tone" in a customer support reply: include a task description, the response to evaluate, and a 1–4 scale with labeled anchors for each value
**Reference doc:** `reference/judge-patterns.html`

### Lesson 8: Bias Taxonomy — Position, Verbosity, and Self-Enhancement
**File:** `lessons/0008-judge-biases.html`
**Key concepts:** position bias · verbosity bias · self-enhancement bias · MT-Bench · Chatbot Arena · crowdsourced evaluation · pairwise calibration
**Source paper:** https://arxiv.org/abs/2306.05685 — GPT-4 achieves >80% agreement with human preferences; three primary bias types identified; MT-Bench + Chatbot Arena as complementary benchmarks
**Skill:** Design a pairwise comparison prompt that mitigates at least two of the three identified biases — swap positions across two runs, cap response length in the rubric instruction, or blind the judge to model identity. Write out the prompt and annotate which bias each design choice addresses.
**Reference doc:** *(extend reference/judge-patterns.html)*

### Lesson 9: Rubric Design — Scales, Anchors, and Chain-of-Thought Scoring
**File:** `lessons/0009-rubric-design.html`
**Key concepts:** integer scales · anchor labels · chain-of-thought deliberation · additive scoring · reference answers · few-shot examples · Pearson correlation
**Source paper:** https://huggingface.co/learn/cookbook/en/llm_judge — small integer scales (1–4/1–5) with explicit anchors; reasoning field before final score; prompt improvements raised correlation from 0.57 to 0.84
**Skill:** Improve a weak rubric: given a 0–10 float-range prompt with no anchors, rewrite it using a 1–4 integer scale with explicit labels, a chain-of-thought reasoning step before the score, and one few-shot example
**Reference doc:** `reference/rubric-design.html`

### Lesson 10: Frameworks and Cost — DeepEval, GEval, and Cheaper Judge Strategies
**File:** `lessons/0010-deepeval-and-cost.html`
**Key concepts:** DeepEval · GEval · LLMTestCase · pytest integration · few-shot calibration · composite score weighting · GPT-3.5 vs GPT-4 judge · cost-quality trade-off
**Source paper:** https://deepeval.com/docs/getting-started — GEval, pytest/Vitest integration, agent traces, production monitoring; https://www.databricks.com/blog/LLM-auto-eval-best-practices-RAG — GPT-3.5 + few-shot = 10x cheaper, Correctness 60% / Comprehensiveness 20% / Readability 20%
**Skill:** Write a DeepEval test case in Python using GEval for a correctness metric: define the `LLMTestCase`, create the `GEval` metric with criteria and threshold, and add a `conftest.py` snippet that would make it run in CI
**Reference doc:** `reference/deepeval-setup.html`

---

## Module 4 — Use Cases & Production
*Applying the full stack to real output types and running it in production.*

### Lesson 11: Evaluating Summarization and RAG with RAGAS
**File:** `lessons/0011-ragas-summarization-rag.html`
**Key concepts:** faithfulness · answer relevancy · context precision · context recall · RAGAS score · hallucination detection · MRR · NDCG · LangSmith integration
**Source paper:** https://www.langchain.com/blog/evaluating-rag-pipelines-with-ragas-langsmith — four RAGAS metrics combined via harmonic mean; requires little annotated data; https://www.galileo.ai/blog/mastering-rag-how-to-architect-an-enterprise-rag-system — MRR/NDCG for retrieval quality; log probabilities for hallucination detection
**Skill:** Given a three-sentence RAG response and its source context, manually compute a faithfulness score: list all statements in the response, mark each as supported or unsupported by the context, and calculate the score as supported ÷ total
**Reference doc:** `reference/ragas-metrics.html`

### Lesson 12: Production Eval Pipeline — Tiers, Cadence, Routing, and Drift
**File:** `lessons/0012-production-pipeline.html`
**Key concepts:** three-tier cadence · synthetic dataset bootstrapping · run_experiment() pattern · evaluator drift · prompted vs. finetuned judges · routing strategy · human calibration
**Source paper:** https://hamel.dev/blog/posts/evals/ + https://www.anyscale.com/blog/a-comprehensive-guide-for-building-rag-based-llm-applications-part-1 + https://eugeneyan.com/writing/llm-evaluators/ — CI unit tests daily, human/model eval weekly, A/B tests for major changes; synthetic Q&A bootstrapping; finetuned judges suffer catastrophic drops outside their domain; routing GPT-3.5 for easy queries saves cost
**Skill:** Sketch a production eval plan for a hypothetical product (e.g., a customer support bot): define which eval method runs at each tier, specify the cadence, describe how you would detect evaluator drift over time, and identify one routing rule to cut judge costs
**Reference doc:** `reference/production-pipeline.html`

---

## Suggested Teaching Order

Follow the module sequence: Foundations (1–3) → Deterministic & Semantic (4–6) → LLM-as-a-Judge (7–10) → Production (11–12). Lessons 4–6 should be completed before 7–10 since the judge section assumes familiarity with the limits of cheaper methods. Lesson 12 assumes all prior material.

---

## Reference Documents to Build

| File | Contents |
|------|----------|
| `reference/eval-tiers.html` | Three-tier eval architecture diagram, cadence table, cost comparison |
| `reference/eval-landscape.html` | Decision matrix: task type → recommended eval approach |
| `reference/guardrail-layers.html` | Four guardrail layers with examples per layer |
| `reference/deterministic-checks.html` | Common check types with code patterns (exact match, regex, JSON schema) |
| `reference/pass-at-k.html` | pass@k formula, HumanEval benchmark overview, unit test patterns |
| `reference/semantic-metrics.html` | ROUGE/BLEU/BERTScore comparison table with use cases and limitations |
| `reference/judge-patterns.html` | Three judge types, bias taxonomy, prompt templates, PoLL approach |
| `reference/rubric-design.html` | Rubric checklist: scale selection, anchor writing, CoT structure, few-shot examples |
| `reference/deepeval-setup.html` | DeepEval install, LLMTestCase structure, GEval config, pytest CI integration snippet |
| `reference/ragas-metrics.html` | RAGAS four-metric definitions, harmonic mean formula, LangSmith integration steps |
| `reference/production-pipeline.html` | Full pipeline architecture: dataset bootstrap → generate → evaluate → monitor loop |
