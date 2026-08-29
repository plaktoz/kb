---
source_url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/
author: Diego Melendo Casado, Luke Leonhard
date: 2026-08-26
---

# Intelligent Transcription with Gemini 3.5 Transcribe

Google has launched Gemini 3.5 Transcribe, a speech-to-text model built for intelligent, real-time transcription. Unlike conventional recognition systems that struggle with noise and jargon, this model converts raw audio directly into formatted, polished text.

## Availability

The model is accessible via two APIs:

- **Real-time streaming** (`gemini-3.5-transcribe-live`) — bidirectional streaming with sub-second latency via the Live API
- **Pre-recorded audio** (`gemini-3.5-transcribe`) — handles meetings and call logs with speaker attribution and word-level timestamps via the Interactions API

## Key Capabilities

- **Smart transcription:** Handles self-corrections, removes filler words, and auto-formats output
- **Function calling:** Delegates tasks (image generation, file analysis) to other Gemini models
- **Accuracy:** Achieves a 4.0% Word Error Rate (WER) for streaming and 2.6% for non-streaming, per Artificial Analysis
- **Custom vocabulary:** Adapts to specialized jargon and unique spellings
- **Language support:** Auto-detects and transcribes 85+ languages with regional dialect handling
- **Multi-speaker ID:** Attributes speech to up to three speakers in pre-recorded audio

## Performance vs. Prior Model

Compared to Chirp 3, the new model improves time-to-final-transcription by 70% and achieves 5.50% WER (streaming) and 5.04% WER (non-streaming) on the FLEURS benchmark.

## Surface Integrations

- **Gboard (Android):** Powers the Rambler feature for voice-to-formatted-text with editing commands
- **Google Antigravity:** Uses screen context and chat history for improved accuracy
- **Google AI Studio:** Voice-driven app building
- **Gemini app (macOS):** Voice commands for file summarization, image generation, and cross-app workflows
- **Chrome (coming soon):** Dictate in any web field

## Access

- **Developers:** Public preview via Google AI Studio and Google Antigravity
- **Enterprises:** Public preview via Gemini Enterprise Agent Platform; coming soon to Gemini Enterprise for Customer Experience
- **Consumers:** Available in the Gemini macOS app and via Rambler on Android in select regions; Chrome support forthcoming
