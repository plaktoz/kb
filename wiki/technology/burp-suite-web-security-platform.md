---
type: literature-note
source_url: https://portswigger.net/burp
author: Unknown
tags: [web-security, penetration-testing, dast, appsec]
date_consumed: 2026-08-20
---

## Summary

PortSwigger's Burp Suite is the leading web penetration testing toolkit, offering a product line that spans manual pentesting for security professionals, enterprise-grade automated [[DAST]] scanning for AppSec teams, and CI-integrated scanning for DevOps workflows. The platform also includes an agentic AI extension (Burp AT) that augments human-led pentesting, plus a free community edition and Web Security Academy for learners. Together these products form a unified ecosystem covering the full spectrum of web application security testing.

## Core Concepts

- **[[Burp Suite]]** — the central product family from [[PortSwigger]] for web application security testing
- **[[Burp AT]]** — agentic AI layer that extends human-led pentesting with automated reasoning
- **[[Dynamic Application Security Testing]] (DAST)** — Burp Suite DAST provides enterprise-scale automated vulnerability scanning
- **[[CI/CD Security Integration]]** — scanning embedded in developer pipelines to catch vulnerabilities before production
- **[[OWASP Vulnerability Classes]]** — platform covers [[XSS]], [[SQL Injection]], [[CSRF]], [[XXE]], [[Directory Traversal]], and [[SSRF]]
- **[[Web Security Academy]]** — free learning platform bundled with the PortSwigger ecosystem targeting beginner-to-intermediate security learners

## Key Takeaways

- **Audience segmentation**: Four distinct tiers — pentesters, AppSec/vuln management, DevOps engineers, and learners.
- **Agentic AI extension**: Burp AT adds AI-driven automation on top of human-led manual testing.
- **Enterprise DAST**: Burp Suite DAST targets scalable, CI-driven automated scanning for AppSec teams.
- **Free entry point**: Community Edition and Web Security Academy provide zero-cost access for learners.
- **Vulnerability breadth**: Covers critical web classes including XSS, SQLi, CSRF, XXE, path traversal, and SSRF.
- **Market position**: PortSwigger claims Burp Suite is the world's #1 web penetration testing toolkit.

## 🧠 First Principles & Mental Models

- **[[Separation of Concerns]]**: PortSwigger cleanly separates manual pentesting (professional), automated scanning (DAST), and developer-integrated scanning into distinct products — each optimized for its user's workflow rather than forcing one tool to serve all audiences.
- **[[Shift Left Security]]**: CI-integrated scanning reflects the shift-left principle — moving vulnerability detection earlier in the development lifecycle reduces the cost and blast radius of defects.

## 🃏 Review Questions

**Q1**: What is Burp Suite and who makes it?
**A**: Burp Suite is a web penetration testing toolkit made by PortSwigger, positioned as the world's #1 tool in its category, with products targeting pentesters, AppSec teams, DevOps pipelines, and learners.

**Q2**: What does Burp AT add to the existing Burp Suite lineup?
**A**: Burp AT is an agentic AI layer that extends human-led pentesting with automated AI reasoning, rather than replacing the human tester entirely.

**Q3**: How would a DevOps team integrate Burp Suite into their workflow?
**A**: They would use Burp Suite DAST, which supports CI-driven automated scanning so vulnerabilities are caught before code reaches production.
