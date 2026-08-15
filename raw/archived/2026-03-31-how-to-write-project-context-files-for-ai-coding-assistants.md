---
source_url: https://fordelstudios.com/research/how-to-write-project-context-files-for-ai-coding-assistants
author: Abhishek Sharma
date: 2026-03-31
---

# How to Write a CLAUDE.md That Actually Works

Project context files (CLAUDE.md for Claude Code, .cursorrules for Cursor, .github/copilot-instructions.md for Copilot) are loaded automatically at session start, giving AI coding assistants your project's conventions before any prompt is written. Without one, the assistant defaults to training data — potentially using the wrong framework, naming style, or component patterns.

## Core Principle

Only include what the assistant would get wrong without guidance. Skip what it would naturally infer from your existing config files.

## Recommended Structure

**Section 1 – Project Identity (3–5 lines)**
Name the project, stack, and key constraints. Roughly 40 words can prevent the five most common mistakes.

**Section 2 – Conventions That Break Defaults**
Be specific with examples. Instead of "follow our standards," specify exact file naming, export styles, and where components live.

**Section 3 – The "Do NOT" List**
Explicitly ban unwanted patterns — wrong loggers, CSS-in-JS, unnecessary API routes, unapproved dependency installs.

**Section 4 – File Structure Map**
A short indented directory list so the assistant knows where to place and find files.

**Section 5 – Testing & Quality Gates**
Specify test framework, file placement, and required CI checks before commits.

## Multi-File Context (Claude Code)

Nest CLAUDE.md files in subdirectories for domain-specific rules. Keep the root file under ~200 lines; subdirectory files under ~50.

## Common Mistakes

| Mistake | Fix |
|---|---|
| Writing an essay | Keep it ruthlessly brief |
| Vague instructions | Give concrete examples with file paths |
| Never updating it | Review during sprint retros |
| Duplicating enforced config | Skip what ESLint/tsconfig already handles |
| Only writing what you want | Also explicitly list what you don't want |

## Measuring Effectiveness

Track weekly assistant corrections that a context rule would have prevented. One team reported dropping from ~15–20 such corrections per week to 2–3 after iterating over three weeks. The principle: *"Every correction you give your AI assistant that you do not encode into a context file is a correction you will give again tomorrow."*

## Getting Started

Write five rules based on your last five corrections. Ship that file today, and expand it incrementally. Initial setup takes roughly 30 minutes; ongoing maintenance is about 2 minutes per week.
