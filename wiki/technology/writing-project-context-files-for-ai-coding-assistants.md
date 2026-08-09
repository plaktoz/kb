---
type: literature-note
source_url: https://fordelstudios.com/research/how-to-write-project-context-files-for-ai-coding-assistants
author: Abhishek Sharma
tags: [ai-coding-assistants, context-files, claude-code, developer-workflow]
date_consumed: 2026-08-09
---

## Summary

Project context files (CLAUDE.md, .cursorrules, .github/copilot-instructions.md) are loaded automatically at session start and give [[AI Coding Assistants]] your project's conventions before any prompt is written. The core principle is to include only what the assistant would get wrong without guidance, skipping anything it can already infer from existing config files. Teams that iterate these files consistently report dropping weekly AI correction counts from 15–20 to 2–3.

## Core Concepts

- **Project Context Files**: Tool-specific files ([[CLAUDE.md]] for Claude Code, `.cursorrules` for [[Cursor]], `.github/copilot-instructions.md` for [[GitHub Copilot]]) loaded at session start to pre-load project conventions.
- **Five-Section Structure**: A recommended template — Project Identity, Conventions That Break Defaults, "Do NOT" list, File Structure Map, and Testing & Quality Gates.
- **Multi-File Context (Claude Code)**: Nest CLAUDE.md files in subdirectories for domain-specific rules; root file under ~200 lines, subdirectory files under ~50.
- **Correction Encoding**: The principle that every correction not written into a context file will need to be repeated; encoding corrections into rules is the compounding investment.
- **[[Iterative Refinement]]**: Context files should be reviewed and updated regularly (e.g., during sprint retros) based on observed AI mistakes.

## Key Takeaways

- **Only include what would go wrong**: Skip rules the assistant can infer from ESLint, tsconfig, or existing code.
- **Project Identity (3–5 lines)**: ~40 words naming project, stack, and key constraints prevents the most common mistakes.
- **Be specific with conventions**: Use exact file paths and examples, not vague directives like "follow our standards."
- **Explicit "Do NOT" list**: Ban wrong loggers, CSS-in-JS, unapproved dependencies, and other known anti-patterns.
- **File structure map**: A short directory tree tells the assistant where to place and find files.
- **Measure effectiveness**: Track weekly corrections a context rule would have prevented.
- **Getting started**: Write 5 rules from your last 5 corrections; takes ~30 minutes; ~2 min/week to maintain.
- **15–20 → 2–3 corrections/week**: Reported improvement after iterating context files over three weeks.

## 🧠 First Principles & Mental Models

- **[[Garbage In, Garbage Out]]**: Without project context, the AI defaults to training data — the wrong framework, naming style, or patterns. Context files are the input quality lever.
- **[[Compounding]]**: Each correction encoded into a rule is paid once but saves rework on every future AI interaction; not encoding it means paying the same correction cost repeatedly.

## 🃏 Review Questions

**Q1**: What is the core principle for deciding what to include in a project context file?
**A**: Include only what the assistant would get wrong without guidance; skip what it would naturally infer from existing config files like ESLint or tsconfig.

**Q2**: What measurable improvement did one team report after iterating their context file over three weeks?
**A**: Weekly AI corrections that a context rule would have prevented dropped from roughly 15–20 per week to 2–3.

**Q3**: How should a developer get started with a project context file today?
**A**: Write five rules based on your last five corrections, ship the file today, and expand it incrementally — initial setup is ~30 minutes with ~2 minutes per week ongoing maintenance.
