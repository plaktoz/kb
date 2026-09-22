---
source_url: https://linear.app/now/ci-bottleneck-reworked
author: Mufeez Amjad
date: 2026-09-21
---

# AI Coding Has Made CI a Bottleneck, So We Reworked Ours to Keep Up

Linear's engineering team tackled rising CI costs and slowdowns caused by AI-accelerated development. Despite their test suite nearly quadrupling in size, they reduced PR wait time from over 6 minutes to just over 5, while cutting runner time per test roughly in half.

## Key Improvements

### 1. Infrastructure & Tooling Upgrades
- Migrated from GitHub Actions to third-party runners with faster CPUs and better storage — jobs ran **34% faster** on average
- Adopted `tsgo` (native TypeScript compiler), cutting weekly median `tsc` check time by **73%**
- Rewrote type-dependent lint rules to use static AST analysis, reducing API lint time by **68%** and full-repo lint by **55%**
- Migrated to Oxlint, further reducing linting runner-minutes

### 2. Optimizing Gating Jobs
- Capped fetch depth on change-detection jobs, dropping the slowest gate from **94 seconds to 20**
- Removed unnecessary checkouts from jobs that never needed a working tree (27s → 7s)
- Built a custom retry-with-backoff checkout action using `GIT_HTTP_LOW_SPEED_LIMIT` to handle network instability
- Moved non-blocking cache writes out of the critical path, saving **42 seconds** per API PR

### 3. Reducing Repeated Setup
- Preinstalled shared dependencies (Postgres client, build headers) into a CI base image
- Restricted `pnpm install` to only the relevant package — install time dropped from **44–73s to 16–18s**
- Skipped `node_modules` caching after finding a cache hit (28s) was slower than a filtered install (~7.5s)
- Replaced full DB migration replay with schema snapshots — setup fell from **~12s to 1–2s** per container
- Consolidated 7 independent short-check jobs into 2, running tasks concurrently — saved roughly **87,000 runner-minutes/month** (~11.8% of total CI usage)

### 4. More Efficient Test Execution
- Split oversized test files to improve Vitest shard balance; moving from 4 to 8 shards made the critical job **~19% faster and 19% cheaper**
- Introduced an opt-in `isolate: false` Vitest project to share module state (entity/GraphQL/decorator graph) across files within a worker — **largest single improvement**, reducing slowest shard from ~300–379s to ~195s and cutting total API shard runner time from ~32.8 to ~22 minutes per run
- Updated agent "skills" so AI-generated tests follow the same isolation rules by default

## Compound Effect

Without these optimizations, today's test suite would take roughly **11 minutes** — nearly double the current wait. The team continues to add approximately **2,000 tests per week**, making ongoing CI efficiency work essential.
