---
source_url: https://dbtcharts.com/blog/charts-built-for-chat/
author: Dave Fowler
date: 2026-09-14
---

# Charts Built for Chat

dbt Labs is open-sourcing **dbt Charts**, a declarative YAML language for building dashboards that works natively with AI/chat-based workflows.

## The Problem

AI agents generating reports currently produce messy multi-file codebases (HTML, CSS, JS, React), while traditional BI tools constrain agents to narrow UI-exposed features. Neither option balances freedom with governance.

## The Solution

dbt Charts lets users declare full interactive dashboards in a single auditable YAML file. SQL defines *what* data to retrieve; YAML defines *how* to display it. Jinja handles variables and macros, as in dbt itself.

## Key Features

- Renders to SVG, HTML, PNG, PDF, or terminal via CLI (`dct render`)
- Over 1,100 config options across 16+ chart types
- Cascading styles (chart → board → theme)
- Deep dbt integration: `charts/` lives alongside `models/` in the same Git repo
- Strict validation with agent-friendly error messages
- Planned dbt Semantic Layer support

## Platform

Alongside the open-source language, **dbtCharts.com** launches in public beta, offering hosting, access control, conversational analytics, a visual editor, version history, and sharing with permissions.

**License:** Apache 2.0

**Install:** `uv tool install dbt-charts`
