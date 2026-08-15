---
source_url: https://techcrunch.com/2026/08/14/kog-is-going-deeper-to-squeeze-more-inference-out-of-gpus
author: Anna Heim
date: 2026-08-14
---

# Kog is going deeper to squeeze more inference out of GPUs

The race for faster AI inference is on, and markets gave Cerebras and its purpose-built chips a warm welcome in its IPO debut in May. But French startup Kog is betting that there's a lot more power to be squeezed out of conventional GPUs.

The startup hit the front page of Hacker News in May with a tech preview aimed at proving that "extremely fast single-request decoding is possible on the standard datacenter GPUs enterprises already own" — such as the AMD MI300X and Nvidia H200 GPUs it used for its demo.

With inference speed and costs now being a critical bottleneck, Kog's promise to unlock new capabilities on existing hardware with software optimization attracted more than onlookers. "We had 200 tangible business leads," CEO Gaël Delalleau told TechCrunch.

Based on early feedback, the solo founder expects software engineering to be the first use case. Veteran Claude Code users are well aware that they sometimes have to wait hours to get results. Anthropic itself understands that speed is worth money, and charges a price multiple for Claude's Fast Mode.

Kog is hoping to target customers put off by those delays, usually because they rely on AI workflows for professional tasks. The startup also has design partners that let users generate games and apps with a prompt, for whom a faster outcome thanks to the Kog Inference Engine (KIE) would mean more revenue, Delalleau said.

The company realizes this market is not quite mature yet. While observing demand, Kog learned that its prospective customers aren't prepared to fine-tune small models. "And that's why since the launch, we've been fully focused on accelerating the development of larger models to meet the demand we've seen."

This leaves Kog with a huge leap to make to deliver on its promise of "30x faster LLM inference." Its demo showed an impressive 3,000 per-request tokens per second (TPS) — but with a purpose-built small model with only some 2 billion parameters, the now open-sourced Laneformer 2B.

Contradicting skeptics, Delalleau is confident the same approach can work just as well with LLMs, whose size can be a challenge for inference chips. "GPUs have a bright future," he said. For Kog's CEO, the idea that they aren't well suited for decoding has become a misconception; newer GPUs have more and more memory bandwidth that only begs to be unlocked.

Kog isn't alone in thinking that software optimization can help GPUs do more than it says on the box. ZML, also from France, released hardware-agnostic software that bypasses Nvidia's CUDA to support fast inference across competing chips. But Delalleau said Kog is more akin to Stanford University lab Hazy Research, with an even deeper-level focus on GPU acceleration.

Having studied solid-state physics at France's École Polytechnique, Delalleau went on to work in offensive cybersecurity — also known as white hat hacking. This shaped the mindset he now encourages his team to adopt: understanding the laws of physics and the laws of the GPU to make the most of them, and reverse-engineering things down to assembly language and binary code.

With a team of 11 people, Kog dedicates several weeks or months per new GPU to conduct low-level engineering research, which limits the number of chips it can work with for now. In the longer run, Kog hopes to feed its methodology into agent-based pipelines to support more chips and models — potentially adding European sovereignty tailwinds, as the startup is backed by France's Bpifrance and French Tech 2030.

"Once we've implemented our first major model at 10x speed, which I think will be in September, we'll be able to start demonstrating customer traction and from there, raise our Series A," Delalleau said.
