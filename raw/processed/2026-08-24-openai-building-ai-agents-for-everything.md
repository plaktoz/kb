---
source_url: https://techcrunch.com/2026/08/24/openai-is-building-an-ai-agent-for-everything-will-everyone-use-them/
author: Tim Fernholz
date: 2026-08-24
---

# OpenAI is building AI agents for everything. Will everyone use them?

Getting the most value from a model means giving it the keys. For Andrew Ambrosino, the lead engineer for OpenAI's desktop app, that means his app has access to and control over his inbox, Slack, phone, and apps like Notion and Figma. "I'll do it for the job. I will take the personal hit here and there if I have to," Ambrosino told TechCrunch.

Ambrosino works on ChatGPT Work, OpenAI's biggest bet, released last month on the company's lowest subscription tier at $20/month. The product lets white-collar workers field AI agents hooked up to the digital workflows used by accountants, investors, doctors and others whose day-to-day is dominated by their computer. It's a modified version of OpenAI's Codex coding tool, meant to give non-engineers the same agentic functionality software engineers already get.

Commercially, agents that work longer stretches burn through more tokens, making them more lucrative per user. An OpenAI-backed study found that in June, 98% of OpenAI employees were using Codex, but just 17% of organizational subscribers and less than 1% of individual subscribers were using the agentic coding tool — a gap OpenAI is racing to close.

## How to make AI intuitive

Every LLM requires a "harness" — software wrapped around a model that decides what information it sees, what tools it can use, and how it presents answers. For developers, a command-line interface was enough to change how software gets built. Most people don't use CLIs, so OpenAI is trying to make agentic functionality as easy as prompting, similar to how Claude Code and Codex abstracted away software writing entirely.

OpenAI wouldn't say how many people use Work versus Codex, but the joint app has just 20 million users compared to more than a billion people the company says prompt ChatGPT online.

## The rivalry that drove OpenAI's product design

OpenAI's engineers were reluctant to directly compare ChatGPT Work to Claude Cowork, though the first thing ChatGPT Work asked the author to do on startup was port over Claude Cowork data. Claude Code defined the market for AI coding: it was built around back-and-forth conversation, surveying possibilities and giving users options before proceeding, whereas OpenAI's original Codex bet on the model handling tasks entirely autonomously with minimal input — an approach engineers called "AGI-pilled" that proved premature. OpenAI later added more opportunities for user interaction, becoming today's Codex.

Using download statistics as a proxy for interest, Claude Code was more in demand until April 2026, but Codex has since taken a slight lead, and surveys of enterprise use suggest OpenAI is catching up to Anthropic with business users.

## What makes a good harness, anyway?

Engineers described a "bitter lesson": a better general model matters more than specific domain experience, and any harness advantage is temporary since it can be made obsolete by the next model release within months. Databricks found that Pi, an open-source harness, outperformed Codex while using the same GPT-5.5 model — evidence, its creator says, that a minimalist approach can work for coding tasks, though non-coding work remains harder because there's little training data for tasks like management decisions whose outcomes play out over months rather than in a simple back-and-forth trace.

OpenAI said the focus for GDPval, its benchmark drawn from 44 occupations, is "the promise of the magic box," while acknowledging "there's too much complexity" left to solve.
