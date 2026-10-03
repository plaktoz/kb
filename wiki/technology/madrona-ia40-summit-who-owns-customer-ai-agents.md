---
type: literature-note
source_url: https://www.geekwire.com/2026/the-biggest-unresolved-question-in-ai-right-now-and-more-takeaways-from-madronas-ia40-summit/
author: Todd Bishop
tags: [ai-agents, madrona-ia40, agentic-commerce, enterprise-ai-adoption]
date_consumed: 2026-10-03
---

## Summary

At [[Madrona Venture Group]]'s 2026 [[IA40 Summit]] in Seattle, executives from [[Microsoft]], [[Amazon]], [[Anthropic]], and [[Stripe]] largely agreed on AI's direction but left one question unresolved: once an [[AI Agents|AI agent]] sits between a company and its customer, who keeps the relationship and the data it generates? Speakers also agreed that humans and organizations, not the technology, are now the main bottleneck, with very few companies matching the productivity gains of early adopters. Funding is heavily concentrated: [[OpenAI]], Anthropic, and [[Databricks]] account for 92% of the $410B raised by IA40 companies.

## Core Concepts

- **[[Agentic Commerce]]**: AI agents shopping for users strip merchants of checkout upsells and ad impressions; Stripe saw agent-driven commerce flat for 8–9 months, then rise sharply in the past six weeks.
- **[[Thin Apps]]**: [[Charles Lamanna]] (Microsoft) and [[Jean-Denis Greze]] (Town) argue that business software will mostly be used by AI assistants on a person's behalf. Apps become briefly opened "thin" units with less pricing power.
- **[[Computer-Use Agents]]**: Greze says AI has operated browsers and computers nearly as well as a person, at a reasonable cost, since about July. Agents can work through an app's UI without needing an API.
- **[[Agent Data Ownership]]**: Moderator [[Raphaëlle d'Ornano]] asked who owns the record of an agent's work, including mistakes and corrections. Anthropic CTO [[Rahul Patil]] dodged, saying providers "will use every data that's available to them."
- **[[AWS Context]]**: An AWS service announced in June that maps relationships in company data for agents. [[Swami Sivasubramanian]] expects this kind of service to be a building block for the next 20 years, as cloud storage and databases were.
- **[[Human Bottleneck in AI Adoption]]**: Anthropic writes ~200x more code than 18 months ago. [[Archana Vemulapalli]] (Goldman Sachs) says roles and processes built before AI are now the constraint.
- **[[Vendor Lock-in]] debate**: Patil argues that hedging across AI providers forces "least common denominator" builds. [[Carlos Guestrin]] (Noeri) and [[Thomas Dohmke]] (Entire) push for ownership and choice.
- **[[AI Guardrail Systems]]**: Pairing a model with separate systems that check its work against company rules keeps the model's creativity while catching violations. [[Zico Kolter]] says controllability must keep pace with capability.
- **[[Amazon AgentCore]]**: Amazon's own agent-runtime product, which overlaps with [[Claude Managed Agents]]. That week Amazon also launched a managed agents product with OpenAI, showing a [[Multi-Model Strategy]].

## Key Takeaways

- **Unresolved question**: who keeps the customer relationship and data once agents intermediate.
- **Platform conflict**: Amazon blocked [[Muse AI Agent|Meta's Muse]] from shopping on its site last month.
- **Stripe signal**: agentic commerce flat for 8–9 months, then sharp six-week rise.
- **Anthropic output**: ~200x more code than 18 months ago; customers at 2–3x at most.
- **McKinsey data**: 40% of companies report AI profit gains; only 6% call them substantial.
- **Deployment friction**: Amazon agents built in 2–3 weeks stall on security, identity, monitoring.
- **Capital concentration**: IA40 companies raised $410B; OpenAI, Anthropic, Databricks hold 92%.
- **Anthropic raise**: $143B of $161B total in 12 months to Aug. 15.
- **Anthropic IPO**: filed confidentially, reportedly seeking ~$2T valuation (Reuters).
- **Big Tech capex**: projected up 74% this year to ~$742B (PitchBook).
- **Heavy users**: top Microsoft developers on track to spend more than $1M/year each on AI usage.

## 🧠 First Principles & Mental Models

- **[[Aggregation Theory]]**: Whoever owns the user relationship captures value and commoditizes suppliers. AI agents in the middle turn software makers and merchants into "thin" interchangeable suppliers, so the fight is over who owns the customer and their data.
- **[[Theory of Constraints]]**: A system's throughput is set by its tightest constraint. With AI capability no longer the limit, organizational roles, processes, and security reviews are the binding constraint, which explains why gains lag Anthropic's own.

## 🃏 Review Questions

**Q1**: What was the biggest unresolved question at Madrona's IA40 Summit?
**A**: Who keeps the relationship with the customer, and the data that comes from it, once an AI agent sits between a company and its customers. Anthropic's CTO did not answer directly when asked who owns the record of an agent's work.

**Q2**: What evidence did speakers give that humans, not AI, are now the bottleneck?
**A**: Anthropic writes about 200x more code than 18 months ago, while most customers have only doubled or tripled their output. McKinsey found that only 6% of companies report substantial AI profit gains, and Amazon teams' agents stall on security, identity, and monitoring before rollout.

**Q3**: What trade-off should an enterprise weigh when deciding whether to depend on one AI provider?
**A**: Patil argues that keeping the option to switch forces "least common denominator" builds and pulls engineers away from work that sets the company apart. Guestrin and Dohmke counter that companies should own their AI systems and keep choice rather than ceding control to one lab.
