---
type: literature-note
source_url: https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released
author: Unknown
tags: [htmx, web-development, javascript, frontend]
date_consumed: 2026-08-29
---

## Summary

[[htmx]] 4.0.0 has been released after 8 months of development, bringing breaking changes to attribute inheritance and event naming alongside significant new features. The release modernizes the library by removing implicit behaviors (silent attribute inheritance, localStorage history caching) in favor of explicit opt-in patterns. htmx 2 will continue to receive support indefinitely; htmx 4 remains tagged `next` on NPM until early 2027 to protect users on unversioned CDN URLs.

## Core Concepts

- **[[htmx]]** — HTML-first library enabling AJAX, WebSockets, and server-sent events via HTML attributes, now at version 4.0.0
- **[[Attribute Inheritance]]** — In htmx 4, inheritance of attributes like `hx-confirm` to child elements is opt-in via the `:inherited` suffix, replacing htmx 2's silent implicit inheritance
- **[[DOM Morphing]]** — Technique for updating the DOM by diffing existing and new HTML structure; now built into htmx 4 natively (evolved from [[idiomorph]])
- **[[Out-of-Band Swaps]]** — Server-driven partial page updates; htmx 4 introduces `<hx-partial>` as a cleaner alternative
- **[[hx-live]]** — New lightweight front-end scripting extension inspired by [[Alpine.js]], jQuery, and [[hyperscript]]

## Key Takeaways

- **Breaking: Attribute Inheritance** — Must append `:inherited` to opt into child-element inheritance; CLI upgrade checker available.
- **Breaking: Event Renaming** — Events follow new `htmx:phase:action` pattern; XHR events removed; most errors consolidate into `htmx:error`.
- **Breaking: History** — No longer caches snapshots in `localStorage` by default; back-navigation re-fetches pages.
- **New: Morphing Swaps** — Built-in DOM morphing (from idiomorph) now included natively.
- **New: `<hx-partial>` tag** — Cleaner server-driven multi-element targeting without out-of-band swap boilerplate.
- **New: `htmax.js` bundle** — htmx packaged with the most popular extensions in one file.
- **Upgrade path** — Run `npx htmx.org@4.0.0 upgrade-check -- ./templates` to find affected code; htmx 2 still supported.

## 🧠 First Principles & Mental Models

- **[[Explicit over Implicit]]**: By requiring `:inherited` and removing silent localStorage caching, htmx 4 trades magic for predictability — a recurring principle in maintainable software design where hidden side-effects are the primary source of hard-to-diagnose bugs.

## 🃏 Review Questions

**Q1**: What is the central design philosophy shift in htmx 4.0.0 compared to htmx 2?
**A**: htmx 4 moves from implicit to explicit behavior — attribute inheritance and history caching must now be explicitly opted into rather than happening silently by default.

**Q2**: How does htmx 4 change event naming, and what happens to most error events?
**A**: Events now follow a `htmx:phase:action` pattern (e.g., `htmx:beforeRequest` becomes `htmx:before:request`); XHR events are removed and most error events consolidate into a single `htmx:error` event.

**Q3**: How should a developer safely migrate an existing htmx 2 project to htmx 4?
**A**: Run the CLI upgrade checker (`npx htmx.org@4.0.0 upgrade-check -- ./templates`) to locate affected attribute inheritance usage; htmx 2 remains supported indefinitely so migration is not urgent.
