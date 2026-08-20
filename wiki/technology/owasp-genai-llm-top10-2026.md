---
type: literature-note
source_url: https://owasp.org/www-project-top-10-for-large-language-model-applications/
author: Unknown
tags: [owasp, llm-security, genai, ai-safety]
date_consumed: 2026-08-20
---

## Summary

The OWASP GenAI LLM Top 10 2026 is the official awareness document for the ten most critical security risks in large language model applications, published August 4, 2026. Maintained under the [[OWASP]] GenAI Security Project (600+ contributors, 18+ countries), it targets developers, architects, data scientists, and security practitioners building with LLMs. The project originated as the OWASP Top 10 for LLM Applications in 2023 and migrated to the GenAI Security Project; the original owasp.org page is now a historical archive.

## Core Concepts

- **[[OWASP]] GenAI Security Project** — the governing body maintaining the LLM Top 10 standard
- **[[Prompt Injection]]** (LLM01) — attacker-controlled inputs hijack model behaviour
- **[[Sensitive Information Disclosure]]** (LLM02) — models inadvertently reveal private or confidential data
- **[[Excessive Agency]]** (LLM03) — LLM-driven systems take actions beyond intended scope
- **[[Supply Chain Security]]** (LLM04) — risks from third-party models, datasets, and plugins
- **[[Data and Model Poisoning]]** (LLM05) — corrupted training or fine-tuning data subverting model behaviour
- **[[Unbounded Consumption]]** (LLM06) — uncontrolled resource usage enabling denial-of-service or cost attacks
- **[[AI Misinformation]]** (LLM07) — LLMs generating and propagating false or misleading content
- **[[Hidden Context Exposure]]** (LLM08) — system prompts or internal context leaking to end users
- **[[Vector and Embedding Weaknesses]]** (LLM09) — vulnerabilities in RAG pipelines and semantic search layers
- **[[Improper Output Handling]]** (LLM10) — downstream systems misprocessing raw LLM output (e.g. XSS, SSRF)

## Historical v1.1 Top 10 (2023, Archived)

| ID | Vulnerability |
|----|--------------|
| LLM01 | **[[Prompt Injection]]** — crafted inputs lead to unauthorised access/data breaches |
| LLM02 | **Insecure Output Handling** — unvalidated outputs enable downstream exploits |
| LLM03 | **[[Training Data Poisoning]]** — tampered data compromises model behaviour |
| LLM04 | **Model Denial of Service** — resource-heavy operations cause disruptions |
| LLM05 | **[[Supply Chain Security\|Supply Chain Vulnerabilities]]** — compromised components undermine integrity |
| LLM06 | **[[Sensitive Information Disclosure]]** — unprotected outputs expose sensitive data |
| LLM07 | **Insecure Plugin Design** — insufficient access controls risk remote code execution |
| LLM08 | **[[Excessive Agency]]** — unchecked LLM autonomy causes unintended consequences |
| LLM09 | **Overreliance** — uncritical use of LLM outputs leads to poor decisions |
| LLM10 | **Model Theft** — unauthorised access risks theft of proprietary models |

## Key Takeaways

- **2026 Top 10**: Prompt Injection, Sensitive Info Disclosure, Excessive Agency, Supply Chain, Data Poisoning, Unbounded Consumption, Misinformation, Hidden Context Exposure, Vector/Embedding Weaknesses, Improper Output Handling.
- **2023 v1.1 Top 10 (archived)**: Prompt Injection, Insecure Output Handling, Training Data Poisoning, Model DoS, Supply Chain, Sensitive Info Disclosure, Insecure Plugin Design, Excessive Agency, Overreliance, Model Theft.
- **Project migration**: The original owasp.org page is now a historical archive; active work lives at genai.owasp.org and GitHub `GenAI-Security-Project/GenAI-LLM-Top10`.
- **Scope**: Awareness document — not a compliance checklist but a risk prioritisation framework.
- **Audience**: Developers, architects, data scientists, and security practitioners.
- **License**: CC BY-SA 4.0 — freely shareable with attribution.
- **Canonical source**: `2026/final/` directory; previous 2025 release retained in `2025/`.
- **Community**: OWASP Slack `#team-genai-top-10-llm`; lead Steve Wilson.
- **Corrections**: Submitted via GitHub issue templates; direct pushes to `main` blocked.

## 🧠 First Principles & Mental Models

- **[[Threat Modelling]]**: The Top 10 is an applied threat model — it forces practitioners to enumerate adversarial scenarios before building, which surfaces mitigations earlier and cheaper than post-hoc patching.
- **[[Pareto Principle]]**: Addressing the ten highest-impact risk categories covers the majority of real-world LLM attack surface, making the list a practical 80/20 prioritisation tool rather than an exhaustive catalogue.

## 🃏 Review Questions

**Q1**: What is the OWASP GenAI LLM Top 10 and who is it for?
**A**: It is an awareness document listing the ten most critical security risks in LLM applications, targeting developers, architects, data scientists, and security practitioners working with large language models.

**Q2**: What are two new or notably renamed entries in the 2026 edition compared to prior releases?
**A**: The 2026 list adds Hidden Context Exposure (LLM08) and Unbounded Consumption (LLM06), which were not present as distinct categories in the 2025 edition.

**Q3**: How would a security engineer use this document in practice?
**A**: They would treat the Top 10 as a risk prioritisation checklist during design reviews and threat modelling sessions, ensuring mitigations for each category are considered before deploying an LLM-powered system.
