---
source_url: https://en.wikipedia.org/wiki/Graph_database
author: Unknown
date: 2026-08-03
---

# Graph Database

A graph database (GDB) uses graph structures for semantic queries with nodes, edges, and properties to represent and store data.

## Key Concepts

- **Nodes** represent entities (people, businesses, accounts)
- **Edges** (relationships) connect nodes and can be directed or undirected
- **Properties** are key-value pairs associated with nodes or relationships

Graph databases are classified as NoSQL and prioritize relationships as "first-class citizens," enabling fast traversal and intuitive visualization of interconnected data.

## History

- **Mid-1960s**: IBM's IMS supported hierarchical/tree-like structures
- **Late 1960s**: Network model databases could represent graph structures; CODASYL defined Network Database Language (1969)
- **Mid-1980s**: Labeled graphs supported in databases like the Logical Data Model
- **Early 1990s**: Commercial object databases emerged
- **Mid-to-late 2000s**: ACID-compliant graph databases (Neo4j, Oracle Spatial and Graph) became available
- **2010s**: Horizontally scalable, cloud-based, and multi-model graph databases proliferated

## Graph Models

### Labeled-Property Graph
Nodes and relationships both carry properties as key-value pairs. Edges are always directed with start/end nodes, enabling "constant-time traversal."

### RDF (Resource Description Framework)
Each piece of information is a separate node. Statements use subject-node, object-node, and predicate-arc triples. Nodes may be identified by URIs or left as blank nodes.

## Storage & Performance

Storage mechanisms vary—some use relational engines, others use key-value or document stores. Graph databases typically implement **index-free adjacency**, where nodes store direct references to neighbors, enabling O(1) access to adjacent nodes versus O(log n) for index lookups.

## Comparison with Relational Databases

Relational databases excel at flat data with shallow relationships but require expensive JOIN operations for complex queries. Graph databases avoid joins by storing relationships directly, making multi-hop queries significantly faster. A multi-level query in a graph database runs in roughly O(log n) + O(1) time, while the relational equivalent requires multiple O(log n) lookups plus O(n) joining time.

However, relational databases outperform graph databases when set operations on large uniform datasets are needed.

## Query Languages

- **Cypher** – declarative, used by Neo4j
- **Gremlin** – imperative, Apache TinkerPop
- **SPARQL** – W3C standard for RDF graphs
- **GQL** – emerging ISO standard (ISO/IEC 39075)
- **AQL** – used by ArangoDB

## Notable Graph Databases

| Name | License | Language |
|------|---------|----------|
| Neo4j | GPLv3 / Commercial | Java |
| Amazon Neptune | Proprietary | Undisclosed |
| ArangoDB | Business Source License | C++, JavaScript |
| JanusGraph | Apache 2.0 | Java |
| OrientDB | Apache 2.0 / Commercial | Java |
| TigerGraph | Proprietary | C++ |
| SAP HANA | Proprietary | C, C++, Java |
| NebulaGraph | Apache 2.0 | C++, Go |

## Applications (Gartner's Five Graph Categories)

1. **Social graph** – connections between people
2. **Intent graph** – reasoning and motivation
3. **Consumption graph** – retail/e-commerce tracking
4. **Interest graph** – maps personal interests
5. **Mobile graph** – built from mobile/IoT data
