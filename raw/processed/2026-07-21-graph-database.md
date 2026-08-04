---
source_url: https://en.wikipedia.org/wiki/Graph_database
author: Wikipedia contributors
date: 2026-07-21
---

# Graph Database

A graph database (GDB) uses graph structures for semantic queries, employing nodes, edges, and properties to store data. The core concept is the relationship (edge) connecting data items. Relationships are stored persistently, enabling fast retrieval and intuitive visualization of heavily interconnected data.

Graph databases are classified as NoSQL. They resemble 1970s network model databases but operate at a higher abstraction level and support easier traversal across edge chains.

## History

- **Mid-1960s:** IBM's IMS supported tree-like hierarchical structures
- **Late 1960s:** Network model databases enabled graph structures; CODASYL defined the Network Database Language in 1969
- **Mid-1980s:** Labeled graphs supported in databases like the Logical Data Model
- **Early 1990s:** Commercial object databases emerged
- **Mid-to-late 2000s:** ACID-compliant graph databases like Neo4j became available
- **2010s:** Horizontally scalable graph databases; multi-model databases (OrientDB, ArangoDB, MarkLogic); cloud-based options like Amazon Neptune

## Background

Graph databases store data reflecting conceptual understanding:

- **Nodes** — represent entities (people, accounts, businesses); analogous to rows in relational databases
- **Edges** — connect nodes, representing relationships; can be directed or undirected; a key abstraction absent from relational and document-store models
- **Properties** — key-value information attached to nodes or edges

## Graph Models

### Labeled-Property Graph
Nodes and relationships are named and can carry key-value properties. Edges are always directed (start node → end node). Direct relationship storage allows constant-time traversal.

### Resource Description Framework (RDF)
Each piece of information is a separate node. Statements use subject-node, object-node, and predicate-arc. Nodes may be blank, literal, or URI-identified. Arcs may also carry URIs.

## Properties

- Optimized for graph-like queries (shortest paths, diameter computation, community detection)
- Flexible schema — new data can be inserted without breaking existing functionality

### Storage
Backends vary: some use relational engines with tables, others use key-value or document stores (NoSQL). In document-based storage, edges hold `_from` and `_to` attributes linking nodes.

### Index-Free Adjacency
Nodes store direct references to neighboring nodes — a "micro-index" approach. Adjacent node lookup runs in O(1), versus O(log n) for index-based lookups. Query time scales with the portion of the graph queried, not the total graph size.

## Applications

Gartner identifies five broad graph categories:

1. **Social graph** — connections between people (Facebook, Twitter, six degrees of separation)
2. **Intent graph** — reasoning and motivation
3. **Consumption graph** — retail/e-commerce tracking (Amazon, eBay, Walmart)
4. **Interest graph** — maps personal interests, often paired with social graphs
5. **Mobile graph** — built from mobile data including GPS, apps, IoT devices

## Comparison with Relational Databases

Relational databases require strict schemas and normalization, distributing data across many tables. Complex relationship queries demand multiple JOIN operations and foreign key lookups.

Graph databases offer advantages:
- Faster for associative datasets
- More natural mapping to object-oriented structures
- Avoid costly JOINs
- Handle evolving schemas more easily

Relational databases remain faster for bulk operations on large flat datasets.

Note: The graph model alone is insufficient justification to replace an existing relational database; performance gains of orders of magnitude should be demonstrable.

### Query Language Examples (Finding Jack's Friends)

**SQL:**
```sql
SELECT p2.person_name 
FROM people p1 
JOIN friend ON (p1.person_id = friend.person_id)
JOIN people p2 ON (p2.person_id = friend.friend_id)
WHERE p1.person_name = 'Jack';
```

**Cypher:**
```cypher
MATCH (p1:person {name: 'Jack'})-[:FRIEND_WITH]-(p2:person)
RETURN p2.name
```

**Gremlin:**
```
g.V().hasLabel("person").has("name", "Jack").
    out("friendsWith").hasLabel("person").values("name")
```

**SPARQL (short form):**
```sparql
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
SELECT ?name
WHERE { ?s foaf:name "Jack" ; foaf:knows ?o .
        ?o foaf:name ?name . }
```

## List of Notable Graph Databases

| Name | License | Language | Notes |
|------|---------|----------|-------|
| AllegroGraph | Proprietary | C, Java, Python | RDF and property graph |
| Amazon Neptune | Proprietary | Undisclosed | Managed AWS service; supports Gremlin, SPARQL, openCypher |
| ArangoDB | Business Source / Community | C++, JavaScript | Multi-model: key/value, document, graph, vector |
| Azure Cosmos DB | Proprietary | Undisclosed | Multi-modal; Gremlin query support |
| JanusGraph | Apache 2.0 | Java | Distributed; supports Cassandra, HBase, Bigtable backends |
| Neo4j | GPLv3 / Commercial | Java, Python, .NET+ | ACID, clustering, Bolt protocol, web admin UI |
| OrientDB | Apache 2.0 / Commercial | Java | Graph + document hybrid; full ACID |
| SAP HANA | Proprietary | C, C++, Java | In-memory, ACID property graph |
| TigerGraph | Proprietary | C++ | Massively parallel processing native graph DB |
| TerminusDB | Apache 2.0 | Prolog, Rust | Document-oriented knowledge graph with versioning |
| Ontotext GraphDB | Proprietary/Freeware | Java | RDF + SPARQL; high-availability clustering |

## Graph Query Languages

- **Cypher** — declarative language for Neo4j; SQL-like ad hoc and programmatic access
- **GQL** — ISO/IEC 39075 standard graph query language
- **Gremlin** — imperative graph programming language; part of Apache TinkerPop
- **SPARQL** — W3C-standardized query language for RDF databases
- **AQL** — SQL-like language used in ArangoDB for documents and graphs
- **Regular path queries** — theoretical query language for graph databases
