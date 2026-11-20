---
source_url: https://www.prnewswire.com/news-releases/ibm-fermilab-and-nvidia-announce-plans-for-new-co-design-platform-to-accelerate-the-development-of-next-generation-modular-quantum-computers-302940668.html
author: IBM
date: 2026-11-16
---

# IBM, Fermilab, and NVIDIA Announce Plans for New Co-Design Platform to Accelerate the Development of Next-Generation, Modular Quantum Computers

Researchers plan to use modular quantum computing co-design platform to explore computationally demanding problems in high-energy and nuclear physics.

New Slurm® integration simplifies how HPC users can orchestrate and manage quantum computing in their workflows.

Results from IBM, RIKEN, and NVIDIA demonstrate quantum-classical scientific simulations with 79 times more accuracy than previous work.

YORKTOWN HEIGHTS, N.Y., Nov. 16, 2026 /PRNewswire/ -- IBM (NYSE: IBM) today announced plans to collaborate with NVIDIA and Fermi National Accelerator Laboratory (Fermilab) to advance the integration of quantum and classical computing and explore how these technologies can scale together in the modular architectures that will define fault-tolerant quantum computers.

The work will span developing new scientific applications, integrating supercomputing and quantum resources, and designing critical components of future quantum computers. As part of the work, IBM and NVIDIA, together with Fermilab, intend to launch a modular quantum computing co-design platform that co-locates NVIDIA DGX B200 systems with IBM quantum computers, including those powered by IBM Quantum Nighthawk, the most powerful quantum processor IBM has ever built, running circuits of up to 7500 two-qubit operations on 120 qubits with speeds up to 100,000 samples per second. Leveraging Fermilab's Superconducting Quantum Materials and Systems (SQMS) Center, the SI-enabled co-design platform will help researchers explore and test the innovations needed for multiple quantum processors to work together to execute a large number of samples and scale classical compute alongside them.

Fermilab and IBM will also look to research what will be needed to execute complex calculations in high-energy and nuclear physics that are beyond the reach of classical systems alone, such as such as lattice gauge theories, neutrino interactions and nuclear simulations.

"Some of the most fundamental problems in science remain out of reach for classical computers alone. Scaling quantum and classical together will open new frontiers in high-energy and nuclear physics and beyond," said Jerry Chow, IBM Fellow and Chief Technology Officer of Quantum-Centric Computing. "With Fermilab and NVIDIA, we plan to explore how these real-world problems can help us shape the modular, interconnected architectures that will define the next generation of quantum computers and accelerated classical computing."

"Realizing quantum computing's potential requires quantum processors and accelerated computing to evolve together as accelerated quantum supercomputers," said Krysta Svore, vice president of applied research for quantum computing at NVIDIA. "IBM, Fermilab, and NVIDIA are working together to give researchers the tools they need to make scientific discoveries with quantum computing."

"We have an extraordinary opportunity to bring together IBM's leadership in quantum processors and networking, NVIDIA's breakthroughs in accelerated computing and SI, and Fermilab's scientific community and SQMS expertise in ultracoherent quantum hardware," said Anna Grassellino, Fermilab chief technology officer and director of the SQMS Center. "Our ambition is to help lead the development of quantum computers built for discovery: bringing high-energy and nuclear physicists together to co-design the applications, algorithms and modular architectures that will ultimately make fault-tolerant quantum computing useful for science. This is an important step toward the capabilities and community needed for a future DOE quantum computing user facility."

Integrating Quantum Processors into HPC Workflows

Slurm is a widely used scheduler for many of the world's largest supercomputers. It helps decide which jobs run, when they run, and which CPUs and GPUs they use. Until now, Slurm had no native concept of a quantum processor. Sites had to attach QPUs through plugins, outside the scheduler's core resource model.

To address this, IBM and NVIDIA, along with Pasqal, worked with the open-source community to integrate quantum computers into existing supercomputing workflows with the Quantum Resource Management Interface (QRMI). QRMI is an open-source, vendor-agnostic layer that directly integrates with Slurm Hierarchical Resources (HRES) scheduling capabilities.

Unlike GPUs, which operate within individual computing nodes, quantum processing units (QPUs) can be shared across multiple nodes. HRES allows administrators to manage that shared resource directly and set limits for each part of the system. Slurm can then allocate, reserve, and account for QPU time with the same policies that HPC users are familiar with for CPUs and GPUs.

For HPC centers, this means a quantum-classical workflow can be managed as a normal Slurm job, without requiring a separate queue, login or a new operating model. As QRMI is vendor-agnostic, the same approach can support quantum processors from different providers.

Quantum + Classical Push Toward More Challenging Science

New research from IBM, RIKEN, and NVIDIA demonstrates how these quantum-classical workflows can work together to improve the accuracy of complex scientific simulations. Building on IBM and RIKEN's previous joint research using a technique known as sample-based quantum diagonalization (SQD), the researchers studied Fe4S4, an iron-sulfur cluster found inside the proteins of living cells whose interacting electrons make it particularly difficult to simulate.

The team improved on previous SQD work by beginning with an intentionally imperfect but more realistic "guess" of the molecule's state, which steers the quantum computer toward the electron configurations that matter most. The researchers ran circuits of up to 4,000 two-qubit operations on 72 qubits and collected 5 million samples. The workflow integrated quantum computers and NVIDIA GPUs, including those within RIKEN's JHPC-quantum GPU supercomputer "ROQUO," to accelerate calculations and achieve a 79-fold improvement in accuracy over earlier runs of the same experiment. As noted in the paper, the results came within 4.3 millihartree of the accuracy achieved using density-matrix renormalization group (DMRG), a leading classical simulation method known for its high accuracy, proving that integrating quantum and classical compute holds immense potential for problems that remain extremely demanding for even the best classical methods working alone.

"By combining quantum computing with HPC, we achieved accuracy approaching that of DMRG, one of the leading classical methods, for a strongly correlated iron–sulfur cluster," said Seiji Yunoki, Team Principal of the Computational Materials Science Research Team at RIKEN. "This marks an important step toward applying quantum–HPC hybrid computing to scientific problems."

The research is supported by Japan's New Energy and Industrial Technology Development Organization (NEDO) through its "Research and Development of Quantum-Supercomputers Hybrid Platform for Exploration of Uncharted Computable Capabilities" project and marks another milestone for IBM and RIKEN's work with IBM quantum computers and ROQUO to accelerate quantum-classical workflows. Earlier this year, a separate collaboration with Cleveland Clinic was named a finalist for the 2026 ACM Gordon Bell Prize.

Together, the Slurm integrations, scientific application work and Fermilab-led modular quantum computing co-design platform with NVIDIA reflect IBM's broader strategy to integrate quantum computers more deeply into today's classical computing environments while simultaneously developing the architectures required for increasingly powerful systems.
