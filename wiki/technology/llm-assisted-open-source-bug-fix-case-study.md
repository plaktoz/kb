---
type: literature-note
source_url: https://anchore.com/blog/can-an-llm-really-fix-a-bug-a-start-to-finish-case-study/
author: Sonja Schweigert
tags: [llm, ai-coding, open-source, pair-programming]
date_consumed: 2026-08-09
---

## Summary

Sonja Schweigert ran a controlled experiment to determine whether an [[LLM]] could guide a contributor from issue selection through to a merged pull request on Anchore's open-source tools ([[Syft]], Grype, Grant). Using [[GitHub Copilot]] in agent mode within VS Code, she iteratively prompted the LLM while reviewing all generated code rather than accepting it blindly. The result was a merged PR with development estimated at 3–5x faster than working manually.

## Core Concepts

- **[[LLM]]-assisted issue triage**: [[Claude]] evaluated candidate GitHub issues across five weighted criteria — impact (30%), complexity (25%), information quality (20%), LLM assistance potential (15%), community need (10%).
- **[[GitHub Copilot]] agent mode**: Used for iterative, human-supervised code generation rather than autonomous execution.
- **[[Syft]]**: Anchore's open-source software composition analysis tool; the target repository for the bug fix.
- **[[Pair Programming]] with AI**: LLM treated as a "knowledgeable pair-programming partner," not a black-box solution.
- **Contributing guidelines as context**: Pointing the LLM to project conventions and contributing docs early is critical for code quality.

## Key Takeaways

- **Issue selection**: LLM picked Syft #2250 (npm `package.json` authors field parsing) citing clear requirements.
- **3–5x speed**: Development estimated 3–5 times faster than working manually.
- **Maintainer acceptance**: Maintainers could identify AI assistance but accepted it given quality.
- **Human oversight required**: All generated code was reviewed before acceptance — not blind auto-accept.
- **Context matters**: LLM should be given contributing guidelines early, not mid-session.
- **Best fit**: Works well for issues with clear requirements and routine/pattern-matching logic.

## 🧠 First Principles & Mental Models

- **[[Garbage In, Garbage Out]]**: The LLM's output quality depended entirely on the quality of context provided — pointing it to contributing guidelines earlier would have saved rework, illustrating that AI tools amplify the quality of their inputs.
- **[[Pair Programming]]**: Treating the LLM as a collaborative partner who needs direction rather than an autonomous agent produced better outcomes; the human remained the reviewer and decision-maker throughout.

## 🃏 Review Questions

**Q1**: What is the central finding of this LLM bug-fix case study?
**A**: An LLM guided a contributor from issue selection to a merged pull request on Anchore's open-source tools, with development estimated 3–5x faster than manual work.

**Q2**: How did the LLM score and select which GitHub issue to tackle?
**A**: Claude evaluated candidates across five weighted criteria — impact (30%), complexity (25%), information quality (20%), LLM assistance potential (15%), and community need (10%) — selecting Syft issue #2250 for its clear requirements and pattern-matching suitability.

**Q3**: What is the key condition that makes LLM-assisted coding effective, and what lesson did the author learn?
**A**: The approach works best for issues with clear requirements and routine logic; the author noted she should have directed the LLM to contributing guidelines earlier in the session rather than mid-way through.
