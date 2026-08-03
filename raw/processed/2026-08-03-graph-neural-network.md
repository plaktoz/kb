---
source_url: https://en.wikipedia.org/wiki/Graph_neural_network
author: Wikipedia contributors
date: 2026-08-03
---

# Graph Neural Network

Graph neural networks (GNNs) are artificial neural networks designed for graph-structured inputs. Because graphs lack a canonical node ordering, GNN architectures are typically designed to be permutation equivariant. A key design element is *pairwise message passing*, where nodes iteratively update representations by exchanging information with neighbors.

In geometric deep learning, CNNs can be interpreted as GNNs over pixel graphs, while transformer layers correspond to GNNs over complete graphs of tokens.

## Architecture

A generic GNN implements three layer types:

1. **Permutation-equivariant layers** — map graphs to updated representations via message passing; each layer expands the receptive field by one hop
2. **Local pooling layers** — coarsen the graph through downsampling (e.g., top-k, self-attention pooling)
3. **Global pooling/readout layers** — produce fixed-size graph representations via sum, mean, or max

Standard message-passing GNNs are bounded in expressiveness by the Weisfeiler-Leman graph isomorphism test.

## Message Passing Layers

For graph G=(V,E), an MPNN layer updates node representations as:

> **h**_u = φ(**x**_u, ⊕_{v∈N_u} ψ(**x**_u, **x**_v, **e**_uv))

Where φ is the update function, ψ is the message function, and ⊕ is a permutation-invariant aggregation operator.

Stacking n layers allows nodes to communicate up to n hops away. Common issues with deep stacking include:
- **Oversmoothing**: node representations become indistinguishable
- **Oversquashing**: long-range dependencies squeezed into fixed-size representations

### Graph Convolutional Network (GCN)
Introduced by Kipf and Welling (2017). Defines a first-order approximation of a localized spectral filter. Does not support multidimensional edge features, though scalar edge weights can be encoded in the adjacency matrix.

### Graph Attention Network (GAT)
Introduced by Veličković et al. (2018). Combines GNN with attention, computing attention coefficients α_uv measuring node v's importance to node u, normalized via softmax. A GCN is a special case where attention coefficients are fixed rather than learned.

### Gated Graph Sequence Neural Network (GGS-NN)
Introduced by Yujia Li et al. (2015). Extends GNN to output sequences using GRU cells for node representation updates.

## Local Pooling Layers

Transforms a graph into a smaller coarsened graph. Two broad approaches:
- **Node-selection**: retain a subset of original nodes (top-k, self-attention pooling)
- **Node-clustering**: assign nodes to clusters forming supernodes

### DiffPool (2018)
Learns soft node-to-cluster assignments; fully differentiable and trainable end-to-end.

### Top-k Pooling
Retains nodes with the highest scores under a learnable projection vector **p**; sigmoid activation enables backpropagation.

### Self-attention Pooling
Extends top-k pooling by computing scores via a full GNN layer, incorporating both features and graph topology.

## Heterophilic Graph Learning

The homophily assumption (connected nodes share labels/attributes) underlies much GNN success. However, in heterophilic settings (low homophily), GNN performance can lag behind standard neural networks. Research now addresses heterophily across heterogeneous graphs, temporal graphs, and hypergraphs, with applications in fraud detection, adversarial robustness, and recommender systems.

## Scalability and Distributed Training

Two main settings arise:

- **Single large graph**: Cluster-GCN uses graph partitioning; GraphSAINT uses stochastic subgraph sampling; DistDGL extends training across machines
- **Collections of large graphs**: **Graph Parallelism** distributes a single graph across multiple GPUs, enabling models with hundreds of millions to billions of parameters for atomic simulation tasks

## Applications

| Domain | Use |
|---|---|
| Social networks | Recommender systems |
| Combinatorial optimization | Shortest paths, chip placement, branch-and-bound |
| Cyber security | Anomaly/intrusion detection in provenance graphs |
| Water networks | Demand forecasting, metamodeling |
| Computer vision | Graph-based image patch representation |
| NLP | Text classification, QA, machine translation |
| Materials science | Interatomic potentials, crystal stability prediction |

### Atomic Simulations
GNNs reduce quantum chemistry computation from O(n³) to O(n). Key architectures include SchNet (2017), DimeNet (2020), NequIP, and MACE. Large datasets like OC20 (260M+ DFT calculations) have driven universal interatomic potential development, including CHGNet, MACE-MP, and Meta's UMA model trained on ~500M atomic structures. Google DeepMind's GNoME reportedly identified millions of new stable candidate materials.

## Open Source Libraries

- **PyTorch Geometric** (PyTorch)
- **TensorFlow GNN** (TensorFlow)
- **Deep Graph Library** (framework-agnostic)
- **jraph** (JAX)
- **GraphNeuralNetworks.jl / GeometricFlux.jl** (Julia/Flux)
