---
type: literature-note
source_url: https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM02_InsecureOutputHandling.md
author: OWASP
tags: [owasp, llm-security, output-handling, xss]
date_consumed: 2026-08-20
---

## Summary

[[OWASP]] classifies Insecure Output Handling as LLM02 — the failure to validate, sanitize, or encode LLM-generated content before it reaches downstream components or users. Because LLM output is shaped by user-controlled prompt input, insufficient handling effectively grants indirect access to backend functionality. Successful exploitation can produce XSS, CSRF, SSRF, privilege escalation, or remote code execution.

## Core Concepts

- **[[Insecure Output Handling]]**: Passing raw LLM-generated content to downstream systems without validation, sanitization, or encoding.
- **[[Cross-Site Scripting]] (XSS)**: Unsanitized LLM output rendered in a browser can execute attacker-controlled JavaScript.
- **[[Cross-Site Request Forgery]] (CSRF)**: LLM-generated content can embed requests that the victim's browser sends with their credentials.
- **[[Server-Side Request Forgery]] (SSRF)**: LLM output passed to backend URL-fetching functions can redirect internal requests to attacker-controlled endpoints.
- **Remote Code Execution (RCE)**: LLM output fed directly into `exec` or `eval` functions enables arbitrary command execution on backend systems.
- **[[Prompt Injection]]**: Indirect injection is a prerequisite condition that amplifies insecure output handling — malicious external content can steer what the LLM outputs, which then propagates unsanitized downstream.
- **[[Zero Trust]]**: Treating LLM responses as untrusted user input and applying the same validation rigor as any external data source.
- **[[OWASP ASVS]]**: Application Security Verification Standard — provides concrete guidance on input validation, sanitization, and output encoding that directly applies to LLM output pipelines.

## Key Takeaways

- **Treat LLM output as untrusted**: Apply zero-trust input validation on all model responses before use.
- **Encode output for context**: HTML-encode, URL-encode, or shell-escape LLM output based on where it is rendered.
- **Never pipe output to exec/eval**: Direct shell or code execution of LLM responses enables RCE.
- **Follow OWASP ASVS Section 5**: Covers validation, sanitization, and encoding — directly applicable to LLM output.
- **Privilege amplification risk**: Granting the LLM excessive backend privileges worsens the blast radius of output exploitation.
- **Plugin validation matters**: Third-party plugins that skip input validation are an additional exploitation vector.
- **Indirect injection compounds the risk**: Prompt injection in source content steers LLM output, making sanitization the last line of defense.

## 🧠 First Principles & Mental Models

- **[[Defense in Depth]]**: Output sanitization is a distinct security layer from access control — even if an attacker injects a malicious prompt, proper output encoding can prevent the injected payload from executing in the browser or backend.
- **[[Confused Deputy Problem]]**: The LLM acts as a trusted intermediary between users and backend systems; without output validation, it can be coerced into issuing privileged commands on behalf of an attacker, mirroring the classic confused deputy dynamic.

## 🃏 Review Questions

**Q1**: What is the core risk that Insecure Output Handling introduces in LLM applications?
**A**: LLM output is shaped by user-controlled input, so without validation and sanitization, downstream systems that consume that output can be exploited to execute XSS, RCE, SSRF, or privilege escalation attacks.

**Q2**: What conditions increase the severity of an Insecure Output Handling vulnerability?
**A**: The risk is amplified when the LLM is granted privileges beyond what end users should have, when the app is vulnerable to indirect prompt injection, and when third-party plugins fail to validate their inputs.

**Q3**: What is the primary mitigation strategy OWASP recommends for Insecure Output Handling?
**A**: Adopt a zero-trust approach — treat model output as untrusted user input, apply proper validation and sanitization before passing it to any backend function, and follow OWASP ASVS guidelines for output encoding.
