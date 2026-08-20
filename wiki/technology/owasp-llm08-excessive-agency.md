---
type: literature-note
source_url: https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM08_ExcessiveAgency.md
author: OWASP
tags: [llm-security, owasp, ai-agents, least-privilege]
date_consumed: 2026-08-20
---

## Summary

OWASP LLM08 defines Excessive Agency as a vulnerability where an LLM-based system can perform damaging actions due to being granted more functionality, permissions, or autonomy than its intended operation requires. The root causes are excessive functionality (unnecessary plugins/tools), excessive permissions (overly broad access rights), and excessive autonomy (no human approval for high-impact actions). Unlike Insecure Output Handling, this vulnerability is about what an LLM agent is empowered to do, not just what it outputs.

## Core Concepts

- **[[Excessive Agency]]** — the vulnerability class enabling an LLM to take damaging actions beyond intended scope
- **[[Principle of Least Privilege]]** — the foundational defense: grant only the minimum functionality, permissions, and autonomy needed
- **[[Prompt Injection]]** — a key trigger for Excessive Agency exploits; malicious inputs can hijack over-permissioned agents
- **[[Human-in-the-Loop]]** — requiring human approval before high-impact actions are executed
- **[[Confused Deputy Problem]]** — when an LLM agent with broad permissions is manipulated into acting against its principal's interests
- **[[OAuth]]** — recommended for scoped authentication in downstream system integrations
- **[[Rate Limiting]]** — a damage-limiting control when full prevention is not feasible
- **[[Complete Mediation Principle]]** — all downstream requests via plugins should be validated against security policies

## Key Takeaways

- **Three root causes**: Excessive functionality, excessive permissions, excessive autonomy.
- **Least functionality**: Offer agents only the plugins/tools strictly required for intended operation.
- **Minimal plugin scope**: Implement only necessary functions within each plugin (e.g., read-only email, no send).
- **Avoid open-ended tools**: Prefer specific-purpose plugins over generic ones like shell-execute or fetch-URL.
- **Least-privilege access**: Grant database/API identities only the minimum permissions (e.g., SELECT, not INSERT/UPDATE/DELETE).
- **User-scoped credentials**: Use per-user OAuth tokens, not shared high-privileged service accounts.
- **Human approval gates**: Require user confirmation before irreversible or high-impact actions.
- **Downstream authorization**: Enforce access control in downstream systems, not inside the LLM.
- **Logging and monitoring**: Detect undesirable actions after the fact when prevention is incomplete.
- **Rate limiting**: Slow damage accumulation and increase detection window.

## 🧠 First Principles & Mental Models

- **[[Principle of Least Privilege]]**: Granting an LLM agent only the minimum access it needs is the direct application of least privilege — this is the primary mitigation for all three root causes of Excessive Agency.
- **[[Confused Deputy Problem]]**: An over-permissioned LLM agent becomes a confused deputy when manipulated via prompt injection — it acts with its own broad credentials in ways the legitimate principal never intended.

## 🃏 Review Questions

**Q1**: What is Excessive Agency in the context of LLM systems, and what are its three root causes?
**A**: Excessive Agency is a vulnerability where an LLM can take damaging actions beyond its intended scope. The three root causes are excessive functionality (unnecessary plugins/tools), excessive permissions (overly broad access rights), and excessive autonomy (no human approval for high-impact actions).

**Q2**: How does a prompt injection attack exploit Excessive Agency, using the email plugin example?
**A**: A maliciously crafted incoming email tricks the LLM into calling the plugin's "send message" function — an ability that exists because the plugin has more functionality than needed for summarization. The exploit is possible only because the plugin was not restricted to read-only operations.

**Q3**: What is the recommended approach to authorization when building LLM plugins that interact with downstream systems?
**A**: Authorization should be enforced in the downstream systems themselves (not left to the LLM to decide), applying the complete mediation principle so every plugin request is validated against security policies; user actions should also be executed under per-user, minimum-scope credentials rather than shared high-privileged accounts.
