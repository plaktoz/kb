---
type: literature-note
source_url: https://www.usetranscribe.io/yt/PoQh2iQGjY0/testing-generative-ai?format=md
author: Jason Ross
tags: [ai-security, prompt-injection, red-teaming, llm-vulnerabilities]
date_consumed: 2026-08-17
additional_sources:
  - https://www.promptfoo.dev/docs/red-team/
  - https://blog.google/technology/safety-security/googles-ai-red-team-the-ethical-hackers-making-ai-safer/
---

## Summary

Jason Ross, who leads the [[OWASP]] GenAI red team initiative, argues that traditional penetration testing fundamentally breaks down against generative AI because AI behavior is probabilistic rather than binary. Hallucinations and [[Prompt Injection]] are not bugs to be patched but architectural inevitabilities — the security goal shifts from elimination to blast-radius containment. Agentic systems that take real-world actions dramatically raise the stakes compared to text-only chatbots.

## Core Concepts

- **[[Generative AI]] Red Teaming**: Testing GenAI systems requires social-engineering mindsets, not binary exploit logic. Operationally: generate adversarial inputs → evaluate responses → analyze vulnerabilities — runnable as one-off assessments or integrated into CI/CD pipelines.
- **[[Prompt Injection]]**: Direct (user-facing input) and indirect (malicious data embedded in processed sources) variants both exist. Described as architecturally unavoidable. Researchers demonstrated injections that hijack LLMs, extract user data, and redirect users to malware; prompt-to-SQL attacks succeeded across seven tested LLMs.
- **Model Layer vs. Application Layer Threats**: Model-layer risks include hallucinations, hate speech, bias, PII leaks from training data, and copyright violations. Application-layer risks — indirect prompt injections, PII leaks from [[RAG]] context, tool misuse (privilege escalation, SQL injection), data exfiltration — present the greatest technical risk for most teams.
- **White Box vs. Black Box Testing**: White-box testing grants full model access for highly effective attacks but is model-specific and slow; black-box testing simulates real-world adversaries using only inputs/outputs and is more practical for AppSec teams without access to model internals.
- **[[OWASP]] LLM Top 10**: Ross helped rewrite the system prompt leakage entry; treats system prompts as public by default.
- **[[Hallucination]]**: Inherent to the technology — AI presents fabricated information with full confidence, making black-box validation impossible without ground-truth data.
- **[[Context Poisoning]]**: Corrupting [[RAG]] databases or web-scraped content upstream to influence model outputs.
- **[[Agentic AI]] Blast Radius**: Agents that write to databases and call APIs transform probabilistic misbehavior into real-world consequences.
- **[[Garak]]** (Nvidia) and **[[PyRIT]]** (Microsoft): Leading open-source red-teaming frameworks.
- **CROP Attack**: Uses cultural references to circumvent content filters; Ross released Crop Duster (open-source, spaCy NLP) to automate this.
- **Crescendo Attack**: Gradually escalating conversation from benign to harmful content across multiple turns.
- **TAP (Tree of Attacks with Pruning)**: Iterative prompt refinement using tree-of-thought reasoning; demonstrated jailbreaking leading LLMs for more than 80% of prompts using only a small number of queries.
- **BOLA / BFLA**: Broken Object-Level Authorization (cross-user resource access) and Broken Function-Level Authorization (actions beyond authorized scope) — authorization vulnerabilities surfaced at the application layer.

## Key Takeaways

- **Binary vs. Probabilistic**: Classic pen testing is pass/fail; GenAI testing is probabilistic — same input, different outputs.
- **Reproducibility Crisis**: If a red teamer finds an exploit the developer can't reproduce, traditional remediation workflows break.
- **Application Layer is the Priority**: Most teams should focus on application-layer threats; model-layer issues tend to improve over time.
- **System Prompt Leakage**: Treat all system prompts as public — they will leak in mutated form; design for harmless exposure.
- **Social Engineering Analogy**: AI systems trained to be helpful respond to persuasion, urgency, role-play, pretexting, and refusal suppression.
- **Black-Box Testing is Largely Useless**: Without ground-truth data access, AI findings cannot be validated.
- **Agentic Cascading Failures**: In multi-agent systems, one agent going off-course causes others to follow.
- **Tooling Immaturity**: Most commercial tools test for toxicity/bias, not data exfiltration or agentic misuse.
- **Trust Hierarchy is Nascent**: GPT-5 is the first OpenAI model trained to respect data-source hierarchy — mitigation remains immature.
- **Containment Framing**: "You can't defuse the bomb. You put garbage can lids around it."
- **Quantitative Risk Measure**: Red teaming runs thousands of probes to give developers quantitative risk data before deployment — the same process used internally at OpenAI, Anthropic, and Google.

### Attack Taxonomy

| Attack Type | Description |
|---|---|
| Direct Prompt Injection | User-facing input manipulation |
| Indirect Prompt Injection | Malicious data in processed sources (resumes, CRM, web forms) |
| Context Poisoning | Corrupting RAG databases or scraped content upstream |
| CROP Attack | Cultural references to bypass content filters |
| Crescendo Attack | Incremental escalation across a conversation |
| ASCII/Unicode Smuggling | Invisible characters carrying hidden instructions; demonstrated as guardrail bypass |
| Context Window Exhaustion | Flooding context so early guardrails are forgotten |
| Adversarial Suffixes | Token strings activating restricted-content neural pathways |
| TAP (Tree of Attacks with Pruning) | Tree-of-thought iterative refinement; >80% jailbreak rate on leading LLMs |

**Update (additional source, 2026-08-22, Google's AI Red Team blog):** Google's public AI Red Team report describes a similar dual approach at organizational scale: the team combines traditional red-team tradecraft with specialized AI expertise, drawing on threat intelligence from Mandiant, the Threat Analysis Group (TAG), and Google DeepMind, and its work supports Google's **[[Secure AI Framework (SAIF)]]**. Google's simulated attack taxonomy overlaps with Ross's (prompt attacks, adversarial examples) but adds **model backdooring**, **training data extraction**, and **data poisoning/exfiltration** as distinct categories. Google's key lessons echo the OWASP findings: traditional red teams are a useful starting point but AI attacks grow complex quickly; many findings lack a simple fix and should feed ongoing R&D rather than one-off patches; and — reinforcing the containment framing above — locking down systems via conventional security controls (not AI-specific fixes) still meaningfully reduces risk, since many AI attacks remain detectable using conventional methods.

### Case Study: Discord's Clyde AI

Discord launched Clyde (OpenAI-powered) in March 2023; users quickly found the "grandma exploit" — framing forbidden requests as roleplay to bypass filters. Consequences included policy violations, reputational damage, and eroded user trust. Discord's response: adopted Promptfoo-based evaluations for every prompt change, deployed passive moderation and observability tools, and built user feedback loops feeding back into red team setups.

### Practical Recommendations

1. Never do black-box AI red teaming without system access.
2. Never put sensitive data in system prompts — assume leakage.
3. Integrate prompt injection testing into CI/CD as a baseline benchmark.
4. Think like a social engineer when testing AI behavior.
5. Evaluate vendors rigorously — most address surface-level jailbreaks only.
6. Communicate irreducible risk to stakeholders — goal is blast-radius reduction.
7. Use gradual rollouts to limit blast radius when deploying new AI features.

## 🧠 First Principles & Mental Models

- **[[Goodhart's Law]]**: Most commercial AI red-teaming tools optimize for toxicity/bias scores rather than systemic risk — measuring what is easy to count rather than what actually matters for security.
- **[[Defense in Depth]]**: Because prompt injection and hallucination cannot be eliminated at the model level, layered containment (blast-radius reduction) at every architectural boundary is the only viable mitigation strategy.

## 🃏 Review Questions

**Q1**: Why does traditional binary penetration testing break down for generative AI systems?
**A**: GenAI behavior is probabilistic — identical inputs may produce different outputs even at temperature zero, so pass/fail exploit logic no longer applies and findings cannot be reliably reproduced.

**Q2**: What is the difference between model-layer and application-layer threats, and which should most teams prioritize?
**A**: Model-layer threats (hallucinations, hate speech, PII from training data) are baked into the base model; application-layer threats (indirect prompt injection, tool misuse, data exfiltration) arise from how the model is deployed. Most teams should focus on application-layer risks as they present the greatest technical risk and are within the team's control.

**Q3**: How should practitioners communicate AI security risk to business stakeholders given that prompt injection cannot be eliminated?
**A**: Frame the goal as blast-radius reduction rather than zero incidents — "you can't defuse the bomb, you put garbage can lids around it" — and ensure stakeholders understand these are architectural properties, not fixable bugs.
