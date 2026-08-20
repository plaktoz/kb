---
type: literature-note
source_url: https://owasp.org/www-project-top-10-for-large-language-model-applications/
author: Steve Wilson, Ads Dawson, John Sotiropoulos, Scott Clinton, Sandy Dunn (community project)
tags: [llm-security, owasp, ai-safety, genai]
date_consumed: 2026-08-20
---

## Summary
The OWASP Top 10 for LLM Applications catalogues the ten most critical security risks in deploying large language models, ranging from prompt injection to model theft. Originally released as v1.1 in 2023, the project has since evolved into the broader OWASP GenAI Security Project covering agentic AI, multimodal models, and RAG architectures. The 2026 release (OWASP GenAI LLM Top 10) reflects a community of 600+ contributors and addresses the expanded attack surface of modern generative AI systems.

## Core Concepts
- **[[Prompt Injection]]**: Crafted inputs that override original instructions to manipulate model behavior or gain unauthorized access.
- **Insecure Output Handling**: Unvalidated LLM outputs passed downstream, enabling [[XSS]], [[SSRF]], or privilege escalation.
- **Training Data Poisoning**: Tampered training data introducing biases or backdoors that persist into production.
- **Model Denial of Service**: Resource-exhaustion attacks against LLM inference infrastructure.
- **Supply Chain Vulnerabilities**: Compromised datasets, pre-trained models, or third-party components in the LLM pipeline.
- **Sensitive Information Disclosure**: PII, credentials, or proprietary data extracted via clever prompting.
- **Insecure Plugin Design**: Insufficient access controls in [[LLM plugins]] enabling unauthorized actions or code execution.
- **[[Excessive Agency]]**: Unchecked model autonomy causing unintended consequences from overly permissive capabilities.
- **Overreliance**: Uncritical acceptance of LLM outputs leading to cascading failures from hallucinations.
- **Model Theft**: Unauthorized extraction of proprietary models via API attacks, model inversion, or weight theft.
- **[[OWASP GenAI Security Project]]**: The successor initiative at genai.owasp.org covering LLMs, agentic AI, and multimodal systems.

## Key Takeaways
- **Prompt Injection is #1**: The dominant LLM attack vector; inputs can override system instructions. [[Prompt Injection]]
- **Output handling matters**: LLM outputs fed to downstream systems can trigger classic web exploits like [[XSS]].
- **Supply chain risk is real**: Poisoned datasets or models introduce backdoors that are hard to detect post-training.
- **Plugins expand attack surface**: Every plugin integration is a potential unauthorized action or data-access vector.
- **Excessive agency is unique to AI**: Over-permissioned models can take harmful autonomous actions without human oversight. [[Excessive Agency]]
- **Overreliance causes cascading failures**: Systems built without LLM output verification fail badly when models hallucinate.
- **Project has expanded scope**: v1.1 (2023) → GenAI Top 10 2026; now covers agentic AI and [[RAG]] architectures.
- **Community-driven standard**: 600+ contributors across 18+ countries; widely referenced in AI security audits.

## 🧠 First Principles & Mental Models
**Least Privilege applied to AI**: Just as system accounts should have minimal permissions, LLM agents should be granted only the capabilities strictly necessary for their task — the Excessive Agency risk directly violates this principle.

**Trust Boundary thinking**: Every interface where untrusted data enters (user prompts, plugin outputs, scraped content) is a potential injection point. Mapping trust boundaries is the first step to securing an LLM application.

## 🃏 Review Questions

**Q1**: What is the #1 risk in the OWASP Top 10 for LLM Applications, and why is it considered the most critical?
**A**: Prompt Injection, because attackers can craft inputs that override the model's original instructions, enabling unauthorized behavior manipulation or access — and it is difficult to fully prevent given how LLMs process natural language.

**Q2**: How does Insecure Output Handling differ from Sensitive Information Disclosure?
**A**: Insecure Output Handling occurs when unvalidated LLM outputs are passed to downstream systems, triggering exploits like XSS or SSRF; Sensitive Information Disclosure is about the LLM itself leaking PII or credentials in its responses through clever prompting.

**Q3**: How has the OWASP LLM project evolved beyond the original Top 10 list?
**A**: It expanded into the OWASP GenAI Security Project (genai.owasp.org), which now covers agentic AI systems, multimodal models, RAG architectures, and AI-driven application pipelines — reflecting the broader attack surface of modern generative AI beyond pure LLMs.
