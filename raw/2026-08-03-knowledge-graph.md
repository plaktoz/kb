# Knowledge Graph

source: https://en.wikipedia.org/wiki/Knowledge_graph
scraped: 2026-08-03

## Definition
A knowledge graph is a knowledge base using a graph-structured data model to represent entities, their relationships, and underlying semantics.

---

## History

- **1972**: Term coined by Austrian linguist Edgar W. Schneider for modular instructional systems
- **Late 1980s**: University of Groningen & University of Twente began a "Knowledge Graphs" project focused on semantic networks
- **1985**: WordNet founded for semantic word relationships
- **2005**: Geonames founded for geographic entity relationships
- **2007**: DBpedia and Freebase launched as graph-based knowledge repositories
- **2012**: Google introduced its Knowledge Graph, drawing on DBpedia, Freebase, Wikidata, and Wikipedia
- **2019**: IEEE combined conferences into the International Conference on Knowledge Graph
- **2024**: Microsoft Research's GraphRAG integrated LLM-generated graphs into retrieval-augmented generation

---

## Definitions

No single accepted definition exists. Common features include:

- Flexible relations among entities in topical domains
- A network of entities, semantic types, properties, and relationships
- Support for reasoning via ontologies to derive new knowledge

A simpler framing: a digital structure representing knowledge as concepts and the relationships between them.

---

## Implementations

Used by:
- **Search engines**: Google, Bing, Yahoo
- **AI assistants**: Siri, Alexa, WolframAlpha
- **Social/business platforms**: LinkedIn, Facebook, Airbnb, Uber, eBay
- **Open projects**: YAGO, Wikidata, Linked Open Data cloud
- **Note-taking apps** (personal knowledge graphs)

Graph databases like **Neo4j**, **GraphDB**, and **AgensGraph** emerged from knowledge graph popularization.

**Virtual knowledge graphs** rely on underlying relational databases rather than specialized storage.

---

## Reasoning Over Data

Knowledge graphs use ontologies as schema layers, enabling **logical inference** to retrieve implicit knowledge beyond explicit queries.

**Knowledge graph embeddings** connect graph data to machine learning via feature vectors. **Graph Neural Networks (GNNs)** are the primary tools for generating these embeddings, supporting tasks like node prediction and edge prediction.

---

## Entity Alignment

When the same real-world entity appears in multiple knowledge graphs, identifying those matches is called *entity alignment*. Methods look for:

- Similar substructures
- Shared semantic relationships
- Common attributes

In 2023, large language models showed success in entity alignment, particularly through meaningful syntactic embeddings.
