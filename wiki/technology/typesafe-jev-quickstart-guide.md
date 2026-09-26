---
type: literature-note
source_url: https://docs.typesafe.ai/introduction/quickstart
author: Unknown
tags: [jev, typesafe-ai, api, developer-tools]
date_consumed: 2026-09-26
---

## Summary

The TypeSafe AI quickstart covers three entry points for using [[Jev]]: a browser playground for instant experimentation, a REST API for direct integration, and a Python SDK for production code. Authentication requires a single API key from the console, and the core call pattern is the same across all three: pass `state` (your text), a `model` name, and a map of typed `questions`.

## Core Concepts

- **[[TypeSafe AI]] console** — `console.typesafe.ai/playground` for interactive experimentation without writing code
- **REST endpoint** — `POST https://api.typesafe.ai/v1/systemone` with `Authorization: Bearer <API_KEY>`; request body has `state`, `model`, `questions`
- **[[Jev]] model name** — use `jev-latest` as the model identifier
- **Question types**: `noul` (yes/no float 0–1), `choice` (categorical selection), `score` (rated scale)
- **Python SDK** — `pip install typesafe-sdk`; reads `TYPESAFE_API_KEY` from environment; call `client.system_one(state=..., questions={...})`
- **Agent Skill** — `claude plugin marketplace add typesafe-ai/skills` for Claude Code integration; enables natural-language TypeSafe workflow authoring

## Key Takeaways

- **Three entry points**: playground (no code), REST API (any language), Python SDK (production Python)
- **Auth**: single `TYPESAFE_API_KEY` environment variable — set once, works across all clients
- **Model**: `jev-latest` is the current production model identifier
- **Answer access**: `response.answers["key"].choice` / `.score` / `.noul`
- **Agent integration**: Claude Code plugin available for AI-assisted TypeSafe workflow design
- **Docs index**: `https://docs.typesafe.ai/llms.txt` for full reference

## 🃏 Review Questions

**Q1**: What are the three ways to start using Jev, and which requires no code?
**A**: Browser playground at `console.typesafe.ai/playground` (no code), REST API at `https://api.typesafe.ai/v1/systemone`, and Python SDK via `pip install typesafe-sdk`. The playground requires no code.

**Q2**: What three fields does every Jev API call require?
**A**: `state` (the input text), `model` (e.g. `jev-latest`), and `questions` (a map of named question objects with type and instructions).

**Q3**: How does the Claude Code agent skill extend the quickstart experience?
**A**: Installing `typesafe-ai/skills` lets you describe TypeSafe workflows in natural language and have Claude Code generate the implementation; invoke explicitly with `/typesafe:typesafe-ai`.
