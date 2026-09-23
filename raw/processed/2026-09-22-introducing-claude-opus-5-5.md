---
source_url: https://www.anthropic.com/claude-opus-5-5
author: Anthropic
date: 2026-09-22
---

# Introducing Claude Opus 5.5

Anthropic released Claude Opus 5.5, the first model in their 5.5 family. It matches Claude Fable 5.1 performance on most tasks while costing 40% less than Opus 5.

## Performance Highlights

- Completed a 680,000-line code migration in under one day
- Successfully cut load times on a web app 39 out of 40 attempts (vs. Opus 5's smaller, behavior-altering changes)
- Leads benchmarks in agentic coding, computer use, and knowledge work

## Pricing (per 1M tokens)

| Token Type | Opus 5.5 | Opus 5 |
|---|---|---|
| Cache reads | $0.20 | $0.50 |
| Input | $4 | $5 |
| Output | $20 | $25 |

## Safety

- Best scores on Anthropic's automated behavioral audit (~2,000 scenarios)
- ~85% fewer containment boundary violations vs. Opus 5
- Launches with biology and cybersecurity safeguards matching Fable 5.1
- Includes "preserved thinking" anti-distillation measures

## Communication

Opus 5.5 was redesigned for clarity — leads with key information, avoids jargon, and follows user-defined writing rules. Early testers noted it "writes like a good colleague."

## Availability

Available now on AWS, Google Cloud, Microsoft Azure, and the Claude Platform (`claude-opus-5-5`).
