# Research: Use of Local LLMs for Coding
*Generated: 2026-08-01 | Scope: A comprehensive overview of local LLMs for coding — covering available tools, technical underpinnings, the 2026 ecosystem state, and practical workflow recommendations.*

## Research Outline

1. Local LLM coding tools landscape — what exists and how to get started
2. Technical underpinnings — quantization, inference optimization, and hardware requirements
3. Coding model benchmarks and selection — which models perform best and how to read benchmarks
4. 2026 ecosystem developments — recent model releases and tooling shifts
5. Practical workflow integration — opinionated recommendations for daily use

---

## Local LLM Coding Tools Landscape

### Ollama

- **Source**: https://ollama.com/blog
- **Summary**: Ollama is the most popular local model runner, now serving 8.9 million developers after raising $88M. It offers a unified CLI/API for downloading and running models, with an OpenAI-compatible endpoint. Its `ollama launch` command bootstraps Claude Code, OpenCode, and Codex CLI with zero configuration. Apple Silicon users get an MLX engine that delivers up to 90% faster inference for coding agents with models like Gemma 4.
- **Relevance**: Ollama is the de facto standard backend for local LLM coding — most other tools plug into it.

### LM Studio

- **Source**: https://lmstudio.ai
- **Summary**: LM Studio is a desktop GUI application for running local models, powered by llama.cpp and MLX. It includes a built-in agent called "Bionic" designed for coding tasks, automations, and computer control. All voice processing and inference stays fully on-device, making it a strong choice for privacy-sensitive workflows. It supports frontier open models including DeepSeek V4 Pro, Kimi K3, and GLM 5.2.
- **Relevance**: LM Studio provides the most polished GUI experience for getting started with local LLMs without touching the CLI.

### Cline (VS Code / JetBrains extension)

- **Source**: https://github.com/cline/cline
- **Summary**: Cline is an open-source agentic coding extension for VS Code and JetBrains with native Ollama and LM Studio support. It supports Plan & Act modes, cross-project edits, terminal execution with real-time error monitoring, multi-agent coordination, and `.clinerules` for project-specific guidance. It also works with any OpenAI-compatible API endpoint.
- **Relevance**: Cline is the most capable IDE-native coding agent that works out-of-the-box with local models.

### Aider (terminal)

- **Source**: https://github.com/paul-gauthier/aider
- **Summary**: Aider is a terminal-based AI pair programmer that connects to virtually any LLM including local models via Ollama. It builds a repo-map of your entire codebase, commits changes with meaningful git messages, lints and tests after each edit, and supports 100+ programming languages. Voice input and image/URL context are also supported.
- **Relevance**: Aider excels at multi-file refactors and greenfield projects from the terminal, with a detailed public benchmark leaderboard for model comparison.

### OpenCode

- **Source**: https://opencode.ai
- **Summary**: OpenCode is a terminal-and-IDE agent with 7.5 million monthly users. It connects to 75+ providers via Models.dev, explicitly including local models. Key differentiators include automatic LSP loading for better code intelligence and parallel multi-session support for running multiple agents simultaneously on the same project.
- **Relevance**: OpenCode is a strong Aider alternative for developers who want LSP-aware local coding agents.

### Continue.dev (legacy, now archived)

- **Source**: https://github.com/continuedev/continue
- **Summary**: Continue.dev was a pioneering open-source VS Code and JetBrains coding extension with deep Ollama/LM Studio integration. It reached 35,000+ GitHub stars before being acquired by Cursor in 2026 and entering read-only status. The Apache 2.0 codebase remains available as a foundation for forks.
- **Relevance**: Understanding Continue.dev's architecture is useful if building a custom IDE integration; its acquisition reflects the consolidation happening in this space.

### FastChat (API server)

- **Source**: https://github.com/lm-sys/FastChat
- **Summary**: FastChat is an open-source platform for serving local LLMs with an OpenAI-compatible REST API, enabling any tool built on the OpenAI SDK to switch to a local backend. It supports a three-component architecture (controller, model workers, API server) and accepts CPU, GPU, and Apple Silicon hardware. Integrates with vLLM for high-throughput scenarios.
- **Relevance**: FastChat is the glue layer for teams that want to self-host a local model API endpoint their existing tooling can consume.

---

## Technical Underpinnings

### llama.cpp and the GGUF Format

- **Source**: https://github.com/ggml-org/llama.cpp
- **Summary**: llama.cpp is the foundational C/C++ inference engine powering Ollama, LM Studio, and most local tools. It runs with no external dependencies and supports 1.5-bit through 8-bit integer quantization, with GGUF as the standard file format. A critical feature for consumer hardware is CPU+GPU hybrid inference: models larger than total VRAM are partially offloaded to RAM, allowing, for example, a 32B model to run on a 16GB GPU by keeping some layers in system RAM.
- **Relevance**: GGUF and llama.cpp are the foundation of the entire local LLM ecosystem — understanding them clarifies hardware decisions.

### vLLM (high-throughput inference)

- **Source**: https://github.com/vllm-project/vllm
- **Summary**: vLLM is a high-performance Python inference library from UC Berkeley that uses PagedAttention for efficient KV cache management, continuous batching, speculative decoding (EAGLE), and FlashAttention kernels. It exposes an OpenAI-compatible API and supports NVIDIA, AMD, and Intel GPUs. Quantization formats supported include FP8, GPTQ, AWQ, and GGUF. Best suited for multi-user or production local serving where throughput matters.
- **Relevance**: vLLM is the preferred serving layer for teams running local LLMs at scale or in CI/CD pipelines, distinct from single-developer llama.cpp use.

### Hardware Requirements by Model Size

| Model Size | VRAM Needed (Q4) | Example Models | Suitable Hardware |
|------------|-----------------|----------------|-------------------|
| 7B | ~5–6 GB | Qwen2.5-Coder 7B, CodeLlama 7B | Any modern GPU, M1/M2 |
| 14B | ~10 GB | Phi-4, Qwen2.5-Coder 14B | RTX 3080/4070, M2 Pro |
| 32B | ~20 GB | Qwen2.5-Coder 32B | RTX 3090/4090, M2 Max/Ultra |
| 70B+ | ~45 GB+ | Llama 3.3 70B | Multi-GPU or M2 Ultra |
| 480B MoE | ~60–80 GB active | Qwen3-Coder | High-end multi-GPU |

**Apple Silicon advantage**: Unified memory architecture means GPU and CPU share the same RAM pool. An M2 Max with 96GB can run 70B+ models at full quality that would require expensive multi-GPU setups on PC. The MLX engine adds further acceleration.

**Quantization tradeoffs**: Q4_K_M is the community sweet spot — roughly 50% size reduction with minimal quality loss versus BF16. Q8_0 is near-lossless but approximately doubles memory use versus Q4. Going below Q4 (Q3, Q2) yields noticeable quality degradation on reasoning tasks.

---

## Coding Model Benchmarks and Selection

### EvalPlus (correctness benchmark)

- **Source**: https://github.com/EvalPlus/EvalPlus
- **Summary**: EvalPlus is a rigorous coding benchmark framework that expands HumanEval by 80x and MBPP by 35x, making it significantly harder to game than the originals. It also includes EvalPerf for measuring code efficiency. Top open-source models evaluated on EvalPlus include Qwen2.5-Coder, DeepSeek-Coder V2, Meta's Llama 3.3, and StarCoder2.
- **Relevance**: EvalPlus gives a more honest picture of coding correctness than vanilla HumanEval, especially for edge cases.

### SWE-bench (agentic benchmark)

- **Source**: https://swebench.com
- **Summary**: SWE-bench measures an AI agent's ability to resolve real GitHub issues in open-source repositories — a proxy for actual software engineering work rather than toy problems. It has Verified, Lite, Full, Multilingual, and Multimodal tiers with filterable leaderboards for open-source vs. proprietary models.
- **Relevance**: SWE-bench is the most practically relevant benchmark for evaluating local LLMs in autonomous coding workflows.

### Aider Polyglot Leaderboard

- **Source**: https://aider.chat/docs/leaderboards/
- **Summary**: Aider's polyglot benchmark tests 225 exercises across C++, Go, Java, JavaScript, Python, and Rust, measuring both solution correctness and the model's ability to edit code without human intervention. GPT-5 leads at 88%. Among open/local options: DeepSeek V3.2 Exp reaches 74.2% at $1.30/run (outstanding value), DeepSeek R1 0528 hits 71.4% at $4.80/run, and Qwen3 235B A22B scores 59.6%.
- **Relevance**: This leaderboard is specifically tuned to the agentic code-editing task that tools like Aider perform — directly actionable for model selection.

### Key Models Ranked for Local Use

| Model | HumanEval | Params (active) | VRAM (Q4) | Notes |
|-------|-----------|-----------------|-----------|-------|
| Qwen3-Coder 480B | ~Claude Sonnet | 35B active | Multi-GPU | Flagship agentic model, 1M context |
| Qwen2.5-Coder 32B | "GPT-4o level" | 32B | ~20 GB | Best single-GPU option |
| DeepSeek-Coder V2 16B Lite | Near GPT-4 Turbo | 2.4B active | ~10 GB | MoE efficiency advantage |
| Phi-4 14B | 82.6% | 14B | ~10 GB | Python-heavy training |
| Qwen2.5-Coder 7B | Strong 7B | 7B | ~5 GB | Best sub-10GB option |

---

## 2026 Ecosystem Developments

### Ollama Funding and Scale

- **Source**: https://ollama.com/blog
- **Summary**: In 2026, Ollama raised $88M from Benchmark, Theory Ventures, 8VC, and Y Combinator — signaling institutional confidence in local LLM infrastructure. The platform reached 8.9M developers and launched a web search API, image generation, and streaming tool calls. The `ollama launch` command was introduced as a zero-config way to bootstrap coding agent environments.
- **Relevance**: Ollama's growth and funding confirm that local LLM tooling is a serious infrastructure category, not just a hobbyist niche.

### Apple Silicon MLX Engine

- **Source**: https://ollama.com/blog
- **Summary**: Ollama's Apple Silicon MLX engine delivers up to 90% faster inference for coding agents compared to the llama.cpp backend on the same hardware. Gemma 4 is specifically cited as a beneficiary. This closes much of the performance gap between consumer Mac hardware and cloud APIs for coding workloads.
- **Relevance**: Apple Silicon Macs are now first-class local LLM hardware — the MLX engine makes them competitive with dedicated NVIDIA GPU setups for many coding tasks.

### Qwen3-Coder: MoE Flagship for Coding Agents

- **Source**: https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct
- **Summary**: Alibaba released Qwen3-Coder-480B in 2026 — a Mixture-of-Experts architecture with 480B total parameters but only 35B active per token, targeting "Claude Sonnet-level" performance. It achieves 38.7 on SWE-bench Pro and supports a native 256K context window extendable to 1M tokens. It is the current open-weight frontier model for agentic coding and integrates with Ollama, LM Studio, Cline, and vLLM.
- **Relevance**: Qwen3-Coder represents the state-of-the-art in locally deployable coding models as of mid-2026, with hardware requirements manageable via quantization.

### Continue.dev Acquired by Cursor

- **Source**: https://github.com/continuedev/continue
- **Summary**: Continue.dev, formerly the leading open-source VS Code coding extension, was acquired by Cursor and placed in read-only/archived status. Its Apache 2.0 codebase remains for community forks. The vacuum it leaves is being filled by Cline and OpenCode for local-model users.
- **Relevance**: A major consolidation event — developers who built workflows around Continue.dev need to migrate to actively maintained alternatives.

### LM Studio Bionic Agent

- **Source**: https://lmstudio.ai
- **Summary**: LM Studio launched Bionic, its built-in desktop coding agent, designed to handle coding tasks, automations, and computer control entirely on-device. This makes LM Studio a complete end-to-end local coding environment without needing separate tool integrations.
- **Relevance**: LM Studio is no longer just a model runner — it is evolving into a full local AI coding IDE.

---

## Practical Workflow Integration

### Recommended Starter Setup

- **Source**: https://ollama.com/blog, https://github.com/cline/cline
- **Summary**: The simplest production-ready local coding setup in 2026 is: (1) Install Ollama; (2) Pull `qwen2.5-coder:32b` or `phi4` depending on available VRAM; (3) Install the Cline extension in VS Code and point it at the Ollama OpenAI-compatible endpoint (`http://localhost:11434/v1`). This takes under 30 minutes and requires no API keys. For terminal-first users, replace Cline with Aider (`pip install aider-chat`) and set `OLLAMA_API_BASE`.
- **Relevance**: Getting from zero to working local LLM coding assistant is now a one-afternoon task.

### When to Use Local vs. Cloud

| Scenario | Recommendation |
|----------|---------------|
| Privacy-sensitive code (proprietary IP) | Local — data never leaves machine |
| Greenfield projects, early exploration | Local — iterate freely with no API cost |
| Complex multi-file refactors | Cloud or Qwen3-Coder locally — needs strong reasoning |
| CI/CD pipelines, automation at scale | Local vLLM server — cost control |
| Pair programming, real-time completions | Local 7B–14B for latency; cloud for quality |
| Agentic SWE-bench-style tasks | Qwen3-Coder or cloud — frontier capability needed |

### Context Management Tips

- Limit context to what's actually needed — don't paste entire repos unless using Qwen3-Coder's 1M context window
- Use Aider's repo-map feature: it builds a compact structural summary of the codebase so you don't have to manually manage which files to include
- For Cline: use `.clinerules` files to pre-load project conventions, reducing redundant prompting
- Prefer fill-in-the-middle (FIM) models (CodeGemma, Codestral) for inline completion; use instruct models for chat/agent workflows

### Model Selection Heuristic

- **8–12 GB VRAM / 16 GB unified memory**: Phi-4 14B or Qwen2.5-Coder 7B
- **16–24 GB VRAM / 32 GB unified memory**: Qwen2.5-Coder 32B — the community's best single-GPU coding model
- **Apple Silicon M2 Max or M3 Pro (36GB+)**: Qwen2.5-Coder 32B via Ollama MLX for best speed
- **Multi-GPU or 64GB+ unified memory**: Qwen3-Coder (quantized) for Claude Sonnet-class coding

---

## Articles to Ingest

URLs ready for `/kb-scrapecontent` → `/kb-ingest`:

- https://ollama.com/blog
- https://lmstudio.ai
- https://github.com/cline/cline
- https://github.com/paul-gauthier/aider
- https://opencode.ai
- https://github.com/continuedev/continue
- https://github.com/ggml-org/llama.cpp
- https://github.com/vllm-project/vllm
- https://github.com/EvalPlus/EvalPlus
- https://swebench.com
- https://aider.chat/docs/leaderboards/
- https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct
- https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct
- https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Instruct
- https://huggingface.co/microsoft/Phi-4
- https://github.com/lm-sys/FastChat
- https://ollama.com/library
