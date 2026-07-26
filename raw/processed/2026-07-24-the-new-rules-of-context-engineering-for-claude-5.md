# The New Rules of Context Engineering for Claude 5 Generation Models

source_url: https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models

---

Author: Thariq Shihipar, Member of Technical Staff, Anthropic
Published: July 24, 2026

Anthropic eliminated over 80% of Claude Code's system prompt for Claude 5-generation models (Opus 5, Fable 5) without measurable coding performance loss. The key insight: newer models exercise better judgment and no longer need heavy guardrails.

Key shifts:

Rules → Judgment: Instead of rigid directives like "never write multi-line comments," the new prompt says: "write code that reads like the surrounding code: match its comment density, naming, and idiom."

Examples → Interface design: Providing examples constrains exploration; better tool parameter design guides behavior more effectively.

Front-loading → Progressive disclosure: Load context only when needed, including deferred tool definitions requiring a ToolSearch before use.

Repetition → Concise tool descriptions: Redundant cross-references between system prompts and tool descriptions were removed.

Manual memory → Auto-memory: Claude now saves relevant memories automatically rather than requiring user-triggered writes.

Simple specs → Rich references: HTML artifacts, test suites, and rubrics outperform plain markdown for complex references.

Practical guidance: Keep CLAUDE.md lightweight, focused on codebase-specific "gotchas." Use Skills for progressive disclosure of specialized knowledge. Run /doctor in Claude Code to automatically rightsize your context files.
