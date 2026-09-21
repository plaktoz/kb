---
type: literature-note
source_url: https://agentexecutor.io
author: Unknown
tags: [ai-agents, runtime, google, infrastructure]
date_consumed: 2026-09-21
---

## Summary

AX is an open-source agentic task runtime developed from [[Google DeepMind]] research, designed to run declaratively defined agent workloads at massive scale. It addresses the gap between stateless microservice orchestrators and the bursty, stateful nature of agent workloads by providing sandboxing, workspace setup, network isolation, and cluster-level scheduling. Built on [[Agent Substrate]], it enables billions of concurrent agent sessions per cluster with sub-second resumption from checkpoints.

## Core Concepts

- **[[AX Runtime]]** — Open-source runtime for defining and executing agentic tasks at scale with declarative configuration
- **[[Agent Substrate]]** — Underlying compute runtime designed for high-density actor lifecycles on which AX is built
- **[[Task Sandbox]]** — Isolated execution unit with CPU/memory limits; cheap to create, suspend, or delete
- **[[Generative Workspaces]]** — Environment provisioning driven by plain-English descriptions; an agent configures the workspace automatically on first boot
- **[[Google DeepMind]]** — Origin of AX's agentic runtime research
- **[[MCP Servers]]** — Supported toolchain auto-configured by Workspaces before a task starts

## Key Takeaways

- **Task primitive**: Isolated sandbox with CPU/memory limits; cheap to create, suspend, or delete.
- **Workspace primitive**: Auto-configures Git repos, [[MCP Servers]], and toolchains before task starts.
- **Gateway primitive**: Network policy management with explicit allowlists and credential injection.
- **Model primitive**: Centralized config for model parameters, API keys, and version pinning.
- **Scale**: Supports billions of concurrent agent sessions per cluster via lightweight actors.
- **Sub-second resumption**: Idle agents checkpointed and restored with zero cold-start delay.
- **Dense multiplexing**: Dozens of tasks share worker resources, reducing idle costs.
- **License**: Apache 2.0; repo at github.com/google/ax.

## 🧠 First Principles & Mental Models

- **[[Separation of Concerns]]**: AX decouples task execution, workspace provisioning, network policy, and model configuration into discrete primitives — each concern managed independently for composability and scalability.
- **[[Actor Model]]**: Treating each agent session as a lightweight, suspendable actor enables the massive concurrency AX achieves without the overhead of heavy VM-per-session approaches.

## 🃏 Review Questions

**Q1**: What core problem does AX solve that existing microservice orchestrators do not?
**A**: AX addresses the gap between stateless microservice orchestrators and the bursty, stateful nature of agent workloads by providing sandboxing, checkpointing, and workspace provisioning tailored to agentic sessions.

**Q2**: How does AX achieve sub-second resumption for idle agents?
**A**: Idle agents are checkpointed and can be restored with "zero cold-start delay," allowing the runtime to reclaim resources from paused agents without losing session state.

**Q3**: How would an operator use the Workspace primitive to bootstrap a new agent environment?
**A**: An operator describes the desired environment in plain English; the Workspace primitive auto-configures the Git repos, MCP servers, and toolchains required before the task starts.
