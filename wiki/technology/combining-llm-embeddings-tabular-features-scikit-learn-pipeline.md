---
type: literature-note
source_url: https://machinelearningmastery.com/combining-llm-embeddings-with-tabular-features-in-a-unified-scikit-learn-pipeline/
author: Iván Palomares Carrascosa
tags: [llm-embeddings, scikit-learn, feature-engineering, text-classification]
date_consumed: 2026-09-01
---

## Summary

This article demonstrates how to build a deployment-ready [[Scikit-learn]] pipeline that fuses LLM-generated text embeddings with structured tabular features using `ColumnTransformer`. A custom `TextEmbedder` class wraps Hugging Face's `sentence-transformers` library to make embeddings a first-class sklearn transformer. Applied to a hybrid spam-detection dataset, the unified pipeline achieves 99% accuracy while remaining self-contained and reusable.

## Core Concepts

- **[[ColumnTransformer]]**: A scikit-learn utility that applies different preprocessing pipelines to different column types in parallel, then concatenates the results — eliminating manual feature splitting and re-joining.
- **[[Sentence Transformers]]**: Hugging Face's `sentence-transformers` library; `all-MiniLM-L6-v2` is used here as a lightweight, CPU-friendly text embedding model.
- **[[Custom Sklearn Transformer]]**: A class inheriting from `BaseEstimator` and `TransformerMixin` that implements `fit()` and `transform()`, making any arbitrary logic (including LLM inference) composable in an sklearn pipeline.
- **[[Mixed-Type Feature Preprocessing]]**: Handling text, numeric, and categorical columns through separate branches — `TextEmbedder`, `StandardScaler`, and `OneHotEncoder` respectively — unified under one `ColumnTransformer`.
- **[[RandomForestClassifier]]**: Ensemble classifier appended as the final pipeline step; 100 estimators trained end-to-end after the unified feature matrix is assembled.
- **[[SMS Spam Collection Dataset]]**: Benchmark text dataset augmented here with synthetic tabular columns (`account_age_days`, `is_premium`, `priority_score`) to simulate realistic mixed-modality input.

## Key Takeaways

- **Custom transformer pattern**: Wrap any embedding model in `BaseEstimator` + `TransformerMixin` for sklearn compatibility.
- **Initialization inside `fit()`**: Load the sentence transformer model inside `fit()`, not `__init__`, to comply with sklearn's cloning rules.
- **Three-branch ColumnTransformer**: Text → `TextEmbedder`; numeric → `StandardScaler`; categorical → `OneHotEncoder(handle_unknown='ignore')`.
- **Single `pipeline.fit()` call**: All preprocessing and training executes in one step after assembly.
- **99% test accuracy**: Achieved on a 20% held-out split of the hybrid SMS dataset (1,115 samples).
- **Recall on spam class was 91%**: Synthetic noise intentionally prevents trivial separability and perfect recall.
- **Deployment-ready**: The pipeline is self-contained — embed, scale, encode, and classify in one serializable object.

## 🧠 First Principles & Mental Models

- **[[Composability]]**: The sklearn pipeline API embodies the principle that complex systems should be built from small, independently testable units — each transformer does exactly one job and the pipeline wires them together, making the whole inspectable and replaceable in parts.
- **[[Separation of Concerns]]**: Keeping text, numeric, and categorical preprocessing in separate branches means a change to one branch (e.g., swapping embedding models) cannot break another, a direct application of the modular design principle.

## 🃏 Review Questions

**Q1**: What is the central architectural pattern this article demonstrates?
**A**: Using scikit-learn's `ColumnTransformer` to run text, numeric, and categorical preprocessing in parallel branches, then feeding the concatenated output into a classifier — all within a single unified pipeline.

**Q2**: Why must the `SentenceTransformer` model be initialized inside `fit()` rather than `__init__()`?
**A**: Scikit-learn's cloning mechanism calls `__init__` with the original constructor arguments when cloning an estimator; initializing the model inside `fit()` ensures it is created fresh after cloning rather than sharing state across clones.

**Q3**: How would you adapt this pipeline to a new mixed-data classification problem?
**A**: Replace the `TextEmbedder`'s model with a domain-appropriate sentence transformer, update the column names passed to each `ColumnTransformer` branch to match your dataset's schema, and swap the `RandomForestClassifier` for whichever estimator suits your data size and latency constraints.
