---
source_url: https://docs.typesafe.ai/introduction/quickstart
author: Unknown
date: 2026-09-26
---

# Quick Start — TypeSafe AI

## Playground

1. Open [console.typesafe.ai/playground](https://console.typesafe.ai/playground)
2. Paste text as state
3. Add questions using `noul`, `choice`, or `score` types

## API

**Endpoint:** `POST https://api.typesafe.ai/v1/systemone`
**Auth:** `Authorization: Bearer <API_KEY>`

Request requires three fields: `state` (your text), `model` (e.g. `jev-latest`), and `questions` (a map of named question objects).

Each question has a `type`:
- **`noul`** — yes/no float (0–1)
- **`choice`** — picks from labeled criteria
- **`score`** — rates along a scale of described levels

Responses include `answers` (typed results with confidence/probabilities) and `usage` (token counts).

## Python SDK

```bash
pip install typesafe-sdk
```

Reads `TYPESAFE_API_KEY` from the environment. Call `client.system_one(state=..., questions={...})` and access results via `response.answers["key"].choice` / `.score` / `.noul`.

## Agent Skill (Claude Code)

```bash
claude plugin marketplace add typesafe-ai/skills
claude plugin install typesafe@typesafe-ai
```

For other agents: `npx skills add typesafe-ai/skills --skill typesafe-ai`

Skill reference: [github.com/typesafe-ai/skills](https://github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md)
