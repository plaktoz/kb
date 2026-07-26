---
type: literature-note
source_url: https://anvilproject.org/guides/content/creating-links
author: Unknown
tags: [markdown, documentation, links, anvil-portal]
date_consumed: 2026-07-26
---

## Summary

This guide explains the [[Markdown]] syntax for creating links on the [[AnVIL Portal]], covering internal links, external links, and heading anchors. Internal links use relative paths starting with a forward slash and omit the `.md` extension. Heading anchors are created by hovering over a heading, clicking the link icon, and copying the URL fragment.

## Core Concepts

- [[Markdown]] — lightweight markup language used for formatting and linking
- [[Internal Links]] — relative links within the same site, using path without domain or `.md`
- [[External Links]] — full-URL links pointing to resources outside the site
- [[Anchor Links]] — links targeting a specific heading within a page using `#fragment`
- [[AnVIL Portal]] — genomics data platform using Markdown-based documentation

## Key Takeaways

- **Link syntax**: `[Link text](url)` — square brackets for text, parentheses for URL
- **Internal links**: use relative path starting with `/`, omit `.md` suffix
- **Internal example**: `[Page](/guides/content/editing-an-existing-page)`
- **Heading anchors**: hover heading → click icon → copy `#fragment` from address bar
- **External links**: use full URL including protocol (e.g. `https://`)
