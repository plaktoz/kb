---
source_url: https://www.ignorance.ai/p/skills-tools-and-mcps-whats-the-difference
author: Charlie Guo
date: 2026-01-24
---

# Skills, Tools and MCPs - What's The Difference?

The article traces the evolution of AI capability primitives from OpenAI's 2023 function calling through MCP to the emerging "Skills" format.

## Tools (Function Calling)

The original breakthrough: describe a function via JSON schema, and the model outputs structured JSON to invoke it. Enabled ChatGPT Plugins, Code Interpreter, and web browsing. Limitation: every integration was bespoke, with no shared infrastructure or interoperability between AI platforms.

## MCP (Model Context Protocol)

Anthropic's standardization layer — "USB-C for AI systems." MCP servers expose capabilities dynamically, so any compliant client (Claude, Cursor, ChatGPT) can discover and call them. Enables community-built connectors for Slack, GitHub, Notion, etc. Two remaining problems: **security** (auditing combined tool access) and **judgment** (having tools ≠ knowing how to use them well).

## Skills

A `SKILL.md` file with YAML frontmatter (name/description) loaded as a lightweight hint, with full markdown instructions loaded only when relevant. This progressive disclosure avoids bloating the context window. Skills encode *expertise* — the "playbook" a human expert would follow — rather than raw capabilities. Both Anthropic and OpenAI independently converged on nearly identical formats.

## The Stack

- **Tools** → atomic capabilities
- **MCP** → standardized infrastructure/discovery
- **Skills** → domain expertise and sequencing knowledge

The author compares today's AI apps to early mobile websites: "m.google.com" era products, with truly AI-native experiences still ahead. Further fragmentation is expected before standards stabilize.
