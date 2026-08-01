---
type: literature-note
source_url: https://blog.bytebytego.com/p/ep217-latency-vs-throughput-vs-bandwidth
author: ByteByteGo
tags: [system-design, networking, ai-hardware, performance]
date_consumed: 2026-08-01
---

## Summary

Latency, throughput, and bandwidth are distinct performance metrics that are often confused: latency measures delay for a single packet, throughput measures actual data delivery rate, and bandwidth is the theoretical maximum capacity of a link. Google's TPU has evolved into two specialized 8th-generation variants — one optimized for training throughput and one for inference latency — reflecting how hardware is being purpose-built for different stages of AI workloads. The article also surveys five major AI trends for 2026, including efficient reasoning, persistent agents, and open-weight model proliferation.

## Core Concepts

- **[[Latency]]**: The time for a single packet to travel from sender to receiver (e.g., 40 ms round-trip ping).
- **[[Throughput]]**: The actual data delivery rate achieved per second (e.g., 62 Mbps download speed).
- **[[Bandwidth]]**: The maximum theoretical capacity of a network link (e.g., a 100 Mbps connection ceiling).
- **[[Google TPU]]**: Google's custom [[Tensor Processing Unit]] designed from scratch for matrix multiplications in deep learning; 8th generation splits into TPU 8t (training) and TPU 8i (inference).
- **[[Claude Code]] Permission Modes**: Seven modes controlling how the Claude Code agent handles tool-call approvals, from fully interactive (`default`) to unrestricted (`bypassPermissions`).
- **[[RLVR Training]]**: Reinforcement Learning from Verifiable Rewards — scales reasoning by auto-checking math and code outputs.
- **[[Mixture of Experts]] (MoE)**: Sparse architecture used in models like Qwen3.5 to improve efficiency at scale.

## Key Takeaways

- **Bandwidth ceiling**: Throughput is always lower than bandwidth due to congestion, packet loss, and overhead.
- **Latency ≠ throughput**: Low latency does not guarantee high throughput; small payloads and tight windows limit delivery rate.
- **Highway analogy**: Bandwidth = highway width; throughput = traffic flow; latency = travel time A→B.
- **TPU specialization**: TPU 8t maximizes raw throughput for training; TPU 8i minimizes latency for inference.
- **Shared stack**: Both TPU 8t and 8i share Axion CPUs, liquid cooling, and software — code is portable across both.
- **Claude Code modes**: Only 5 of 7 permission modes are user-selectable; `auto` is feature-flagged, `bubble` is internal-only.
- **2026 AI trends**: Efficient reasoning, persistent agents, repo-scale coding, open-weight models, and world models / physical AI.
- **Persistent agents**: Expect always-on agents with file access completing multi-day tasks autonomously.
- **Open-weight competition**: Models like GLM-5 and Kimi K2.5 are closing the gap with closed frontier models.

## 🧠 First Principles & Mental Models

- **[[Capacity vs. Utilization]]**: Bandwidth is the theoretical ceiling while throughput is realized output — the gap between them is explained by friction (congestion, overhead, loss), a first-principles reminder that designed capacity rarely equals operational performance.
- **[[Specialization Trade-off]]**: Google splitting the TPU 8 into training (throughput-optimized) and inference (latency-optimized) variants illustrates the core systems principle that optimizing for one dimension often comes at a cost to another, and that purpose-built tools outperform general ones when the workload is well-understood.
