---
type: literature-note
source_url: https://cloud.google.com/blog/products/data-analytics/whats-new-in-managed-service-for-apache-spark-4-0
author: Meera Srinivasan
tags: [apache-spark, google-cloud, lakehouse, data-engineering]
date_consumed: 2026-11-22
---

## Summary
Google announces general availability of Managed Service for [[Apache Spark]] 4.0, a runtime built on Spark 4.2, Java 25, Python 3.13 and [[Apache Iceberg]] 1.12 for serverless and managed clusters. The release pairs a redesigned console with an AI agent that diagnoses failed jobs, IDE setup through the [[Data Agent Kit]], and the [[Lightning Engine]] native execution engine. Google positions the platform as part of its [[Lakehouse]], where Spark, [[BigQuery]] and AlloyDB read and write the same Iceberg tables.

## Core Concepts
- **Apache Spark 4.2 runtime**: Ships with Spark Declarative Pipelines, Real-Time Mode, Delta Lake 4.4 and Scala 2.13.
- **Agentic troubleshooting**: An AI agent analyzes logs, metrics and query plans to recommend fixes, within existing IAM permissions.
- **Data Agent Kit**: Configures [[Model Context Protocol]] servers, skills and API access for VS Code, [[Claude Code]] and Antigravity.
- **Lightning Engine**: A native C++ vectorized engine built on Apache Gluten and Velox, compiling Spark query plans into native SIMD instructions.
- **Lakehouse runtime catalog**: Replaces the legacy Hive Metastore as the default catalog, surfacing tables in [[Knowledge Catalog]].
- **Serverless capacity**: Infrastructure fungibility across VM families and zones, with quotas set in Data Compute Units (DCUs).

## Key Takeaways
- **Runtime Upgrade**: Spark 4.2, Java 25, Python 3.13 and Iceberg 1.12 now generally available.
- **Agentic Troubleshooting**: AI agent diagnoses failed or slow jobs and recommends a fix.
- **IDE Integration**: Data Agent Kit sets up MCP servers and skills for VS Code and Claude Code.
- **Lightning Engine**: Google claims up to 3.25x price-performance over a leading Spark alternative.
- **Faster Startups**: Serverless Premium tier starts faster at no additional cost.
- **Capacity Fallback**: Serverless jobs switch VM families when preferred capacity is constrained.
- **DCU Quotas**: One unified quota replaces separate per-machine-family CPU quotas.
- **Shared Tables**: Spark, BigQuery and AlloyDB read and write the same Iceberg tables without copies.

## 🃏 Review Questions

**Q1**: What is the core announcement in this post?
**A**: Managed Service for Apache Spark 4.0 is generally available, with a new runtime, a redesigned console, IDE integration and faster serverless performance.

**Q2**: How does the release reduce operational work for data teams?
**A**: An AI agent diagnoses failed or slow jobs, and serverless capacity can fall back to other VM families and zones instead of failing the job.

**Q3**: What does this imply for teams using several engines?
**A**: Spark and BigQuery can share the same Iceberg tables through the Lakehouse runtime catalog, which avoids ETL pipelines and data copies, according to Google.
