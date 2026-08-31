---
type: literature-note
source_url: https://aws.amazon.com/blogs/machine-learning/how-decathlon-runs-demand-forecasting-at-scale-with-chronos-2/
author: Vianney Bruned, Abdul Fatir Ansari, Belkiss Saidi, Carlos Ramirez, Filippo Giruzzi, Ioan Catana, and Oleksandr Shchur
tags: [demand-forecasting, time-series, foundation-models, retail-ai]
date_consumed: 2026-08-31
---

## Summary

Decathlon, one of the world's largest sporting goods retailers, adopted [[Chronos-2]] — an encoder-only transformer foundation model — for weekly demand forecasting across up to 25,000 products per supply zone globally. After benchmarking on 101 rolling evaluation cutoffs across nearly two years of data, fine-tuned Chronos-2 achieved the lowest WAPE across both 12-week and 52-week horizons, reducing forecast error by 6–15 percentage points versus legacy tools. The switch also slashed deployment time for new regions from ~6 months to 2–3 months and cut inference runtime from up to 15 minutes to under 75 seconds.

## Core Concepts

- **[[Chronos-2]]**: An encoder-only transformer (T5 encoder design) for probabilistic time series forecasting; uses patch-based embeddings, robust scaling, and an alternating attention pattern for native multivariate covariate support.
- **[[Time Series Foundation Models]] (TSFMs)**: Pretrained models capable of zero-shot or few-shot forecasting across diverse domains, evaluated here against Decathlon's proprietary retail data.
- **[[LoRA Fine-Tuning]]**: Low-Rank Adaptation used to fine-tune Chronos-2 on Decathlon data every 6 months — infrequent but impactful for accuracy.
- **[[Weighted Absolute Percentage Error]] (WAPE)**: Primary evaluation metric; each 1 pp improvement translates to 0.3 days of inventory savings and 0.3 points of product availability.
- **[[AutoGluon]]**: Framework used to orchestrate fine-tuning on GPU instances (g5.4xlarge).
- **[[Alternating Attention]]**: Chronos-2's mechanism alternating between time attention (within a series) and group attention (across series) to natively handle covariates without workarounds.
- **[[MLflow]]**: Model registry used for per-supply-zone versioning.
- **[[Temporal Fusion Transformer]] (TFT)**: Previous production model (2024 onward) replaced by Chronos-2.
- **[[Amazon SageMaker DeepAR]]**: Earlier short-term forecasting model (2021–2024), combined with Holt-Winters exponential smoothing for longer horizons.

## Key Takeaways

- **Scale**: Forecasts cover 25,000 products per supply zone, 80+ sports, across Europe, India, China, SEA, and LATAM.
- **Zero-shot baseline**: Several TSFMs matched production accuracy without any fine-tuning.
- **Fine-tuning ROI**: LoRA fine-tuning every 6 months (down from weekly retraining) still meaningfully improves accuracy.
- **WAPE gains**: SEA 12-week improved 11 pp (39% → 28%); LATAM 12-week improved 15 pp (53% → 38%).
- **Inference cost**: ~$0.03 per weekly run on a single CPU instance (m6i.8xlarge).
- **Runtime**: Inference dropped from 10–15 minutes to 40–75 seconds.
- **New region deployment**: Onboarding time fell from ~6 months to 2–3 months.
- **Benchmark on your own data**: Global leaderboard rankings diverged from Decathlon's domain-specific results.
- **Start focused**: Decathlon began with a single fine-tuned model before adding covariates.
- **Next steps**: Mixture of Experts ensembling, Middle East/Africa expansion, external covariates (price, weather), and cold-start cross-learning.

## 🧠 First Principles & Mental Models

- **[[Goodhart's Law]] (inverse application)**: Decathlon deliberately chose WAPE as a primary metric and validated it against downstream business KPIs (inventory days, availability, sales lift), avoiding the trap of optimizing for a proxy that diverges from actual business value.
- **[[Occam's Razor]]**: Chronos-2 on CPU at $0.03/run outperforms the more complex TFT pipeline — the simplest sufficient model wins, especially when operational overhead of retraining is factored in.

## 🃏 Review Questions

**Q1**: What was Chronos-2's key advantage over other TSFMs evaluated in Decathlon's benchmark?
**A**: Fine-tuned Chronos-2 achieved the lowest WAPE across both 12-week and 52-week horizons, and its native covariate support via alternating attention eliminated the workarounds other models required.

**Q2**: How does Chronos-2's alternating attention mechanism enable multivariate forecasting?
**A**: It alternates between time attention (processing patterns within a single series) and group attention (processing relationships across multiple series), allowing the model to incorporate covariates natively without external preprocessing.

**Q3**: What operational efficiencies did switching to Chronos-2 unlock for Decathlon?
**A**: New region deployment dropped from ~6 months to 2–3 months, inference runtime fell from 10–15 minutes to 40–75 seconds, fine-tuning frequency dropped from weekly to every 6 months, and weekly inference costs roughly $0.03 per supply zone.
