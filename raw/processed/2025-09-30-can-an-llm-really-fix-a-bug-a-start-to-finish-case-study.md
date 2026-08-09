---
source_url: https://anchore.com/blog/can-an-llm-really-fix-a-bug-a-start-to-finish-case-study/
author: Sonja Schweigert
date: 2025-09-30
---

# Can an LLM Really Fix a Bug? A Start-to-Finish Case Study

Schweigert conducted a controlled experiment to test whether an LLM could guide a contributor from selecting a GitHub issue through to a merged pull request on Anchore's open source tools (Syft, Grype, Grant).

## Issue Selection

A shell script using the `gh` CLI gathered "good-first-issue" labeled tickets across Anchore repositories. Claude then evaluated candidates across five weighted criteria: impact (30%), implementation complexity (25%), information quality (20%), LLM assistance potential (15%), and community need (10%). It selected Syft issue #2250 — npm `package.json` authors field parsing — citing "crystal clear requirements" and suitability for pattern-matching assistance.

## Development Process

Using VS Code with GitHub Copilot in agent mode, Schweigert prompted iteratively, reviewing all generated code rather than accepting it blindly. The LLM was directed to contributing guidelines and developing docs for project conventions.

## Outcomes

- The pull request was merged after maintainer review
- Development was estimated "3-5 times faster" than working manually
- Maintainers could identify AI assistance but found it acceptable given quality
- Schweigert noted she should have pointed the LLM to contributing guidelines earlier

## Key Takeaway

The approach works best for issues with clear requirements and routine logic — not as a black-box solution, but as a "knowledgeable pair-programming partner."
