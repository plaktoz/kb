---
type: literature-note
source_url: https://www.mindstudio.ai/blog/andrej-karpathy-llm-wiki-obsidian-codeex-second-brain
author: MindStudio Team
tags: [personal-knowledge-management, obsidian, llm-agents, second-brain]
date_consumed: 2026-07-26
---

## Summary

The article describes building a self-organizing personal knowledge base inspired by [[Andrej Karpathy]]'s LLM wiki architecture, using an AI agent layer to convert raw inputs into a structured, interlinked Markdown wiki inside [[Obsidian]]. The entire system behavior is controlled by a single `agents.md` file, making it instantly editable without code deployment. Extensions include a CRM folder for people notes and a journal folder grounded in prior wiki entries.

## Core Concepts

- [[Personal Knowledge Management]] — organizing knowledge through capture, structure, and retrieval
- [[Andrej Karpathy]] — author of the original LLM wiki architecture on GitHub
- [[Obsidian]] — local Markdown editor used as the wiki interface
- [[LLM Agents]] — AI layer that converts raw inputs into structured wiki notes
- [[Second Brain]] — external system for storing and retrieving personal knowledge
- [[Codeex]] — automation tool that runs hourly to process raw files and push commits
- [[agents.md]] — plain-text behavioral spec controlling all agent actions
- [[Obsidian Web Clipper]] — Chrome extension that drops articles and transcripts into `/raw`

## Key Takeaways

- **Folder structure**: `/raw` for unprocessed clips; `/wiki` for AI-generated notes
- **Single operational spec**: `agents.md` controls all agent behavior — edit to change instantly
- **Automation**: [[Codeex]] processes `/raw`, updates `/wiki`, and pushes commits hourly
- **Input layer**: [[Obsidian Web Clipper]] drops articles and YouTube transcripts into `/raw`
- **CRM extension**: `/CRM` folder tracks people notes via natural language trigger
- **Journal extension**: entries grounded in wiki, CRM, and prior journals — not generic responses
- **Over-generation risk**: prune with a follow-up prompt to maintain minimal spec
