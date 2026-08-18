---
source_url: https://www.usetranscribe.io/yt/PoQh2iQGjY0/testing-generative-ai?format=md
author: Jason Ross
date: 2026-08-17
---

# Breaking the Black Box: Why Testing Generative AI Is Full Spectrum

Jason Ross, who leads the OWASP GenAI red team initiative, argues that traditional penetration testing methods fundamentally break down when applied to generative AI systems. The core problem: conventional security testing is binary, but AI behavior is probabilistic.

## The Binary Problem Disappears

Classic pen testing offers clear pass/fail outcomes — SQL injection either returns data or it doesn't. With GenAI, that clarity vanishes. Testers are no longer hunting fixed code vulnerabilities; they're attempting to manipulate non-deterministic behavior. Even with temperature set to zero, identical inputs won't guarantee identical outputs.

This creates a reproducibility crisis: if a red teamer finds a working exploit but the developer can't reproduce it, who's right? And if a fix is deployed, how do you confirm it worked when the system was already inconsistent?

## Hallucination as a Structural Flaw

Ross is direct: hallucinations aren't bugs to be patched — they're inherent to the technology. AI systems present fabricated information with complete confidence. He demonstrates this with a mock SQL injection scenario where the "database" and its "leaked credentials" were entirely invented by the model.

The implication for red teamers: black-box AI testing is largely useless without access to ground-truth data for validation. Any finding must be cross-referenced against real system data.

## System Prompt Leakage — Rethink the Threat Model

Ross helped rewrite the OWASP LLM Top 10 entry on system prompt leakage. His position: treat system prompts as public. They will leak, often in mutated form with key phrases intact. The solution isn't better concealment — it's writing prompts that cause no harm if exposed.

## AI Red Teaming Resembles Social Engineering

Because AI systems are trained to be maximally helpful, attacking them resembles social engineering more than traditional exploitation. Effective techniques include:

- Persuasion ("come on, you can do it")
- Appeals to authority or urgency
- Role-play / persona adoption — once a model believes it's "acting," guardrails often drop
- Pretexting — seeding fake prior conversation history the model accepts as real
- Crescendo attacks — gradually escalating from benign to harmful content across multiple turns
- Refusal suppression — simply telling the model it cannot say no

## Attack Taxonomy

| Attack Type | Description |
|---|---|
| Direct Prompt Injection | User-facing input manipulation |
| Indirect Prompt Injection | Malicious data embedded in processed sources (resumes, CRM records, web forms) |
| Context Poisoning | Corrupting RAG databases or web-scraped content upstream |
| CROP Attack | Using cultural references to circumvent content filters |
| Crescendo Attack | Incremental escalation across a conversation |
| ASCII/Unicode Smuggling | Invisible characters carrying hidden instructions |
| Context Window Exhaustion | Flooding context so early guardrails are effectively forgotten |
| Adversarial Suffixes | Token strings that activate similar neural pathways to restricted content |

## Agentic Systems Raise the Stakes

Chatbots that only produce text have limited blast radius. Agents that take actions — writing to databases, calling APIs, executing workflows — transform probabilistic misbehavior into real-world consequences. Multi-agent systems compound this: when one agent goes off-course, others tend to follow, creating cascading failures.

## Current Tooling Is Immature

Ross is critical of the commercial AI red-teaming market. Most tools:
- Use single-shot, simplistic jailbreak prompts
- Test for toxicity and bias rather than data exfiltration or agentic misuse
- Require only a model inference endpoint, missing the full agent ecosystem

He co-authored the OWASP AI Red Teaming Vendor Evaluation Guide to help organizations distinguish credible solutions from marketing noise.

Open-source options he highlights:
- Garak (Nvidia) — flexible, not opinionated, good baseline framework
- PyRIT (Microsoft) — better suited for Azure-native environments

He also released Crop Duster, an open-source tool implementing CROP attacks using spaCy NLP to reword attack goals while preserving semantic meaning.

## Prompt Injection Cannot Be Eliminated

Like hallucination, prompt injection is described as an architectural inevitability. Once user data, system instructions, and tool outputs enter the model's context window, the model decides what to prioritize — and it has no reliable concept of trust hierarchy. Ross notes GPT-5 is the first OpenAI model trained to respect a data-source hierarchy, indicating how nascent mitigation efforts remain.

His framing: "You can't defuse the bomb. You put garbage can lids around it to contain the blast." Security practitioners must communicate this risk clearly to business stakeholders rather than promising elimination.

## Practical Recommendations

1. Don't do black-box AI red teaming — you cannot validate findings without system access
2. Never put sensitive data in system prompts — assume they will leak
3. Integrate prompt injection testing into CI/CD pipelines as a baseline benchmark, not a guarantee
4. Think like a social engineer when testing AI behavior
5. Evaluate vendors rigorously — most current tools address surface-level jailbreaks, not systemic risk
6. Communicate irreducible risk clearly — the goal is blast-radius reduction, not zero incidents
