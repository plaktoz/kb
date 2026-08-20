---
type: literature-note
source_url: https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM10_ModelTheft.md
author: OWASP
tags: [llm-security, model-theft, owasp, ai-security]
date_consumed: 2026-08-20
---

## Summary

LLM10 covers unauthorized access and exfiltration of proprietary [[Large Language Model]] weights, parameters, or functional equivalents by malicious actors. Attackers may exploit infrastructure misconfigurations, insider threats, or API querying techniques like "functional model replication" to reconstruct a working duplicate. Consequences include economic loss, reputational damage, and erosion of competitive advantage.

## Core Concepts

- **[[Model Theft]]**: Exfiltration of LLM weights, parameters, or a functional replica without authorization.
- **[[Functional Model Replication]]**: Using synthetic training data generated via API prompts to fine-tune a separate [[Foundation Model]] — creating a shadow duplicate.
- **[[RBAC]] / [[Least Privilege]]**: Access control principles used to restrict who can reach model artifacts.
- **[[ML Model Registry]]**: Centralized inventory for tracking and auditing model access and provenance.
- **[[Model Watermarking]]**: Embedding identifiers into model weights or embeddings to trace leakage back to the source.
- **[[Rate Limiting]]**: Throttling API queries to limit data accumulation by adversaries attempting replication.
- **[[OWASP LLM Top 10]]**: The broader framework classifying the ten most critical LLM application vulnerabilities.

## Key Takeaways

- **Infrastructure exploits**: Misconfigurations in hosting can expose model weights directly.
- **Insider threats**: Disgruntled employees may leak model artifacts or training data.
- **API-based replication**: Adversaries accumulate query outputs to build a shadow model for further attacks.
- **Access controls**: RBAC and least-privilege principles are the primary defense.
- **Audit logging**: Regular monitoring of access logs catches anomalous extraction patterns early.
- **Watermarking**: Embedding fingerprints in model weights enables post-theft attribution.
- **Rate limiting**: Reduces the volume of outputs an attacker can harvest per unit time.

## 🧠 First Principles & Mental Models

- **[[Defense in Depth]]**: No single control stops model theft — layering access controls, rate limits, watermarking, and audit logs ensures that breaking one layer does not compromise the entire asset, which is exactly the multi-control posture OWASP prescribes here.
- **[[Least Privilege]]**: Granting only the minimum access needed to each role minimizes the blast radius of both compromised credentials and insider threats — the principle directly underpins the RBAC recommendation.

## 🃏 Review Questions

**Q1**: What is the core risk described in OWASP LLM10?
**A**: Malicious actors gaining unauthorized access to proprietary LLM weights or extracting a functional equivalent, resulting in economic loss, reputational damage, and loss of competitive advantage.

**Q2**: What is "functional model replication" and why is it dangerous?
**A**: It is a technique where an attacker uses carefully crafted API prompts to generate synthetic training data, then fine-tunes a separate foundation model into a working duplicate — no direct access to weights is required.

**Q3**: How does model watermarking help defend against LLM theft?
**A**: By embedding identifiers into the model's embeddings and weights during training, organizations can detect if a leaked or replicated model originated from their system, enabling attribution even after the theft occurs.
