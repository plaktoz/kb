---
type: literature-note
source_url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/
author: Diego Melendo Casado, Luke Leonhard
tags: [speech-to-text, gemini, google-ai, transcription]
date_consumed: 2026-08-28
---

## Summary

Google has launched [[Gemini]] 3.5 Transcribe, a speech-to-text model designed for intelligent, real-time transcription that converts raw audio directly into formatted, polished text. Unlike conventional ASR systems, it handles self-corrections, removes filler words, supports 85+ languages, and achieves a 2.6% Word Error Rate (WER) for non-streaming audio. The model is available via two APIs and integrates into surfaces like Gboard, Google AI Studio, and the Gemini macOS app.

## Core Concepts

- **[[Gemini 3.5 Transcribe]]** — Google's new speech-to-text model; two variants: `gemini-3.5-transcribe-live` (real-time streaming) and `gemini-3.5-transcribe` (pre-recorded audio with speaker attribution)
- **[[Automatic Speech Recognition]] (ASR)** — the underlying task; this model improves on traditional ASR by handling noise, jargon, and filler words intelligently
- **[[Word Error Rate]] (WER)** — standard benchmark metric for transcription accuracy; Gemini 3.5 Transcribe achieves 4.0% WER (streaming) and 2.6% WER (non-streaming)
- **[[Live API]]** — Google's bidirectional streaming API enabling sub-second latency transcription
- **[[Function Calling]]** — the model can delegate tasks (image generation, file analysis) to other Gemini models mid-transcription
- **[[FLEURS Benchmark]]** — multilingual speech benchmark; Gemini 3.5 Transcribe achieves 5.50% WER (streaming) and 5.04% WER (non-streaming), improving time-to-final-transcription by 70% over [[Chirp 3]]
- **[[Rambler (Gboard)]]** — consumer-facing feature powered by this model for voice-to-formatted-text on Android

## Key Takeaways

- **Accuracy**: 4.0% WER (streaming), 2.6% WER (non-streaming) per Artificial Analysis
- **Speed**: 70% improvement in time-to-final-transcription vs. [[Chirp 3]] on FLEURS
- **Language support**: Auto-detects and transcribes 85+ languages with regional dialect handling
- **Multi-speaker ID**: Attributes speech to up to three speakers in pre-recorded audio
- **Custom vocabulary**: Adapts to specialized jargon and unique spellings
- **Function calling**: Can delegate to other Gemini models for image generation, file analysis
- **Surfaces**: Gboard Rambler (Android), Google Antigravity, Google AI Studio, Gemini macOS app, Chrome (coming soon)
- **Access**: Public preview for developers via Google AI Studio; enterprise preview via Gemini Enterprise Agent Platform

## 🧠 First Principles & Mental Models

- **[[Composability]]**: By enabling function calling mid-transcription, Google embeds Gemini 3.5 Transcribe as a node in a broader multi-agent pipeline — the model's value multiplies when it can hand off to specialized tools rather than acting in isolation.
- **[[Platform Strategy]]**: Deep integration into Gboard, Chrome, and AI Studio reflects Google's approach of using model launches as surface expansion — each integration point increases switching costs and data flywheel effects.

## 🃏 Review Questions

**Q1**: What is the core capability that distinguishes Gemini 3.5 Transcribe from conventional speech recognition systems?
**A**: It converts raw audio directly into formatted, polished text — handling self-corrections, removing filler words, and auto-formatting output rather than producing raw transcriptions.

**Q2**: What Word Error Rate does Gemini 3.5 Transcribe achieve, and how does it compare to its predecessor?
**A**: It achieves 4.0% WER (streaming) and 2.6% WER (non-streaming); on the FLEURS benchmark it improves time-to-final-transcription by 70% over Chirp 3.

**Q3**: How can developers and enterprises access Gemini 3.5 Transcribe?
**A**: Developers can access it via public preview in Google AI Studio and Google Antigravity; enterprises can access it via public preview in the Gemini Enterprise Agent Platform.
