---
source_url: https://every.to/vibe-check/fable-5-1-vibe-check
author: Katie Parrott & Dan Shipper
date: 2026-09-01
---

# Vibe Check: Fable 5.1—Anthropic Is So Back (Again)

Fable 5.1 is Anthropic's latest model—faster, friendlier, and more token-efficient than its predecessor. The Every team tested it for a week across coding, writing, and knowledge work.

## Key Findings

**Coding:** Rebuilt a full document editor from a single prompt. Dan moved all coding tasks to it; Claude Code requests jumped ~5x after access. Security-related refusals dropped significantly.

**Writing:** First Claude model in a year the writing team wants to draft with. Reads at a 7th-grade level, fewer AI tells than competitors. Weakness: fabricated quotes and ignores word-count limits.

**Knowledge Work:** Beats GPT-5.6 Sol on judgment-heavy tasks (slide decks, persona interviews). Loses points ignoring explicit constraints—a 1,000-word brief returned 1,288 words.

**Agents:** Matches Opus 5 quality at roughly half the tokens and 60% of the time. At highest effort, it spawns unneeded subagents and sometimes ignores interruptions.

## Pricing

- Input: $10/M tokens | Output: $50/M tokens (unchanged from Fable 5)
- Cached input: $0.25/M tokens (75% reduction)
- Estimated ~25–45% overall savings vs. prior workloads

## When to Use It / When to Keep Alternatives

| Use Fable 5.1 | Keep Opus 5 or Sol |
|---|---|
| In-loop coding/writing | Tasks with hard limits |
| Long delegated builds | Multi-tool pipelines |
| Existing Opus 5 agent prompts | Verified quotes required |

## Team Ratings

- **Dan & Kieran:** Paradigm shift
- **Mike:** Psyched (holding gold for broader pricing access)
- **Katie:** Psyched ("my trust issues with Claude are starting to heal")
- **Marcus:** Psyched, with caveat on heavy multi-tool tasks
