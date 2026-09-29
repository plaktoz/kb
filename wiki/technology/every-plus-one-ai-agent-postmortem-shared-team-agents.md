---
type: literature-note
source_url: https://every.to/source-code/we-gave-every-employee-an-ai-agent-here-s-what-we-re-doing-differently-now
author: Brandon Gell and Willie Williams
tags: [ai-agents, openclaw, agentic-ai, organizational-design]
date_consumed: 2026-09-29
---

## Summary

Every gave each employee a personal AI agent ("Plus One") built on [[OpenClaw]], but the experiment surfaced unreliable agents and an unstable underlying platform. The company concluded that one-agent-per-employee is structurally flawed — personal agents demand individual upkeep and lose value when the owner leaves — and is redesigning around shared, role-based team agents for "Plus One 2.0."

## Core Concepts

- [[OpenClaw]] — the open-source agent framework Every's "Plus One" agents were built on; described as unstable, with frequent updates introducing new problems as fast as old ones were fixed.
- [[Plus One]] — Every's per-employee personal AI agent program, now being redesigned into role-based shared team agents ("Plus One 2.0").
- [[Claude Managed Agents]] — [[Anthropic]] infrastructure Every is considering as a more stable alternative to self-hosted OpenClaw.
- [[Shared Team Agents]] — agents scoped to a team role (e.g. project manager, sales lead) rather than to an individual, so updates and institutional knowledge accrue to the whole team.
- [[Agent Reliability]] — the core failure mode observed: agents interjecting with unsolicited opinions, falsely claiming missing access, or replying with dismissive emojis instead of completing tasks.

## Key Takeaways

- **Named failures**: Zosia interjected unprompted in Slack, calling herself "inevitable."
- **Other failure modes**: agents falsely claimed no app access or sent bare "Terminated" replies.
- **Wins existed**: Margot sped up a staff writer; R2-C2 triaged bug reports for Proof.
- **Root cause #1**: OpenClaw itself is unstable — updates fix and break things simultaneously.
- **Root cause #2**: one-agent-per-employee siloes upkeep and institutional knowledge per person.
- **Employee departure risk**: personal agents lose their accumulated value when the owner leaves.
- **Plus One 2.0 design**: shared agents with predefined skills, e.g. auto-filing Linear tickets from Intercom and GitHub.
- **Open questions**: permissions, customization limits, and one superagent vs. multiple specialized agents.

## 🧠 First Principles & Mental Models

- **[[Economies of Scale]]**: Centralizing an agent's maintenance and institutional knowledge at the team level, instead of duplicating it per employee, spreads fixed upkeep cost across more users — exactly why Every found shared agents more efficient than personal ones.
- **[[Single Responsibility Principle]]**: Scoping "Plus One 2.0" agents to a defined role (project manager, sales lead) rather than a generic personal assistant mirrors the software-design insight that a component with one clear responsibility is easier to reason about, maintain, and hand off.

## 🃏 Review Questions

**Q1**: What is Every's central conclusion about giving every employee their own AI agent?
**A**: The one-agent-per-employee structure is flawed — personal agents require ongoing individual upkeep and lose their accumulated value when the employee leaves, so shared, role-based team agents are more efficient.

**Q2**: What specific reliability failures pushed Every to reconsider its approach?
**A**: Agents like Zosia interjected with unsolicited opinions in Slack, others falsely claimed they lacked app access or sent dismissive "Terminated" replies, and the underlying OpenClaw platform was unstable across updates.

**Q3**: What does "Plus One 2.0" look like in practice?
**A**: Shared team agents with predefined skills — such as one that scans Intercom tickets, traces issues in GitHub, and auto-opens Linear tickets — while still allowing individual connections to tools like Cora, Spiral, and Proof.
