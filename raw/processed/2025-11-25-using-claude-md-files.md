---
source_url: https://claude.com/blog/using-claude-md-files
author: Unknown
date: 2025-11-25
---

# Using CLAUDE.md Files: Customizing Claude Code for Your Codebase

CLAUDE.md files provide Claude Code with persistent, project-specific context loaded automatically into every conversation, eliminating repetitive explanations of architecture and conventions.

## What It Is

A configuration file placed in your repository root, parent directories (for monorepos), or home folder. It becomes part of Claude's system prompt on every session.

## Getting Started with /init

Running `/init` analyzes your project and generates a starter CLAUDE.md, capturing build commands, test instructions, and key directories. Treat it as a starting point, not a finished product.

## Recommended Structure

- Project architecture map with directory trees
- Custom tool documentation with usage examples
- Standard workflow definitions (e.g., explore → plan → code → commit)

## Additional Best Practices

- Use `/clear` between unrelated tasks to reset accumulated context
- Delegate distinct work phases to subagents for isolated context
- Store reusable prompts as custom slash commands in `.claude/commands/`

## Important Cautions

- Keep the file concise — it loads every session
- Never include API keys, credentials, or security vulnerability details
- Break large content into separate markdown files and reference them

**Example Workflow Instruction:**
> "Before modifying code in the following locations: X, Y, Z — consider how it might affect A, B, C"
