---
type: literature-note
source_url: https://www.prnewswire.com/news-releases/ibm-fermilab-and-nvidia-announce-plans-for-new-co-design-platform-to-accelerate-the-development-of-next-generation-modular-quantum-computers-302940668.html
author: IBM
tags: [quantum-computing, ibm-quantum, nvidia, hpc]
date_consumed: 2026-11-20
---

## Summary
IBM, NVIDIA and Fermilab plan a modular quantum computing co-design platform that co-locates NVIDIA DGX B200 systems with IBM quantum computers such as Nighthawk. IBM also announced Slurm integration via the open-source QRMI so quantum processors can be scheduled like CPUs and GPUs. New IBM, RIKEN and NVIDIA results show a 79-fold accuracy gain in a quantum-classical simulation of an iron-sulfur cluster.

## Core Concepts
- [[IBM Quantum Nighthawk]]: IBM's most powerful quantum processor, with 120 qubits running up to 7,500 two-qubit operations at up to 100,000 samples per second.
- [[Modular Quantum Computing]]: multiple quantum processors working together as the architecture for [[Fault-Tolerant Quantum Computing]].
- [[Quantum-Classical Hybrid Computing]]: pairing QPUs with [[NVIDIA]] GPUs and HPC to solve problems beyond classical systems alone.
- [[Fermilab]] and its SQMS Center: contribute ultracoherent quantum hardware expertise and high-energy and nuclear physics applications (lattice gauge theories, neutrino interactions, nuclear simulations).
- [[Slurm]] and [[Quantum Resource Management Interface (QRMI)]]: an open-source, vendor-agnostic layer integrating QPUs with Slurm Hierarchical Resources (HRES) scheduling.
- [[Sample-Based Quantum Diagonalization]] (SQD): technique applied to the Fe4S4 iron-sulfur cluster with RIKEN, compared against [[Density-Matrix Renormalization Group]] (DMRG).
- [[Jerry Chow]], [[Krysta Svore]], [[Anna Grassellino]], [[Seiji Yunoki]]: quoted leaders from IBM, NVIDIA, Fermilab and RIKEN.

## Key Takeaways
- **Co-Design Platform**: DGX B200 systems co-located with IBM quantum computers, leveraging Fermilab's SQMS Center.
- **Scheduler Gap Closed**: Slurm previously had no native concept of a quantum processor.
- **QPU Sharing**: Unlike GPUs, QPUs can be shared across multiple nodes via HRES.
- **Normal Slurm Job**: Quantum-classical workflows need no separate queue, login, or operating model.
- **Accuracy Result**: 79-fold accuracy improvement over earlier SQD runs of the same experiment.
- **Scale of Run**: Up to 4,000 two-qubit operations on 72 qubits, 5 million samples.
- **Near-Classical Parity**: Within 4.3 millihartree of DMRG accuracy.
- **Realistic Guess**: An intentionally imperfect initial state steers the quantum computer toward relevant electron configurations.

## 🧠 Core Principles

**T1. Shared scarce resources need native scheduling and accounting** — A resource is easiest to adopt when it is allocated, reserved, and accounted for through the same policies as familiar resources, not bolted on outside the core model. · *model:* [[Abstraction Layers]]
→ explains: Scheduler Gap Closed, QPU Sharing, Normal Slurm Job

## 🃏 Review Questions

**Q1**: What is the core aim of the IBM, NVIDIA and Fermilab collaboration?
**A**: To advance the integration of quantum and classical computing through a modular co-design platform, exploring how both scale together in the architectures that will define fault-tolerant quantum computers.

**Q2**: How does QRMI let Slurm manage quantum processors?
**A**: QRMI is an open-source, vendor-agnostic layer that integrates with Slurm Hierarchical Resources (HRES) scheduling, so QPU time, which can be shared across nodes, is allocated, reserved, and accounted for like CPU and GPU time.

**Q3**: What does the Fe4S4 result imply for hybrid quantum-HPC work?
**A**: Starting from an intentionally imperfect, more realistic state guess and combining quantum computers with GPUs gave a 79-fold accuracy gain, landing within 4.3 millihartree of DMRG. This suggests hybrid workflows can approach leading classical methods on very demanding problems.
