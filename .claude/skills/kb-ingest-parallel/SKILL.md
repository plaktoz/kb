---
name: kb-ingest-parallel
description: Parallel ingest of raw articles into structured wiki notes — 1 dedicated agent per file, up to 14 concurrent. Faster and higher quality than kb-ingest for large batches. Use when the user wants a parallel ingest run.
---

Run the Workflow tool with `name: "kb-ingest-parallel"`. Wait for the workflow to complete, then report the result: how many files were ingested.
