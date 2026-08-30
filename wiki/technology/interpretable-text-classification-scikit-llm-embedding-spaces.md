---
type: literature-note
source_url: https://machinelearningmastery.com/interpretable-text-classification-probing-scikit-llm-embedding-spaces/
author: Iván Palomares Carrascosa
tags: [llm-embeddings, interpretability, scikit-llm, shap]
date_consumed: 2026-08-30
---

## Summary

The article demonstrates how to interpret LLM-generated text embeddings using three complementary techniques: probing classifiers, UMAP dimensionality reduction, and SHAP values. Using 1,000 IMDB movie reviews and a locally-run `all-minilm` embedding model via Ollama and [[Scikit-LLM]], the workflow partially illuminates the black-box nature of high-dimensional embeddings. The approach validates embedding quality while identifying which latent dimensions most influence downstream classification outcomes.

## Core Concepts

- **[[Probing Classifiers]]**: A simple [[Logistic Regression]] model trained on frozen embeddings to test how linearly separable the representations are, thereby validating embedding quality in isolation.
- **[[UMAP]] (Uniform Manifold Approximation and Projection)**: Dimensionality reduction technique projecting high-dimensional embeddings to 2D using cosine similarity; used here to visualize class clustering in embedding space.
- **[[SHAP Values]] (SHapley Additive exPlanations)**: `shap.LinearExplainer` applied to identify the most influential latent dimensions driving positive and negative sentiment predictions.
- **[[Scikit-LLM]]**: Python library integrating LLMs into scikit-learn pipelines; `GPTVectorizer` used here to produce embeddings from a local Ollama model.
- **[[Ollama]]**: Local LLM runtime enabling free, offline embedding generation via the `all-minilm` model.
- **[[Embedding Interpretability]]**: The broader challenge of understanding what information high-dimensional vector representations encode and how they influence downstream tasks.

## Key Takeaways

- **Probing accuracy**: Logistic regression on embeddings achieved ~77% accuracy on IMDB sentiment — respectable for a linear model.
- **UMAP clustering**: Negative reviews clustered in the southern plot region; positive reviews in the upper half.
- **SHAP dimensions**: Dimension 208 was the primary signal for negative reviews; dimension 139 for positive reviews.
- **Local-first setup**: Entire workflow runs free and offline via Ollama — no API costs.
- **Interpretability limit**: These techniques partially illuminate embeddings; the full semantics of latent dimensions remain opaque.
- **Validation use case**: Probing classifiers are a principled way to isolate and validate embedding quality before building complex classifiers.

## 🧠 First Principles & Mental Models

- **[[Black Box Probing]]**: Rather than opening the LLM itself, probing uses an external simple model as a diagnostic — applying the principle that you can learn about a system's internals by observing its outputs under controlled conditions.
- **[[Reductionism]]**: Decomposing embedding interpretability into three orthogonal lenses (linear separability, geometric structure, feature attribution) reflects the first-principles move of breaking a hard problem into independently tractable sub-problems.

## 🃏 Review Questions

**Q1**: What is the core purpose of applying a probing classifier to LLM embeddings?
**A**: To validate embedding quality by isolating whether the embeddings alone contain linearly separable signal for the target task, independent of any complex downstream model.

**Q2**: Which SHAP dimensions were identified as the primary drivers for negative and positive sentiment in the IMDB experiment?
**A**: Dimension 208 was the primary signal for negative reviews, and dimension 139 was the main driver for positive reviews.

**Q3**: How would you use this interpretability workflow in a real project?
**A**: Run probing and UMAP early to verify that your chosen embedding model captures task-relevant structure before investing in a more complex classifier; use SHAP post-hoc to debug model decisions or surface potential bias in the embedding space.
