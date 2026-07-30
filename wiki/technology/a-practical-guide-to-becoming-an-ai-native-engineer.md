---
type: literature-note
source_url: https://blog.bytebytego.com/p/a-practical-guide-to-becoming-an
author: Shah Rahman
tags: [ai-native-engineering, context-engineering, software-engineering, ai-security]
date_consumed: 2026-07-29
---

## Summary

Shah Rahman argues that real AI productivity gains come from engineers shifting from writing code to orchestrating it, built on four core practices — [[Context Engineering]], [[Specification-Driven Development]], critical verification, and problem decomposition — with an ideal time split of 40% context-setting, 20% generation, and 40% review. He outlines a three-phase individual mastery path (Foundation, Integration, Mastery), a redefined [[Agentic Development Life Cycle]] (ADLC) replacing the traditional SDLC, and extensive security guardrails needed because AI-generated code carries high vulnerability rates and enables new attack surfaces like [[Slopsquatting]] and [[Prompt Injection]].

## Core Concepts

- [[AI-Native Engineering]] — orchestrating AI agents to engineer things not possible pre-AI, distinct from [[Vibe Coding]]
- [[Andrej Karpathy]] — coined "vibe coding" in early 2025
- [[Context Engineering]] — systematic curation of project-specific information into AI working memory; the single most important AI-native skill
- [[Specification-Driven Development]] — defining clear specs and milestones before asking AI to build
- [[Agentic Development Life Cycle]] (ADLC) — redefines planning, building, testing, review, and documentation for AI-agent-driven development
- [[MCP]] and [[CLAUDE.md]] — described as core infrastructure for context engineering, not optional documentation
- [[Prompt Injection]] — hidden instructions in external content that hijack agent behavior
- [[Slopsquatting]] — attackers register hallucinated AI-suggested package names with malicious code
- [[Claude Code]] — cited among agentic coding tools supporting orchestrator-style development

## Key Takeaways

- Coding was always ~20-30% of engineering; more AI code isn't more productive
- Four core practices: context engineering, spec-driven dev, verification, decomposition
- Teams with rigorous context engineering report 40-50% speed increases
- Around 45% of AI-generated code contains security flaws per research cited
- A METR/Anthropic RCT found experienced devs 19% slower with AI on familiar code
- Optimal time split: 40% context, 20% generation, 40% review/verification
- ADLC redefines planning, building, testing, review, and documentation phases
- Slopsquatting exploits AI-hallucinated package names with malicious registrations
- Gartner: 50% of orgs will require "AI-free" skills assessments by 2026

## 🧠 First Principles & Mental Models

- **[[Garbage In, Garbage Out]]**: The article states this explicitly — AI-generated code quality matches the quality of the input specification, so vague prompts produce unreliable output regardless of model capability.
