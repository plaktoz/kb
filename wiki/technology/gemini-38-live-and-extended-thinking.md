---
type: literature-note
source_url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/
author: Tom Ouyang, Malini Jaganathan
tags: [google, gemini, voice-ai, multimodal]
date_consumed: 2026-09-16
---

## Summary

Google announced two new voice-first AI models: [[Gemini 3.8 Live]], optimized for scale and cost efficiency with real-time visual grounding and 97-language auto-detection, and [[Gemini 3.8 Live Extended Thinking]], designed for complex multi-step reasoning during uninterrupted conversational flow. Both models are rolling out across Google's developer and consumer platforms, with Extended Thinking ranking first on Artificial Analysis' Speech to Speech Quality Index at 82.6.

## Core Concepts

- **[[Gemini 3.8 Live]]**: A voice AI model built for fluid, scalable dialogue; supports real-time visual input processing, automatic mid-conversation language switching across 97 languages, and background tool/API execution without pausing speech.
- **[[Gemini 3.8 Live Extended Thinking]]**: A higher-capability variant that applies multi-step reasoning to complex queries while maintaining conversational continuity, using verbal cues like "Let me check that…" to signal active reasoning.
- **[[SynthID]]**: Google's audio watermarking system applied to all output from both models, enabling AI-content transparency and provenance tracking.
- **[[τ-Voice Benchmark]]**: An agentic voice evaluation; Extended Thinking leads at 68.6%, with 35.1% on the harder banking-domain variant (Sierra's τ-Voice-banking).
- **[[Big Bench Audio]]**: Broad audio reasoning benchmark on which Extended Thinking scores 97.7%.
- **[[Artificial Analysis Speech to Speech Quality Index]]**: Independent ranking on which Extended Thinking holds the #1 position with a score of 82.6.

## Key Takeaways

- **Two-tier design**: Live targets cost/scale; Extended Thinking targets accuracy and complex reasoning.
- **Real-time visual grounding**: Processes visual inputs near-instantaneously within a live voice session.
- **Non-blocking tool calls**: Background API execution keeps conversation flowing during agentic tasks.
- **Multilingual**: Auto-detects and switches language mid-conversation across 97 languages.
- **Benchmark leadership**: Extended Thinking ranks #1 on Speech to Speech Quality Index (82.6), 68.6% on τ-Voice, 97.7% on Big Bench Audio.
- **AI transparency**: All audio output watermarked via [[SynthID]] for content provenance.
- **Distribution**: Available via Gemini API, Google AI Studio, Google Workspace (Docs, Gmail, Keep), Search Live, and Gemini Enterprise preview.

## 🧠 First Principles & Mental Models

- **[[Separation of Concerns]]**: Google explicitly splits reasoning depth from latency by offering two distinct model tiers — the 3.8 Live model handles scale and cost while Extended Thinking handles complexity, rather than forcing a single model to optimize both simultaneously.
- **[[Transparency by Design]]**: SynthID watermarking is baked into the output pipeline rather than treated as an optional compliance add-on, reflecting a first-principles approach to AI content provenance at deployment scale.

## 🃏 Review Questions

**Q1**: What is the core distinction between Gemini 3.8 Live and Gemini 3.8 Live Extended Thinking?
**A**: Gemini 3.8 Live is optimized for cost-efficient, scalable fluid dialogue with real-time visual grounding; Extended Thinking adds multi-step reasoning for complex, high-stakes tasks while preserving uninterrupted conversational flow.

**Q2**: How does Extended Thinking signal that it is actively reasoning without interrupting the conversation?
**A**: It uses verbal cues such as "Let me check that…" to indicate background reasoning is in progress, keeping the dialogue natural while the model works through multi-step problems.

**Q3**: How would a developer deploy Gemini 3.8 Live Extended Thinking for an enterprise use case?
**A**: The model is available via the Gemini API and Google AI Studio, and through Gemini Enterprise preview, allowing developers to integrate high-accuracy agentic voice interactions — such as banking support or complex query handling — into enterprise applications.
