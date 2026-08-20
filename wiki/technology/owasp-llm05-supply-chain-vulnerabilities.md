---
type: literature-note
source_url: https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM05_SupplyChainVulnerabilities.md
author: OWASP
tags: [owasp, llm-security, supply-chain, ai-safety]
date_consumed: 2026-08-20
---

## Summary

LLM05 from the OWASP Top 10 for LLM Applications identifies supply-chain vulnerabilities as a key risk, extending traditional software supply-chain concerns to ML-specific assets such as pre-trained models, training datasets, and third-party plugins. Attackers can compromise integrity at multiple stages — from package registries to public model repositories — leading to biased outputs, backdoors, or full system compromise. Mitigations center on vendor vetting, Software Bill of Materials (SBOM), model signing, and anomaly detection in MLOps pipelines.

## Core Concepts

- **[[LLM Supply Chain]]**: The end-to-end chain covering third-party packages, pre-trained models, training datasets, and [[LLM Plugin]] extensions that an LLM application depends on.
- **[[Training Data Poisoning]]**: Attackers corrupt publicly available datasets or pre-trained models to embed backdoors or biases, exploiting the fact that fine-tuning inherits upstream flaws.
- **[[Software Bill of Materials]] (SBOM)**: An inventory of all software components; currently does not cover ML models or datasets, creating a gap that MLOps practices must fill.
- **[[Model Signing]]**: Cryptographic signing of models and code to verify provenance and detect tampering when sourcing from external suppliers.
- **[[OWASP A06:2021 Vulnerable and Outdated Components]]**: The traditional OWASP control for dependency management directly applies to LLM stacks in addition to ML-specific risks.
- **[[MLOps]]**: Practices and platforms for secure model repository management, data/experiment tracking, and adversarial robustness testing integrated into CI/CD pipelines.
- **[[Adversarial Robustness Testing]]**: Anomaly detection and adversarial tests applied to supplied models and data to surface tampering or poisoning before deployment.

## Key Takeaways

- **Traditional + ML Risks**: Supply chain risk spans both classic package CVEs and ML-specific poisoning/backdoors.
- **Poisoned Model Marketplace**: Attackers can upload backdoored models to Hugging Face-style registries for unsuspecting fine-tuners.
- **SBOM Gap**: SBOMs don't yet cover models or datasets — MLOps tooling is the current workaround.
- **Plugin Surface**: Third-party LLM plugins expand the attack surface; vet with [[LLM07 Insecure Plugin Design]] criteria.
- **T&Cs as Risk Vector**: Operator policy changes can cause sensitive data to be used for model training without explicit user action.
- **Patching Policy**: Maintain pinned, maintained API versions and model artifacts; unpatched components remain the #1 exploitation path.
- **Monitoring**: Cover component scanning, unauthorized plugin detection, and model artifact integrity continuously.

## 🧠 First Principles & Mental Models

- **[[Trust but Verify]]**: LLM applications implicitly trust upstream artifacts (models, datasets, packages); this OWASP entry forces explicit verification gates at each supply-chain node — exactly the principle that SBOM and model signing operationalize.
- **[[Attack Surface Expansion]]**: Each new dependency — package, pre-trained model, plugin — is an independently owned trust boundary; the more dependencies, the larger the adversary's available attack surface, making inventory and vetting non-optional at scale.

## 🃏 Review Questions

**Q1**: What is the central claim of OWASP LLM05 Supply-Chain Vulnerabilities?
**A**: LLM applications inherit risk not just from traditional software dependencies but also from pre-trained models and training data supplied by third parties, which are susceptible to tampering and poisoning attacks that can introduce backdoors, biased outputs, or system failures.

**Q2**: Why are SBOMs insufficient for LLM supply-chain risk today, and what is the recommended workaround?
**A**: SBOMs currently do not cover ML models, their artifacts, or datasets; organizations should compensate by adopting MLOps best practices and platforms that provide secure model repositories with data, model, and experiment tracking, alongside model and code signing.

**Q3**: How can an organization detect whether a supplied pre-trained model has been tampered with before deployment?
**A**: Run anomaly detection and adversarial robustness tests on the supplied model and data — ideally integrated into MLOps pipelines — or conducted as part of red-teaming exercises to surface backdoors or poisoning before the model reaches production.
