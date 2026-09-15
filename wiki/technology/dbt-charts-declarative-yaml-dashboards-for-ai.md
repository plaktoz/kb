---
type: literature-note
source_url: https://dbtcharts.com/blog/charts-built-for-chat/
author: Dave Fowler
tags: [dbt, data-visualization, ai-agents, open-source]
date_consumed: 2026-09-15
---

## Summary

dbt Labs is open-sourcing **dbt Charts**, a declarative YAML language for building interactive dashboards designed to work natively with AI/chat-based workflows. It solves the tension between AI agents generating messy multi-file codebases and traditional BI tools that restrict agents to narrow UI features. Users declare full dashboards in a single auditable YAML file, with SQL handling data retrieval and YAML defining presentation.

## Core Concepts

- **[[dbt Charts]]** — an open-source declarative language for dashboard creation using YAML, built by [[dbt Labs]]
- **[[Declarative Configuration]]** — separation of concerns: SQL defines *what* data to retrieve; YAML defines *how* to display it; [[Jinja]] handles variables and macros
- **[[AI-Native Tooling]]** — design philosophy that balances agent freedom with governance, avoiding both unconstrained code generation and overly restrictive BI tool UIs
- **[[dbt Semantic Layer]]** — planned integration that would connect dbt Charts to dbt's metrics and semantic definitions
- **[[Conversational Analytics]]** — the dbtCharts.com platform offers chat-based interaction alongside hosting, access control, and version history

## Key Takeaways

- **Single-file dashboards**: Entire interactive dashboard declared in one auditable YAML file.
- **Multi-format rendering**: Outputs SVG, HTML, PNG, PDF, or terminal via `dct render` CLI.
- **Scale of options**: 1,100+ config options across 16+ chart types with cascading styles.
- **Git-native**: `charts/` directory lives alongside `models/` in the same dbt repo.
- **Agent-friendly errors**: Strict validation with error messages designed for LLM consumption.
- **Dual offering**: Open-source language (Apache 2.0) + hosted platform (dbtCharts.com in beta).
- **Problem framing**: AI agents today produce messy HTML/CSS/JS/React; dbt Charts offers a structured middle ground.

## 🧠 First Principles & Mental Models

- **[[Separation of Concerns]]**: Splitting data retrieval (SQL) from presentation (YAML) mirrors the foundational engineering principle that keeps systems auditable and composable — exactly why this approach is more governable than agent-generated multi-file codebases.
- **[[Constraints as Enablers]]**: By limiting agents to a well-defined declarative grammar with strict validation, dbt Charts paradoxically gives agents *more* reliable capability than open-ended code generation — a narrow, well-specified interface beats a wide, ill-defined one.

## 🃏 Review Questions

**Q1**: What core problem does dbt Charts solve for AI agents building reports?
**A**: AI agents currently generate messy multi-file codebases (HTML, CSS, JS, React), while traditional BI tools are too restrictive — dbt Charts offers a single-file declarative YAML format that balances freedom with governance.

**Q2**: How does dbt Charts separate data from presentation, and what templating does it support?
**A**: SQL defines what data to retrieve while YAML defines how to display it; Jinja handles variables and macros, consistent with existing dbt conventions.

**Q3**: How can teams integrate dbt Charts into an existing dbt project, and what deployment options exist?
**A**: The `charts/` directory sits alongside `models/` in the same Git repo for local/CLI use; teams can also host on dbtCharts.com (public beta) for access control, version history, and conversational analytics.
