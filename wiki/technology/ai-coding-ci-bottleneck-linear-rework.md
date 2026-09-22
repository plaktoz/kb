---
type: literature-note
source_url: https://linear.app/now/ci-bottleneck-reworked
author: Mufeez Amjad
tags: [ci-cd, software-engineering, ai-coding, developer-productivity]
date_consumed: 2026-09-22
---

## Summary

Linear's engineering team found that [[AI-Accelerated Development]] caused their test suite to nearly quadruple in size, making CI a critical bottleneck. Through a series of infrastructure, tooling, and test execution improvements, they reduced PR wait time from over 6 minutes to just over 5, while cutting runner time per test roughly in half. Without these optimizations, today's suite would take ~11 minutes — nearly double the current wait.

## Core Concepts

- [[Continuous Integration]] optimization in the context of AI-generated code
- [[GitHub Actions]] migration to third-party runners for faster CPUs and storage
- [[tsgo]] — native [[TypeScript]] compiler replacing `tsc`, slashing compile times
- [[Oxlint]] — faster linting tool replacing legacy lint pipeline
- [[Vitest]] sharding and module-state isolation for test parallelism
- [[pnpm]] selective installs and skipping `node_modules` caching
- [[Database Schema Snapshots]] as a replacement for full migration replay in CI
- [[Critical Path Optimization]] — moving non-blocking steps off the gating sequence

## Key Takeaways

- **Faster runners**: Migrating from GitHub Actions cut job times by **34%** on average.
- **Compiler speed**: `tsgo` cut weekly median `tsc` check time by **73%**.
- **Lint rewrites**: Static AST-based lint rules cut API lint time by **68%**.
- **Fetch depth cap**: Slowest gate dropped from **94s → 20s** by capping git fetch depth.
- **Install time**: Selective `pnpm install` cut setup from **44–73s down to 16–18s**.
- **Schema snapshots**: DB setup shrank from **~12s to 1–2s** per container.
- **Job consolidation**: Merging 7 short-check jobs into 2 saved ~**87,000 runner-minutes/month**.
- **Vitest isolation**: Sharing module state within workers cut slowest shard from ~**340s to ~195s**.
- **Growth rate**: Team adds ~**2,000 tests per week** — ongoing CI efficiency is essential.

## 🧠 First Principles & Mental Models

- **[[Critical Path Method]]**: Every optimization Linear made targeted jobs on the critical path (gating jobs, slowest shards) — removing non-blocking steps from the gate is the highest-leverage move, regardless of their absolute duration.
- **[[Goodhart's Law]]**: Optimizing purely for raw test count (a proxy for coverage quality) created a runaway CI cost; Linear's fix required treating test *execution efficiency* as an equal constraint alongside coverage breadth.

## 🃏 Review Questions

**Q1**: What is the core problem Linear's CI rework was solving?
**A**: AI-accelerated development caused the test suite to nearly quadruple, making CI a growing bottleneck that threatened to slow down the entire PR cycle.

**Q2**: What was the single largest performance improvement Linear achieved in test execution?
**A**: Introducing `isolate: false` in Vitest to share module state (entity/GraphQL/decorator graph) across files within a worker — cutting the slowest shard from ~300–379s to ~195s and reducing total API shard runner time from ~32.8 to ~22 minutes per run.

**Q3**: How should teams apply Linear's approach as AI coding tools generate more tests?
**A**: Treat CI efficiency as a first-class engineering concern: optimize the critical path, consolidate short jobs, use schema snapshots instead of full replays, and update AI agent "skills" to follow isolation rules so generated tests stay shard-friendly by default.
