---
source_url: https://distill.pub/2021/gnn-intro/
author: Benjamin Sanchez-Lengeling, Emily Reif, Adam Pearce, Alexander B. Wiltschko
date: 2021-09-02
---

# A Gentle Introduction to Graph Neural Networks

## Core Concept

Graphs represent relationships (edges) between entities (nodes). GNNs are neural networks adapted to operate on this structure. Applications include antibiotic discovery, physics simulations, fake news detection, traffic prediction, and recommendation systems.

## Graphs in the Real World

Data naturally expressed as graphs includes:
- **Images** — pixels as nodes, adjacency determined by spatial proximity
- **Text** — tokens as nodes connected sequentially
- **Molecules** — atoms as nodes, covalent bonds as edges
- **Social networks** — individuals as nodes, relationships as edges
- **Citation networks** — papers as nodes, citations as directed edges

## Prediction Task Types

| Level | Description | Analogy |
|-------|-------------|---------|
| Graph | Property of entire graph | Image classification |
| Node | Property per node | Image segmentation |
| Edge | Property or presence of edges | Scene relationship detection |

## Key Challenges

Representing graph connectivity for neural networks is non-trivial. Adjacency matrices are space-inefficient and not permutation-invariant — the same graph topology can be encoded by many different matrices. **Adjacency lists** offer an O(n_edges) alternative versus O(n_nodes²) for full matrices.

## GNN Architecture Components

### Basic GNN Layer
Applies separate MLPs to each graph attribute (nodes, edges, global context) independently, without using connectivity.

### Pooling
When information must move between attribute types (e.g., edge→node), pooling:
1. Gathers embeddings from source attributes
2. Aggregates them (typically via sum)

### Message Passing
Nodes/edges exchange information with neighbors in three steps:
1. Gather neighboring embeddings
2. Aggregate (sum/mean/max)
3. Pass through an update function (learned network)

"By stacking message passing GNN layers, a node can eventually incorporate information from across the entire graph"

### Global Representations (Master Node)
A global context vector connected to all nodes/edges acts as a communication bridge for distant nodes — addressing the limitation that k-layer GNNs only propagate information k steps.

## Empirical Design Lessons (from playground experiments)

- More communicating graph attributes → better average performance
- GNNs are parameter-efficient; strong performance achievable with ~3k parameters
- Deeper isn't always better — 2-layer models sometimes outperform 3–4 layer ones (due to representation "dilution")
- Sum aggregation has a slight mean performance edge, but max/mean can match it
- Higher embedding dimensionality improves mean performance but not necessarily peak performance

## Advanced Topics

**Graph Attention Networks (GATs):** Use learned weighted aggregation; weights reflect neighbor relevance. Transformers can be viewed as GNNs on fully-connected graphs with attention-derived edge weights.

**Aggregation Operations:** No single operation dominates — mean normalizes, max highlights salient features, sum balances both.

**Graph Types:**
- *Multigraphs*: multiple edge types between node pairs
- *Hypergraphs*: edges connecting more than two nodes
- *Hypernodes*: nodes that themselves represent graphs (hierarchical)

**Generative Modeling:** Learning to generate new graphs (e.g., novel drug candidates) is an active area; challenges include variable topology and O(N²) adjacency terms.

**GNNExplainer:** Identifies relevant subgraphs driving model predictions, aiding interpretability.

**Matrix/Graph duality:** Multiplying adjacency matrix A by feature matrix X implements sum-based message passing; A^k counts walks of length k between nodes.

## Citation

Sanchez-Lengeling et al., "A Gentle Introduction to Graph Neural Networks," *Distill*, 2021. https://distill.pub/2021/gnn-intro
