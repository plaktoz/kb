---
type: literature-note
source_url: https://www.eetimes.com/ibm-details-quantum-ai-developments-in-india
author: Yashasvini Razdan
tags: [quantum-computing, post-quantum-cryptography, ai-accelerators, ibm-india]
date_consumed: 2026-10-01
---

## Summary

At SEMICON India 2026, IBM distinguished engineer Rahul Rao detailed India's expanding role across quantum processor scaling, post-quantum cryptography (PQC), and AI accelerator design, framing India's contribution as "talent arbitrage" rather than cost arbitrage. IBM's roadmap aims to scale quantum processors from 200-300 qubits today to 4,000 qubits, backed by a new dedicated quantum-wafer foundry (Anderon) in Albany, New York. IBM's India engineering lab (ISDL) also co-developed the 75-watt Spyre AI accelerator and is pursuing PQC proofs of concept with Indian public-sector institutions.

## Core Concepts

- **[[IBM]] India Systems Development Lab (ISDL)**: Engineering hub spanning processor design, AI accelerators, quantum computing, and PQC; developed the [[Spyre]] accelerator and much of its enablement work.
- **[[Anderon]]**: IBM's new pure-play quantum-wafer manufacturing foundry in Albany, New York, using standard 300-mm wafers — described by Rao as "the kitchen for qubits."
- **[[Post-Quantum Cryptography]] (PQC)**: Cryptographic transition using algorithms like ML-KEM (key exchange) and ML-DSA (digital signatures) to defend against future quantum attacks on RSA.
- **[[Spyre]]**: IBM's AI accelerator chip, 75-watt power envelope, ~20mm×20mm die with 18-20 billion transistors, developed largely at ISDL.
- **[[Qiskit]]**: IBM's quantum computing framework, integrated into India's academic ecosystem via a free course with IIT Madras.
- **[[Open Hardware]]**: Movement IBM supports via projects like UC Berkeley's Chipyard, Google's OpenTitan, and open PDKs, enabling reuse of standard components like PCI Express.

## Key Takeaways

- **Course adoption**: IBM/IIT Madras free quantum computing course recorded 208,785 enrollments in India in 2026, over 100,000 from Andhra Pradesh.
- **Qubit roadmap**: Scaling from today's Heron processor (200-300 qubits) toward the upcoming Nighthawk chip and eventually 4,000 qubits.
- **PQC performance cost**: A system doing 10,000 standard authentications might manage only 1,000 under PQC without hardware acceleration.
- **PQC hardware**: IBM z17 secure-boot and the Crypto Express card (with FPGAs) support PQC, though acceleration figures are still in qualification.
- **Threat framing**: Adversaries are already "harvesting" encrypted data now to decrypt it once quantum computers become powerful enough.
- **Quantum System Two**: A dilution refrigerator model showcased IBM's planned installation in Amaravati, cooling from 4K down to 10-20 millikelvin.

## 🃏 Review Questions

**Q1**: What is the central claim about India's role in IBM's global operations?
**A**: Rahul Rao frames India's contribution as "talent arbitrage" rather than cost arbitrage, with ISDL engineering teams working across processor design, AI accelerators, quantum computing, and post-quantum cryptography at a level comparable to IBM's other global centers.

**Q2**: What specific performance tradeoff does PQC introduce, and how is IBM addressing it?
**A**: Without hardware acceleration, an organization capable of 10,000 standard authentications might manage only one-tenth of that under PQC algorithms; IBM is developing hardware acceleration (e.g., the Crypto Express card) to recover that lost performance, while offering software enablement today.

**Q3**: Why does IBM recommend a hybrid approach when transitioning to post-quantum cryptography?
**A**: Organizations should retain existing algorithms like RSA while layering ML-KEM alongside them, only removing the traditional algorithm once they've gained confidence in the new approach — reducing transition risk for critical use cases like e-KYC.
