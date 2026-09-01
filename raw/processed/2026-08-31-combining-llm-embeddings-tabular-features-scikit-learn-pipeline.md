---
title: "Combining LLM Embeddings with Tabular Features in a Unified Scikit-learn Pipeline"
source_url: "https://machinelearningmastery.com/combining-llm-embeddings-with-tabular-features-in-a-unified-scikit-learn-pipeline/"
date: "2026-08-31"
author: "Iván Palomares Carrascosa"
---

# Combining LLM Embeddings with Tabular Features in a Unified Scikit-learn Pipeline

## Introduction

Real-world classification tasks — like ticket triage or spam detection — rarely involve data of a single type. Practitioners frequently encounter a blend of structured numeric/categorical data alongside unstructured text. This article demonstrates how to construct a deployment-ready scikit-learn pipeline that integrates LLM-generated text embeddings with tabular features using a `ColumnTransformer`.

## Prerequisites

Rather than using a paid API or a massive model, the tutorial employs Hugging Face's `sentence-transformers` library — a lightweight, CPU-friendly option for generating text embeddings.

```bash
pip install -q sentence-transformers scikit-learn pandas numpy
```

## Dataset Construction

A hybrid dataset is assembled by loading the SMS Spam Collection dataset from GitHub and augmenting it with three synthetic tabular columns:

- **`account_age_days`** — numeric; spammers skew toward newer accounts, but overlap exists
- **`is_premium`** — categorical; spammers are 95% free-tier users vs. 80% for legitimate users
- **`priority_score`** — numeric float; distributions overlap between 0.4–0.7 to avoid trivial separability

The intentional noise ensures the classifier faces a realistic challenge rather than achieving trivial 100% accuracy.

## Custom Text Transformer

A custom class `TextEmbedder` inherits from scikit-learn's `BaseEstimator` and `TransformerMixin`, implementing the required `fit()` and `transform()` methods:

- **`fit()`** — initializes the `SentenceTransformer` model (default: `all-MiniLM-L6-v2`)
- **`transform()`** — encodes input texts into a 2D NumPy embedding array

The model is initialized inside `fit()` to comply with scikit-learn's cloning rules.

## Pipeline Assembly

Three parallel preprocessing branches are defined inside a `ColumnTransformer`:

| Branch | Columns | Transformer |
|--------|---------|-------------|
| `text` | `message` | `TextEmbedder()` |
| `num` | `account_age_days`, `priority_score` | `StandardScaler()` |
| `cat` | `is_premium` | `OneHotEncoder(handle_unknown='ignore')` |

A `RandomForestClassifier` (100 estimators) is appended as the final pipeline step. Calling `pipeline.fit()` triggers all preprocessing and model training in a single call.

## Results

Evaluated on a held-out 20% test split:

```
              precision    recall  f1-score   support
           0       0.99      1.00      0.99       966
           1       1.00      0.91      0.95       149
    accuracy                           0.99      1115
   macro avg       0.99      0.95      0.97      1115
weighted avg       0.99      0.99      0.99      1115
```

The high accuracy reflects the SMS dataset's inherent separability, while the synthetic noise prevents the model from achieving a perfect score.

## Key Takeaways

- Wrapping a Hugging Face sentence transformer in a custom scikit-learn class makes it a first-class citizen in any sklearn pipeline.
- `ColumnTransformer` elegantly handles parallel, type-specific preprocessing without manual feature splitting and re-joining.
- The resulting pipeline is self-contained, reusable, and suitable for deployment scenarios involving mixed text and tabular data.
