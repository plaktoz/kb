---
type: literature-note
source_url: https://simonwillison.net/guides/agentic-engineering-patterns/hoard-things-you-know-how-to-do/
author: Simon Willison
tags: [agentic-engineering, coding-agents, personal-knowledge-base, llm-workflows]
date_consumed: 2026-07-29
---

## Summary

Building a personal collection of "things you know how to do" — proof-of-concept code, TIL notes, small working examples — pays compounding dividends once coding agents enter the workflow, because a documented working example lets an agent combine two known solutions into something new almost instantly. [[Simon Willison]] illustrates this with a browser-based OCR tool built by combining two previously-hoarded code snippets (Tesseract.js and PDF.js) into a single prompt that produced a working proof-of-concept in minutes.

## Core Concepts

- **[[Solution Hoarding]]** — maintaining a personal archive (blog posts, TIL notes, GitHub repos, single-file "HTML tools") of proven working examples rather than relying on memory of what's theoretically possible
- **[[Prompt Combination Pattern]]** — feeding an agent two or more known-working examples and asking it to combine them, rather than describing a novel solution from scratch
- **[[Agent-Assisted Research Repos]]** — using a coding agent to research a problem and return both working code and a written report, expanding a personal hoard faster than manual experimentation

## Key Takeaways

- **Proof beats theory**: seeing something demonstrated in running code is more reliable than knowing it's "theoretically possible"
- **Public repos become agent inputs**: coding agents can be told to clone a person's own repositories as reference material for new tasks
- **A trick only needs to be solved once**: once documented with a working example, agents can reapply it to any similarly-shaped future problem
- **Search-capable agents reduce hoarding overhead**: agents with internet/search access can locate relevant prior examples themselves, including fetching raw HTML via `curl` rather than a summarizing WebFetch tool
