---
type: literature-note
source_url: https://michaelheap.com/github-wiki-is-an-antipattern/
author: Michael Heap
tags: [github, documentation, software-development, best-practices]
date_consumed: 2026-09-23
---

## Summary

Michael Heap argues that GitHub's built-in wiki feature is an anti-pattern for project documentation, offering only the convenience of single-click access while introducing serious drawbacks around versioning, review, and tooling. The recommended alternative is a `/docs` folder co-located with the source code, published via [[GitHub Pages]]. This approach aligns documentation with established code workflows and makes migrations straightforward as the project grows.

## Core Concepts

- [[GitHub Wiki]] — a built-in wiki feature tied to a repository but stored in a separate, largely unknown clone target
- [[Documentation as Code]] — treating docs like source code: version-controlled, pull-request-reviewed, and CI-linted
- [[GitHub Pages]] — static site hosting that can publish a `/docs` folder directly from the main repository
- [[Vale]] — a prose linting tool that can enforce documentation style in CI pipelines
- [[Just the Docs]] — a simple GitHub Pages theme for publishing project documentation

## Key Takeaways

- **Versioning gap**: Docs in `/docs` stay in sync with code; wiki content is decoupled.
- **Hidden clone**: Wiki content requires a separate `git clone`, unknown to most contributors.
- **Review discipline**: A `/docs` folder forces docs through [[Pull Request]] review like any code change.
- **CI integration**: `/docs` enables linting (e.g., [[Vale]]) and familiar editor tooling with spellcheck.
- **Branding limit**: All GitHub wikis look identical; hosted Pages allows custom themes.
- **No native images**: GitHub wikis do not support direct image uploads.
- **Migration path**: Starting in `/docs` makes moving to a dedicated docs repo straightforward later.

## 🧠 First Principles & Mental Models

- **[[Locality of Reference]]**: Keeping documentation adjacent to the code it describes reduces context-switching and the risk of drift — changes to behaviour and changes to docs travel together through the same review process.
- **[[Defaults Shape Outcomes]]**: GitHub's wiki is prominently accessible, so teams reach for it by default; recognizing that convenience is not the same as correctness is the first step to choosing a better workflow.

## 🃏 Review Questions

**Q1**: What is the core argument against using GitHub's wiki for project documentation?
**A**: GitHub wikis offer a single convenience (easy access) but sacrifice version alignment with code, pull-request review, CI tooling, and contributor familiarity — making a `/docs` folder a strictly better default.

**Q2**: Why does cloning a repository not include the wiki, and why does this matter?
**A**: The wiki lives in a separate git repository that most contributors don't know exists, so documentation updates can be made without any review and may go unnoticed by the broader team.

**Q3**: How should a project transition away from a GitHub wiki according to Heap's recommendation?
**A**: Add a `/docs` folder, publish it via GitHub Pages (using a theme like Just the Docs or a Hugo + Actions workflow), and leave a single wiki page redirecting users to the hosted docs site.
