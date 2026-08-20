---
type: literature-note
source_url: https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM06_SensitiveInformationDisclosure.md
author: OWASP
tags: [owasp, llm-security, data-privacy, ai-safety]
date_consumed: 2026-08-20
---

## Summary

LLM06 from the OWASP Top 10 for LLM Applications identifies sensitive information disclosure as a risk arising from LLMs revealing confidential data, PII, or proprietary details in their outputs. The consumer-LLM interaction forms a two-way trust boundary where neither client input nor LLM output can be inherently trusted. Mitigations center on data sanitization before training, input validation, and least-privilege access controls on data used for fine-tuning.

## Core Concepts

- **[[LLM Sensitive Information Disclosure]]**: When an LLM application leaks confidential data — PII, proprietary algorithms, or trade secrets — through responses, either due to training memorization or improper output filtering.
- **[[Two-Way Trust Boundary]]**: The consumer-LLM interaction where both the client→LLM input and the LLM→client output are untrusted channels; neither can be assumed safe without explicit validation and filtering.
- **[[Training Data Memorization]]**: The tendency of LLMs to overfit or memorize sensitive data seen during training, making it reproducible via carefully crafted prompts.
- **[[Data Sanitization]]**: Scrubbing user data and sensitive content from datasets before they enter model training pipelines to prevent future disclosure.
- **[[Least Privilege in Fine-Tuning]]**: The principle that models should not be trained on data accessible only to high-privileged users if that data could later be surfaced to lower-privileged users.
- **[[Prompt Injection]]**: An attack vector capable of circumventing system-prompt restrictions designed to prevent disclosure, underscoring that prompt-level controls alone are insufficient.
- **[[LLM Data Privacy]]**: Policies and technical controls — including Terms of Use and opt-out mechanisms — informing users how their data is processed and preventing unintended training inclusion.

## Key Takeaways

- **Filtering Is Not Enough**: Incomplete output filtering is the most common disclosure vector.
- **Training Memorization Risk**: Sensitive data in training sets can be extracted later via prompts.
- **Two-Way Boundary**: Both input and output are attack surfaces; treat both as untrusted.
- **Least Privilege Training**: Never train on data the highest-privileged user sees if lower-privileged users query the model.
- **Runtime Data Access**: External data sources accessed at inference time must have strict access controls.
- **System Prompts Are Bypassable**: Prompt injection and other vectors can circumvent disclosure restrictions in system prompts.
- **Transparency Obligation**: LLM application owners must publish Terms of Use and provide opt-out for training data inclusion.

## 🧠 First Principles & Mental Models

- **[[Principle of Least Privilege]]**: Fine-tuning models on high-privilege data and then exposing the model to low-privilege users violates least privilege — the OWASP mitigation directly operationalizes this principle to prevent cross-privilege data leakage.
- **[[Defense in Depth]]**: Relying solely on system-prompt restrictions to prevent disclosure is a single layer of control; robust mitigation requires layered defenses — data sanitization at ingestion, input validation at runtime, and access controls on external data sources — because any single layer can be bypassed.

## 🃏 Review Questions

**Q1**: What is the core risk identified by OWASP LLM06 Sensitive Information Disclosure?
**A**: LLM applications can reveal sensitive data, PII, or proprietary information through their outputs due to training memorization, improper output filtering, or misinterpretation — creating privacy violations and unauthorized data access.

**Q2**: Why are system-prompt restrictions insufficient as the sole defense against sensitive information disclosure?
**A**: The unpredictable nature of LLMs means system-prompt restrictions may not always be honored, and they can be circumvented via prompt injection or other attack vectors, making them an unreliable single-layer control.

**Q3**: How should organizations apply least-privilege principles when fine-tuning LLMs on internal data?
**A**: Avoid training the model on data that only high-privileged users can access, since fine-tuned knowledge can be surfaced to lower-privileged users; also limit and strictly access-control any external data sources used for runtime data enrichment.
