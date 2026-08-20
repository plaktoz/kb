---
source_url: https://owasp.org/www-project-top-10-for-large-language-model-applications/
author: Steve Wilson, Ads Dawson, John Sotiropoulos, Scott Clinton, Sandy Dunn (community project)
date: 2026-08-04
---

# OWASP Top 10 for Large Language Model Applications

This page serves as a legacy archive for the original OWASP Top 10 for LLM Applications project, while active development has shifted to the OWASP GenAI Security Project at genai.owasp.org.

The current release is the **OWASP GenAI LLM Top 10 2026**. The broader GenAI Security Project covers LLMs, agentic AI, and AI-driven applications, grown to over 600 contributors across 18+ countries.

## Archived v1.1 Top 10 (2023)

1. **Prompt Injection** – Crafted inputs enabling unauthorized access or behavior manipulation. Attackers override original instructions via malicious inputs.

2. **Insecure Output Handling** – Unvalidated LLM outputs enabling downstream exploits such as XSS, SSRF, or privilege escalation when outputs are passed to other systems.

3. **Training Data Poisoning** – Tampered training data compromising model behavior, introducing biases or backdoors that persist into production.

4. **Model Denial of Service** – Resource-heavy operations disrupting availability. Attackers send requests designed to consume excessive compute resources.

5. **Supply Chain Vulnerabilities** – Compromised components, datasets, or pre-trained models undermining integrity of the entire LLM pipeline.

6. **Sensitive Information Disclosure** – Unprotected sensitive data revealed in outputs, including PII, proprietary business data, or security credentials extracted through clever prompting.

7. **Insecure Plugin Design** – Insufficient access controls in LLM plugins allowing unauthorized actions, data access, or code execution through the plugin interface.

8. **Excessive Agency** – Unchecked LLM autonomy causing unintended consequences when models are given too much permission or capability without adequate oversight.

9. **Overreliance** – Uncritical acceptance of LLM outputs without verification, leading to cascading failures when the model hallucinates or produces incorrect information.

10. **Model Theft** – Unauthorized access to proprietary models through API extraction attacks, model inversion, or direct theft of model weights.

## GenAI Security Project

The project has evolved beyond LLMs alone to address the full landscape of generative AI security including:
- Agentic AI systems
- Multimodal models
- AI-driven application pipelines
- Retrieval Augmented Generation (RAG) architectures

For the latest guidance, visit genai.owasp.org.
