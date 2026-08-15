---
type: literature-note
source_url: https://www.anthropic.com/news/claude-text-watermark
author: Anthropic
tags: [ai-safety, watermarking, eu-ai-act, claude]
date_consumed: 2026-08-15
---

## Summary
Anthropic is rolling out text watermarking for future Claude models to comply with the EU AI Act and the EU Code of Practice on Transparency of AI-Generated Content. The watermark, based on Google DeepMind's SynthID-Text method, encodes a detectable pattern into the low-stakes word choices Claude makes during generation, without affecting output quality, speed, or cost.

## Core Concepts
- **[[SynthID-Text]]**: Google DeepMind's watermarking method (published in *Nature*, 2024), rooted in a 2022 Scott Aaronson proposal, which Claude's watermark is a version of.
- **[[Low-Stakes Token Watermarking]]**: LLMs generate text by choosing among near-equivalent candidate words (e.g., "overcast" vs "grey"); watermarking replaces the random number used to break such ties with one derived from a secret key plus preceding words, creating a statistically detectable pattern.
- **[[EU AI Act]]** / **[[EU Code of Practice on Transparency of AI-Generated Content]]**: The regulatory driver — ~190 signatories, including Anthropic, committed in July 2026 to marking AI-generated text, prompting global (not just EU-scoped) rollout since regional scoping isn't yet technically durable.
- **[[C2PA Content Credentials]]**: A separate, non-hidden metadata mechanism Claude attaches to generated files like images — distinct from the hidden text watermark.

## Key Takeaways
- The watermark only estimates "likelihood Claude was involved," never confirms human authorship, and is weak on small samples, factual passages, or code (where there's often only one correct token).
- No speed, cost, or quality impact — internal testing and DeepMind's own SynthID-Text paper found no statistically significant rating differences between watermarked and unwatermarked text.
- A full rewrite likely removes the watermark; light editing likely does not. Translations retain it since every output word is still Claude-chosen.
- Only Anthropic can verify the cryptographic watermark via its private key — fundamentally different from stylistic AI-detectors like Pangram that look for "tells" (e.g., overused phrasing).
- Watermarking doesn't change ownership, authorship, or legal responsibility for Claude's outputs; a detection API is coming soon.

## 🃏 Review Questions
**Q1**: How does Claude's text watermark actually get embedded in generated text?
**A**: At low-stakes word-choice points where multiple candidates are roughly equally good, the model normally picks using a random number; watermarking instead derives that "random" number from a secret key plus the preceding text, creating a pattern later checkable against the key.

**Q2**: Why is the watermark less effective on code or factual text?
**A**: Because those domains often have only one correct next token (an exact variable name, a specific fact), leaving little room for the low-stakes word-choice variability the watermark relies on.

**Q3**: What regulatory requirement is driving Anthropic's global rollout of this watermark, rather than an EU-only rollout?
**A**: The EU AI Act and the EU Code of Practice on Transparency of AI-Generated Content require marking AI-generated content; Anthropic applies it globally because there isn't yet a durable technical way to scope the watermark by region.
