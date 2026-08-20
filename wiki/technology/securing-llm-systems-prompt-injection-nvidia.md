---
type: literature-note
source_url: https://developer.nvidia.com/blog/securing-llm-systems-against-prompt-injection/
author: Rich Harang
tags: [prompt-injection, llm-security, langchain, cve]
date_consumed: 2026-08-20
---

## Summary

[[NVIDIA]]'s AI Red Team identified three exploitable [[Prompt Injection]] vulnerabilities in [[LangChain]] chains — remote code execution (CVE-2023-29374), SSRF (CVE-2023-32786), and SQL injection (CVE-2023-32785) — all patched in later releases. The root cause across all three is the inseparability of the control and data planes in LLM prompts: a single prompt carries both instructions and data, so attacker-controlled input can redirect downstream external service calls. The core mitigation principle is to treat all LLM output as potentially malicious and apply least-privilege access to every external integration.

## Core Concepts

- **[[Prompt Injection]]**: Attacker embeds override instructions inside user input, causing the LLM to follow injected commands instead of the developer's system prompt.
- **Control-Data Plane Conflation**: Unlike traditional systems, LLM prompts cannot separate control signals (instructions) from data — this is the structural root cause of all three CVEs.
- **[[LangChain]] Chain Architecture**: Three-layer model — core library, chains/agents, third-party APIs. Vulnerabilities existed in the chains layer, not core.
- **CVE-2023-29374 (RCE via `llm_math`)**: Attacker instructs LLM to "repeat the following code exactly," causing a Python evaluation engine to execute arbitrary user-supplied code.
- **CVE-2023-32786 (SSRF via `APIChain`)**: Attacker declares a `NEW QUERY` directing the LLM to fetch from an unintended URL via `APIChain.from_llm_and_api_docs`.
- **CVE-2023-32785 (SQL Injection via `SQLDatabaseChain`)**: "Ignore all previous instructions" format causes the LLM to emit and execute attacker-chosen SQL.
- **[[Least Privilege]]**: Restricting external service permissions to the minimum required for each chain call.
- **Parameterized Plug-in Templates**: Fixing variable slots in templates to prevent injected content from reshaping API calls.

## Key Takeaways

- **CVSS 9.8 RCE**: `llm_math` chain allowed arbitrary Python execution via natural language.
- **Chains layer, not core**: Vulnerabilities were isolated; LangChain core engine was unaffected.
- **Upgrade first**: All three CVEs are fixed in current LangChain versions.
- **Treat LLM output as untrusted**: Inspect and sanitize before passing to external services.
- **Parameterize templates**: Lock down plug-in call shapes to prevent injection reshaping.
- **Least privilege on every call**: Scope each external service call to the minimum needed.
- **Avoid authorization after plug-in calls**: Cross-plug-in authorization is complex; don't chain privileged calls.
- **Multistep chains are high-risk**: Chains calling multiple external services multiply the attack surface.

## 🧠 First Principles & Mental Models

- **[[Confused Deputy Problem]]**: LangChain chains act as privileged deputies calling external services on behalf of the user — prompt injection exploits this by having the LLM carry attacker instructions through the deputy boundary, triggering unintended RCE, SSRF, or SQL execution.
- **[[Defense in Depth]]**: No single fix eliminates the control-data plane conflation in LLMs; layering least-privilege access, output sanitization, parameterized templates, and input inspection is the only structural mitigation.

## 🃏 Review Questions

**Q1**: What is the structural root cause that enables all three LangChain prompt injection CVEs?
**A**: The control and data planes are inseparable in LLM prompts — a single prompt carries both instructions and user data, so attacker-controlled input can inject control directives that the LLM then routes to external service calls.

**Q2**: How did the `llm_math` chain (CVE-2023-29374) achieve remote code execution?
**A**: Instead of posing a math question, the attacker instructed the LLM to "repeat the following code exactly," causing the chain's Python evaluation engine to execute arbitrary user-supplied code; the CVSS score was 9.8.

**Q3**: What is the most important architectural principle for securing LLM chains that call external services?
**A**: Treat all LLM output as potentially malicious — inspect and sanitize it before passing it downstream — and apply least-privilege access so that even a successful injection has minimal blast radius.
