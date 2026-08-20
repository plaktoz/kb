---
source_url: https://www.promptfoo.dev/docs/red-team/
author: Unknown
date: 2026-08-20
---
# LLM Red Teaming Guide


## Overview

LLM red teaming proactively identifies vulnerabilities in AI systems through simulated adversarial inputs before deployment. Different architectures (RAG, agents, chatbots) face distinct vulnerability types.

---

## Why It Matters

Red teaming provides a **quantitative risk measure before deployment** — running thousands of probes to help developers make informed decisions. Major labs (OpenAI, Anthropic, Google) use this process internally. Regulatory frameworks including OWASP LLM Top 10, NIST AI RMF, and the EU AI Act increasingly support systematic pre-deployment testing.

---

## How It Works

1. **Generate adversarial inputs** — diverse malicious prompts incorporating injection/jailbreak techniques
2. **Evaluate responses** — run inputs through the LLM application
3. **Analyze vulnerabilities** — use deterministic and model-graded metrics

Can be applied as **one-off runs** or integrated into **CI/CD pipelines**.

---

## Model vs. Application Layer Threats

### Model Layer
- Prompt injections/jailbreaks
- Hate speech, bias, toxicity
- Hallucinations
- PII leaks from training data
- Copyright violations

### Application Layer
- Indirect prompt injections
- PII leaks from context (e.g., RAG)
- Tool misuse (unauthorized data access, privilege escalation, SQL injection)
- Data/chat exfiltration
- Hijacking/off-topic use

Most teams focus on **application layer threats** as they present the greatest technical risk.

---

## White Box vs. Black Box Testing

| White Box | Black Box |
|-----------|-----------|
| Full model access | Inputs/outputs only |
| Highly effective attacks | Simulates real-world scenarios |
| Slower, model-specific | Practical for most teams |
| Useful for model developers | Accessible to non-experts |

For most AppSec teams, **black box testing** is more practical since model internals are rarely accessible.

---

## Common Threats

### Privacy Violations
Research shows adversarial LLMs can extract training data from other models. PII leakage — phone numbers, email addresses — can enable identity theft and unauthorized resource access.

### Prompt Injections
Similar to SQL injections but distinct — they chain untrusted user input with trusted developer prompts. Researchers have demonstrated injections that hijack LLMs, extract user data, and redirect users to malware sites. Prompt-to-SQL attacks have been shown effective across seven tested LLMs.

### Jailbreaking
Attacks that subvert foundational safety filters. A notable example: a Chevrolet dealership chatbot was manipulated into "agreeing to sell" a vehicle for $1 via a simple objective-override prompt. Research shows the TAP (Tree of Attacks with Pruning) method jailbreaks leading LLMs "for more than 80% of the prompts using only a small number of queries." ASCII art has also been demonstrated as a guardrail bypass technique.

### Generation of Unwanted Content
Even without jailbreaking, broad model knowledge bases can produce off-topic, harmful, or misleading content — ranging from criminal instructions to dangerous misinformation at scale.

---

## Best Practices

### Step 1: Define Your Strategy
- Identify vulnerability types most relevant to your use case
- Choose testing checkpoints: model testing, pre-deployment, CI/CD, post-deployment monitoring
- Balance depth with resource constraints (automated attacks can range from cents to hundreds of dollars)
- Account for regulatory requirements (GDPR, HIPAA, NIST AI RMF, OWASP LLM)

### Step 2: Implementation
- Generate diverse adversarial inputs (automated tools + human ingenuity)
- Set up an evaluation framework integrated with your pipeline
- Test end-to-end in a production-like environment
- Store outputs in structured, analyzable formats

### Step 3: Analysis and Remediation
- Review flagged outputs regularly with security and development teams
- Prioritize technical security vulnerabilities (model-layer issues tend to improve over time)
- Develop mitigations: prompt engineering, additional safeguards, architectural changes
- Re-run evaluations to confirm fixes
- Continuously update test suites with new adversarial inputs

---

## Case Study: Discord's Clyde AI

Discord launched Clyde (OpenAI-powered) in March 2023 with a gradual rollout. Initial satisfaction was high among moderators, but users quickly discovered the "grandma exploit" — framing forbidden requests as roleplay scenarios to bypass content filters.

**Consequences:**
- Policy violations via filtered content bypasses
- Reputational damage from public exploits
- Erosion of user trust

**Discord's Response:**
- Adopted an evaluation framework (an early version of Promptfoo)
- Required evaluations for every prompt/workflow change
- Deployed passive moderation and observability tools
- Created dedicated reporting mechanisms

**Key Takeaways:**
1. Test comprehensive adversarial inputs pre-launch
2. Use gradual rollouts to limit blast radius
3. Build a culture of continuous risk monitoring
4. Create user feedback loops feeding back into red team setups

---

## Key Concepts

- **TAP (Tree of Attacks with Pruning)** — iterative prompt refinement using tree-of-thought reasoning
- **BOLA** — Broken Object-Level Authorization (cross-user resource access)
- **BFLA** — Broken Function-Level Authorization (actions beyond authorized scope)
- **Indirect prompt injection** — malicious instructions embedded in external content processed by the LLM
