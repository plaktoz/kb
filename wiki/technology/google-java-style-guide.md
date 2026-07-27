---
type: literature-note
source_url: https://google.github.io/styleguide/javaguide.html
author: Google
tags: [java, style-guide, code-formatting, naming-conventions]
date_consumed: 2026-07-27
---

## Summary

The Google Java Style Guide is the authoritative, complete definition of Google's coding standards for Java source code, covering formatting, naming, programming practices, and Javadoc. It establishes hard-and-fast rules universally applied at Google rather than advisory suggestions. The guide ensures that any Java file "in Google Style" is readable, consistent, and tooling-friendly across large codebases.

## Core Concepts

- **[[Source File Structure]]**: Canonical ordering — license → package → imports (static then non-static) → one top-level class.
- **[[Code Formatting]]**: 2-space block indentation, 100-character column limit, K&R brace style for nonempty blocks, one statement per line.
- **[[Naming Conventions]]**: UpperCamelCase for classes, lowerCamelCase for methods/variables, `UPPER_SNAKE_CASE` for constants, all-lowercase for packages. No special prefixes (`mName`, `s_name`, `kName`).
- **[[Camel Case Rules]]**: Acronyms treated as words — `XmlHttpRequest` not `XMLHTTPRequest`; `supportsIpv6OnIos` not `supportsIPv6OnIOS`.
- **[[Java Imports]]**: No wildcard imports, no module imports, ASCII-sorted within static and non-static groups.
- **[[Javadoc]]**: Required on all visible classes and members; summary fragment must be a noun/verb phrase; `@param`, `@return`, `@throws` in that order.
- **[[Switch Expressions]]**: Must be new-style (arrow syntax); all switches must be exhaustive including a `default` label.
- **[[Google Style Guide]]**: Industry reference point for Java formatting; compatible with automated formatters like google-java-format.

## Key Takeaways

- No wildcard imports; each import on its own line, ASCII-sorted.
- Indentation: +2 spaces per block; continuation lines: at least +4.
- Column limit: 100 characters (not the old 80).
- Constants use `UPPER_SNAKE_CASE`; no `name_` or `mName` prefixes.
- `long` literals always use uppercase `L` (e.g., `3000000000L`).
- Text block opening `"""` always on a new line.
- `@Override` always present when legal; omit only when parent is `@Deprecated`.
- Do not override `Object.finalize` — scheduled for removal.
- `TODO` comments must include a bug reference link and a hyphen-prefixed explanation.
- Horizontal alignment (padding tokens) is never required and discourages adding it.

## 🧠 First Principles & Mental Models

- **[[Consistency Principle]]**: The guide's deepest value is organizational consistency over personal preference — a uniform codebase is cheaper to read and maintain than an individually "optimal" one, so rules are followed even when the local choice seems arbitrary.
