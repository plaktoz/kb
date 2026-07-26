# Andrej Karpathy's LLM Wiki: Build a Personal Knowledge Base with Obsidian and Codeex in 5 Minutes

source_url: https://www.mindstudio.ai/blog/andrej-karpathy-llm-wiki-obsidian-codeex-second-brain

author: MindStudio Team
date: 2026-05-08

---

The article describes building a self-organizing personal knowledge base inspired by Andrej Karpathy's published LLM wiki architecture on GitHub. The core idea: instead of saving content and forgetting it, an AI agent layer converts raw inputs into a structured, interlinked markdown wiki inside Obsidian.

**Folder structure (5 components):**
- `/raw` — untouched source material (web clips, transcripts)
- `/wiki` — AI-generated structured pages
- `agents.md` — plain-text behavioral spec controlling all agent actions
- `index.md` — catalog of all wiki pages
- `log.md` — timestamped audit trail

**Key insight:** The `agents.md` file acts as the entire operational spec. Editing it directly changes agent behavior instantly — no code redeployment needed.

**Extensions added beyond Karpathy's base:**
- A `/CRM` folder for people notes, triggered by telling the agent "I'm giving you information for the CRM"
- A `/journal` folder where entries are grounded in the wiki, CRM, and prior journals — not generic LLM responses

**Input layer:** The Obsidian Web Clipper (Chrome extension) drops full article text and YouTube transcripts into `/raw` in one click.

**Automation:** A Codeex hourly automation processes unprocessed `/raw` files, updates the wiki, and pushes commits to a private GitHub repo — running without manual intervention.

**Practical caution noted:** Codeex may over-generate files; a follow-up prompt to prune back to the minimal spec is recommended.

The article positions `agents.md` as underappreciated: "the entire operational spec is in one readable file" — editable by anyone, no technical deployment required.
