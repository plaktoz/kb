---
source_url: https://www.eetimes.com/ibm-details-quantum-ai-developments-in-india
author: Yashasvini Razdan
date: 2026-09-29
---

# IBM Details Quantum, AI Developments in India

## IBM's Rahul Rao details India's role in quantum scaling, Qiskit education, and AI accelerators.

A free online quantum computing course co-created by IBM and IIT Madras recorded 208,785 enrollments in India in 2026, including more than 100,000 from Andhra Pradesh, according to IBM.

At SEMICON India 2026, EE Times spoke to Rahul Rao, distinguished engineer in processor design at IBM's India Systems Development Lab (ISDL), about IBM's integration of Qiskit into India's academic ecosystem.

"Almost every aspect of IBM has an important presence here in India," he said. "India is as important as every other center."

Rao said IBM's India engineering teams work across processor design, AI accelerators, quantum computing, and post-quantum cryptography (PQC), with additional teams working on Power processors, storage components, Linux, and some operating systems for Power processors. IBM's consulting operations are also heavily concentrated in India. He described the approach as "talent arbitrage" rather than cost arbitrage.

IBM is separately establishing Anderon, a pure-play manufacturing foundry for quantum wafers, in Albany, New York. Rao called Anderon "the kitchen for qubits." He said the foundry will use 300-mm wafers, the same standard size used in conventional CMOS manufacturing.

Rao said IBM's roadmap over the next few years calls for scaling quantum processors from 200 and 300 qubits to 1,000 and eventually 4,000 qubits, building on the current Heron processor and an upcoming chip called Nighthawk.

"Achieving that scale requires the kind of robust manufacturing Anderon is meant to provide," he said.

### Post-quantum cryptography

At SEMICON India, IBM demonstrated a PQC process using an electronic know-your-customer (e-KYC) example. Rao explained that current public-key mechanisms such as Rivest-Shamir-Adleman (RSA) could be broken by a sufficiently powerful quantum computer. He said adversaries are already "harvesting" encrypted data today so they can decrypt it once such a computer becomes available.

IBM's proposed approach is to introduce post-quantum algorithms, including ML-KEM for key exchange and ML-DSA for digital signatures, alongside existing algorithms during the transition.

For the RSA-based key exchange used in the e-KYC demo, Rao recommended starting with a hybrid approach.

"You retain the existing algorithms and layer ML-KEM with them," he said.

The traditional algorithm can eventually be removed once organizations gain confidence in the new approach and complete the transition to PQC.

According to Rao, IBM systems can already execute PQC algorithms. He cited the IBM z17 system's secure-boot capabilities, as well as the Crypto Express card, a hardware security module with FPGAs and accelerators to speed up PQC operations. Rao stopped short of providing performance figures for the card's PQC acceleration, saying the work was still in the qualification phase.

PQC involves more complex mathematical operations, which can reduce performance when implemented conventionally.

"An organization capable of 10,000 authentications under standard algorithms might manage only one-tenth of that using PQC without acceleration," Rao said.

Hardware acceleration is therefore being developed to recover some of that performance.

"Today, we provide software enablement, which people can buy," he said. "It is available in the market. Hardware acceleration is part of the roadmap we are working on."

IBM said it is also discussing proofs of concept with major public-sector institutions in India for hardware-accelerated PQC implementations. Rao pointed to work at the Indian Institute of Science (IISc) in Bangalore, where professor Utsav Banerjee has developed accelerator chips for PQC algorithms.

### AI accelerators

ISDL is also involved in IBM's Spyre AI accelerator, which has a 75-watt power envelope and is built around a die roughly 20 mm × 20 mm, containing 18 billion to 20 billion transistors, Rao said.

That works out, in his words, to "two transistors on this chip for every person on the planet."

"A chip of that size can carry 20 billion to 40 billion transistors and 25 to 40 kilometers of wiring spread across 18 layers of metal," he said. "It is not just about the physical arrangement. We have to ensure electrical robustness, mechanical sturdiness, and temperature reliability."

The engineering also involves managing heat, cooling the chip, fitting it into the system, and maintaining power grid integrity.

"A lot of the Spyre accelerator work was done at ISDL," Rao said. "The accelerator component was developed there, and much of the enablement work is also being done at ISDL."

### Open hardware

Rao also discussed IBM's interest in open hardware, which he linked to the broader evolution of digital design.

"Just as we have open source in the software stack, there is open hardware," he said.

As examples of the broader movement, he pointed to projects such as UC Berkeley's Chipyard framework, Google's OpenTitan root-of-trust chip, and open process design kits (PDKs). He also cited industry-standard components such as PCI Express that engineers can reuse rather than build from scratch.

Engineers should not need to develop every component themselves, Rao said.

"There is an entire world out there in open hardware," he said. "There is Open PDK, which enables people to get access. It is almost like a democratization of digital design."

He added that organizations still need to be aware that some information is restricted.

IBM's own software approach combines open-source and proprietary components. Rao said the software stack around Power processors is essentially open source, with IBM among the top contributors to the Linux community.

"We have always believed in going open where it makes sense, which is higher up the stack, and being proprietary where you need an explicit component structure to ensure reliability, performance, and so on," he said.

Rao pushed back on the idea that India's role in global semiconductor development is limited to engineering execution. He pointed to patents filed by Indian inventors, papers with primarily Indian author lists, and IBM's work on AI for scan-chain optimization using reinforcement learning, as well as design-technology co-optimization.

At SEMICON India, IBM's model of the dilution refrigerator for the Quantum System Two, which is set to be installed in Amaravati, drew attention and prompted conversations. Its chandelier-like arrangement of gold wiring and cooling stages, dropping from 4 kelvin to the 10–20 millikelvin range where the quantum processing unit sits, showed the complexity of the setup.

In an earlier conversation with EE Times, Amith Singhee, CTO of IBM India and South Asia, described the arrangement. However, the scale of the model was difficult to appreciate until seen up close.

Alongside the refrigerator, IBM displayed information about the Anderon announcement, PQC demonstrations, and the Spyre accelerator card. Visitors moved between the exhibits, each representing a different part of the company's work in advanced computing.
