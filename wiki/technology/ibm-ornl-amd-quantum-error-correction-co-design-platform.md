---
type: literature-note
source_url: https://newsroom.ibm.com/2026-11-05-oak-ridge-national-lab,-ibm,-and-amd-launch-new-co-design-platform-for-quantum-error-correction
author: Unknown
tags: [quantum-error-correction, ibm-quantum, hpc, amd]
date_consumed: 2026-11-10
---

## Summary
IBM, the DOE-funded Quantum Science Center at Oak Ridge National Laboratory, and AMD launched a co-design platform for quantum error correction that co-locates IBM quantum computers, including the 120-qubit Nighthawk, with ORNL's AMD-powered Umbra HPC system. The research challenge is now scaling error correction using more classical computing, in service of the DOE Quantum Genesis Mission's 2028 target. Findings may inform IBM's path to the fault-tolerant Starling system.

## Core Concepts
- [[Quantum Error Correction]]: protecting quantum information from noise; the focus has shifted from whether it works to how to scale it.
- [[Co-Design Platform]]: joint evaluation of quantum, HPC and AI architectures, software and workflows so they evolve together.
- [[IBM Quantum Nighthawk]]: 120-qubit processor with square lattice connectivity, fast circuit throughput and real-time pulse control.
- [[Umbra HPC System]]: ORNL system built on [[AMD Instinct MI355X]] GPUs and 5th Gen AMD EPYC CPUs, supplying classical compute for decoding and orchestration.
- [[Quantum-Centric Supercomputing]]: integrating quantum processors with classical HPC, as in sample-based quantum diagonalization.
- [[Quantum Genesis Mission]]: DOE program whose Q Competition targets 100 logical qubits running 100,000 hard operations by late 2028.
- [[IBM Quantum Starling]]: IBM's planned first fault-tolerant quantum computer.
- [[Oak Ridge National Laboratory]], [[Quantum Science Center]], [[IBM]], [[AMD]]; people include [[Jay Gambetta]], [[Travis Humble]] and [[Mark Papermaster]].

## Key Takeaways
- **Platform Launch**: IBM, ORNL's Quantum Science Center and AMD are initial partners.
- **Co-Location**: Nighthawk quantum hardware sits alongside ORNL's Umbra HPC system.
- **Classical Role**: AMD compute handles error-correction research, decoding optimization and software orchestration.
- **Target Gap**: DOE targets 100 logical qubits and 100,000 hard operations by late 2028.
- **Current Progress**: IBM has shown 70 logical qubits and 438 hard operations.
- **Scale Needed**: Roughly 230-fold increase in hard operation count required.
- **Pulse-Level Access**: IBM's Quantum System API supports mid-circuit measurement and real-time action on results.
- **Workflow Stack**: Concatenated codes, space-time codes, algorithm-aware decoders and compilation integrated in one stack.
- **Prior Work**: Earlier IBM-AMD decoding on AMD chips and IBM-ORNL materials simulations with Frontier.
- **Gambetta View**: The question is no longer if error correction works, but how to accelerate it.

## 🧠 Core Principles

**T1. Scaling quantum error correction is bounded by classical compute** — Correcting errors in real time requires fast classical decoding and orchestration alongside the quantum hardware, so progress depends on tight integration of the two rather than on qubits alone.
→ explains: Classical Role, Co-Location, Workflow Stack, Scale Needed

## 🃏 Review Questions

**Q1**: What did IBM, ORNL and AMD announce, and why?
**A**: They launched a co-design platform for quantum error correction that co-locates IBM quantum computers with ORNL's AMD-powered Umbra HPC system. The research challenge now is to scale error correction advances using more classical computing.

**Q2**: How large is the gap between current progress and the DOE target?
**A**: The DOE targets 100 logical qubits running 100,000 hard operations by late 2028, while IBM has demonstrated up to 70 logical qubits and 438 hard operations. Closing it needs roughly a 230-fold increase in hard operations.

**Q3**: What will researchers do with the platform, and what could it inform?
**A**: They will compare what each error correction method requires in qubits, time, samples and classical resources, to learn where GPU accelerators help most. The learnings may inform IBM's path to Starling and future HPC supercomputers.
