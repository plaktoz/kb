---
type: literature-note
source_url: https://www.aymannadeem.com/artificial/intelligence,/developer/tools/2026/09/24/plan-mode-is-dead.html
author: Ayman Nadeem
tags: [ai-coding, plan-mode, developer-tools, agentic-workflows]
date_consumed: 2026-09-26
---

## Summary

Ayman Nadeem reflects on building Nuanced, a desktop coding app built around structured AI planning workflows, and concludes that formalized "plan modes" are now obsolete. Better models make autonomous reasonable assumptions, rendering explicit spec documents unnecessary and even counterproductive. The real insight: planning still happens, but as an emergent property of an iterative act–inspect–adjust loop, not as a named artifact.

## Core Concepts

- **[[Plan Mode]]** — a formalized pre-coding step where users specify intent as a structured document before AI generates code; Nadeem argues this pattern is now dead
- **[[Nuanced]]** — Nadeem's desktop AI coding app that centered on persistent collaborative plans to bridge developer intent and AI implementation
- **[[AI-Assisted Development]]** — the broader paradigm where models generate code faster than humans can fully comprehend it, creating a mental-model gap
- **[[Iterative Coding Loop]]** — the replacement pattern: understand → act → inspect → clarify → adjust → act again, where planning is implicit, not explicit
- **[[Parallel AI Agents]]** — the emerging challenge: as multiple agents act concurrently, maintaining a coherent human mental model of a rapidly changing codebase becomes the next unsolved problem

## Key Takeaways

- **Planning vs. a Plan**: Conflating the act of thinking with a document artifact was a core product mistake.
- **Model improvement erodes explicit planning**: Better models autonomously handle assumptions, shrinking the human spec-writing job.
- **Long AI-generated specs are unreadable**: Overly structured text causes cognitive glazing; users don't engage.
- **Waterfall spec → build is unnatural**: Real developer understanding is iterative, not front-loaded.
- **New loop**: understand → act → inspect → clarify → adjust → act; planning lives inside the loop.
- **Open problem**: Surfacing where human attention matters most inside fast-moving parallel agent systems remains unsolved.

## 🧠 First Principles & Mental Models

- **[[Goodhart's Law]]**: By making "the plan" a target artifact, Nuanced incentivized users to produce a document rather than to actually think — the proxy displaced the goal it was meant to serve.
- **[[Iterative vs. Waterfall Thinking]]**: Real understanding is built through feedback cycles, not pre-specified in advance; forcing "finish thinking before building" violated this first principle of how cognition actually works.

## 🃏 Review Questions

**Q1**: What is the central claim of "Plan Mode is Dead"?
**A**: Formalized planning documents in AI-assisted coding have become obsolete because better models handle assumptions autonomously and the act of planning is better expressed through an iterative act–inspect–adjust loop than through a named artifact.

**Q2**: What specific product failure led Nadeem to this conclusion?
**A**: Users had little appetite for lengthy AI-generated specs, found the text hard to read, and experienced the sequential "finish thinking before building" workflow as unnatural — leading Nadeem to recognize he had conflated the act of planning with a plan document.

**Q3**: What is the next unsolved problem Nadeem identifies?
**A**: As parallel agents multiply, helping developers maintain a coherent mental model of a rapidly changing system and surfacing where human attention matters most remains an open challenge.
