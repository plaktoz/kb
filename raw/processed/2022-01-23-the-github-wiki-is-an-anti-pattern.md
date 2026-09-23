---
source_url: https://michaelheap.com/github-wiki-is-an-antipattern/
author: Michael Heap
date: 2022-01-23
---

# The GitHub Wiki is an Anti-Pattern

Michael Heap argues that using GitHub's wiki feature is an anti-pattern, with essentially one benefit — single-click accessibility — versus numerous drawbacks.

## Why Avoid the Wiki?

- Docs in a `/docs` folder are **versioned with your code**, making old versions easy to find
- Cloning a repo doesn't include wiki content (separate clone required, and largely unknown)
- A `/docs` folder means documentation goes through **pull request review** like any other code change
- Enables CI tooling (e.g., Vale for linting) and familiar editors with spellcheck
- Wikis offer "limited branding opportunities" — they all look similar
- Wikis don't support image uploads natively

## Recommended Approach

1. Add documentation to `/docs` in your repository (not `gh-pages`)
2. Configure GitHub Pages to publish it — `just-the-docs` theme for simplicity, or Hugo + a publish Action for custom workflows
3. Leave a single wiki page pointing to the hosted docs

As your project matures, docs may eventually warrant their own repository. Since contributors will already be comfortable working with docs in a repo, that migration becomes straightforward.
