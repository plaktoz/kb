---
type: literature-note
source_url: https://investors.delltechnologies.com/node/21766/pdf
author: Dell Technologies
tags: [dell, rtx-spark, local-ai, ai-workstations]
date_consumed: 2026-10-08
---

## Summary

[[Dell Technologies]], with [[NVIDIA]] and [[Microsoft]], announced on Oct. 7, 2026 a line of Windows PCs and workstations built for [[Agentic AI]]: the XPS 16 Creator Edition laptop, the Dell Creator Edition Desktop, and Dell Pro Precision with GB300 running Windows. The two creator machines are the first Dell systems built on the [[NVIDIA RTX Spark]] superchip, whose unified memory lets them run large AI models locally without relying on the cloud. Dell argues that AI now runs continuously and makes decisions inside everyday work, so creators and enterprise developers need always-on local compute in the Windows environments they already manage.

## Core Concepts

- **[[NVIDIA RTX Spark]] superchip**: up to a 6,144-core [[NVIDIA Blackwell]] RTX GPU, up to a 20-core [[NVIDIA Grace]] CPU, and up to 128GB of [[Unified Memory]].
- **[[Unified Memory Architecture]]**: the CPU and GPU share one memory pool, so the machine can handle 3D scenes, 8K timelines and AI models too big for a discrete-GPU laptop.
- **XPS 16 Creator Edition**: 17.8mm CNC aluminum chassis; 3.2K [[Tandem OLED]] display (DisplayHDR True Black 600, up to 1,000 nits, 100% DCI-P3, Delta E < 2, Pantone Validated, 20–120Hz variable refresh rate).
- **Connectivity**: SDXC v7.1 card reader, 3x USB4 Type-C with DisplayPort 2.1 and Power Delivery, HDMI 2.1b, universal audio jack.
- **[[Local AI]] development**: the full [[CUDA]] stack for prototyping, fine-tuning and running inference on one machine; [[GitHub Copilot]], [[Claude Code]], [[ComfyUI]] and [[Cursor]] run on RTX Spark.
- **Compatibility**: native Blender, DaVinci Resolve, Photoshop and Premiere; x86 apps such as MATLAB run through [[Prism Emulation]]; supports Easy Anti-Cheat, BattlEye and the Xbox PC app.
- **Dell Creator Edition Desktop**: the same RTX Spark chip and up to 128GB of memory in a compact desktop, without a laptop's thermal or battery limits; up to 1 petaflop of FP4 compute and models up to 200B parameters.
- **Rebrand**: Dell Pro Max with GB10/GB300 is renamed Dell Pro Precision with GB10/GB300.
- **Dell Pro Precision with GB300 on Windows**: the [[NVIDIA GB300 Grace Blackwell Ultra]] Desktop Superchip, up to 20 petaflops of FP4 and 748GB of coherent memory, models up to 1 trillion parameters locally; Dell MaxCool claims up to 5x higher cooling efficiency.
- **[[Windows Subsystem for Linux]]**: gives developers CUDA and Linux AI frameworks inside Windows with no dual boot. Dell notes enterprises have traditionally used Linux for heavy AI workloads.
- **[[Rob Bruckner]]**: president of Client Devices at Dell; says AI "is no longer something you build in the cloud and deploy later."

## Key Takeaways

- **First for XPS**: XPS 16 Creator Edition is the first XPS built on RTX Spark.
- **Memory edge**: 128GB of unified memory handles models a discrete-GPU laptop can't fit.
- **Desktop scale**: 1 PFLOP FP4 and support for models up to 200B parameters.
- **Workstation scale**: GB300 delivers 20 PFLOPs FP4, 748GB memory and 1T-parameter models.
- **Windows over Linux**: GB300 on Windows needs no new group policies or OS changes.
- **Agent tooling**: Claude Code, Cursor, Copilot and ComfyUI run natively on RTX Spark.
- **Availability**: XPS 16 pre-orders at Best Buy from Oct. 7; the desktop and GB300 on Windows are "coming soon."

## 🃏 Review Questions

**Q1**: What is Dell's main argument for this new lineup of Windows PCs and workstations?
**A**: Agentic AI now runs continuously inside daily work, so creators and enterprise developers need always-on local compute without full cloud dependency. Dell, NVIDIA and Microsoft are offering that compute inside Windows.

**Q2**: What hardware feature lets the XPS 16 Creator Edition run workloads a traditional laptop can't?
**A**: The RTX Spark superchip gives the CPU and GPU one shared pool of up to 128GB of memory. That lets the laptop handle huge 3D scenes, multi-layer 8K timelines and large AI models that would exceed a discrete GPU's memory.

**Q3**: Why does Windows support for Dell Pro Precision with GB300 matter to enterprise IT teams?
**A**: Heavy AI work has traditionally run on Linux, while most other work happens on Windows. GB300 on Windows fits into existing managed infrastructure without new policies, and WSL still gives developers CUDA and Linux frameworks.
