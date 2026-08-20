---
type: literature-note
source_url: https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM09_Overreliance.md
author: OWASP
tags: [llm-security, owasp, hallucination, ai-trust]
date_consumed: 2026-08-20
---

## Summary

OWASP LLM09 defines Overreliance as the risk that arises when people or systems trust LLM outputs without sufficient oversight or validation — particularly because LLMs can produce factually incorrect, inappropriate, or unsafe content in an authoritative tone. This phenomenon, known as hallucination or confabulation, can lead to security breaches, misinformation, legal issues, and reputational damage. LLM-generated code carries a parallel risk: unnoticed security vulnerabilities introduced when AI suggestions are adopted without rigorous review.

## Core Concepts

- **[[LLM Hallucination]]** — the tendency of LLMs to generate plausible-sounding but factually incorrect or fabricated content
- **[[Confabulation]]** — a related term describing confident, authoritative output that lacks factual grounding
- **[[Prompt Engineering]]** — a technique to improve output quality and reduce hallucination risk
- **[[Chain of Thought Prompting]]** — structured reasoning technique that can reduce hallucination by making reasoning steps explicit
- **[[Parameter Efficient Tuning]]** — fine-tuning approach (including PET) to improve factual accuracy of model outputs
- **[[Self-Consistency Sampling]]** — comparing multiple model responses to the same prompt to filter inconsistent outputs
- **[[Retrieval-Augmented Generation]]** — grounding LLM outputs in external, verifiable knowledge sources
- **[[Human-in-the-Loop]]** — continuous oversight and validation as the primary safeguard against unchecked LLM errors
- **[[Dependency Confusion Attack]]** — a supply chain risk highlighted when LLMs hallucinate non-existent package names that attackers can register as malicious packages

## Key Takeaways

- **Core risk**: LLMs produce incorrect content in an authoritative tone, misleading users or systems.
- **Code vulnerability**: AI-generated code can introduce security flaws when adopted without review.
- **Monitor outputs**: Use self-consistency or voting techniques to filter inconsistent responses.
- **Cross-check facts**: Validate critical outputs against trusted external sources.
- **Fine-tune for accuracy**: Use prompt engineering, PET, or full tuning to reduce hallucination.
- **Automate validation**: Implement mechanisms to cross-verify LLM output against known facts.
- **Decompose tasks**: Break complex tasks across multiple agents to reduce individual hallucination risk.
- **Communicate limitations**: Clearly disclose LLM risks and inaccuracies to end users.
- **Responsible interfaces**: Build APIs with content filters and clear AI-generated content labeling.
- **Secure coding practices**: Treat AI code suggestions as untrusted; review before integrating.

## 🧠 First Principles & Mental Models

- **[[Automation Bias]]**: Users systematically over-trust authoritative-sounding automated output — the same cognitive tendency that causes pilots to miss instrument errors applies directly to LLM-generated facts and code, making oversight mechanisms structurally necessary rather than optional.
- **[[Dependency Confusion Attack]]**: When an LLM hallucinates a non-existent library name, any developer who installs that package without verification becomes the unwitting entry point for a supply chain attack — the hallucination creates the exact naming gap attackers need.

## 🃏 Review Questions

**Q1**: What is Overreliance in the LLM context, and what are its primary harmful outcomes?
**A**: Overreliance occurs when users or systems trust LLM outputs without adequate oversight, especially given LLMs' tendency to hallucinate authoritative-sounding but incorrect content. Harmful outcomes include security breaches, misinformation, miscommunication, legal issues, and reputational damage.

**Q2**: How does the hallucinated-package scenario illustrate the code-specific risk of Overreliance?
**A**: An LLM may suggest a non-existent library; a developer who installs it without verification could unknowingly integrate a malicious package registered by an attacker under that name, turning an LLM hallucination into a live supply chain vulnerability.

**Q3**: What combination of techniques does OWASP recommend to reduce Overreliance risk in production LLM systems?
**A**: OWASP recommends layering output monitoring with self-consistency checks, cross-validating against trusted external sources, improving model accuracy via fine-tuning or prompt engineering, implementing automatic fact-verification mechanisms, and clearly communicating LLM limitations to users.
