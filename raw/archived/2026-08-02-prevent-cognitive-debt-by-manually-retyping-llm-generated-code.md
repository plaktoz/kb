---
source_url: https://ankursethi.com/blog/prevent-cognitive-debt-by-manually-retyping-llm-generated-code/
author: Ankur Sethi
date: 2026-08-02
---

# Prevent cognitive debt by manually retyping LLM-generated code

Sethi describes a deliberate, slower workflow for using AI coding assistants on personal projects. Rather than letting the LLM write directly to files, he has it suggest code in chat, then types every line himself.

His agent instructions prohibit the AI from modifying files directly: "Never create, edit, move, rename, or delete project files unless I explicitly ask you to do so."

## Why this approach?

He finds AI-generated PRs unpleasant to review and wants genuine comprehension, not just output. Manual typing lets him:

- Catch hallucinations and poor design choices
- Refactor and adapt code to his own style
- Build a "spatial map" of his codebase
- Look up anything he doesn't understand in real time

He estimates this makes him roughly 2x faster (vs. 10x if fully delegating), but he trades speed for understanding.

He draws a parallel to advice given to beginner programmers: never copy-paste — always type examples out yourself.

## The broader concern

His broader concern is industry-wide: "cognitive debt" accumulating as developers ship code they don't fully understand, potentially leaving critical infrastructure opaque to its own maintainers.
