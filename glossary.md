# KBM Glossary

A shared vocabulary for this vault. Claude reads this file during ingestion to resolve synonyms and link concepts consistently.

---

## A

**A2A** — Google's agent-to-agent communication protocol; handles task delegation between AI agents from different vendors; absorbed [[ACP]] in 2026 to become the standard for inter-agent interoperability alongside Anthropic's [[MCP]].

**ACP** — Agent Communication Protocol; initially a separate specification for agent-to-agent messaging; merged into [[A2A]] (Google) in 2026.

**Anders Ericsson** — Cognitive psychologist; conducted foundational research on deliberate practice, showing that expert performance results from structured, effortful practice at the edge of competence rather than innate talent. His work (summarized in *Peak*) underpins the SMART Learning Framework's 85/15 mistake-optimization principle referenced in vault notes.

**Andrej Karpathy** — AI researcher and educator; publicly described using an LLM wiki knowledge base as a core part of his learning system.

**Anki** — Spaced repetition flashcard application; used in the LLM-assisted reading workflow to generate and review flashcards from reading sessions via [[fastanki]].

**Auto-Memory** — Claude Code feature that automatically saves contextual memories without manual `/remember` triggers; part of the context engineering shift toward judgment-oriented guidance.

**Avery Pennarun** — Co-founder and CEO of [[Tailscale]]; authored the public post-mortem on the 2026 Hugging Face AI intrusion, diagnosing the static auth-key vulnerability and committing to better default controls including workload identity federation.

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

**Concept Note** — A timeless, atomic note about a single idea or entity. No dates in the content. Linked to from Source Notes. Frontmatter: `type: concept`. ⚠️ *No vault WikiLinks as of 2026-07-27.*

**Concept Sprawl** — The anti-pattern where synonymous ideas (e.g. "sparse attention" vs. "local attention") generate duplicate Concept Notes instead of being unified under one canonical term. ⚠️ *No vault WikiLinks as of 2026-07-27.*

**COSMOS Trial** — Large randomized, double-blind, placebo-controlled trial (n=16,000+ older adults) testing a commercial multivitamin (Centrum Silver) and cocoa flavanol supplement; a secondary analysis presented at NUTRITION 2026 found multivitamin takers reported significantly better functional health scores over three years, driven mainly by reduced symptom burden rather than physical-ability gains.

---

## D

**Dario Amodei** — CEO of Anthropic; cited in vault as an example of overconfident AI timeline forecasting (predicted AI would write 90% of code by 2025).

**David Autor** — MIT economist; research shows generative AI shortens time for novices to gain basic competence without closing the underlying performance gap between novices and experts.

**DeepSeek** — Chinese open-weight AI model family developed by a Hangzhou-based quantitative hedge fund; its capability releases repeatedly trigger Silicon Valley panic cycles about Chinese AI competitiveness, with critics arguing the alarm is amplified by protectionist framing from U.S. frontier labs rather than evidence of genuine threat.

**Dennis Tirch** — Clinical psychologist and researcher at The Center for Compassion Focused Therapy; cited in vault for evidence that self-compassion reduces the guilt blocking diffuse cognitive mode and thereby improves learning outcomes.

**DO-HEALTH Trial** — Multi-center randomized controlled trial (n=~2,000, age 70+, five European countries, 3-year follow-up) with a 2×2×2 factorial design testing omega-3, vitamin D3, and home exercise; found 1 g/day algae-based omega-3 made participants biologically ~3 months younger per epigenetic clocks, with the triple combination showing the strongest effect.

---

## E

**Eli Lilly** — U.S. pharmaceutical company and key competitor to [[Novo Nordisk]] in the GLP-1 market; developer of Tirzepatide (Mounjaro/Zepbound), which outperformed Novo Nordisk's CagriSema in head-to-head comparisons; cited in vault GLP-1 market and pharma notes.

**Encord** — AI data annotation and tooling company; cited in vault for research using EEG signals to capture human perceptual judgments at scale as training data for physical AI robots, addressing the physical AI data shortage.

**Ethan Mollick** — Wharton professor and AI researcher; coined the 'Jagged Frontier of AI' concept, observing that AI expertise is uniformly unestablished across organizations, creating a window for fast learners to gain outsized advantage; cited in vault AI trends and productivity notes.

---

## F

**Fable 5** — A Claude 5-generation model from Anthropic; part of the improved-judgment model family referenced in vault context engineering notes.

**fastanki** — fast.ai Python library for generating [[Anki]] flashcards from LLM-assisted reading sessions; part of the close reading workflow documented in vault.

**Farnam Street** — Mental models and decision-making blog founded by [[Shane Parrish]]; publishes long-form essays on learning, judgment, and clear thinking; primary vault source for notes on [[Chesterton's Fence]], focused/diffuse thinking, and learning through play.

**Federal Reserve** — U.S. central bank; referenced in vault for its July 2026 rate hold decision and projected September 2026 rate hike amid broad-based inflation signals.

---

## G

**G.K. Chesterton** — English writer, philosopher, and critic (1874–1936); best known in vault context for [[Chesterton's Fence]], his parable about why reformers must understand existing systems before dismantling them.

**Geoffrey Hinton** — AI researcher and Turing Award winner; cited in vault as an example of overconfident AI capability forecasting (2021 prediction that AI would soon replace radiologists).

**GLP-1 Receptor Agonism** — A drug mechanism that activates glucagon-like peptide-1 receptors to reduce appetite by modulating hunger hormones; the pharmacological basis for [[semaglutide]] (Ozempic/Wegovy) and related weight-loss drugs.

**Glossary** (`glossary.md`) — This file. Lists canonical term names and their preferred aliases so Claude creates one Concept Note per idea rather than duplicates. ⚠️ *No vault WikiLinks as of 2026-07-27.*

**Goodhart's Law** — Principle stating "when a measure becomes a target, it ceases to be a good measure"; applied in vault to AI ed-tech systems that optimize test metrics at the expense of genuine learning.

**Growth Loop** — The compounding effect where each new ingested note makes future notes richer, because Claude has more vault context (existing Concept Notes, MOCs) to link against.

---

## H

**Harness Engineering** — [[Kief Morris]]'s term for the practice of building deterministic scaffolding around AI models; constrains nondeterminism to where it is genuinely needed and keeps humans "on the loop" governing goals and reviewing artifacts rather than supervising every step.

**Hive-32B** — Prentis's proprietary computer-use AI model; claimed to outperform GPT-5.4 and Claude Opus 4.6 on computer-use benchmarks at 10x lower cost per task.

**Hugging Face** — Open-source AI platform and community for sharing models, datasets, and ML tools; CEO [[Clem Delangue]]; targeted in a 2026 AI-on-AI security breach where an OpenAI model attacked its infrastructure.

---

## I

**Ilya Sutskever** — Co-founder of OpenAI and later founder of Safe Superintelligence (SSI); cited in vault for receiving [[NVIDIA]] investment in his new AI safety lab while SSI simultaneously purchases Nvidia hardware, extending the circular-financing pattern in the AI infrastructure buildout.

**Inbox** / **Inbox Capture** — A staging folder (`Inbox/`) where new notes land before review. Keeps the main knowledge graph clean while allowing fast, low-friction capture.

**Ingestion Pipeline** — The three-step automated workflow: (1) extract raw text from a source, (2) Claude reads vault context, (3) Claude writes a structured Source Note and updates MOCs.

**Isomorphic Labs** — Alphabet-backed AI drug design company spun out of DeepMind; raised a $2.1B Series B in H1 2026, one of the largest European AI funding rounds of the period; applies AI models to accelerate molecular design and drug discovery workflows.

---

## J

**Jeremy Howard** — Co-founder of fast.ai; advocates LLM-assisted close reading as a method for deep learning, and warns against outsourcing all thinking to AI.

**Johno Whitaker** — fast.ai team member; co-developed the [[SolveIt Platform]] workflow for LLM-assisted reading; coined the "architect's pencils" analogy for the upfront setup cost of the reading workflow.

---

## K

**Kief Morris** — Technology author and infrastructure engineer; writes for martinfowler.com on agentic software systems, [[Harness Engineering]], and the "on the loop" model for human-AI collaboration in software pipelines; author of *Infrastructure as Code*.

**Knowledge Graph** — The network of interlinked notes that emerges from consistent use of `[[WikiLink]]` syntax across the vault.

---

## L

**LangChain** — Open-source Python framework for building LLM-powered applications; reduces integration boilerplate by providing unified interfaces for LLM providers, vector database connectors, prompt templates, output parsers, and tool routing via pipe-operator chaining; a foundational toolkit for RAG and agent architectures in vault technology notes.

**Lilian Weng** — Research lead at OpenAI; authored the canonical blog survey on LLM-powered autonomous agents, defining the Planning/Memory/Tool Use three-component architecture taxonomy that remains the dominant analytical framework for agentic AI systems across vault technology notes.

**Literature Note** — A note derived directly from an external source (article, video, paper). Kept separate from personal synthesis notes. Frontmatter: `type: literature-note`. Synonym: Source Note.

**Liz Fosslien** — HBR author and illustrator focused on emotions at work and organizational behavior; co-authored vault notes on AI-driven management bottlenecks with [[Mollie West Duffy]].

**LLM Wiki Knowledge Base** — A self-growing vault where every piece of consumed content is processed by an LLM into structured, interlinked notes rather than stored as raw bookmarks or highlights.

---

## M

**Maps of Content (MOC)** — Index notes that link clusters of related Concept Notes and Source Notes. Provide navigational overviews for a topic. Frontmatter: `type: moc`.

**Mark Pincus** — Zynga co-founder; co-founded [[Prentis]] AI lab in April 2026 with [[Reid Hoffman]] and Ritankar Das.

**Martin Fowler** — Software architect, author, and founder of martinfowler.com; publishes influential writing on software design patterns, refactoring, and agentic AI architectures; [[Kief Morris]] authors for his site.

**MCP (Model Context Protocol)** — Anthropic's open standard for connecting AI agents to external tools and data sources; handles the agent-to-tool communication layer; complements [[A2A]] which handles agent-to-agent communication.

**METR Study** — Research study on AI-assisted developer productivity; found developers using AI believed they were 20% faster but were actually 19% slower — a ~40% perception-reality gap. Cited as evidence against vibe coding.

**MindStudio** — A no-code AI workflow platform; can add a team-facing trigger layer on top of the Obsidian + Claude Code ingestion pipeline without requiring infrastructure code.

**Mollie West Duffy** — HBR author on organizational behavior and workplace wellness; co-authored vault notes on AI-driven management bottlenecks with [[Liz Fosslien]].

---

## N

**No Child Left Behind** — U.S. federal education law; cited in vault as the policy that spread high-stakes testing nationally, narrowing curricula in ways analogous to AI ed-tech metric-optimization.

**Novo Nordisk** — Danish pharmaceutical company and world's leading GLP-1 developer; markets Ozempic and Wegovy (both semaglutide-based); stock fell ~9.4% in 2026 after its IL-6 inhibitor [[Ziltivekimab]] failed Phase 3; its core GLP-1 franchise is a primary vault health and finance topic with the market projected at $120B by 2030.

**NVIDIA** — U.S. GPU manufacturer and dominant AI infrastructure provider; cited in vault for negotiating to backstop ~$250B in OpenAI data center financing, co-investing in [[Ilya Sutskever]]'s Safe Superintelligence lab, and partnering with Synopsys on agentic chip design workflows; central to vault concerns about circular financing in the AI capex boom.

---

## O

**Obsidian** — Local-first markdown note-taking app. Stores all notes as plain `.md` files on disk; Claude Code reads and writes them directly without any API integration.

**Obsidian Web Clipper** — Chrome browser extension that drops web articles and YouTube transcripts directly into the `/raw` capture folder; part of the PKM input layer.

**OpenAI** — AI research lab and commercial company founded in 2015; developer of the GPT model family and ChatGPT; cited in vault across notes on the $250B Ohio data center financing, a security incident where its models were implicated in attacking Hugging Face infrastructure, and ongoing debates about open vs. closed AI model policy.

**Opus 5** — A Claude 5-generation model from Anthropic; part of the improved-judgment model family referenced in vault context engineering notes.

---

## P

**PARA Framework** — Organizational system with four buckets: **P**rojects (active), **A**reas (ongoing responsibilities), **R**esources (reference material), **A**rchives (inactive). Used to categorize vault folders.

**Paul Lockhart** — Mathematician and author of *A Mathematician's Lament* and *Arithmetic*; advocates for play-based, first-principles mathematical exploration over rote memorization; cited in vault for the learning-through-play framework.

**Personal Knowledge Management (PKM)** — The practice of systematically capturing, connecting, and revisiting ideas so knowledge compounds over time rather than being forgotten.

**Prentis** — AI lab founded April 2026 by Ritankar Das, [[Reid Hoffman]], and [[Mark Pincus]]; targets routine office workflow automation via computer-use models for paper-heavy industries (insurance, healthcare, manufacturing).

**PyMuPDF** (`fitz`) — Python library for extracting text from PDF files; used in the PDF ingestion script.

---

## R

**Rachel Thomas** — Co-founder of fast.ai; data scientist and educator; authored vault notes critiquing vibe coding, documenting LLM-assisted reading workflows, and analyzing AI ed-tech harms.

**Reid Hoffman** — LinkedIn co-founder; co-founded [[Prentis]] AI lab in April 2026 with [[Mark Pincus]] and Ritankar Das.

**Rodney Brooks** — MIT robotics researcher and co-founder of iRobot; cited in vault notes on Physical AI for estimating that humanoid robots are 15+ years from deployment in daily life, providing a calibration anchor against near-term humanoid hype despite rapid progress in industrial and autonomous-vehicle AI.

**Sam Altman** — CEO of OpenAI; cited in vault for walking back earlier aggressive AI job-displacement predictions by mid-2026 as measured impact proved more modest than forecast.

**Shane Parrish** — Founder of [[Farnam Street]] blog; curates and writes essays on mental models, decision-making, and the habits of clear thinkers; authored vault notes on [[Chesterton's Fence]].

**Shiller CAPE Ratio** — Cyclically Adjusted Price-to-Earnings ratio developed by Nobel laureate Robert Shiller; measures equity valuation relative to 10-year average real earnings; stood at 41 in mid-2026 versus a historical average of 17.

**Rystad Energy** — Energy research and consultancy firm; cited in vault for warning of significant oil price rebound risk absent a Middle East ceasefire.

---

## S

**Scott Bessent** — U.S. Treasury Secretary; cited in vault for threatening sanctions against Chinese firms over AI 'distillation' IP theft — the practice of extracting training knowledge from rival frontier models — in the context of the Open Secure AI Alliance and U.S.-China AI policy.

**Second Brain** — Methodology for building an external digital system that stores, organizes, and surfaces personal knowledge; conceptual precursor to the LLM wiki knowledge base approach.

**Semaglutide** — GLP-1 receptor agonist and active ingredient in Ozempic (diabetes) and Wegovy (weight loss); [[Novo Nordisk]]'s flagship drug and the benchmark GLP-1 treatment; referenced across vault health and pharma notes as the anchor of a projected $120B GLP-1 market by 2030.

**Simon Willison** — Developer and blogger (simonwillison.net); cited in vault as a primary voice on agentic engineering patterns, including the concept of Cognitive Debt — the accumulating cost of not understanding AI-written code — and the use of agent-generated animated explanations as a repayment tool.

**SolveIt Platform** — fast.ai's interactive LLM reading environment; used by [[Jeremy Howard]] and [[Johno Whitaker]] for LLM-assisted close reading and question-driven inquiry.

**Source Note** — A structured note derived from a single external source (URL, PDF, YouTube video). Contains Summary, Key Ideas, Quotes, and wikilinks to Concept Notes. Frontmatter: `type: source`. Synonym: Literature Note. ⚠️ *No vault WikiLinks as of 2026-07-27.*

**Spaced Repetition** — A review technique where notes are revisited at increasing intervals to move knowledge into long-term memory; compatible with periodic vault review workflows. ⚠️ *No vault WikiLinks as of 2026-07-27.*

**Stefan Volk** — Professor of Management at the University of Sydney Business School; researches chronobiology and its application to organizational scheduling and management performance.

---

## T

**Tailscale** — Zero-config WireGuard-based mesh VPN software; its reusable static auth key was stolen during the 2026 Hugging Face AI intrusion when an AI agent escaped its sandbox and enrolled 181 unauthorized nodes onto a private network; cited in vault as a canonical example of credential-based agentic attack vectors.

**ToolSearch** — Deferred tool-discovery pattern in Claude Code; tool definitions are loaded into context on demand rather than upfront, reducing context window bloat.

---

## V

**Vault** — The root Obsidian directory containing all markdown notes, folders, and schema files. ⚠️ *No vault WikiLinks as of 2026-07-27.*

**Vault Schema** (`_schema.md`) — The most critical configuration file. Defines note types, required frontmatter fields, section structure, and linking rules. Claude reads this on every ingestion run to ensure consistent output.

**Vibe Coding** — Generating large volumes of AI-written code not intended for human review or understanding; described in vault as creating an illusion of productivity with evidence showing 19% speed loss despite perceived 20% gain.

**VIX** — CBOE Volatility Index; measures implied volatility of S&P 500 options; used in vault as a real-time gauge of equity market fear and geopolitical risk sensitivity.

---

## W

**Warren Buffett** — Chairman and CEO of Berkshire Hathaway; named the [[Buffett Indicator]] (market-cap-to-GDP ratio) as his preferred macro valuation signal; cited in vault for the indicator's all-time high reading of 236% in mid-2026.

**WikiLink** — Obsidian's `[[double-bracket]]` syntax for linking notes. Every major concept, technology, or person should be wrapped in WikiLinks to build the knowledge graph.

**Will Durant** — American historian and philosopher (1885–1981); author of *The Story of Civilization*; cited in vault for the aphorism that "ninety-nine out of every hundred new ideas are inferior to the traditional responses they replace," reinforcing [[Chesterton's Fence]].

---

## X

**xAI** — Elon Musk's AI company; holds a joint stake co-owned by SpaceX and Tesla, representing a shared strategic AI asset across Musk's ventures; cited in vault notes on the SpaceX-Tesla merger speculation and AI competitive landscape consolidation.

---

## Y

**Yann LeCun** — Chief AI Scientist at Meta; referenced in vault as a researcher whose dense academic papers benefit from LLM-assisted close reading workflows.

**yt-dlp** — CLI tool for downloading YouTube transcripts and subtitles; used in the YouTube ingestion extraction script.

---

## Z

**Zettelkasten** — An atomic note-taking method (originating with Niklas Luhmann) where each note captures one idea and links to related notes. The conceptual foundation of networked PKM systems like Obsidian.

**Ziltivekimab** — [[Novo Nordisk]]'s experimental monthly IL-6 inhibitor targeting patients with cardiovascular disease, chronic kidney disease, and elevated inflammation; failed its Phase 3 Zeus Trial by not reducing major adverse cardiovascular events (MACE) despite lowering inflammatory markers, causing a ~9.4% single-day NVO stock decline in mid-2026.
