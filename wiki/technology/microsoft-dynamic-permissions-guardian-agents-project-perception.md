---
type: literature-note
source_url: https://www.helpnetsecurity.com/2026/10/20/microsofts-ai-agents-threats-guardian-agents
author: Anamarija Pogorelec
tags: [ai-agents, security, microsoft, least-privilege]
date_consumed: 2026-10-21
---

## Summary
Microsoft announced Guardian Agents and Playbooks as extensions of Project Perception, wrapping non-deterministic AI agents in deterministic controls. New Dynamic Permissions, Dynamic Agent Risk and Dynamic Conditional Access grant agents only task-scoped authority and tighten it as risk rises. Humans retain control over objectives and consequential decisions.

## Core Concepts
- [[Guardian Agents]]: agents that explain risk changes, investigate evidence, and recommend or apply containment.
- [[Project Perception]]: Microsoft's agentic security system, sharing signals and a unified registry with [[Microsoft Agent 365]].
- [[Microsoft Entra Agent ID]]: gives agents identities distinct from the people sponsoring them.
- [[Dynamic Permissions]]: task-scoped, time-limited authority within organization-wide policy.
- [[Dynamic Agent Risk]]: continuously updated risk score combining identity, data, endpoint, cloud, network and activity signals.
- [[Dynamic Conditional Access]]: risk-driven restrictions from blocking writes up to isolating or stopping the runtime.
- [[Model Context Protocol]]: one of the connections (with tools, APIs, data, other agents) that must be monitored.
- [[Satya Nadella]]: argues frontier models should be treated like insider risks.

## Key Takeaways
- **Four Duties**: Know, contain, protect and adapt govern each agent.
- **Discovery**: Support expands by 35 types to 60 local agents, including Claude Code and Codex.
- **Agent Identity**: Separate identities distinguish a person's actions from an agent's.
- **Task-Scoped Access**: Agents get only needed authority, which shrinks or expires with the task.
- **Residual Risk**: Least privilege still misses malicious instructions hidden in external documents.
- **Graduated Response**: Preserve reads, block writes, narrow access, require approval, then isolate.
- **Expense Example**: A drifting expense agent loses approval rights but keeps review rights.
- **Scale**: Microsoft already operates hundreds of thousands of agents internally.

## 🧠 Core Principles

**T1. Grant only the authority a task needs** — An actor should hold the minimum access for the shortest time its task requires, and that access should lapse when the task ends. · *model:* [[Principle of Least Privilege]]
→ explains: Task-Scoped Access, Agent Identity

**T2. Static permissions cannot contain a drifting actor** — Correct initial access does not prevent misuse once behavior changes, so controls must respond continuously to observed risk with graduated restrictions.
→ explains: Residual Risk, Graduated Response, Expense Example

## 🃏 Review Questions

**Q1**: What is Microsoft's overall approach to securing AI agents?
**A**: It surrounds non-deterministic intelligence with deterministic controls, independent evidence and containment boundaries, organized around know, contain, protect and adapt.

**Q2**: Why does Microsoft add Dynamic Agent Risk on top of Dynamic Permissions?
**A**: Least privilege does not remove risk, since an agent with proper access could follow a malicious instruction hidden in a document. Continuously updated risk lets Dynamic Conditional Access tighten restrictions as behavior drifts.

**Q3**: How would the system respond to a compromised expense-processing agent?
**A**: It could remove the agent's permission to approve expenses while preserving review access, and escalate to isolation or stopping the agent if risk rises further.
