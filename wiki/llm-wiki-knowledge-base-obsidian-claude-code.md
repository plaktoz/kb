---
type: literature-note
source_url: https://www.mindstudio.ai/blog/how-to-build-llm-wiki-knowledge-base-obsidian-claude-code
author: MindStudio
tags: [obsidian, llm, knowledge-management, claude-code]
date_consumed: 2026-07-25
---

## Summary

The article describes how to build a self-growing LLM wiki by combining [[Obsidian]]'s local markdown vault with [[Claude Code]]'s file-system awareness and three extraction scripts for YouTube, PDFs, and web pages. A vault schema file (`_schema.md`) governs note formatting, which is the single most critical piece for keeping output consistent across hundreds of ingested notes. [[Andrej Karpathy]] is cited as a practitioner of this approach, and the article provides a complete step-by-step implementation guide.

## Core Concepts

- [[Obsidian]] — local markdown vault; the "database" of structured notes
- [[Claude Code]] — AI coding agent with direct filesystem read/write access to the vault
- [[LLM Wiki Knowledge Base]] — a structured, self-growing network of interlinked notes built via AI ingestion
- [[Knowledge Graph]] — the interconnected note network that makes each new note richer than the last
- [[Maps of Content]] — MOC index notes that link clusters of related topics
- [[Vault Schema]] — `_schema.md` file defining note types, frontmatter, and linking rules
- [[Ingestion Pipeline]] — the extract → read context → write note → update MOC workflow
- [[Andrej Karpathy]] — publicly described an LLM wiki as a core part of how he learns
- [[PARA Framework]] — Sources, Concepts, MOCs, Inbox folder structure echoes PARA
- [[yt-dlp]] — CLI tool for extracting YouTube transcripts
- [[PyMuPDF]] — Python library for extracting text from PDF files
- [[MindStudio]] — no-code platform that can add a team-facing trigger layer over the pipeline

## Key Takeaways

- **Retention problem**: passive reading loses ~80% within a week; active ingestion fixes this.
- **[[Andrej Karpathy]] uses this**: LLM wiki cited as a core personal learning system.
- **Three-layer architecture**: Vault ([[Obsidian]]) → Ingestion ([[Claude Code]]) → [[Growth Loop]].
- **Vault folder structure**: `Sources/`, `Concepts/`, `MOCs/`, `Inbox/` — Inbox first for review.
- **[[Vault Schema]] is critical**: `_schema.md` is what keeps output consistent at scale.
- **Three extraction scripts**: YouTube via [[yt-dlp]], PDF via [[PyMuPDF]], URL via BeautifulSoup.
- **Single command ingestion**: `ingest.sh` wraps all scripts + [[Claude Code]] prompt call.
- **Teach Claude your vocabulary**: `glossary.md` prevents concept sprawl from synonym drift.
- **Periodic synthesis**: run a synthesis prompt every few weeks to merge and relink concepts.
- **Large PDFs**: chunk documents exceeding the context window; merge notes afterward.
- **Duplicate detection**: [[Claude Code]] should check source URL against existing frontmatter.
- **[[MindStudio]]**: adds no-code trigger layer for team knowledge bases without infrastructure code.
