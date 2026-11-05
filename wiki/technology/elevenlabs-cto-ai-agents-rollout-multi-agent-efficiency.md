---
type: literature-note
source_url: https://fortune.com/2026/11/04/waters-new-ai-tool-targets-one-of-the-pharmaceutical-industrys-most-tedious-tasks-2
author: John Kell
tags: [ai-agents, elevenlabs, enterprise-ai, multi-agent-systems]
date_consumed: 2026-11-06
---

## Summary
ElevenLabs field CTO Alex Holt describes deploying AI agents across sales, recruiting, and internal support while keeping the same business metrics as before. He expects bigger efficiency gains as the company moves toward multi-agent systems with shared context and handoffs, backed by a human-led monitoring layer.

## Core Concepts
- [[Alex Holt]]: Field CTO of [[ElevenLabs]], previously five years at [[Palantir Technologies]].
- [[Agentic AI]]: Agents handle sales leads, sales coaching, first-round recruiting interviews, and internal Slack questions.
- [[Multi-Agent Systems]]: Next frontier; agents share context and hand off complex work, as when an SDR agent and an account executive agent closed a sale.
- [[Forward Deployed Engineers]]: An engineer sits on every team; each group has fewer than 10 people.
- [[Agent Monitoring and Guardrails]]: Human-led observation layer that governs agents and turns errors into test cases.
- [[BCG]]: Research putting agentic AI's share of AI value at 17% in 2025, 22% in 2026, and 39% by 2030.

## Key Takeaways
- **SDR Agent**: Handled over 3,000 leads this year, qualifying over 90% in 32 languages.
- **Same Metrics**: Business units own the goals; agents are just a tool to hit them.
- **Recruiting Agent**: Screens nearly all candidates, freeing recruiters' 30 minutes for closing.
- **Multi-Agent Handoff**: A customer closed a sale entirely via an SDR agent and an account executive agent.
- **Slow Metrics**: Hiring quality and satisfaction scores lag, so business owners pick leading indicators.
- **Error Handling**: A wrongly issued sub-$30 refund became a simulated test case plus updated guardrails.
- **Data Dividend**: Tracking every agent decision exposes mistakes a human equivalent would hide.
- **Readiness Gap**: Most surveyed businesses are ill-prepared to orchestrate multi-agent processes.

## 🧠 Core Principles

**T1. Slow outcomes need proxies** — When the real outcome of a change takes a long time to show up, you must pick earlier signals to steer by. Holt leans on business owners to identify leading indicators because metrics like hiring quality take a long time. · *model:* [[Leading vs. Lagging Indicators]]
→ explains: Slow Metrics, Same Metrics

**T2. Observed failures improve the system** — Recording each decision and replaying a failure as a test makes the error a permanent improvement rather than a repeated one. The refund mistake was simulated and the prompts and guardrails updated. · *model:* [[Feedback Loops]]
→ explains: Error Handling, Data Dividend

## 🃏 Review Questions

**Q1**: What is Holt's core claim about ElevenLabs' use of AI agents?
**A**: Agents already deliver efficiency gains across sales, recruiting, and internal support, and he expects even more in six months, particularly through multi-agent systems. The business metrics stay exactly the same, and business units drive the initiative.

**Q2**: What evidence shows the SDR agent works, and how did a multi-agent sale happen?
**A**: The SDR agent handled over 3,000 leads this year and qualified over 90% in 32 languages with no human intervention. One customer closed a sale entirely through the SDR agent plus an account executive agent that handled legal documents and contracts.

**Q3**: How does ElevenLabs handle agent mistakes, and what does that imply for others?
**A**: A human-led monitoring layer catches errors, and a wrong refund was turned into a simulated test case and updated guardrails. Tracking every agent decision also yields data that would be invisible with human mistakes.
