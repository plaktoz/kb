---
type: literature-note
source_url: https://www.usetranscribe.io/yt/VUZpQgNaO4s/defensive-coding-ai?format=md
author: Erlend Oftedal
tags: [ai-coding-agents, security, owasp, defensive-coding]
date_consumed: 2026-08-17
---

## Summary

Erlend Oftedal argues that [[AI Coding Agents]] frequently produce insecure code because they are trained on unlabeled internet code that prioritizes functionality over security. He proposes a proactive approach: injecting targeted security guidance from the [[OWASP ASVS]] into the agent's planning phase before code is written, rather than relying on after-the-fact vulnerability scanning. The core principle is that security reasoning must be front-loaded, not retrofitted.

## Core Concepts

- **[[AI Coding Agents]]**: Probabilistic models that can amplify both good and bad practices already present in a codebase.
- **[[OWASP ASVS]]** (Application Security Verification Standard): 345 verifications across 17 categories used as a structured security foundation for agent skills.
- **[[Defensive Coding]]**: Embedding security constraints proactively at the planning stage rather than reactively after code generation.
- **[[DORA State of AI-Assisted Development]]**: Report finding that AI acts as an amplifier — good and bad practices alike get replicated and extended.
- **[[Erlend Oftedal]]**: Security researcher demonstrating live token-probability effects on algorithm selection.
- **[[Anthropic]]**: Released a parallel security guidance skill using regex-based post-edit detection and a background review agent.
- **[[JWT]]** (JSON Web Tokens): Established authentication standard agents should be steered toward instead of inventing custom token formats.

## Key Takeaways

- **AI as Amplifier**: AI replicates existing codebase patterns — vulnerabilities included.
- **Probabilistic Insecurity**: Unrelated context changes (e.g., a package name) can shift suggested crypto algorithm to weaker options.
- **Reactive Loop Problem**: Write → scan for bugs → fix → repeat wastes tokens and risks introducing new issues.
- **Front-Loading Security**: Inject [[OWASP ASVS]] guidance during planning, not after code is written.
- **Context-Lean Retrieval**: Retrieve only relevant ASVS checks per task (e.g., DB queries, auth) to keep context window efficient.
- **No Invented Crypto**: Claude invented unsigned base64 tokens for login — agents must be steered to standards like [[JWT]].
- **Self-Reminder Hooks**: Leverage agent self-reminder patterns to trigger security checks after each file edit.
- **Fast Tools for Dependency Scanning**: Use `npm audit` instead of burning LLM tokens on tasks purpose-built tools handle better.

## 🧠 First Principles & Mental Models

- **[[Goodhart's Law]]**: Training AI to produce *functional* code makes functionality the target metric — security, being unlabeled and unmeasured, gets optimized away, exactly as Oftedal documents with probabilistic insecurity.
- **[[Prevention Over Detection]]**: Catching security issues at the planning phase is categorically cheaper than finding them post-generation — the same first-principles reasoning behind shift-left security in traditional software engineering.

## 🃏 Review Questions

**Q1**: What is Erlend Oftedal's core argument about AI-generated code security?
**A**: AI coding agents produce insecure code not maliciously but because they are trained on unlabeled internet code that prioritizes functionality; security guidance must be injected proactively at the planning phase.

**Q2**: How does the token-probability demonstration illustrate the security problem?
**A**: Changing an unrelated detail (a package name) caused the model to suggest SHA — a weak algorithm — as its top choice for password hashing, showing that security decisions shift unpredictably with unrelated context changes.

**Q3**: How should teams apply this approach to prevent agents from inventing insecure mechanisms?
**A**: Build skills that retrieve relevant [[OWASP ASVS]] guidance before code is written, and explicitly steer agents toward established standards like [[JWT]] rather than allowing algorithm selection by default.
