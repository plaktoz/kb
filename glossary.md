# KBM Glossary

A shared vocabulary for this vault. Claude reads this file during ingestion to resolve synonyms and link concepts consistently.

---

## A

**A2A** — Google's agent-to-agent communication protocol; handles task delegation between AI agents from different vendors; absorbed [[ACP]] in 2026 to become the standard for inter-agent interoperability alongside Anthropic's [[MCP]].

**ACP** — Agent Communication Protocol; initially a separate specification for agent-to-agent messaging; merged into [[A2A]] (Google) in 2026.

**Andrej Karpathy** — AI researcher and educator; publicly described using an LLM wiki knowledge base as a core part of his learning system.

**Anki** — Spaced repetition flashcard application; used in the LLM-assisted reading workflow to generate and review flashcards from reading sessions via [[fastanki]].

**Auto-Memory** — Claude Code feature that automatically saves contextual memories without manual `/remember` triggers; part of the context engineering shift toward judgment-oriented guidance.

---

## B

**Barbara Oakley** — Engineering professor and author of *A Mind for Numbers*; popularized the focused/diffuse mode framework showing the brain requires both deliberate analysis and relaxed mind-wandering to consolidate learning.

**Beth Hammack** — Federal Reserve official; cited in July 2026 vault notes as warning of broad-based inflation ahead of an expected September 2026 rate hike.

**Body, Heart and Mind in Business Research Group** — Research group at the University of Sydney Business School led by [[Stefan Volk]]; studies chronobiology and its application to management and organizational performance.

**Botsitting** — [[Cal Newport]]'s term for the low-value overhead of attending to AI outputs — correcting errors, rerunning prompts, managing tool failures — that consumes the time AI was supposed to free up; a key driver of the AI productivity gap.

**Buffett Indicator** — The ratio of total stock market capitalization to GDP; popularized by [[Warren Buffett]] as a long-run valuation signal; hit an all-time high of 236% in mid-2026, exceeding dot-com era peaks.

**ByteByteGo** — System design newsletter and YouTube channel by Alex Xu; publishes distilled technical reference guides on distributed systems, APIs, and AI engineering; primary source for vault notes on multi-tenancy and AI agent best practices.

---

## C

**Cal Newport** — Georgetown professor and author of *Deep Work* and *Slow Productivity*; vault's primary voice on the AI productivity gap, [[Botsitting]], and the structural mismatch between AI capabilities and broken organizational workflows.

**Capture** — The first step in the PKM workflow; dumping raw ideas, snippets, or links into an [[Inbox Capture]] buffer with minimal friction before any organization occurs. ⚠️ *No vault WikiLinks as of 2026-07-27.*

**Chesterton's Fence** — The principle that one should not remove or modify something until understanding why it was put there; named after [[G.K. Chesterton]]'s parable about a gate on a road; not a defense of the status quo but a prerequisite for effective reform.

**Clem Delangue** — Co-founder and CEO of [[Hugging Face]]; responded to the 2026 OpenAI-on-Hugging Face security breach with a $100M open-source compute pledge and a call for radical AI industry transparency.

**Claude 5** — Generation of Anthropic's Claude models with significantly improved contextual judgment; includes [[Opus 5]], [[Fable 5]], and related variants. Characterized by a shift from rule-following to context-reading behavior.

**Claude Code** — Anthropic's AI coding agent CLI (`@anthropic-ai/claude-code`) with direct filesystem read/write access; used here as the ingestion engine that reads the vault and writes structured notes.

**Codeex** — Automation tool used in the Karpathy-style PKM workflow; runs hourly to process raw files from `/raw`, update the wiki, and push commits to the repository.

**Concept Note** — A timeless, atomic note about a single idea or entity. No dates in the content. Linked to from Source Notes. Frontmatter: `type: concept`.

**Concept Sprawl** — The anti-pattern where synonymous ideas (e.g. "sparse attention" vs. "local attention") generate duplicate Concept Notes instead of being unified under one canonical term.

---

## D

**Dario Amodei** — CEO of Anthropic; cited in vault as an example of overconfident AI timeline forecasting (predicted AI would write 90% of code by 2025).

**David Autor** — MIT economist; research shows generative AI shortens time for novices to gain basic competence without closing the underlying performance gap between novices and experts.

---

## F

**Fable 5** — A Claude 5-generation model from Anthropic; part of the improved-judgment model family referenced in vault context engineering notes.

**fastanki** — fast.ai Python library for generating [[Anki]] flashcards from LLM-assisted reading sessions; part of the close reading workflow documented in vault.

**Federal Reserve** — U.S. central bank; referenced in vault for its July 2026 rate hold decision and projected September 2026 rate hike amid broad-based inflation signals.

---

## G

**Geoffrey Hinton** — AI researcher and Turing Award winner; cited in vault as an example of overconfident AI capability forecasting (2021 prediction that AI would soon replace radiologists).

**Glossary** (`glossary.md`) — This file. Lists canonical term names and their preferred aliases so Claude creates one Concept Note per idea rather than duplicates.

**Goodhart's Law** — Principle stating "when a measure becomes a target, it ceases to be a good measure"; applied in vault to AI ed-tech systems that optimize test metrics at the expense of genuine learning.

**Growth Loop** — The compounding effect where each new ingested note makes future notes richer, because Claude has more vault context (existing Concept Notes, MOCs) to link against.

---

## H

**Hive-32B** — Prentis's proprietary computer-use AI model; claimed to outperform GPT-5.4 and Claude Opus 4.6 on computer-use benchmarks at 10x lower cost per task.

---

## I

**Inbox** / **Inbox Capture** — A staging folder (`Inbox/`) where new notes land before review. Keeps the main knowledge graph clean while allowing fast, low-friction capture.

**Ingestion Pipeline** — The three-step automated workflow: (1) extract raw text from a source, (2) Claude reads vault context, (3) Claude writes a structured Source Note and updates MOCs.

---

## J

**Jeremy Howard** — Co-founder of fast.ai; advocates LLM-assisted close reading as a method for deep learning, and warns against outsourcing all thinking to AI.

**Johno Whitaker** — fast.ai team member; co-developed the [[SolveIt Platform]] workflow for LLM-assisted reading; coined the "architect's pencils" analogy for the upfront setup cost of the reading workflow.

---

## K

**Knowledge Graph** — The network of interlinked notes that emerges from consistent use of `[[WikiLink]]` syntax across the vault.

---

## L

**Literature Note** — A note derived directly from an external source (article, video, paper). Kept separate from personal synthesis notes. Frontmatter: `type: literature-note`. Synonym: Source Note.

**Liz Fosslien** — HBR author and illustrator focused on emotions at work and organizational behavior; co-authored vault notes on AI-driven management bottlenecks with [[Mollie West Duffy]].

**LLM Wiki Knowledge Base** — A self-growing vault where every piece of consumed content is processed by an LLM into structured, interlinked notes rather than stored as raw bookmarks or highlights.

---

## M

**Maps of Content (MOC)** — Index notes that link clusters of related Concept Notes and Source Notes. Provide navigational overviews for a topic. Frontmatter: `type: moc`.

**Mark Pincus** — Zynga co-founder; co-founded [[Prentis]] AI lab in April 2026 with [[Reid Hoffman]] and Ritankar Das.

**METR Study** — Research study on AI-assisted developer productivity; found developers using AI believed they were 20% faster but were actually 19% slower — a ~40% perception-reality gap. Cited as evidence against vibe coding.

**MindStudio** — A no-code AI workflow platform; can add a team-facing trigger layer on top of the Obsidian + Claude Code ingestion pipeline without requiring infrastructure code.

**Mollie West Duffy** — HBR author on organizational behavior and workplace wellness; co-authored vault notes on AI-driven management bottlenecks with [[Liz Fosslien]].

---

## N

**No Child Left Behind** — U.S. federal education law; cited in vault as the policy that spread high-stakes testing nationally, narrowing curricula in ways analogous to AI ed-tech metric-optimization.

---

## O

**Obsidian** — Local-first markdown note-taking app. Stores all notes as plain `.md` files on disk; Claude Code reads and writes them directly without any API integration.

**Obsidian Web Clipper** — Chrome browser extension that drops web articles and YouTube transcripts directly into the `/raw` capture folder; part of the PKM input layer.

**Opus 5** — A Claude 5-generation model from Anthropic; part of the improved-judgment model family referenced in vault context engineering notes.

---

## P

**PARA Framework** — Organizational system with four buckets: **P**rojects (active), **A**reas (ongoing responsibilities), **R**esources (reference material), **A**rchives (inactive). Used to categorize vault folders.

**Personal Knowledge Management (PKM)** — The practice of systematically capturing, connecting, and revisiting ideas so knowledge compounds over time rather than being forgotten.

**Prentis** — AI lab founded April 2026 by Ritankar Das, [[Reid Hoffman]], and [[Mark Pincus]]; targets routine office workflow automation via computer-use models for paper-heavy industries (insurance, healthcare, manufacturing).

**PyMuPDF** (`fitz`) — Python library for extracting text from PDF files; used in the PDF ingestion script.

---

## R

**Rachel Thomas** — Co-founder of fast.ai; data scientist and educator; authored vault notes critiquing vibe coding, documenting LLM-assisted reading workflows, and analyzing AI ed-tech harms.

**Reid Hoffman** — LinkedIn co-founder; co-founded [[Prentis]] AI lab in April 2026 with [[Mark Pincus]] and Ritankar Das.

**Rystad Energy** — Energy research and consultancy firm; cited in vault for warning of significant oil price rebound risk absent a Middle East ceasefire.

---

## S

**Second Brain** — Methodology for building an external digital system that stores, organizes, and surfaces personal knowledge; conceptual precursor to the LLM wiki knowledge base approach.

**SolveIt Platform** — fast.ai's interactive LLM reading environment; used by [[Jeremy Howard]] and [[Johno Whitaker]] for LLM-assisted close reading and question-driven inquiry.

**Source Note** — A structured note derived from a single external source (URL, PDF, YouTube video). Contains Summary, Key Ideas, Quotes, and wikilinks to Concept Notes. Frontmatter: `type: source`. Synonym: Literature Note.

**Spaced Repetition** — A review technique where notes are revisited at increasing intervals to move knowledge into long-term memory; compatible with periodic vault review workflows.

**Stefan Volk** — Professor of Management at the University of Sydney Business School; researches chronobiology and its application to organizational scheduling and management performance.

---

## T

**ToolSearch** — Deferred tool-discovery pattern in Claude Code; tool definitions are loaded into context on demand rather than upfront, reducing context window bloat.

---

## V

**Vault** — The root Obsidian directory containing all markdown notes, folders, and schema files.

**Vault Schema** (`_schema.md`) — The most critical configuration file. Defines note types, required frontmatter fields, section structure, and linking rules. Claude reads this on every ingestion run to ensure consistent output.

**Vibe Coding** — Generating large volumes of AI-written code not intended for human review or understanding; described in vault as creating an illusion of productivity with evidence showing 19% speed loss despite perceived 20% gain.

**VIX** — CBOE Volatility Index; measures implied volatility of S&P 500 options; used in vault as a real-time gauge of equity market fear and geopolitical risk sensitivity.

---

## W

**WikiLink** — Obsidian's `[[double-bracket]]` syntax for linking notes. Every major concept, technology, or person should be wrapped in WikiLinks to build the knowledge graph.

---

## Y

**Yann LeCun** — Chief AI Scientist at Meta; referenced in vault as a researcher whose dense academic papers benefit from LLM-assisted close reading workflows.

**yt-dlp** — CLI tool for downloading YouTube transcripts and subtitles; used in the YouTube ingestion extraction script.

---

## Z

**Zettelkasten** — An atomic note-taking method (originating with Niklas Luhmann) where each note captures one idea and links to related notes. The conceptual foundation of networked PKM systems like Obsidian.
