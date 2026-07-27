---
type: literature-note
source_url: https://owasp.org/www-project-java-html-sanitizer/
author: OWASP
tags: [java, security, xss, html-sanitization]
date_consumed: 2026-07-27
---

## Summary

The OWASP Java HTML Sanitizer is a fast, security-reviewed Java library that sanitizes untrusted HTML to prevent XSS attacks when third-party HTML content must be included in a web application. It uses a policy-based API to define exactly which HTML elements and attributes are permitted, stripping everything else. Dual-licensed under Apache 2 and New BSD; built on Guava with minimal dependencies.

## Core Concepts

- **[[HTML Sanitization]]**: The process of removing or escaping unsafe HTML tags, attributes, and content from untrusted input before rendering in a browser.
- **[[XSS Prevention]]**: Cross-Site Scripting prevention — sanitizing user-generated HTML is the primary defense when input must be rendered as HTML (not just escaped).
- **[[PolicyFactory]]**: The core API — defines which elements and attributes are allowed; produced via `HtmlPolicyBuilder` and applied via `policy.sanitize(untrustedHTML)`.
- **[[HtmlPolicyBuilder]]**: Fluent builder for constructing custom sanitization policies; supports `allowElements()`, `allowAttributes()`, `allowUrlProtocols()`, `requireRelNofollowOnLinks()`.
- **[[Prepackaged Policies]]**: Built-in policies for common use cases: `Sanitizers.FORMATTING`, `Sanitizers.LINKS`, `Sanitizers.TABLES`, `Sanitizers.IMAGES`, `Sanitizers.INTEGERS`.
- **[[ElementPolicy]]**: Custom policy callback for renaming elements or modifying attributes during sanitization (e.g., converting `h1`–`h6` to `div` with a class).
- **[[CSS Sanitization]]**: `position:fixed` and `position:sticky` are blocked to prevent overlay attacks; full CSS is high-risk — not using CSS is the safest option.
- **[[OWASP Java Encoder]]**: Companion library for HTML escaping (distinct from sanitization); use both together for defense in depth.

## Key Takeaways

- Use prepackaged policies (`Sanitizers.FORMATTING.and(Sanitizers.LINKS)`) for common cases.
- Build custom policies with `HtmlPolicyBuilder` when specific elements/attributes are needed.
- Elements `a`, `font`, `img`, `input`, `span` must be explicitly allowed with `allowWithoutAttributes()` to pass without attributes.
- `allowUrlProtocols("data")` enables inline image data URIs — add attribute matchers to restrict to image-only data URIs.
- CSS has a large attack surface; blocking all CSS is the safest choice when not strictly required.
- Embedders of sanitized content must use `position:relative; overflow:hidden` to contain self-styling content.
- Use URL rewriting for background image URLs and set appropriate `Referrer-Policy` headers to prevent tracking.
- Available on Maven Central as `com.googlecode.owasp-java-html-sanitizer`.
