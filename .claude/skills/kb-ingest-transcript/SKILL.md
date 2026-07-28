---
name: kb-ingest-transcript
description: Full YouTube transcript pipeline — fetch URLs from raw/youtube/, download and speaker-ID each transcript, stage to raw/, parallel ingest into wiki notes, then archive. Use when the user wants to ingest YouTube videos into the knowledge base.
---

Run the Workflow tool with `name: "kb-ingest-transcript"`. Wait for the workflow to complete, then report the result: how many transcripts were ingested.
