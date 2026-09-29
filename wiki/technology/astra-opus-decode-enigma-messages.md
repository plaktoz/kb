---
type: literature-note
source_url: https://techcrunch.com/2026/09/25/astra-and-opus-just-passed-turings-other-test/
author: Tim Fernholz
tags: [ai-agents, cryptanalysis, llm-research, historical-archives]
date_consumed: 2026-09-28
---

## Summary

Two independent researchers used frontier LLMs — OpenAI's Astra and Anthropic's [[Claude Opus 5]] — to decode previously unbroken WWII-era Enigma messages that had resisted human cryptanalysts for decades. A veteran cryptanalyst validated one solution and called the model's archival research and simulation-building capability "awe"-inspiring, describing work that took the model two days but would have taken a human researcher far longer.

## Core Concepts

- **[[Enigma Cipher]]** — the WWII Nazi Germany encryption machine whose remaining unsolved messages (seven, plus one with known plaintext but unbroken code) are relics of Alan Turing's original codebreaking challenge.
- **[[Astra]]** (OpenAI) — used by developer Carter Leffen to search an archival database, identify context clues, build a machine simulator from scratch, and recover plaintext of a message unsolved since 2005.
- **[[Claude Opus 5]]** (Anthropic) — used by cybersecurity executive Jack Willis to break a separate unsolved message, leveraging a known officer's signature as a more direct guide than Leffen's approach.
- **[[Frode Weierud]]** — retired electrical engineer running the Crypto Cellar research site; validated Leffen's Astra-derived solution and assessed the model's archival research skill.
- **[[Carter Leffen]]** — developer who prompted Astra and used it to build an interactive website explaining the decoded message.
- **[[Alan Turing]]** — historical reference point; his Bombe machine broke Enigma during WWII, but a handful of archival messages remained unsolved, often due to original transcription errors.

## Key Takeaways

- Astra decoded a message unsolved since 2005 by combining archival search, context inference, and simulator-building.
- Weierud: Astra behaves "like a very professional cryptanalyst and archive researcher."
- Astra's model logs referenced a "private collection" not hosted by Weierud — source unclear.
- Astra's two-day output reportedly exceeded weeks of equivalent human archival effort.
- Willis used [[Claude Opus 5]] with a known officer's signature to crack a different message.
- Willis contacted Weierud on September 21 to report the Opus 5 result.
- Seven Enigma messages remain fully unbroken; one more has known plaintext but unbroken code.

## 🧠 First Principles & Mental Models

- **[[Constraint Satisfaction]]**: Both solutions worked by narrowing the search space with a strong contextual anchor (archival metadata for Astra, a known officer's signature for Opus 5) rather than brute-forcing the cipher — the classic first-principles move in cryptanalysis of turning an intractable search into a constrained one.

## 🃏 Review Questions

**Q1**: What is the central claim of the article?
**A**: Two frontier LLMs, OpenAI's Astra and Anthropic's Claude Opus 5, independently decoded previously unbroken WWII Enigma messages, matching or exceeding what specialist human cryptanalysts had achieved.

**Q2**: What specific evidence supports the claim that Astra performed genuine archival research rather than pattern-matching?
**A**: Astra searched a database for an unbroken message, identified contextual clues, and built its own machine simulator to recover the plaintext, with its logs referencing an archive collection not hosted by the validating researcher, Frode Weierud.

**Q3**: What does this imply about applying LLMs to other historical or archival research problems?
**A**: A well-constrained search — anchored by a strong contextual clue like a known signature — lets an LLM compress research that would take a human weeks into a couple of days, suggesting similar approaches could unlock other archival puzzles beyond cryptanalysis.
