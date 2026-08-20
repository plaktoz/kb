---
source_url: https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM10_ModelTheft.md
author: OWASP
date: 2026-08-20
---

## LLM10: Model Theft

### Description

This entry covers unauthorized access and exfiltration of LLM models by malicious actors. When proprietary models are compromised, copied, or have their "weights and parameters extracted to create a functional equivalent," the consequences include economic loss, reputational damage, and erosion of competitive advantage.

### Common Vulnerability Examples

Attackers may exploit infrastructure misconfigurations, leverage insider threats, or use carefully crafted queries against model APIs. One notable technique involves "functional model replication," where synthetic training data generated via prompts is used to fine-tune a separate foundational model — creating a working duplicate.

### Key Prevention Strategies

- Deploy strong access controls using RBAC and least-privilege principles
- Restrict LLM network resource access
- Maintain a centralized ML Model Registry
- Monitor and audit access logs regularly
- Apply rate limiting to reduce "risk of data exfiltration from the LLM applications"
- Implement "a watermarking framework into the embedding and detection stages"

### Notable Attack Scenarios

Threat vectors range from infrastructure exploits and disgruntled employees leaking artifacts, to API querying that accumulates enough outputs to build a shadow model useful for staging further adversarial attacks.

### References

Full reference links are included in the original source document at:
https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM10_ModelTheft.md
