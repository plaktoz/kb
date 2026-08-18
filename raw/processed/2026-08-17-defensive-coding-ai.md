---
source_url: https://www.usetranscribe.io/yt/VUZpQgNaO4s/defensive-coding-ai?format=md
author: Erlend Oftedal
date: 2026-08-17
---

# Teaching Your Coding Agent Defensive Coding

## Overview

Erlend Oftedal makes the case that AI coding agents frequently generate insecure code — not out of malice, but due to fundamental limitations in how they're trained and how they reason probabilistically.

## Why AI Agents Produce Insecure Code

AI models are trained on massive amounts of internet code, much of which is insecure. Critically, that code isn't labeled — there's no distinction between safe and unsafe examples. Training reinforcement has largely prioritized *functional* code over *secure* code.

A key finding from the DORA State of AI-Assisted Development report: **AI is an amplifier**. Good practices get amplified, but so do bad ones. If your codebase already has vulnerabilities, AI will replicate and extend them.

Erlend demonstrates this with a live token-probability tool: changing something unrelated to password storage (a package name) caused SHA — a weak choice — to become the top suggested algorithm. Security decisions, in other words, can shift based on unrelated context.

## The Problem With Reactive Approaches

Many existing tools focus on *finding* vulnerabilities after code is written. Erlend argues this creates a wasteful loop: write code → make mistakes → spend tokens finding bugs → attempt fixes (which may introduce new bugs).

He also notes that prompts like "avoid vulnerabilities" or "use best practices" have limited effectiveness — they lack specificity and may pull from outdated advice the model absorbed during training.

## The Defensive Coding Skill Approach

Erlend proposes injecting security guidance *before* code is written, during the planning phase. His approach uses the **OWASP Application Security Verification Standard (ASVS)** — 345 verifications across 17 categories — as a foundation.

Rather than dumping all 345 checks into the context window, a skill retrieves *relevant* guidance based on what the agent is about to do (e.g., database queries, file uploads, authentication). This keeps context lean while ensuring timely, targeted advice.

The workflow:
1. Agent enters planning mode
2. Skill retrieves applicable ASVS guidance
3. Guidance is incorporated into the plan
4. Code is written with security context already in place

## Hooks and Self-Reminders

By observing Claude's own behavior, Erlend noticed it uses self-reminders — for example, after reading a file, it appends a note about potential malicious content. He leverages this pattern by adding hooks that trigger security reminders after file edits, prompting the agent to confirm it applied relevant guidance.

## Don't Let Agents Invent Security

A concrete cautionary example: when asked to add login functionality, Claude invented its own token format — base64-encoded strings with timestamps and usernames, but **no signatures**. The lesson: "creativity in security is not always a good choice." Skills should steer agents toward established standards like JWT rather than leaving algorithm selection to chance.

## Anthropic's Parallel Approach

Shortly before the talk, Anthropic released their own security guidance skill. It uses regex patterns to detect risky code patterns after each file edit, then injects relevant warnings. It also includes a background agent that reviews code at the end of each turn or before git commits.

Erlend appreciates the technique but prefers front-loading security thinking: catching problems after writing code still perpetuates the reactive loop he's trying to eliminate.

## Key Takeaways

- AI agents *can* produce secure code, but probabilistic behavior means they often don't
- Security guidance delivered at planning time outperforms after-the-fact scanning
- OWASP ASVS provides a solid, structured foundation for building security skills
- Avoid letting agents invent cryptographic or authentication mechanisms
- Use fast, purpose-built tools (e.g., `npm audit`) for dependency scanning rather than burning tokens on tasks they handle poorly
