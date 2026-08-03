---
type: literature-note
source_url: https://en.wikipedia.org/wiki/Graph_neural_network
author: Wikipedia contributors
tags: [graph-neural-networks, deep-learning, message-passing, geometric-deep-learning]
date_consumed: 2026-08-03
additional_sources:
  - url: https://distill.pub/2021/gnn-intro/
    author: Benjamin Sanchez-Lengeling, Emily Reif, Adam Pearce, Alexander B. Wiltschko
    date: 2021-09-02
---

## Summary

Graph neural networks (GNNs) are neural architectures designed for graph-structured inputs, using *pairwise message passing* to iteratively update node representations by aggregating neighbor information. Their expressiveness is bounded by the [[Weisfeiler-Leman graph isomorphism test]], and they subsume both CNNs and Transformers under the [[Geometric Deep Learning]] framework. GNNs are applied across domains from antibiotic discovery and materials science to fake news detection and traffic prediction, with recent large-scale models trained on hundreds of millions of atomic structures.

## Core Concepts

- **[[Message Passing Neural Network]] (MPNN)**: Core paradigm where nodes exchange information with neighbors across layers; each layer expands the receptive field by one hop. Three steps: gather neighbor embeddings → aggregate (sum/mean/max) → pass through a learned update function.
- **[[Graph Convolutional Network]] (GCN)**: Kipf & Welling (2017); first-order spectral filter approximation; no multidimensional edge features.
- **[[Graph Attention Network]] (GAT)**: Veličković et al. (2018); learns attention coefficients α_uv to weight neighbor importance; equivalent to GNNs on fully-connected graphs with attention-derived edge weights — the same mechanism as Transformers.
- **[[Gated Graph Sequence Neural Network]] (GGS-NN)**: Yujia Li et al. (2015); uses GRU cells to extend GNN to sequence outputs.
- **[[Permutation Equivariance]]**: GNN layers must be order-agnostic because graphs have no canonical node ordering. Adjacency matrices are not permutation-invariant; adjacency lists are preferred at O(n_edges) vs. O(n_nodes²).
- **[[Global Context Vector]] (Master Node)**: A single vector connected to all nodes and edges, enabling communication between distant nodes without waiting for k message-passing steps.
- **[[DiffPool]]**: Learns soft node-to-cluster assignments for differentiable hierarchical pooling.
- **[[Geometric Deep Learning]]**: Unifying framework in which CNNs are GNNs over pixel graphs and Transformers are GNNs over complete graphs.
- **[[Weisfeiler-Leman Test]]**: Upper bound on standard MPNN expressiveness for graph isomorphism.
- **[[GNNExplainer]]**: Identifies relevant subgraphs driving model predictions, aiding interpretability.
- **[[PyTorch Geometric]]**, **[[Deep Graph Library]]**, **[[TensorFlow GNN]]**: Major open-source GNN libraries.

## Prediction Task Levels

| Level | Description | Analogy |
|-------|-------------|---------|
| Graph | Property of entire graph | Image classification |
| Node | Property per node | Image segmentation |
| Edge | Property or presence of edges | Scene relationship detection |

## Key Takeaways

- **Three layer types**: Permutation-equivariant (message passing), local pooling (coarsening), global readout (fixed-size output).
- **Oversmoothing**: Stacking too many layers makes node representations indistinguishable; 2-layer models sometimes outperform 3–4 layer ones.
- **Oversquashing**: Long-range dependencies get compressed into fixed-size vectors.
- **Heterophily gap**: GNNs underperform when connected nodes do not share labels (fraud detection, adversarial settings).
- **Parameter efficiency**: Strong GNN performance achievable with ~3k parameters; more communicating graph attributes → better average performance.
- **Aggregation tradeoffs**: Sum has a slight mean performance edge, but mean (normalizes magnitude) and max (highlights salient features) can match it; no single aggregation dominates.
- **Embedding dimensionality**: Higher dimensionality improves mean performance but not necessarily peak performance.
- **Matrix/graph duality**: Multiplying adjacency matrix A by feature matrix X implements sum-based message passing; A^k counts walks of length k between nodes.
- **Scalability**: Cluster-GCN partitions graphs; GraphSAINT uses stochastic subgraph sampling; Graph Parallelism scales to billions of parameters.
- **Atomic simulation speedup**: GNNs reduce quantum chemistry from O(n³) to O(n); models like MACE-MP and Meta's UMA trained on ~500M structures.
- **GNoME (DeepMind)**: Reportedly identified millions of new stable candidate materials using GNNs.
- **Top-k pooling**: Retains highest-scoring nodes under learnable projection with sigmoid for backprop.

## Advanced Graph Types

- *Multigraphs*: multiple edge types between node pairs
- *Hypergraphs*: edges connecting more than two nodes
- *Hypernodes*: nodes that themselves represent graphs (hierarchical)
- *Generative modeling*: learning to generate new graphs (e.g., novel drug candidates) is an active area; challenges include variable topology and O(N²) adjacency terms.

## First Principles & Mental Models

- **[[Locality Principle]]**: Message passing builds representations bottom-up from immediate neighbors outward — the same inductive bias underlying CNNs and local receptive fields, generalized to arbitrary graph topology.
- **[[Expressiveness vs. Efficiency Tradeoff]]**: Bounding GNN power by the Weisfeiler-Leman test reveals that more expressive models (higher-order GNNs) require exponentially more computation — a direct instance of the fundamental tradeoff between representational power and tractability.
- **[[Representation Dilution]]**: Deeper GNN stacks cause a node's embedding to incorporate increasingly diffuse global context, eventually washing out local structure — the same phenomenon as oversmoothing, explained by the degradation of information-to-noise ratio with each aggregation hop.

## Review Questions

**Q1**: What is the central architectural innovation of GNNs and why is it necessary for graph-structured data?
**A**: GNNs use permutation-equivariant message passing because graphs lack a canonical node ordering; nodes iteratively aggregate neighbor representations so the learned embedding is invariant to how nodes are indexed.

**Q2**: What are oversmoothing and oversquashing, and when do they occur?
**A**: Oversmoothing occurs when many message-passing layers cause node representations to converge to indistinguishable vectors; oversquashing occurs when long-range dependencies must be compressed into fixed-size representations, losing signal.

**Q3**: How do GNNs enable practical atomic simulation, and what is the computational advantage?
**A**: GNNs model interatomic potentials by treating atoms as nodes and bonds as edges, reducing quantum chemistry calculations from O(n³) to O(n); models like MACE-MP trained on ~500M structures from datasets such as OC20 now power universal interatomic potentials for materials discovery.
