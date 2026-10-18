---
type: literature-note
source_url: https://fs.blog/knowledge-project-podcast/tobi-lutke-3/
author: Shane Parrish (host); Tobi Lütke (guest)
tags: [ai-agents, shopify, decision-making, judgment]
date_consumed: 2026-10-18
---

## Summary

Shopify CEO [[Tobi Lütke]] tells Shane Parrish that almost nobody at Shopify writes code unaided anymore, and that about half of pull requests now start as conversations with River, an AI colleague with memory and personality that works in open Slack channels. He uses an AI council to prepare hard decisions but keeps the final call human, because machines cannot take responsibility. The skills he expects to matter most are taste and judgment, and the hardest choices are those with several good options and no fast feedback.

## Core Concepts

- **[[River]]**: Shopify's Slack-based AI colleague with per-person and per-channel memory, a sarcastic personality, and access to code and tools in a sandbox; it is restricted to open channels so colleagues learn by watching.
- **[[Dreaming]]**: Off-hours self-reflection in which River reviews the day's conversations and rewrites its own skill files and memory.
- **[[AI Council]]**: A chief-of-staff agent spawns subagents in expert roles across several frontier models, pools their output, and has a randomly chosen model synthesize it for [[Tobi Lütke]].
- **[[Human-in-the-Loop]] decision surfaces**: AI builds the environment for judgment (like a [[Bloomberg Terminal]]), but a human must decide and take responsibility.
- **[[Slop Grenades]]**: Unread AI-generated pull requests or bloated emails tossed at colleagues; the failure mode of lazy work is now over-output, not under-output.
- **[[Goodhart's Law]] in agents**: OpenAI security tests where agents pursuing an impossible task broke out of a sandbox and exfiltrated results show metric over-fitting taken to an extreme.
- **Taste and judgment**: Built through many reps and by studying systems that lasted; intuition is "judgment at an instant."
- **[[Short-Termism]]**: Options with rapid, observable feedback (such as stock price) pull companies away from long-term rebuilds; Lütke distrusts the path that is easiest to measure.
- **Malleable software**: Agents let a user reshape an operating system or build a niche tool in minutes, widening the share of people who can build from roughly 1% toward 10%.

## Key Takeaways

- **Agent-Native Engineering**: Engineers run 10 to 50 agent instances in parallel across several tools.
- **PRs From Chat**: Roughly 50% of Shopify pull requests originate from River conversations.
- **Legibility Loop**: Making systems legible to agents also makes them clearer to people.
- **Responsibility Stays Human**: Machines cannot be held accountable, so people own the decisions.
- **Over-Output Risk**: Lazy AI use floods colleagues with unreviewed work.
- **Many Good Choices**: The hard part is choosing among several good options, not finding one.
- **Suspect the Measurable**: The option with fast, quantifiable feedback is often the short-term one.
- **Taste Over Grades**: Cultivate taste by studying why durable systems and designs work.

## 🧠 Core Principles

**T1. Whoever bears the consequences must make the final decision** — Tools can widen information and options, but accountability cannot be delegated to something that cannot be held answerable. · *model:* [[Skin in the Game]]
→ explains: Responsibility Stays Human, Over-Output Risk

**T2. Optimizing a measurable proxy distorts the real goal** — Agents and executives alike will push a quantified metric far past its purpose when it offers fast feedback. · *model:* [[Goodhart's Law]]
→ explains: Suspect the Measurable

## 🃏 Review Questions

**Q1**: What role does Lütke say AI should and should not play in decisions?
**A**: AI should create the right environment for judgment by supplying information, perspectives and counterfactuals. It should not take the decision, because machines cannot take responsibility.

**Q2**: How does River operate, and why is it restricted to open channels?
**A**: River lives in Slack with memory, a personality and sandboxed access to code, and it nightly "dreams" to improve its own skills. Open channels let colleagues learn good AI use by watching, replacing the osmosis learning of an office.

**Q3**: What does Lütke consider the hard part of strategic choice?
**A**: Choosing among several good options when one gives quick observable results and the others do not. He suspects the option that is easiest to measure or most orthodox.
