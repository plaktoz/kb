---
type: literature-note
source_url: https://blog.bytebytego.com/p/token-spend-out-of-control-the-case
author: ByteByteGo
tags: [llm-routing, token-optimization, ai-agents, cost-management]
date_consumed: 2026-08-01
---

## Summary

LLM agents are expensive because they run in loops, resend growing context on every step, and default to the most expensive frontier models. Routing — directing each request to the cheapest model capable of handling it — cuts costs by 40–70% with minimal quality loss, as demonstrated by [[Kilo]] (an open-source coding agent) whose production data shows routing alone saved ~$87,000 in a single quarter. As agents grow more autonomous and run longer loops, routing is shifting from a nice-to-have optimization to a foundational requirement for making ambitious agents economically viable.

## Core Concepts

- **[[LLM Token Routing]]**: Directing each request to the cheapest model that can handle it — the core strategy for agent cost control.
- **[[Frontier Models]]**: The most capable (and expensive) LLMs; routing minimizes reliance on them for routine tasks.
- **[[Agent Loop Cost]]**: Agents resend the full growing context on every step, causing per-call costs to compound rapidly.
- **[[Kilo Gateway]]**: Kilo's open-source routing layer that normalizes requests across 500+ models and routes by task mode (planning, editing, debugging, etc.).
- **[[RouteLLM]]**: Shared routing infrastructure used across tools like [[Cursor]], [[Cline]], [[Aider]], and [[OpenRouter]].
- **[[Context Window Growth]]**: Each agent turn adds tool calls, results, and thinking to the context — cost rises with every step.
- **[[Prompt Caching]]**: Reuses repeated context to avoid re-paying for it; Kilo found caching alone insufficient when request volume is high.
- **[[Tiered Model Selection]]**: Organizing models into cost tiers (top, balanced, free, background) and mapping task modes to tiers.

## Key Takeaways

- **Cost multiplier**: Frontier models cost 10x+ more per token than small models.
- **Context explosion**: Agent context can grow from thousands to 100k+ tokens across a loop.
- **No human brake**: Agents fire requests as fast as software allows — no natural throttle.
- **Routing savings**: UC Berkeley/Anyscale study shows 50% cost cut with 95% quality retained.
- **Kilo's result**: 80–90% of requests don't need frontier models; routing cut avg cost per request by ~33%.
- **Tier gap**: Balanced tier costs 10x less than top tier for identical coding work.
- **Caching is not enough**: Even with 80%+ cache reuse, total spend stays high due to volume and uncacheable context.
- **Route on existing signals**: Task type (planning vs. edit) is a free, reliable routing signal — prefer it over classifiers.
- **Measure by tokens, not requests**: Token count per feature group reveals true spend drivers.
- **Budget framing**: Lower per-token cost drives more usage; set a fixed total budget instead.
- **Mid-task model switching**: Switching model families drops intermediate reasoning context, slightly reducing quality.

## First Principles & Mental Models

- **[[Jevons Paradox]]**: Cutting per-token cost via cheaper models tends to increase total usage — so total spend climbs even as unit price falls, which is why a fixed budget beats chasing the lowest rate.
- **[[Pareto Principle]]**: 80–90% of agent requests are routine and cheap to serve; targeting that majority with cheaper models captures most of the savings for minimal quality tradeoff.
