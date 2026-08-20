---
type: literature-note
source_url: https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM03_TrainingDataPoisoning.md
author: OWASP
tags: [llm-security, training-data-poisoning, owasp, ai-safety]
date_consumed: 2026-08-20
---

## Summary

Training data poisoning (OWASP LLM03) is an integrity attack where adversaries manipulate pre-training data, fine-tuning datasets, or embedding pipelines to introduce backdoors, biases, or vulnerabilities into a large language model. Poisoned models can produce misleading, harmful, or biased outputs that affect end users even when they distrust the AI's responses. External data sources carry the highest risk because model creators lack visibility into their content quality and provenance.

## Core Concepts

- **[[Training Data Poisoning]]**: Deliberate manipulation of data used during [[Pre-training]], [[Fine-tuning]], or [[Embedding]] to corrupt model behaviour.
- **[[Pre-training]]**: Initial broad training on large text corpora; poisoning here affects foundational model knowledge.
- **[[Fine-tuning]]**: Adapting a pre-trained model to a specific domain using a curated input-output dataset; a high-value poisoning target due to smaller, easier-to-infiltrate datasets.
- **[[Embedding Process]]**: Converting categorical text into continuous vector representations; poisoned embeddings can skew retrieval and downstream reasoning.
- **[[Integrity Attack]]**: Poisoning is classified here because it undermines the correctness of the model's predictions rather than just its availability.
- **[[Split-View Data Poisoning]]** and **[[Frontrunning Poisoning]]**: Named attack vectors where adversaries serve different content to crawlers vs. users, or race to inject content before it is indexed.
- **[[ML-BOM (Machine Learning Bill of Materials)]]**: Provenance methodology for tracking training data sources, analogous to software SBOMs.
- **[[MLSecOps]]**: Security-integrated ML operations lifecycle that embeds adversarial robustness, auditing, and red-teaming into model development.
- **[[DVC (Data Version Control)]]**: Tool for tracking dataset versions to detect unauthorized modifications.
- **[[Federated Learning]]**: Distributed training approach that limits centralised data exposure and can reduce the blast radius of poisoning.
- **[[Prompt Injection]]**: Can act as a secondary attack vector that feeds malicious data into the model if user inputs are recycled as training data without sanitisation.

## Key Takeaways

- **Integrity Attack**: Poisoning corrupts model predictions; even distrustful users face residual harm.
- **Attack Surfaces**: Pre-training corpora, fine-tuning datasets, and embedding pipelines are all viable targets.
- **External Data Risk**: Third-party data sources are highest-risk — creators have no content guarantees.
- **Supply Chain Verification**: Use [[ML-BOM]] attestations and verify data provenance at every stage.
- **Sandboxing**: Network controls prevent models from ingesting unintended external sources during training.
- **Statistical Detection**: Outlier detection and anomaly detection can filter adversarial data before training.
- **[[DVC (Data Version Control)]]**: Enables precise identification of dataset tampering leading to poisoning.
- **Vector DB Fix**: User-supplied corrections via a vector database can mitigate poisoning in production without retraining.
- **Red Teaming**: LLM-based red team exercises and vulnerability scanning should be part of the training lifecycle.
- **Prompt Injection Link**: Insufficient input sanitisation can channel malicious user inputs back into training data.

## 🧠 First Principles & Mental Models

- **[[Supply Chain Security]]**: Just as software dependencies can be compromised upstream, training data is a supply chain — trust must be verified at the source, not assumed from the consumer's vantage point. The ML-BOM methodology applies the same provenance-tracking discipline used in software SBOMs.
- **[[Defence in Depth]]**: No single control (sandboxing, outlier detection, red teaming, human review) is sufficient alone; layering independent mitigations ensures that a bypass of one layer does not result in full compromise — exactly the rationale behind the 10-point prevention list.

## 🃏 Review Questions

**Q1**: What makes training data poisoning an "integrity attack" rather than another class of vulnerability?
**A**: Poisoning tampers with the training data that determines model predictions, directly undermining the correctness of outputs rather than targeting availability or confidentiality.

**Q2**: Which training stage is most commonly targeted for fine-tuning and embedding attacks, and why?
**A**: Fine-tuning and embedding pipelines are the most common targets because they use smaller, domain-specific datasets that are easier for adversaries to infiltrate with falsified or malicious content.

**Q3**: How can a vector database be used to mitigate an already-deployed poisoned model?
**A**: User-supplied corrections can be added to a vector database to override poisoned outputs, allowing in-production fixes without the cost of retraining the underlying model.
