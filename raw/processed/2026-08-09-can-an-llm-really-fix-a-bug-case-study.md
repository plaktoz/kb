# Can an LLM Really Fix a Bug? A Start-to-Finish Case Study

**Author:** Sonja Schweigert
**Date:** Sep 30, 2025
**Source:** https://anchore.com/blog/can-an-llm-really-fix-a-bug-a-start-to-finish-case-study/

---

## Summary

Anchore engineer Sonja Schweigert ran a controlled experiment to test whether an LLM could guide a developer from issue selection all the way through a merged pull request on a real open source project.

## The Problem

Open source backlogs grow faster than contributor bandwidth allows. "Good first issue" tickets can sit untouched for months across projects like Syft, Grype, and Grant.

## The Approach

**Step 1 – Issue Discovery:** A bash script using the `gh` CLI fetched all "good-first-issue" labeled tickets across multiple Anchore repos, saving full issue data (title, body, comments) as JSON files.

**Step 2 – LLM Issue Selection:** Claude evaluated issues using a weighted scoring framework:

| Criterion | Weight |
|---|---|
| Impact & User Value | 30% |
| Implementation Complexity | 25% |
| Information Quality | 20% |
| LLM Assistance Potential | 15% |
| Community Need | 10% |

The LLM selected **Syft issue #2250** — fixing `package.json` authors field parsing — citing it as ideal because it involved "JSON parsing, regex patterns, and code generation."

**Step 3 – Development:** Using VS Code with GitHub Copilot agent mode, the author used iterative, collaborative prompting — reviewing all generated code, asking clarifying questions, and directing the LLM to project contributing guidelines.

**Step 4 – Testing & PR:** The LLM identified existing test patterns and generated appropriate test cases. The pull request was drafted using the project's own template, then lightly edited before submission.

## Results

- PR was **merged** after maintainer review
- Development was roughly **3–5× faster** than an unassisted approach
- Maintainers could tell the code was AI-assisted but found the quality acceptable
- Key lesson: explicitly pointing the LLM to contributing guidelines earlier would have reduced iteration cycles

## When This Works Best

- Issues with clear, well-documented requirements
- Learning a new codebase quickly
- Routine parsing or data transformation tasks
- Time-constrained development scenarios

## Caveats

The author notes that consuming all "good first issues" with AI would deprive human newcomers of valuable learning opportunities. The recommendation is to preserve those tickets and target more complex issues instead — and to disclose AI assistance in PRs.
