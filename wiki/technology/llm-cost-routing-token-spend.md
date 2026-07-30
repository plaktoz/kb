---
type: literature-note
source_url: https://blog.bytebytego.com/p/token-spend-out-of-control-the-case
author: ByteByteGo
tags: [llm-routing, agent-cost, token-spend, model-routing]
date_consumed: 2026-07-29
---

## Summary
LLM agents burn far more tokens than single chatbot queries because they loop, resending growing context on every call, and often default to the most expensive frontier model. [[Model Routing]] cuts cost by sending each request to the cheapest model capable of handling it, based on a case study of [[Kilo Gateway]] in production. Kilo found routing on a known signal (agent mode) cut average cost per request by about a third, and tier choice mattered more than caching.

## Core Concepts
- **[[Model Routing]]** — deciding which model handles a given request, separate from the entry-point problem of talking to many providers.
- **[[Kilo Gateway]]** — a unified request layer in front of 500+ models, used by the [[Kilo]] open-source coding agent to route by task mode (planning, editing, debugging).
- **[[Frontier Model]]** pricing — top models can cost 10x+ more per token than small models for comparable work.
- **[[Agent Loop]]** — the core cost multiplier: context grows every step and calls fire without a human "brake."
- **[[Prompt Caching]]** — reduces repeated-context cost but does not solve volume growth on its own; Kilo found spend stayed high even with 80%+ cache reuse.
- **[[RouteLLM]]** and the UC Berkeley/Anyscale routing study — cited as evidence routing can cut cost ~50% while retaining 95% of frontier quality.

## Key Takeaways
- 80–90% of Kilo's production requests didn't need a frontier model.
- Routing on a known task signal (mode) beats predicting difficulty from raw text.
- Tier choice mattered more than caching: balanced tier cost 10x less per request than top tier.
- Routing across model families can lose intermediate reasoning tokens mid-task.
- Treat AI spend like infrastructure cost: set a fixed budget, not a lowest-price-per-request target.
- Log tokens per request tagged by task type, not by product feature, to find real cost drivers.
