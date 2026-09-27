---
type: literature-note
source_url: https://machinelearningmastery.com/rag-vs-fine-tuning-for-domain-adaptation-when-to-use-which/
author: Shittu Olumide
tags: [rag, fine-tuning, domain-adaptation, llm-deployment]
date_consumed: 2026-09-27
---

## Summary

RAG and fine-tuning solve fundamentally different problems and should not be treated as a binary choice — roughly 60% of production LLM deployments now combine both. [[Retrieval-Augmented Generation]] handles *what the model needs to know* by injecting retrieved documents at inference time, while fine-tuning handles *how the model needs to behave* by internalizing tone, structure, and domain vocabulary via weight modification. Critically, fine-tuning does not reliably add factual knowledge; it is a behavior tool, not a knowledge tool.

## Core Concepts

- **[[Retrieval-Augmented Generation]] (RAG)**: Leaves model weights unchanged; retrieves and injects documents into the context window at inference time. Best when knowledge is large, frequently updated, or must be auditable.
- **[[Fine-Tuning]]**: Modifies model weights (typically via [[LoRA]]/[[QLoRA]], touching under 1% of parameters) to internalize behavioral patterns — tone, output structure, domain vocabulary.
- **[[LoRA]] / [[QLoRA]]**: Parameter-efficient fine-tuning methods that train a small fraction of weights via low-rank decomposition, making fine-tuning practical on consumer hardware.
- **[[Domain Adaptation]]**: Adapting a general-purpose LLM to perform well in a specific domain, either by augmenting its knowledge (RAG) or reshaping its behavior (fine-tuning).
- **TF-IDF + Cosine Similarity**: Classical retrieval technique used in the article's RAG demo over engineering runbooks — simpler than dense embeddings but still effective for structured corpora.
- **[[Production LLM Deployment]]**: Real-world systems serving LLM-powered features at scale; majority now combine RAG and fine-tuning rather than choosing one.

## Key Takeaways

- **Key distinction**: RAG = knowledge tool; fine-tuning = behavior tool. Not interchangeable.
- **Fine-tuning myth**: Fine-tuning does not reliably inject new factual knowledge into a model.
- **RAG strengths**: Dynamic/large knowledge, compliance citation requirements, fast deployment without labeled data.
- **Fine-tuning strengths**: Enforcing tone/structure at scale, low-latency (no retrieval hop), cost reduction via smaller specialized models.
- **RAG demo**: TF-IDF retrieval over runbooks → chunks fed to Claude with citation-enforcing system prompt.
- **Fine-tuning demo**: LoRA adapter for proprietary complaint taxonomy → strict JSON output where prompting alone fails.
- **Production reality**: ~60% of LLM deployments use both approaches together.
- **Decision trigger for fine-tuning**: High query volume, latency budget exceeded by retrieval, or prompting fails at scale.

## 🧠 First Principles & Mental Models

- **[[Separation of Concerns]]**: RAG and fine-tuning each own a distinct axis — external knowledge vs. internal behavior — and conflating them leads to misapplied solutions (e.g., fine-tuning to "teach" facts that will drift or need auditing).
- **[[Right Tool for the Job]]**: The 6-point decision framework is an instance of matching tool capability to problem structure rather than defaulting to the most popular technique; fine-tuning on dynamic data is like hammering a screw.

## 🃏 Review Questions

**Q1**: What is the fundamental distinction between RAG and fine-tuning as tools for domain adaptation?
**A**: RAG addresses what the model needs to know by retrieving external documents at inference time; fine-tuning addresses how the model needs to behave by modifying its weights to internalize tone, structure, and vocabulary.

**Q2**: Why is fine-tuning unreliable for injecting factual knowledge into a model?
**A**: Fine-tuning modifies behavioral patterns in model weights but does not reliably encode specific facts — facts encoded this way can hallucinate, drift, or become stale; RAG with auditable sources is the correct tool for factual grounding.

**Q3**: When should a team default to combining both RAG and fine-tuning in a production system?
**A**: When the application requires both dynamic, citable knowledge (favoring RAG) and consistent structured output or domain tone at scale (favoring fine-tuning) — approximately 60% of production deployments already use this hybrid approach.
