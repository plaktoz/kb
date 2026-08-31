---
source_url: https://aws.amazon.com/blogs/machine-learning/how-decathlon-runs-demand-forecasting-at-scale-with-chronos-2/
author: Vianney Bruned, Abdul Fatir Ansari, Belkiss Saidi, Carlos Ramirez, Filippo Giruzzi, Ioan Catana, and Oleksandr Shchur
date: 2026-08-28
---

# How Decathlon Runs Demand Forecasting at Scale with Chronos-2

## Overview

Decathlon — one of the world's largest sporting goods retailers, serving roughly 400 million users — adopted Chronos-2 as a core element of its demand forecasting infrastructure after running a thorough comparative evaluation of time series foundation models (TSFMs).

## The Forecasting Challenge

Decathlon must predict weekly sales across tens of thousands of products spanning over 80 sports, sold across multiple continents with highly seasonal patterns. Two forecast horizons are required:

- **12-week replenishment** window for purchase planners
- **52-week strategic horizon** for long-term capacity planning

This runs weekly across regions including Europe, India, China, SEA, and LATAM, with up to 25,000 products per supply zone.

## Prior Approach

- **2021–2024:** Amazon SageMaker DeepAR (short-term) combined with Holt-Winters exponential smoothing (longer-term); retrained weekly
- **2024 onward:** Temporal Fusion Transformer (TFT) with covariates for improved long-horizon accuracy

Both approaches carried significant operational overhead — weekly retraining cycles and substantial engineering effort to expand into new regions.

## Model Evaluation

Decathlon ran a large-scale benchmark on its own retail data:

- **101 rolling evaluation cutoffs** spanning nearly two years
- ~25,000 products per cutoff (39,000 unique series across the full period)
- Primary metric: Weighted Absolute Percentage Error (WAPE), supplemented by RMSE, bias, and pairwise winning rates

Key findings:
- Several TSFMs matched or exceeded the production baseline in **zero-shot** mode
- Fine-tuning — even infrequently — delivered meaningful accuracy gains
- Chronos-2 fine-tuned achieved the lowest error across both horizons

Beyond raw accuracy, Chronos-2's native covariate support via a group attention mechanism was a significant differentiator, eliminating the workarounds other models required.

## Architecture

The production pipeline on AWS includes:

1. **PySpark data preparation** to assemble input time series
2. **AutoGluon-based fine-tuning** (every 6 months, using LoRA) on GPU instances (g5.4xlarge)
3. **MLflow model registry** for versioning per supply zone
4. **Weekly batch inference** on CPU instances (m6i.8xlarge)
5. **PySpark exposition pipeline** delivering forecasts downstream

Jobs are orchestrated via Databricks and Airflow.

## Chronos-2 Architecture

Chronos-2 is an encoder-only transformer following the T5 encoder design. It applies robust scaling to each series, splits series into non-overlapping patches mapped to real-valued embeddings, and produces forecasts as continuous quantiles. Its distinguishing feature is an **alternating attention pattern** — alternating between time attention (within a series) and group attention (across series), enabling native multivariate forecasting with covariates.

## Results

**Forecast Accuracy (WAPE improvements vs. legacy tool):**

| Region | Horizon | Previous WAPE | Chronos-2 WAPE | Reduction |
|--------|---------|--------------|----------------|-----------|
| SEA | 12 weeks | 39% | 28% | 11 pp |
| LATAM | 12 weeks | 53% | 38% | 15 pp |
| SEA | 52 weeks | 44% | 38% | 6 pp |
| LATAM | 52 weeks | 55% | 46% | 9 pp |

**Business impact** per percentage point of 12-week WAPE improvement:
- 0.3 days of inventory savings
- 0.3 points of product availability improvement
- ~0.12 points of sales increase per WAPE point (average across zones)

**Operational efficiency gains:**
- Deployment time for a new region dropped from ~6 months to 2–3 months
- Inference runtime fell from 10–15 minutes (with retraining) to roughly 40–75 seconds
- Fine-tuning cadence reduced from weekly to every 6 months
- Compute cost: approximately $0.03 per weekly inference run on a single CPU instance

## Key Lessons

1. **Benchmark on your own data** — global leaderboard rankings can diverge significantly from performance on domain-specific datasets
2. **Fine-tuning with LoRA**, even infrequently, measurably improves on zero-shot performance
3. **Start focused, then iterate** — Decathlon began with a single fine-tuned model before layering in covariates
4. Foundation models make sophisticated forecasting accessible: Chronos-2 runs on standard CPU hardware at negligible cost per run

## Next Steps

Decathlon plans to deploy a **Mixture of Experts ensembling** approach, expand to Middle East and Africa, integrate external covariates (price, weather), and explore Chronos-2's cross-learning capabilities for cold-start products.
