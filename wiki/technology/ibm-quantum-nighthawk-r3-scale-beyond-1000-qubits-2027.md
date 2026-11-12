---
type: literature-note
source_url: https://www.prnewswire.com/news-releases/ibm-quantum-nighthawk-demonstrates-new-levels-of-speed-and-quality-with-plans-to-scale-beyond-1-000-qubits-in-2027--302935826.html
author: IBM
tags: [quantum-computing, ibm, nighthawk, hybrid-hpc]
date_consumed: 2026-11-13
---

## Summary
IBM announced that Nighthawk r3 will execute 10,000 quantum operations across 520 qubits, with two r3 processors to be linked into a single 1,040-qubit system in 2027. Clients using the current Nighthawk r2 report speedups of up to 19x over earlier IBM processors across 34 billion circuits. IBM also enhanced its Quantum Platform to unite quantum and classical HPC compute in one managed environment.

## Core Concepts
- **[[IBM Quantum Nighthawk]] r2**: Delivers up to 100,000 samples per second and 7,500+ operations on 120 qubits, using fast [[Qubit Reset]].
- **Nighthawk r3**: 520 programmable qubits (2,034 physical), square-lattice connectivity, and 10 chip-to-chip [[L-Couplers]] for [[Modular Quantum Architecture]].
- **[[Quantum Advantage]]**: Algorithmiq experiment extended to r2 ran 8x faster, and needs an estimated 240x more memory to simulate classically with [[Tensor Network Methods]].
- **[[Quantum Error Correction]] and mitigation**: Require growing classical compute alongside quantum hardware.
- **[[IBM Quantum Platform]]**: Unifies [[High-Performance Computing]] and quantum workflows; supports pulse-level control.
- **[[Jay Gambetta]]**: IBM Research Director; frames accuracy and speed as both fundamental to useful quantum computing.
- **Partners**: E.ON, Algorithmiq, Q-CTRL, [[RIKEN]], Cleveland Clinic, [[Oak Ridge National Laboratory]], [[AMD]].

## Key Takeaways
- **Speed Matters**: Quantum answers arrive as samples, so throughput decides practical timeframes and cost.
- **r2 Results**: Up to 19x speedups reported across 34 billion circuits.
- **Customer Wins**: E.ON saw 15x in quantum machine learning for grid optimization.
- **Scaling Plan**: Two Nighthawk r3 processors link into a 1,040-qubit system in 2027.
- **Modularity Proof**: l-couplers reached 99.3% state-transfer fidelity against a 99.9% target.
- **Cryogenic Link**: Two cryogenic modules joined, cooling below 15 millikelvin in under five days.
- **Hybrid Compute**: SQD workflow ran about 5x faster with 100x more computations on the new platform.
- **Error Correction**: ORNL and AMD co-design platform co-locates Nighthawk with an HPC system.

## 🧠 Core Principles

**T1. Throughput gates practicality** — When a computation returns one probabilistic result per run, answers require millions to billions of runs, so run speed sets whether a workload is feasible in time and cost, alongside accuracy and scale.
→ explains: Speed Matters, r2 Results, Customer Wins

## 🃏 Review Questions

**Q1**: What is IBM's central claim about useful quantum computing?
**A**: Useful quantum computing needs both quality and speed, because results arrive as samples and millions to billions are required. Nighthawk r2 shows this today and r3 extends the architecture to larger systems.

**Q2**: What evidence shows Nighthawk r2's speed advantage?
**A**: r2 delivers up to 100,000 samples per second, and partners ran 34 billion circuits with speedups up to 19x. E.ON saw 15x, and IBM saw 12x on an Oak Ridge materials experiment, both versus Heron.

**Q3**: How does IBM plan to scale beyond a single chip?
**A**: Nighthawk r3 adds 10 l-couplers so two processors can be linked into one 1,040-qubit system in 2027. IBM has already shown 99.3% state-transfer fidelity and a two-module cryogenic connection.
