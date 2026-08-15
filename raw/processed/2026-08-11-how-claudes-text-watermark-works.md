---
source_url: https://www.anthropic.com/news/claude-text-watermark
author: Anthropic
date: 2026-08-11
---

# How Claude's text watermark works

Future Claude models will generate text that contains a watermark, determining the likelihood that Claude was involved in writing the text. Anthropic, along with several other major AI providers, is implementing this to comply with the EU AI Act.

**What is watermarking?** LLMs generate text one word at a time, choosing among candidates where low-stakes choices (e.g., "overcast" vs "grey") are settled by a random number. Watermarking uses these low-stakes choices to leave a pattern: instead of an arbitrary random number generator, the source of randomness is a key plus preceding words, so one can later check whether a sequence is consistent with the choices Claude would make using that key.

**Impact on outputs:** Watermarking does not impact quality — a watermarked response is indistinguishable from an unwatermarked one to a reader. Internal testing and Google DeepMind's SynthID-Text paper found no statistically significant difference in ratings.

**Method:** Claude's watermark is a version of Google DeepMind's SynthID-Text approach (published in *Nature*, 2024), rooted in a 2022 Scott Aaronson proposal. Limitations: it can only estimate "likelihood Claude was involved," not confirm human authorship, doesn't work well on small samples, and is sparser on factual passages or code where there's only one correct next token.

**Proofreading and code:** When Claude lightly edits human text, there's little for the watermark to attach to. Code has generally less watermarking since exact outputs are often required, though comments within code can carry it.

**For users:** No speed or cost impact — no extra tokens are produced. The watermark cannot be traced back to a specific user or organization.

**Why:** Anthropic, along with ~190 signatories, signed the EU Code of Practice on Transparency of AI-Generated Content in July 2026, which requires "marking" of AI-generated text. Watermarking is applied globally at launch since there isn't yet a durable way to scope it by region.

**Detection:** A watermark detection API is coming soon. For files (images etc.), Claude attaches a C2PA content credential in metadata — a different, non-hidden mechanism from the text watermark.

**Editing/translation:** Light editing likely won't remove the watermark; a full rewrite will. Translations carry the watermark since every word is Claude-chosen. Older models (pre-Aug 2, 2026) get watermarking rolled out over coming months under an EU transition period.

**Vs. AI detectors:** Detection software like Pangram looks for stylistic "tells" (e.g., "this isn't X, it's Y", overuse of "quietly") — fundamentally different from checking a cryptographic watermark, which Anthropic alone can verify via its key.

**Ownership:** The watermark doesn't change ownership, authorship, or legal responsibility for outputs.
