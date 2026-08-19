---
source_url: https://www.hpcwire.com/2026/08/18/whats-hot-now-custom-ai-chips
author: Unknown
date: 2026-08-18
---

# What's Hot Now: Custom AI Chips

The AI boom has largely been powered by standardized hardware, including powerful GPUs, all-purpose CPUs, and as much HBM and DRAM as one can comfortably grab. But recent events — including AMD's acquisition of Taalas, Etched's $700 million fundraising round, and frontier AI labs developing their own chips — suggest that custom-built hardware could play a bigger role in AI's future than initially thought.

There has always been a tradeoff between performance and flexibility in hardware design. General-purpose CPUs can run all sorts of workloads efficiently, but math- or graphics-heavy parallel workloads are better served by specialized chips like GPUs. As the AI industry's focus shifts from training to inference, chipmakers are rethinking their priors and doubling down on custom silicon.

Nvidia pivoted away from its DRAM-heavy Rubin CPX GPU in December 2025, instead spending $20 billion to acquire the assets of Groq, whose SRAM-heavy "language processing unit" (LPU) is optimized for extreme low-latency token generation. AMD is making a similar move with its planned acquisition of Taalas, whose HC1 demo chip hard-wires Llama 3.1-8B weights directly onto silicon to generate 16,000 tokens per second — nearly 10x faster than the next fastest chip on that model, at the cost of almost all programmability.

Startup Etched is taking a similar tack with its Sohu ASIC, designed specifically to run transformer models (though not restricted to a single model like Talaas's chip). Etched claims Sohu can generate 500,000 tokens per second on Llama 70B — 20x the throughput of an eight-GPU H100 system. Today, Etched announced it has raised $700 million at a $21 billion valuation in a round led by Jane Street, which is also a customer running an Etched cluster in production. Etched says it has $1 billion in orders across public and private frontier AI companies and clouds, and is also developing "Low Voltage Inference" and "Cluster Scale Memory" techniques to boost cluster efficiency and density.

Leading AI labs are entering the custom-chip game too: OpenAI co-developed its first custom AI inference processor, dubbed Jalapeno, with Broadcom and Celestica. Anthropic is reportedly in talks with Samsung to use its 2nm fabrication nodes for custom AI training chips, while continuing to rely on Nvidia, Google, and Amazon chips. All three major cloud providers already have their own custom silicon — Google's TPU, AWS's Trainium, and Microsoft's Maia — reflecting the economies of scale available to companies running large fractions of the world's computational workload.
