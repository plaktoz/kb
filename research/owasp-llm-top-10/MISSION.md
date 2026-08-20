# Mission: OWASP LLM Top 10 Security

## Why
LLM-based products introduce a new class of vulnerabilities that traditional web security frameworks don't cover — attackers can manipulate model behavior through inputs, extract sensitive data baked into weights, and weaponize the model's own outputs. Knowing the OWASP LLM Top 10 lets you ship AI-powered features without handing attackers a new attack surface, and lets you audit existing systems before they're exploited in production.

## Success looks like
- You can name and explain all 10 OWASP LLM vulnerabilities without reference
- You can look at an LLM application architecture and identify which vulnerabilities each component is exposed to
- You can write a hardened system prompt, design a least-privilege tool/plugin contract, and specify output sanitization for a chatbot
- You can design a 5-layer defense stack (input → LLM core → output → tools → infrastructure) and map each layer to specific OWASP controls
- You can plan and execute a basic red team audit of an LLM application, including indirect injection via RAG and plugin abuse scenarios

## Constraints
- Learning from research reports and OWASP documentation — no access to proprietary systems
- Self-paced, one lesson at a time

## Out of scope
- Classic OWASP Top 10 web application vulnerabilities (assumed background knowledge)
- Model training infrastructure and MLOps in depth
- Specific LLM provider API implementations
