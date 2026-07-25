# KBM Glossary

A shared vocabulary for this vault. Claude reads this file during ingestion to resolve synonyms and link concepts consistently.

---

## A

**Andrej Karpathy** — AI researcher and educator; publicly described using an LLM wiki knowledge base as a core part of his learning system.

---

## C

**Capture** — The first step in the PKM workflow; dumping raw ideas, snippets, or links into an [[Inbox Capture]] buffer with minimal friction before any organization occurs.

**Claude Code** — Anthropic's AI coding agent CLI (`@anthropic-ai/claude-code`) with direct filesystem read/write access; used here as the ingestion engine that reads the vault and writes structured notes.

**Concept Note** — A timeless, atomic note about a single idea or entity. No dates in the content. Linked to from Source Notes. Frontmatter: `type: concept`.

**Concept Sprawl** — The anti-pattern where synonymous ideas (e.g. "sparse attention" vs. "local attention") generate duplicate Concept Notes instead of being unified under one canonical term.

---

## G

**Glossary** (`glossary.md`) — This file. Lists canonical term names and their preferred aliases so Claude creates one Concept Note per idea rather than duplicates.

**Growth Loop** — The compounding effect where each new ingested note makes future notes richer, because Claude has more vault context (existing Concept Notes, MOCs) to link against.

---

## I

**Inbox** / **Inbox Capture** — A staging folder (`Inbox/`) where new notes land before review. Keeps the main knowledge graph clean while allowing fast, low-friction capture.

**Ingestion Pipeline** — The three-step automated workflow: (1) extract raw text from a source, (2) Claude reads vault context, (3) Claude writes a structured Source Note and updates MOCs.

---

## K

**Knowledge Graph** — The network of interlinked notes that emerges from consistent use of `[[WikiLink]]` syntax across the vault.

---

## L

**Literature Note** — A note derived directly from an external source (article, video, paper). Kept separate from personal synthesis notes. Frontmatter: `type: literature-note`. Synonym: Source Note.

**LLM Wiki Knowledge Base** — A self-growing vault where every piece of consumed content is processed by an LLM into structured, interlinked notes rather than stored as raw bookmarks or highlights.

---

## M

**Maps of Content (MOC)** — Index notes that link clusters of related Concept Notes and Source Notes. Provide navigational overviews for a topic. Frontmatter: `type: moc`.

**MindStudio** — A no-code AI workflow platform; can add a team-facing trigger layer on top of the Obsidian + Claude Code ingestion pipeline without requiring infrastructure code.

---

## O

**Obsidian** — Local-first markdown note-taking app. Stores all notes as plain `.md` files on disk; Claude Code reads and writes them directly without any API integration.

---

## P

**PARA Framework** — Organizational system with four buckets: **P**rojects (active), **A**reas (ongoing responsibilities), **R**esources (reference material), **A**rchives (inactive). Used to categorize vault folders.

**Personal Knowledge Management (PKM)** — The practice of systematically capturing, connecting, and revisiting ideas so knowledge compounds over time rather than being forgotten.

**PyMuPDF** (`fitz`) — Python library for extracting text from PDF files; used in the PDF ingestion script.

---

## S

**Source Note** — A structured note derived from a single external source (URL, PDF, YouTube video). Contains Summary, Key Ideas, Quotes, and wikilinks to Concept Notes. Frontmatter: `type: source`. Synonym: Literature Note.

**Spaced Repetition** — A review technique where notes are revisited at increasing intervals to move knowledge into long-term memory; compatible with periodic vault review workflows.

---

## V

**Vault** — The root Obsidian directory containing all markdown notes, folders, and schema files.

**Vault Schema** (`_schema.md`) — The most critical configuration file. Defines note types, required frontmatter fields, section structure, and linking rules. Claude reads this on every ingestion run to ensure consistent output.

---

## W

**WikiLink** — Obsidian's `[[double-bracket]]` syntax for linking notes. Every major concept, technology, or person should be wrapped in WikiLinks to build the knowledge graph.

---

## Y

**yt-dlp** — CLI tool for downloading YouTube transcripts and subtitles; used in the YouTube ingestion extraction script.

---

## Z

**Zettelkasten** — An atomic note-taking method (originating with Niklas Luhmann) where each note captures one idea and links to related notes. The conceptual foundation of networked PKM systems like Obsidian.
