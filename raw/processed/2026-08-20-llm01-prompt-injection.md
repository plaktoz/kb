---
source_url: https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM01_PromptInjection.md
author: Unknown
date: 2026-08-20
---
# LLM01: Prompt Injection


## Description

Prompt Injection occurs when attackers manipulate an LLM through crafted inputs, causing it to unknowingly execute malicious intentions.

**Two main forms:**
- **Direct**: "jailbreaking" — overwriting or exposing the system prompt
- **Indirect**: embedding injections in external content (websites, files) the LLM processes

## Key Vulnerability Examples

1. Crafted direct injection ignoring system prompts to return dangerous info
2. Webpage summarization triggering data exfiltration via JS/Markdown
3. Resume with embedded injection causing LLM to falsely endorse a candidate
4. Rogue instructions exploiting e-commerce plugins for unauthorized purchases

## Mitigations

1. Apply **least privilege** to LLM backend access
2. Require **human approval** for privileged operations
3. **Segregate** external content from user prompts (e.g., ChatML)
4. Treat the LLM as "an untrusted user" and maintain final user control
5. Periodically **monitor** LLM inputs/outputs

## Notable Attack Scenario

An attacker embeds injection in a webpage; when a user summarizes it, the LLM plugin "deletes the user's emails" — without any user awareness.
