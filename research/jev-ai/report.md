# Research: Jev AI (TypeSafe AI)
*Generated: 2026-09-26 | Scope: Jev by TypeSafe AI — beginner's complete guide covering concepts, architecture, comparisons, SDK setup, and a 2–5 hour weekend mini-project*

## Research Outline

1. What is Jev? — Core concepts, the problem it solves, and how it differs from standard LLMs
2. How Jev works technically — RLCD training, typed primitives, calibrated confidence, architecture
3. Jev vs. alternatives — Compared to GPT-4o / Claude structured outputs and OpenAI function calling
4. Getting started: API & SDK — Authentication, installation, and your first API call
5. Weekend mini-project guide — Step-by-step support ticket router in 2–5 hours

---

## What is Jev?

### TypeSafe AI — Introducing System One Models and Jev
- **Source**: https://typesafe.ai/blog/introducing-system-one-models-and-jev
- **Summary**: Jev is a "System One Model" — a new class of AI built for machine-native automation rather than human conversation. Inspired by Kahneman's *Thinking, Fast and Slow*, it makes fast, typed, probabilistic decisions. The name "Jev" references economist William Stanley Jevons: just as steam-engine efficiency expanded coal demand rather than reducing it, cheaper AI intelligence is expected to expand use cases rather than merely cut costs.
- **Relevance**: The primary product announcement; establishes the core philosophy, problem statement, and what makes Jev fundamentally different from chat LLMs.

### TypeSafe AI Homepage
- **Source**: https://typesafe.ai/
- **Summary**: TypeSafe AI is a 2026 San Francisco lab building "machine-native intelligence infrastructure for automation." RLHF-trained LLMs are optimized for human approval, causing mode dropping, overconfidence, and unreliability — requiring humans in the loop. Jev is the alternative: structured typed outputs with calibrated confidence scores, operating more like code than chat.
- **Relevance**: Concise overview of the company, product positioning, pricing ($42/billion input tokens), and performance claims (193.6× faster, 444.6× cheaper than frontier LLMs on automation tasks).

### The Bitterest Lesson — TypeSafe AI Blog
- **Source**: https://typesafe.ai/blog/bitterest-lesson
- **Summary**: Extends Rich Sutton's "bitter lesson" (compute beats algorithms) into a fuller hierarchy: *doing the right task > data > compute > algorithms*. Uses the InstructGPT example — a GPT-2-sized model trained on the right objective outperformed GPT-3 at instruction following, a capability that pure scaling would have required "GPT-7 level" to match. Most ML research attacks the hierarchy in reverse order.
- **Relevance**: Explains TypeSafe's founding philosophy — that picking the right objective (machine-native decisions, not human-pleasing text) is more important than scale, justifying their narrow but deliberate task focus.

### AI: Too Good to Be True, Too Bad to Be Useful — TypeSafe AI Blog
- **Source**: https://typesafe.ai/blog/ai-too-good-to-be-true-too-bad-to-be-useful-typesafe-ai
- **Summary**: Published June 2026. Argues that LLMs simultaneously overpromise (general intelligence) and underdeliver (unreliable for production automation), creating a gap TypeSafe aims to fill with reliable, scoped decision models.
- **Relevance**: Frames the market opportunity and the reliability problem that motivates building a purpose-built automation model instead of patching LLMs.

---

## How Jev Works Technically

### Docs: System One Concepts
- **Source**: https://docs.typesafe.ai/concepts/system-one
- **Summary**: System One models take structured *state* as input and return typed answers with probability distributions — not generated text. Three primitives cover all decision needs: **Choice** (categorical selection), **Score** (continuous 0–N value), and **Noul** (true/false as 0–1 float). Multiple questions are evaluated independently and in parallel in a single API call.
- **Relevance**: Defines the architectural building blocks every Jev project is built from.

### Docs: Machine Learning Primer
- **Source**: https://docs.typesafe.ai/introduction/machine-learning-primer
- **Summary**: Contrasts three post-training methods: RLHF (optimizes for human preference → sycophancy, hallucination), RLVR (optimizes for verifiable rewards → slow/costly), and RLCD (TypeSafe's method: trains for decisions and calibrated probabilities). Explains mode dropping — RLHF narrows a model's output distribution toward a preferred style, suppressing valid alternatives — and calibration (predicted probabilities should match actual outcome frequencies).
- **Relevance**: The technical foundation for understanding why Jev behaves differently from GPT/Claude and why calibration is the key property TypeSafe optimizes for.

### Docs: Confidence Scores
- **Source**: https://docs.typesafe.ai/confidence
- **Summary**: Confidence is computed automatically on every Choice and Score answer from the shape of the probability distribution: `(n × largest_probability − 1) / (n − 1)`. A concentrated distribution → confidence near 1.0; a flat distribution → near 0.0. The docs recommend three behavioral tiers: high confidence → act automatically; medium → proceed cautiously; low → route to human. The raw `probabilities` array is always available for custom thresholds.
- **Relevance**: Confidence-gated routing is the core pattern that lets Jev-powered systems operate autonomously at high confidence while escalating uncertain cases — essential for the mini-project.

### Introducing System One Models — Technical Details
- **Source**: https://typesafe.ai/blog/introducing-system-one-models-and-jev
- **Summary**: Jev uses a **parallel sampler** that generates all outputs in a single query rather than token-by-token, which is the primary driver of its 40×–200× speed advantage. Because possible outputs are defined in advance, type errors are architecturally impossible. High-cardinality choices (up to 255 options) use a two-stage scoring-then-selection system. Benchmarks show Jev costs $0.000081 vs LLM cost $0.013880 for equivalent tasks (70ms vs 8.5s).
- **Relevance**: Explains *why* Jev is faster and cheaper than LLMs — not just a small model, but a fundamentally different architecture.

---

## Jev vs. Alternatives

### System One vs. LLM JSON Mode / Structured Outputs
- **Source**: https://typesafe.ai/blog/introducing-system-one-models-and-jev
- **Summary**: LLM structured-output wrappers (e.g. OpenAI JSON mode, function calling) still generate token-by-token from a full language model — they only constrain the *format* of the output, not the generation process. TypeSafe argues this doesn't fix mode dropping, overconfidence, or latency. The LLM adapter repo (`system-one-adapter-python`) lets you run any LLM in System One format for comparison.
- **Relevance**: Directly addresses the "why not just use OpenAI with structured outputs?" question. The difference isn't just cost/speed — it's that the entire training objective and architecture are different.

### GitHub: system-one-adapter-python
- **Source**: https://github.com/typesafe-ai/system-one-adapter-python
- **Summary**: A drop-in `TypeSafeClient` replacement backed by LLM APIs. Allows developers to write System One-style code and run it against either Jev or a standard LLM, making it easy to benchmark both on the same task and validate that Jev's architecture — not just its price — provides the advantage.
- **Relevance**: Practical tool for comparing Jev against OpenAI/Claude on your specific use case before committing.

---

## Getting Started: API & SDK

### Docs: Quickstart
- **Source**: https://docs.typesafe.ai/introduction/quickstart
- **Summary**: Get an API key at `console.typesafe.ai/keys`. Install with `pip install typesafe-sdk` (Python ≥ 3.10) or `npm install @typesafe-ai/sdk` (Node.js ≥ 20). The client reads `TYPESAFE_API_KEY` from your environment. The primary method is `client.system_one(state=..., questions={...})`. An interactive playground is available at `console.typesafe.ai/playground`.
- **Relevance**: The canonical starting point — everything you need to make your first API call.

### GitHub: Python SDK (typesafe-sdk-python)
- **Source**: https://github.com/typesafe-ai/typesafe-sdk-python
- **Summary**: Official Python SDK. Exposes `TypeSafeClient`, `Choice`, `Score`, and `Noul`. Use as a context manager: `with TypeSafeClient() as client:`. The `system_one()` method accepts a `state` dict and a `questions` dict, returning structured answer objects. Results accessed via `response.answers["question_name"].choice` (or `.score`, `.noul`).
- **Relevance**: Primary SDK for Python projects; includes the three quickstart project ideas: support ticket router, content moderation tagger, lead scoring classifier.

### GitHub: JavaScript/TypeScript SDK (typesafe-sdk-js)
- **Source**: https://github.com/typesafe-ai/typesafe-sdk-js
- **Summary**: Official JS/TS SDK (`@typesafe-ai/sdk`). Requires Node.js ≥ 20. Uses `choice()`, `score()`, and `noul()` helper functions. Answer types are automatically inferred from your question definitions — no manual type assertions. Ships with ESM, CommonJS, and TypeScript declarations.
- **Relevance**: For developers preferring JavaScript/TypeScript; the API mirrors the Python SDK closely, so patterns transfer directly.

### GitHub: Agent Skills (typesafe-ai/skills)
- **Source**: https://github.com/typesafe-ai/skills
- **Summary**: Reusable agent skill modules that teach AI agents how to use the TypeSafe API. Install in Claude Code with `claude plugin marketplace add typesafe-ai/skills`. Once installed, ask your agent to "use TypeSafe to route support tickets" or invoke `/typesafe:typesafe-ai` directly. The skill handles API calls, patterns, and cookbook lookup.
- **Relevance**: If you're building in Claude Code (this environment), installing the skill gives you an AI assistant that can write TypeSafe workflows for you — useful for the mini-project.

---

## Weekend Mini-Project Guide

### Docs: Patterns
- **Source**: https://docs.typesafe.ai/patterns
- **Summary**: Four documented patterns: (1) **Speculative Fan-Out** — ask many questions in one call, let code decide relevance; (2) **Confidence-Gated Routing** — use confidence as a second decision axis to build safer systems; (3) **Composite Scoring** — combine multiple dimensions into a single score; (4) **Intent Routing** — classify user intent and direct traffic to the appropriate handler. No code examples in the pattern docs themselves.
- **Relevance**: The Intent Routing + Confidence-Gated Routing patterns are the backbone of the recommended mini-project below.

---

## Step-by-Step Weekend Mini-Project: Support Ticket Router

**Goal**: Build a CLI tool that reads a support message, classifies it by department, scores its urgency, and routes it automatically if confident — or flags it for human review if uncertain.

**Time estimate**: 2–3 hours for Python, 3–5 hours for TypeScript.

---

### Step 1 — Sign Up and Get an API Key (15 min)
1. Create an account at [console.typesafe.ai](https://console.typesafe.ai)
2. Go to **Keys** and generate a new API key
3. Save it: `export TYPESAFE_API_KEY="your-key-here"` (add to `~/.zshrc` to persist)

---

### Step 2 — Install the SDK (5 min)
```bash
# Python
pip install typesafe-sdk

# Or TypeScript
npm install @typesafe-ai/sdk
```

---

### Step 3 — Write the Classifier (45 min)

**Python version (`router.py`):**
```python
import os
from typesafe_sdk import Choice, Score, Noul, TypeSafeClient

TICKETS = [
    "I was charged twice for my subscription last month.",
    "The app crashes when I try to upload a file larger than 10MB.",
    "How do I change my username?",
    "I need to cancel my account immediately, this is urgent!",
]

with TypeSafeClient() as client:
    for ticket in TICKETS:
        response = client.system_one(
            state={"message": ticket},
            questions={
                "department": Choice(
                    instructions="Which department should handle this ticket?",
                    criteria={
                        "billing": "Payment issues, charges, refunds, subscriptions",
                        "technical": "Bugs, crashes, errors, performance problems",
                        "account": "Account settings, passwords, cancellations",
                        "general": "General questions and inquiries",
                    },
                ),
                "urgency": Score(
                    instructions="How urgent is this ticket? (0 = not urgent, 5 = critical)",
                    criteria=["0: routine question", "3: frustrated customer", "5: data loss or billing emergency"],
                ),
                "is_vip": Noul(
                    instructions="Does this ticket suggest a high-value or long-term customer?",
                ),
            },
        )

        dept = response.answers["department"]
        urgency = response.answers["urgency"]

        # Confidence-gated routing
        if dept.confidence > 0.8:
            action = f"AUTO-ROUTE → {dept.choice.upper()}"
        else:
            action = f"HUMAN REVIEW (confidence: {dept.confidence:.2f})"

        print(f"\nTicket: {ticket[:60]}...")
        print(f"  Department : {dept.choice} (confidence: {dept.confidence:.2f})")
        print(f"  Urgency    : {urgency.score:.1f}/5")
        print(f"  VIP signal : {response.answers['is_vip'].noul:.2f}")
        print(f"  Action     : {action}")
```

**TypeScript version (`router.ts`):**
```typescript
import { choice, score, noul, TypeSafeClient } from "@typesafe-ai/sdk";

const TICKETS = [
  "I was charged twice for my subscription last month.",
  "The app crashes when I try to upload a file larger than 10MB.",
  "How do I change my username?",
  "I need to cancel my account immediately, this is urgent!",
];

const client = new TypeSafeClient();

for (const ticket of TICKETS) {
  const response = await client.systemOne({
    state: { message: ticket },
    questions: {
      department: choice("Which department should handle this?", {
        billing: null,
        technical: null,
        account: null,
        general: null,
      }),
      urgency: score("How urgent is this ticket? 0=routine, 5=critical", {
        min: 0,
        max: 5,
      }),
      isVip: noul("Does this suggest a high-value customer?"),
    },
  });

  const dept = response.answers.department;
  const action = dept.confidence > 0.8
    ? `AUTO-ROUTE → ${dept.choice.toUpperCase()}`
    : `HUMAN REVIEW (confidence: ${dept.confidence.toFixed(2)})`;

  console.log(`\nTicket: ${ticket.slice(0, 60)}...`);
  console.log(`  Department: ${dept.choice} (confidence: ${dept.confidence.toFixed(2)})`);
  console.log(`  Action: ${action}`);
}
```

---

### Step 4 — Run and Observe (15 min)
```bash
# Python
python router.py

# TypeScript
npx tsx router.ts
```

Watch for:
- High-confidence tickets that auto-route immediately
- Ambiguous tickets (e.g. "cancel my account" — is it *account* or *billing*?) that drop below the threshold and get flagged for review
- How urgency score changes across ticket types

---

### Step 5 — Tune the Confidence Threshold (30 min)
Try changing `0.8` to `0.6`, `0.9`, and `0.95` and re-run. Observe:
- At `0.6` — almost everything auto-routes; some wrong routes
- At `0.95` — almost everything goes to human review; only the most obvious cases auto-route
- The right threshold depends on the cost of a wrong auto-route in your use case

---

### Step 6 — Extend the Project (optional, 1–2 hours)
Ideas to continue learning:
- **Read from stdin**: accept a ticket as a command-line argument instead of a hardcoded list
- **JSON output**: write routed tickets to a `results.json` file grouped by department
- **Add a fourth question**: `needs_escalation` as a `Noul` — auto-escalate tickets with urgency ≥ 4 *and* `needs_escalation > 0.7`
- **Compare with an LLM**: install `system-one-adapter-python` and run the same tickets through GPT-4o — compare latency, cost, and consistency

---

### What You'll Have Learned
After this project you'll understand:
- The three Jev primitives (Choice, Score, Noul) and when to use each
- How confidence scores enable autonomous vs. human-review routing
- How to compose multiple independent questions in one API call
- Why Jev is faster and cheaper than calling an LLM with structured output

---

## Articles to Ingest

URLs ready for `/kb-scrapecontent` → `/kb-ingest`:

- https://typesafe.ai/
- https://typesafe.ai/blog/introducing-system-one-models-and-jev
- https://typesafe.ai/blog/bitterest-lesson
- https://typesafe.ai/blog/ai-too-good-to-be-true-too-bad-to-be-useful-typesafe-ai
- https://docs.typesafe.ai/
- https://docs.typesafe.ai/introduction/quickstart
- https://docs.typesafe.ai/introduction/machine-learning-primer
- https://docs.typesafe.ai/concepts/system-one
- https://docs.typesafe.ai/confidence
- https://docs.typesafe.ai/patterns
- https://github.com/typesafe-ai/typesafe-sdk-python
- https://github.com/typesafe-ai/typesafe-sdk-js
- https://github.com/typesafe-ai/skills
