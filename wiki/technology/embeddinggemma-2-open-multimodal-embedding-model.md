---
type: literature-note
source_url: https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/
author: Sahil Dua
tags: [embeddings, on-device-ai, multimodal, gemma]
date_consumed: 2026-10-07
---

## Summary

Google launched [[EmbeddingGemma 2]], an open, Apache 2.0-licensed 740M-parameter embedding model built on the [[Gemma 4]] architecture that maps text, code, images, audio, and video into a single shared embedding space. Google says it leads sub-1B multimodal embedders on benchmarks like MTEB Code and MAEB, and that it is designed to run on-device within tight memory budgets. The aim is to let developers build private, offline, cross-modal search and [[Retrieval-Augmented Generation|RAG]] pipelines on consumer hardware.

## Core Concepts

- **[[EmbeddingGemma 2]]**: Successor to [[EmbeddingGemma]] (text-only, 20M+ downloads). It is natively multimodal and uses the same technology as [[Gemini Embedding]] models.
- **[[Multimodal Embeddings]]**: One unified vector space for text, code, images, audio, and video. This makes cross-modal queries possible, such as finding a video clip from a voice memo.
- **Modular encoders**: A 270M text-only core, plus an optional vision encoder (170M) and audio encoder (300M).
- **[[Matryoshka Representation Learning]]**: Output vectors can be cut from 768 dimensions down to 512, 256, or 128, cutting storage by up to 6x.
- **[[On-Device AI]]**: With [[Quantization]], it needs about 191MB of RAM for text-only use and about 567MB for the full multimodal model on a Pixel 11 Pro.
- **Pairing with [[Gemma 4]]**: Both models share the text tokenizer and audio encoder, so running them together in an on-device RAG pipeline uses less total memory.
- **Benchmarks**: [[MTEB]] (Massive Text Embedding Benchmark) Code and [[MAEB]] (Massive Audio Embedding Benchmark).
- **Ecosystem**: [[Google AI Edge]], [[MediaPipe]], [[LiteRT]], [[Hugging Face]], Kaggle, transformers.js, sentence-transformers, [[MLX]], [[vLLM]], [[llama.cpp]], SGLang, [[Ollama]], LMStudio, [[Qdrant]], and [[Unsloth]] for fine-tuning.

## Key Takeaways

- **Size**: 740M parameters, Apache 2.0 license, built on Gemma 4.
- **Code jump**: MTEB Code rose 9.92 points, from 68.76 to 78.68.
- **Text parity**: Multilingual text performance matches the original EmbeddingGemma.
- **Context**: 8K tokens, 4x larger than EmbeddingGemma 1.
- **Capacity per input**: About 5.5 min of audio, 29 images, or 58 video frames.
- **Storage**: MRL truncation gives up to 6x smaller vector storage.
- **Footprint**: About 191MB RAM for text-only, about 567MB for full multimodal (quantized).
- **Use cases**: Media search, finding moments in video, local file RAG, and classification and routing.
- **Edge benefits**: Privacy, lower latency, and fully offline cross-modal retrieval.
- **Code use cases**: Local codebase indexing, semantic code search, and retrieval for coding agents.

## 🃏 Review Questions

**Q1**: What is EmbeddingGemma 2's core value proposition?
**A**: It is a lightweight, open, natively multimodal embedding model. It puts text, code, images, audio, and video into one shared space and is optimized to run fully on-device.

**Q2**: How does EmbeddingGemma 2 keep storage and memory needs small?
**A**: It uses Matryoshka Representation Learning to truncate 768-dimension vectors down to 128 (up to 6x less storage), and modular encoders so a text-only setup needs just 270M parameters. When quantized, it needs about 191MB of RAM.

**Q3**: Why pair EmbeddingGemma 2 with Gemma 4 in an on-device RAG pipeline?
**A**: The two models share a text tokenizer and audio encoder, so together they use less memory. That allows private, offline multimodal retrieval followed by contextual reasoning.
