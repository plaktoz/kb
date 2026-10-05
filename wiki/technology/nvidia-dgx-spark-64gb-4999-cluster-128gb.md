---
type: literature-note
source_url: https://mixed-news.com/en/nvidia-dgx-spark-64gb-4999-october-23-cluster-128gb/
author: Chris Steven
tags: [nvidia, dgx-spark, local-ai, ai-hardware]
date_consumed: 2026-10-05
---

## Summary

[[Nvidia]] will sell a 64GB version of its [[DGX Spark]] desktop from October 23 at a US starting price of $4,999. It says one unit runs models of up to 100 billion parameters on the device, and two units linked by a QSFP cable pool to 128GB and handle up to 200 billion parameters. The only performance figure, a "1.7x" gain for a two-unit cluster, comes from one Nvidia in-house test that does not say what was measured, and nobody outside Nvidia has tested the machine yet.

## Core Concepts

- **[[DGX Spark]] 64GB**: A cheaper version below the 128GB model. It keeps the [[GB10 Grace Blackwell Superchip]], [[DGX OS]] and the full Nvidia AI software stack, but has half the memory.
- **Partner-only distribution**: Sold "exclusively from manufacturer partners": [[Acer]], [[ASUS]], [[Dell]], [[Gigabyte]], [[HP]] and [[MSI]]. That makes $4,999 a starting price from six vendors, not one Nvidia figure.
- **[[Unified Memory]] pooling**: Two units connect directly through their built-in [[ConnectX-7]] network cards over a 200 GbE fabric, giving 128GB of combined memory.
- **Clustering benchmark**: Nvidia claims "twice the memory bandwidth and up to 1.7x the performance". The figure is tied to one in-house [[Qwen3.8]] 27B test, and the announcement does not say whether it measures tokens per second, latency or time to first token.
- **[[Nvidia Sync Cluster Assistant]]**: Detects connected units, validates their configuration and sets up the ConnectX-7 network, a job owners would otherwise do by hand.
- **[[Nvidia Sync Model Launcher]]**: Due at the end of the month. It will download and launch Qwen3.8 27B on one unit or a cluster and set up [[OpenCode]] as a browser-based coding front end.
- **Bundled software**: [[Nvidia Agent Toolkit]], [[CUDA-X AI]] libraries, [[Nemotron]] open models, and runtimes including [[Ollama]], [[vLLM]] and [[PyTorch]]. Nvidia suggests [[llama.cpp]] or [[LM Studio]] for a first model.
- **Ecosystem mentions**: [[Blender]] support (installer "coming soon"), [[Alibaba]]'s [[Qwen-Image-2.1]] running locally, and [[RTX Spark]] Windows PCs "coming this month". None of these has a date or a price.
- **[[Local AI]] pitch**: Nvidia sells the box as a way to run capable agents "privately, without cloud dependency", as an alternative to renting cloud instances by the hour.

## Key Takeaways

- **Price and date**: 64GB DGX Spark starts at $4,999 (US), on sale October 23.
- **Single-unit ceiling**: Runs models of up to 100B parameters entirely on the device.
- **Clustered ceiling**: Two units pool to 128GB and handle up to 200B parameters.
- **Same chip, half the memory**: Nvidia says the stack matches the 128GB model, but not the performance.
- **Unverified 1.7x**: The only benchmark is Nvidia's own, with no metric specified.
- **Gaps**: No UK or EU price, and no details on how partners will configure storage.
- **Setup automation**: Sync Cluster Assistant means nothing has to be reconfigured when going from one unit to two.

## 🃏 Review Questions

**Q1**: What is Nvidia offering with the 64GB DGX Spark?
**A**: A $4,999 desktop sold through six manufacturer partners from October 23. It keeps the GB10 Grace Blackwell chip and software stack of the 128GB model and runs models of up to 100B parameters locally, or up to 200B when two units are clustered.

**Q2**: Why should the "1.7x performance" clustering claim be treated with caution?
**A**: It comes from a single Nvidia in-house Qwen3.8 27B test that does not say whether it measures throughput, latency or time to first token. No one outside Nvidia has measured the machine yet.

**Q3**: What is the main argument for buying a DGX Spark instead of using cloud compute?
**A**: Nvidia pitches it as a way to run capable local agents privately, without depending on the cloud, rather than renting an instance by the hour. Whether it lives up to that will only be clear once it ships on October 23.
