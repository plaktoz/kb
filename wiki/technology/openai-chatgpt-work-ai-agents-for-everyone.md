---
type: literature-note
source_url: https://techcrunch.com/2026/08/24/openai-is-building-an-ai-agent-for-everything-will-everyone-use-them/
author: Tim Fernholz
tags: [openai, ai-agents, chatgpt-work, harness-design]
date_consumed: 2026-08-28
---

## Summary

OpenAI's [[ChatGPT Work]] is the company's attempt to extend agentic AI from software engineers to white-collar workers broadly, giving models deep access to a user's inbox, calendar and apps. Adoption lags dramatically outside the company itself, exposing the harder challenge of designing a "harness" that makes agentic AI usable — and evaluable — for work that isn't as measurable as code.

## Core Concepts

- [[AI Harness]] — the software wrapped around a model that decides what information it sees, what tools it can use, and how it presents answers; OpenAI engineers describe good harness design as exposing the model to only the context it truly needs.
- [[ChatGPT Work]] — a modified version of OpenAI's Codex coding tool, released to non-engineers on the $20/month tier, meant to give white-collar workers the same agentic functionality software engineers get from Codex.
- [[Claude Code]] vs [[Codex]] — Anthropic's conversational, check-in-heavy approach to agentic coding proved more effective early on than OpenAI's initial bet on full model autonomy, forcing OpenAI to add more user interaction points.
- [[The Bitter Lesson]] — the AI research principle that a better general model matters more than domain-specific harness engineering, since harness advantages become obsolete within a few model-release cycles.

## Key Takeaways

- **Adoption gap**: 98% of OpenAI employees use Codex internally, but just 17% of organizational subscribers and under 1% of individual subscribers use the agentic coding tool.
- **Usage scale**: ChatGPT Work and Codex combined have 20 million users, versus more than a billion people who prompt ChatGPT online.
- **Evaluation is the hard problem**: unlike code, which "either works or it doesn't," most white-collar workflows (a business strategy, a sales pitch) aren't as easy to evaluate or trace, complicating how OpenAI measures whether agents actually help.
- **Harness philosophy split**: Claude's harness surveys options and checks in repeatedly with the user; OpenAI's Codex originally bet on full autonomy before adding more interaction points after Claude Code proved the conversational approach worked better.
- **Real cost gap**: one tester used 80 million tokens in four days on the $20/month plan, costing OpenAI roughly 3x the subscription price in actual compute.

## 🃏 Review Questions

**Q1**: What is the core claim of this article?
**A**: OpenAI is racing to extend agentic AI beyond software engineers to the broader white-collar workforce, but adoption outside the company remains negligible because non-coding work is harder to harness and evaluate than code.

**Q2**: What specific evidence shows the gap between internal and external adoption?
**A**: An OpenAI-backed study found 98% of OpenAI employees use Codex versus just 17% of organizational subscribers and less than 1% of individual subscribers.

**Q3**: How does OpenAI's harness design philosophy differ from Anthropic's, and why does it matter?
**A**: OpenAI initially bet on full model autonomy with minimal user input, while Anthropic's Claude Code was built around back-and-forth conversation and checkpoints; Anthropic's approach proved more effective early on, pushing OpenAI to add more interaction points to its own products.
