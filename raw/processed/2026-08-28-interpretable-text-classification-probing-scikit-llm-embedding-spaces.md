---
source_url: https://machinelearningmastery.com/interpretable-text-classification-probing-scikit-llm-embedding-spaces/
author: Iván Palomares Carrascosa
date: 2026-08-28
---

# Interpretable Text Classification: Probing Scikit-LLM Embedding Spaces

The article demonstrates how to interpret LLM-generated text embeddings using three techniques: probing classifiers, UMAP visualization, and SHAP values.

**Setup:** The workflow runs locally via Ollama (free), using the `all-minilm` embedding model integrated through Scikit-LLM's `GPTVectorizer`.

**Data:** 1,000 balanced IMDB movie reviews (500 positive, 500 negative), split 80/20 for training and testing.

**Probing Classifier:** A logistic regression model trained on the embeddings achieved ~77% accuracy — respectable given a simple linear model on high-dimensional embeddings. This validates embedding quality by isolating their contribution to classification.

**UMAP Visualization:** Embeddings projected to 2D using cosine similarity revealed subtle class clustering — negative reviews concentrated in the southern plot region, positive in the upper half.

**SHAP Analysis:** `shap.LinearExplainer` identified the most influential latent dimensions. "Dimension 208 is the primary signal for negative reviews," while "dimension 139 is the main driver for positive reviews."

The approach shows how interpretability tools can partially illuminate the black-box nature of LLM embeddings in downstream classification tasks.
