---
source_url: https://mixed-news.com/en/nvidia-dgx-spark-64gb-4999-october-23-cluster-128gb/
author: Chris Steven
date: 2026-10-03
---

# Nvidia's DGX Spark gets a 64GB model at $4,999, and two can pool to 128GB

Nvidia will sell a 64GB configuration of its DGX Spark desktop machine from October 23 at a starting price of $4,999 in the US, and the company says a single unit runs models of up to 100 billion parameters entirely on the device. Two of them wired together with a QSFP cable pool their memory to 128GB and raise that ceiling to up to 200 billion parameters, according to Nvidia's announcement of October 2.

The 64GB machine keeps the GB10 Grace Blackwell Superchip Nvidia uses in the 128GB model.

The new version is sold "exclusively from manufacturer partners", which Nvidia names as Acer, ASUS, Dell, Gigabyte, HP and MSI. It sits below the 128GB model, and Nvidia says the cheaper box keeps the GB10 Grace Blackwell Superchip, DGX OS and the full Nvidia AI software stack, "same as the 128GB model".

Nvidia does not claim the two configurations perform alike. That comparison covers the chip, the operating system and the software, and the cheaper box has half the memory to work with.

## The clustering figures come from Nvidia's own test

Every DGX Spark ships with an Nvidia ConnectX-7 network card, and two units connect directly over what Nvidia calls a 200 GbE fabric. The pair delivers "twice the memory bandwidth and up to 1.7x the performance" of a single system, Nvidia says, and it ties the 1.7x to one in-house benchmark: "In NVIDIA's Qwen 3.8 27B test, two clustered 64 GB systems delivered up to 1.7x performance compared with a single system".

Nvidia does not say what the 1.7x measures, so there is no way to tell from the announcement whether the gain lands in tokens per second, in end-to-end latency or in time to first token. It is also the only performance figure in the announcement, it is Nvidia's own, and with the machine not on sale until October 23, nobody outside Nvidia has measured one.

## A cluster assistant does the networking

Nvidia Sync Cluster Assistant detects connected units, validates their configuration and configures the ConnectX-7 network, which is the part owners of two boxes would otherwise do by hand. Every node runs the same software stack, so by Nvidia's account "nothing needs to be reconfigured when scaling from one unit to two".

A companion tool, Nvidia Sync Model Launcher, is "coming at the end of the month". Nvidia says it will download and launch Qwen3.8 27B on one system or a cluster and "set up OpenCode to use the model", which puts the coding front end in a browser on whatever laptop is to hand.

## What is in the box, and what Nvidia leaves out

The machine arrives with the Nvidia Agent Toolkit, CUDA-X AI libraries, the company's own Nemotron open models and runtimes including Ollama, vLLM and PyTorch with CUDA. For a first model Nvidia points to llama.cpp, Ollama, vLLM or LM Studio, and it says Blender "is among the first major creator application providers to support the platform", with an installer described only as coming soon.

The same announcement flags Alibaba's Qwen-Image-2.1 model, which Nvidia says runs locally on RTX GPUs, DGX Spark and DGX Station, and new Windows PCs powered by Nvidia RTX Spark "coming this month" from Acer, ASUS, Dell, HP, Lenovo, Microsoft and MSI. Neither carries a date or a price.

The $4,999 is a starting price from six separate manufacturers rather than one Nvidia figure, and no UK or European price is given, nor any detail of how the six partners will configure storage around the shared 64GB of unified memory. Nvidia's pitch rests elsewhere: it describes the machine as running capable local agents "privately, without cloud dependency", which is the argument for buying one rather than renting an instance by the hour. October 23 is when it has to stand up.
