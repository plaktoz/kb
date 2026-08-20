---
type: literature-note
source_url: https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM01_PromptInjection.md
author: Unknown
tags: [owasp, prompt-injection, llm-security, ai-vulnerabilities]
date_consumed: 2026-08-20
---

## Summary

[[OWASP]] classifies Prompt Injection as LLM01 — the top vulnerability in LLM applications — occurring when attackers manipulate a model through crafted inputs to unknowingly execute malicious intentions. It takes two primary forms: direct injection (jailbreaking the system prompt) and indirect injection (embedding malicious instructions in external content the model processes). Because LLMs cannot reliably distinguish trusted instructions from injected adversarial text, the attack surface spans every external input channel.

## Core Concepts

- **[[Prompt Injection]]**: Attacker-crafted inputs that redirect or override LLM behavior against the developer's intent.
- **Direct Injection (Jailbreaking)**: User overwrites or exposes the system prompt through crafted conversational turns.
- **Indirect Injection**: Malicious instructions embedded in external content — websites, files, emails — that an LLM agent retrieves and processes.
- **[[OWASP]] LLM Top 10**: Standardized vulnerability taxonomy for large language model applications; LLM01 is the highest-priority entry.
- **[[Least Privilege]]**: Restricting LLM backend access to only what is needed to limit injection blast radius.
- **[[Human-in-the-Loop]]**: Requiring explicit user approval before the LLM executes privileged or irreversible operations.
- **Prompt Segregation (ChatML)**: Structuring prompts so external content is clearly delimited from trusted instructions to reduce injection success.

## Key Takeaways

- **Two attack vectors**: Direct (user-facing jailbreaks) and indirect (malicious content in data sources).
- **Least privilege**: Restrict LLM backend access to reduce potential damage from successful injections.
- **Human approval gates**: Require explicit user confirmation for privileged or irreversible actions.
- **Segregate external content**: Use structured formats (e.g., ChatML) to separate external data from instructions.
- **Treat LLM as untrusted**: Maintain final user control; the model should never be the last authorization check.
- **Monitor inputs/outputs**: Periodic monitoring catches injection patterns before they cause large-scale damage.
- **Attack example — unauthorized purchase**: Rogue instructions embedded in e-commerce plugin content trigger purchases without user consent.
- **Attack example — email deletion**: Injected instruction in a summarized webpage silently triggers LLM plugin to delete user emails.
- **Attack example — resume fraud**: Hidden injection in a candidate's resume causes the LLM to falsely endorse them.

## 🧠 First Principles & Mental Models

- **[[Defense in Depth]]**: No single mitigation eliminates prompt injection; layering least-privilege access, human approval gates, content segregation, and monitoring limits blast radius even when injection succeeds.
- **[[Confused Deputy Problem]]**: The LLM acts as a privileged deputy on behalf of the user — indirect injection exploits this by impersonating a trusted principal through external data, causing the deputy to act against the user's interests.

## 🃏 Review Questions

**Q1**: What is the core mechanism that makes prompt injection possible in LLM applications?
**A**: LLMs cannot reliably distinguish trusted developer instructions from adversarial text injected via crafted inputs, so attackers can redirect or override model behavior through any input channel the model processes.

**Q2**: How does indirect prompt injection differ from direct injection, and what makes it particularly dangerous in agentic systems?
**A**: Indirect injection embeds malicious instructions in external content (web pages, files, emails) rather than in the user's direct input; in agentic systems, this is dangerous because the LLM autonomously retrieves and acts on that content — enabling silent, user-unaware actions like email deletion or unauthorized purchases.

**Q3**: What are the two most important architectural mitigations OWASP recommends for limiting prompt injection impact?
**A**: Apply least privilege to LLM backend access so a successful injection has limited scope, and require human approval for privileged operations so the model cannot take irreversible actions autonomously.
