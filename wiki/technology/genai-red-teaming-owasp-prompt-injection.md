---
type: literature-note
source_url: https://www.usetranscribe.io/yt/PoQh2iQGjY0/testing-generative-ai?format=md
author: Jason Ross
tags: [ai-security, prompt-injection, red-teaming, llm-vulnerabilities]
date_consumed: 2026-08-17
---

## Summary

Jason Ross, who leads the [[OWASP]] GenAI red team initiative, argues that traditional penetration testing fundamentally breaks down against generative AI because AI behavior is probabilistic rather than binary. Hallucinations and [[Prompt Injection]] are not bugs to be patched but architectural inevitabilities — the security goal shifts from elimination to blast-radius containment. Agentic systems that take real-world actions dramatically raise the stakes compared to text-only chatbots.

## Core Concepts

- **[[Generative AI]] Red Teaming**: Testing GenAI systems requires social-engineering mindsets, not binary exploit logic.
- **[[Prompt Injection]]**: Direct (user-facing input) and indirect (malicious data embedded in processed sources) variants both exist. Described as architecturally unavoidable.
- **[[OWASP]] LLM Top 10**: Ross helped rewrite the system prompt leakage entry; treats system prompts as public by default.
- **[[Hallucination]]**: Inherent to the technology — AI presents fabricated information with full confidence, making black-box validation impossible without ground-truth data.
- **[[Context Poisoning]]**: Corrupting [[RAG]] databases or web-scraped content upstream to influence model outputs.
- **[[Agentic AI]] Blast Radius**: Agents that write to databases and call APIs transform probabilistic misbehavior into real-world consequences.
- **[[Garak]]** (Nvidia) and **[[PyRIT]]** (Microsoft): Leading open-source red-teaming frameworks.
- **CROP Attack**: Uses cultural references to circumvent content filters; Ross released Crop Duster (open-source, spaCy NLP) to automate this.
- **Crescendo Attack**: Gradually escalating conversation from benign to harmful content across multiple turns.

## Key Takeaways

- **Binary vs. Probabilistic**: Classic pen testing is pass/fail; GenAI testing is probabilistic — same input, different outputs.
- **Reproducibility Crisis**: If a red teamer finds an exploit the developer can't reproduce, traditional remediation workflows break.
- **System Prompt Leakage**: Treat all system prompts as public — they will leak in mutated form; design for harmless exposure.
- **Social Engineering Analogy**: AI systems trained to be helpful respond to persuasion, urgency, role-play, pretexting, and refusal suppression.
- **Black-Box Testing is Largely Useless**: Without ground-truth data access, AI findings cannot be validated.
- **Agentic Cascading Failures**: In multi-agent systems, one agent going off-course causes others to follow.
- **Tooling Immaturity**: Most commercial tools test for toxicity/bias, not data exfiltration or agentic misuse.
- **Trust Hierarchy is Nascent**: GPT-5 is the first OpenAI model trained to respect data-source hierarchy — mitigation remains immature.
- **Containment Framing**: "You can't defuse the bomb. You put garbage can lids around it."

### Attack Taxonomy

| Attack Type | Description |
|---|---|
| Direct Prompt Injection | User-facing input manipulation |
| Indirect Prompt Injection | Malicious data in processed sources (resumes, CRM, web forms) |
| Context Poisoning | Corrupting RAG databases or scraped content upstream |
| CROP Attack | Cultural references to bypass content filters |
| Crescendo Attack | Incremental escalation across a conversation |
| ASCII/Unicode Smuggling | Invisible characters carrying hidden instructions |
| Context Window Exhaustion | Flooding context so early guardrails are forgotten |
| Adversarial Suffixes | Token strings activating restricted-content neural pathways |

### Practical Recommendations

1. Never do black-box AI red teaming without system access.
2. Never put sensitive data in system prompts — assume leakage.
3. Integrate prompt injection testing into CI/CD as a baseline benchmark.
4. Think like a social engineer when testing AI behavior.
5. Evaluate vendors rigorously — most address surface-level jailbreaks only.
6. Communicate irreducible risk to stakeholders — goal is blast-radius reduction.

## 🧠 First Principles & Mental Models

- **[[Goodhart's Law]]**: Most commercial AI red-teaming tools optimize for toxicity/bias scores rather than systemic risk — measuring what is easy to count rather than what actually matters for security.
- **[[Defense in Depth]]**: Because prompt injection and hallucination cannot be eliminated at the model level, layered containment (blast-radius reduction) at every architectural boundary is the only viable mitigation strategy.

## 🃏 Review Questions

**Q1**: Why does traditional binary penetration testing break down for generative AI systems?
**A**: GenAI behavior is probabilistic — identical inputs may produce different outputs even at temperature zero, so pass/fail exploit logic no longer applies and findings cannot be reliably reproduced.

**Q2**: What is the difference between direct and indirect prompt injection, and which is harder to defend against?
**A**: Direct injection comes from user-facing inputs; indirect injection embeds malicious instructions in data sources the model processes (resumes, CRM records, web scrapes). Indirect is harder to defend because the attack surface spans all ingested content.

**Q3**: How should practitioners communicate AI security risk to business stakeholders given that prompt injection cannot be eliminated?
**A**: Frame the goal as blast-radius reduction rather than zero incidents — "you can't defuse the bomb, you put garbage can lids around it" — and ensure stakeholders understand these are architectural properties, not fixable bugs.
