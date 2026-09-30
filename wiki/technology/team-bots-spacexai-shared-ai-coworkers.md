---
type: literature-note
source_url: https://x.ai/news/team-bots
author: xAI
tags: [ai-agents, xai, grok, shared-team-agents]
date_consumed: 2026-09-29
---

## Summary

SpaceXAI launched Team Bots, shared [[Grok]]-based AI coworkers built around a role or workflow that an entire team draws on rather than each person having a separate agent. Each Bot combines context, plugins, credentials, and persistent memory, and SpaceXAI reports using them internally across Sales, Engineering, Marketing, and Data Analytics to ship faster with fewer people.

## Core Concepts

- [[Team Bots]] — SpaceXAI's shared, role-based AI coworker product, in public beta today on Teams and Enterprise plans
- [[Grok Bot]] — SpaceXAI's earlier individual persistent background agent; Team Bots extends the same underlying agent to a team-shared, memory-persistent role rather than a single user
- [[Shared Team Agents]] — the broader design pattern of scoping an agent to a team role instead of an individual, so institutional knowledge and upkeep are centralized
- [[Agent Memory]] — Team Bots retain per-user private context while sharing team-level skills and learned corrections across everyone who uses the Bot
- [[Harper (insurance company)]] — customer case study that built a Team Bot in 24 hours to find lapsed policies, saving customers over $120,000

## Key Takeaways

- **Four building blocks**: every Team Bot combines context, plugins, credentials, and memory.
- **Privacy model**: conversations stay private per user; skills and memory are still shared team-wide.
- **Slack-native**: each Bot has its own Slack handle and can be invited into channels.
- **Internal dogfooding**: a 5-person SpaceXAI team shipped 100+ PRs/day using an Engineering Team Bot.
- **Customer proof point**: Harper automated lapsed-policy checks across 3 platforms, saving $120,000+.
- **Availability**: public beta today on Teams and Enterprise plans, with pre-built Bots for sales, product, marketing, and data.

## 🧠 First Principles & Mental Models

- **[[Economies of Scale]]**: Centralizing an agent's context, credentials, and learned memory at the team-role level instead of duplicating them per person spreads the fixed cost of upkeep across everyone who touches that role — the same efficiency logic Every reached independently with its "Plus One 2.0" redesign.

## 🃏 Review Questions

**Q1**: What is the core claim of this article?
**A**: SpaceXAI is launching Team Bots, shared AI coworkers built around a team's role or workflow that combine context, plugins, credentials, and memory, rather than giving each employee a separate personal agent.

**Q2**: What concrete evidence does SpaceXAI cite for Team Bots' effectiveness?
**A**: A five-person internal team used an Engineering Team Bot to orchestrate hundreds of Cloud Agents and ship more than 100 PRs a day, while customer Harper built a Team Bot in 24 hours that saved customers over $120,000 by automating lapsed-policy checks.

**Q3**: How does the Team Bots design address a known failure mode of personal AI agents?
**A**: By sharing memory, credentials, and skills at the team level while keeping individual conversations private, Team Bots avoid the siloed upkeep and knowledge loss that occurs when a single employee "owns" a personal agent and later leaves.
