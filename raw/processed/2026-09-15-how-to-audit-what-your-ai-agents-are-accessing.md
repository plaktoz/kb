---
source_url: https://hackernoon.com/how-to-audit-what-your-ai-agents-are-accessing
author: ameliepangolin
date: 2026-09-15
---

# How to Audit What Your AI Agents Are Accessing

The article covers Aperture, Tailscale's AI gateway product, explaining how it helps organizations monitor and control what their AI agents (Claude Code, Codex, etc.) are doing.

## Identity-Based Logging

Every request carries cryptographic identity via Tailscale — login name, device ID, and tags. Non-human agents (CI runners, background processes) get identity from their tags. Requests are grouped into sessions for contextual review.

## Data Captured Per Request

- Full request/response bodies
- HTTP headers (sensitive values redacted)
- Token counts (input/output/cached/reasoning)
- Model name, duration, tool use

Capture is asynchronous and doesn't impact performance. Retention is configurable — including down to zero — with S3-compatible export for SIEM integration.

## Access Control

Logs are "deny-by-default." A grants system scopes access by identity (`alice@example.com`), tag (`tag:ci-runner`), provider (`anthropic/**`), or model. Admin log-viewing is itself logged and auditable.

## Pre-Request Enforcement (Guardrails)

Policies run before data reaches providers: PII scrubbing, request blocking, tool-call authorization, and per-user/group spending quotas. Services can be configured to fail closed or open if guardrails are unreachable.

## Integrations

Cribl, Oso, Apollo Research, Cerbos.
