---
type: literature-note
source_url: https://owasp.org/www-project-web-security-testing-guide/
author: Elie Saad, Rick Mitchell
tags: [owasp, web-security, penetration-testing, cybersecurity]
date_consumed: 2026-08-20
---

## Summary

The OWASP Web Security Testing Guide (WSTG) is the leading open-source reference for testing the security of web applications, maintained collaboratively by cybersecurity professionals under CC BY-SA 4.0. It provides structured test scenarios — each identified by a `WSTG-<category>-<number>` code — giving penetration testers and developers a shared, reproducible methodology. The stable release is v4.2 (2020), with v5.0 currently in development.

## Core Concepts

- **[[OWASP]]** (Open Worldwide Application Security Project) — the nonprofit that publishes WSTG as a community-driven resource
- **[[Web Application Security Testing]]** — systematic evaluation of web apps for vulnerabilities using defined test cases
- **[[Penetration Testing]]** — structured, adversarial testing methodology that WSTG formalises for practitioners
- **[[Scenario Identifier Format]]** — each test uses `WSTG-<category>-<number>` (e.g., `WSTG-INFO-02`); cross-version references include the version number
- **[[OWASP ASVS]]** — related OWASP standard (Application Security Verification Standard) that complements WSTG
- **[[Collaborative Open-Source Security]]** — WSTG is maintained via GitHub, with community contributions welcomed through issues and pull requests

## Key Takeaways

- **Stable release:** WSTG v4.2 released 2020-12-03; v5.0 in active development.
- **Scenario codes:** Format `WSTG-<category>-<number>` enables precise cross-referencing of test cases.
- **Version-stable refs:** Include version in IDs (`WSTG-<version>-<category>-<number>`) for durable citations.
- **Availability:** Distributed as web-hosted content and downloadable PDF.
- **License:** CC BY-SA 4.0 — freely shareable and adaptable with attribution.
- **Contribution model:** Open GitHub repo; issues and PRs welcomed from the community.
- **Audience:** Web application developers and security professionals / pen testers worldwide.

## 🧠 First Principles & Mental Models

- **[[Checklists as Cognitive Offload]]**: WSTG externalises the complexity of comprehensive security testing into a shared checklist, reducing the cognitive burden on individual testers and raising the floor of coverage across teams.

## 🃏 Review Questions

**Q1**: What is the OWASP Web Security Testing Guide and who is it for?
**A**: WSTG is the premier open-source cybersecurity testing resource for web applications, used globally by penetration testers and developers to apply a standardised set of best-practice test scenarios.

**Q2**: What is the scenario identifier format used in WSTG, and why does the recommended format include version?
**A**: Each test uses `WSTG-<category>-<number>` (e.g., `WSTG-INFO-02`); including the version (`WSTG-<version>-<category>-<number>`) ensures references remain unambiguous when citing across different guide versions.

**Q3**: How can practitioners contribute to the WSTG, and what is the current development status?
**A**: Contributions are made via the official GitHub repository at github.com/OWASP/wstg through issues and pull requests; the stable release is v4.2, with v5.0 currently under development.
