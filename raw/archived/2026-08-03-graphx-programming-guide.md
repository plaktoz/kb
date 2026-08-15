---
source_url: https://spark.apache.org/docs/latest/graphx-programming-guide.html
author: Apache Spark
date: 2026-08-03
---

# GraphX Programming Guide - Apache Spark 4.2.0

## Overview

GraphX is a Spark component for graphs and graph-parallel computation. It extends the Spark RDD by introducing a **property graph** abstraction: a directed multigraph with properties attached to each vertex and edge.

Key capabilities:
- Core operators: `subgraph`, `joinVertices`, `aggregateMessages`
- Optimized variant of the Pregel API
- Built-in graph algorithms and builders

## Getting Started

```scala
import org.apache.spark._
import org.apache.spark.graphx._
import org.apache.spark.rdd.RDD
```

## The Property Graph

A directed multigraph with user-defined objects on each vertex and edge. Each vertex has a unique 64-bit `VertexId`. Parameterized over vertex type `VD` and edge type `ED`.

```scala
class Graph[VD, ED] {
  val vertices: VertexRDD[VD]
  val edges: EdgeRDD[ED]
}
```

### Example Construction

```scala
val users: RDD[(VertexId, (String, String))] =
  sc.parallelize(Seq((3L, ("rxin", "student")), (7L, ("jgonzal", "postdoc")),
                     (5L, ("franklin", "prof")), (2L, ("istoica", "prof"))))

val relationships: RDD[Edge[String]] =
  sc.parallelize(Seq(Edge(3L, 7L, "collab"), Edge(5L, 3L, "advisor"),
                     Edge(2L, 5L, "colleague"), Edge(5L, 7L, "pi")))

val defaultUser = ("John Doe", "Missing")
val graph = Graph(users, relationships, defaultUser)
```

**Triplet view** (joins vertex + edge properties):
```scala
val facts: RDD[String] =
  graph.triplets.map(triplet =>
    triplet.srcAttr._1 + " is the " + triplet.attr + " of " + triplet.dstAttr._1)
```

## Graph Operators

### Property Operators

```scala
def mapVertices[VD2](map: (VertexId, VD) => VD2): Graph[VD2, ED]
def mapEdges[ED2](map: Edge[ED] => ED2): Graph[VD, ED2]
def mapTriplets[ED2](map: EdgeTriplet[VD, ED] => ED2): Graph[VD, ED2]
```

Use `mapVertices` (not `graph.vertices.map`) to preserve structural indices.

### Structural Operators

```scala
def reverse: Graph[VD, ED]
def subgraph(epred: EdgeTriplet[VD,ED] => Boolean,
             vpred: (VertexId, VD) => Boolean): Graph[VD, ED]
def mask[VD2, ED2](other: Graph[VD2, ED2]): Graph[VD, ED]
def groupEdges(merge: (ED, ED) => ED): Graph[VD, ED]
```

**Subgraph example** (remove broken links):
```scala
val validGraph = graph.subgraph(vpred = (id, attr) => attr._2 != "Missing")
```

**Mask example**:
```scala
val ccGraph = graph.connectedComponents()
val validGraph = graph.subgraph(vpred = (id, attr) => attr._2 != "Missing")
val validCCGraph = ccGraph.mask(validGraph)
```

### Join Operators

```scala
def joinVertices[U](table: RDD[(VertexId, U)])(map: (VertexId, VD, U) => VD): Graph[VD, ED]
def outerJoinVertices[U, VD2](table: RDD[(VertexId, U)])(map: (VertexId, VD, Option[U]) => VD2): Graph[VD2, ED]
```

### Neighborhood Aggregation — `aggregateMessages`

```scala
def aggregateMessages[Msg: ClassTag](
    sendMsg: EdgeContext[VD, ED, Msg] => Unit,
    mergeMsg: (Msg, Msg) => Msg,
    tripletFields: TripletFields = TripletFields.All)
  : VertexRDD[Msg]
```

**Example** — average age of older followers:
```scala
val olderFollowers: VertexRDD[(Int, Double)] = graph.aggregateMessages[(Int, Double)](
  triplet => {
    if (triplet.srcAttr > triplet.dstAttr) {
      triplet.sendToDst((1, triplet.srcAttr))
    }
  },
  (a, b) => (a._1 + b._1, a._2 + b._2)
)
val avgAgeOfOlderFollowers: VertexRDD[Double] =
  olderFollowers.mapValues((id, value) =>
    value match { case (count, totalAge) => totalAge / count })
```

### Computing Degrees

```scala
val maxInDegree: (VertexId, Int)  = graph.inDegrees.reduce(max)
val maxOutDegree: (VertexId, Int) = graph.outDegrees.reduce(max)
val maxDegrees: (VertexId, Int)   = graph.degrees.reduce(max)
```

## Pregel API

Bulk-synchronous parallel messaging constrained to graph topology. Iterates supersteps until no messages remain.

```scala
def pregel[A](initialMsg: A, maxIter: Int = Int.MaxValue, activeDir: EdgeDirection = EdgeDirection.Out)
    (vprog: (VertexId, VD, A) => VD,
     sendMsg: EdgeTriplet[VD, ED] => Iterator[(VertexId, A)],
     mergeMsg: (A, A) => A): Graph[VD, ED]
```

**Single-source shortest path example**:
```scala
val initialGraph = graph.mapVertices((id, _) =>
  if (id == sourceId) 0.0 else Double.PositiveInfinity)

val sssp = initialGraph.pregel(Double.PositiveInfinity)(
  (id, dist, newDist) => math.min(dist, newDist),
  triplet => {
    if (triplet.srcAttr + triplet.attr < triplet.dstAttr)
      Iterator((triplet.dstId, triplet.srcAttr + triplet.attr))
    else Iterator.empty
  },
  (a, b) => math.min(a, b)
)
```

To avoid stack overflow from long lineage chains, set `spark.graphx.pregel.checkpointInterval` to a positive number (e.g., 10) and configure `SparkContext.setCheckpointDir(...)`.

## Graph Builders

| Method | Description |
|--------|-------------|
| `GraphLoader.edgeListFile(sc, path)` | Load from edge list file (skips `#` comments) |
| `Graph.apply(vertices, edges, defaultAttr)` | Build from vertex + edge RDDs |
| `Graph.fromEdges(edges, defaultValue)` | Build from edge RDD only |
| `Graph.fromEdgeTuples(rawEdges, defaultValue)` | Build from `(VertexId, VertexId)` tuples |

`Graph.groupEdges` requires prior `Graph.partitionBy` call since it assumes identical edges are colocated.

## Vertex and Edge RDDs

### VertexRDD

Extends `RDD[(VertexId, VD)]` with guaranteed unique `VertexId`s. Key additional methods:
```scala
def filter(pred: Tuple2[VertexId, VD] => Boolean): VertexRDD[VD]
def mapValues[VD2](map: (VertexId, VD) => VD2): VertexRDD[VD2]
def diff(other: VertexRDD[VD]): VertexRDD[VD]
def leftJoin[VD2, VD3](other: RDD[(VertexId, VD2)])(f: ...): VertexRDD[VD3]
def innerJoin[U, VD2](other: RDD[(VertexId, U)])(f: ...): VertexRDD[VD2]
def aggregateUsingIndex[VD2](other: RDD[(VertexId, VD2)], reduceFunc: ...): VertexRDD[VD2]
```

### EdgeRDD

Extends `RDD[Edge[ED]]`, stores edge attributes and adjacency structure separately:
```scala
def mapValues[ED2](f: Edge[ED] => ED2): EdgeRDD[ED2]
def reverse: EdgeRDD[ED]
def innerJoin[ED2, ED3](other: EdgeRDD[ED2])(f: ...): EdgeRDD[ED3]
```

## Graph Algorithms

### PageRank
```scala
val graph = GraphLoader.edgeListFile(sc, "data/graphx/followers.txt")
val ranks = graph.pageRank(0.0001).vertices
```

### Connected Components
```scala
val cc = graph.connectedComponents().vertices
```
Labels each component with its lowest-numbered vertex ID.

### Triangle Counting
```scala
// Requires canonical orientation and partitioning
val graph = GraphLoader.edgeListFile(sc, "data/graphx/followers.txt", true)
  .partitionBy(PartitionStrategy.RandomVertexCut)
val triCounts = graph.triangleCount().vertices
```

## Caching

- Call `Graph.cache()` before using a graph multiple times
- For iterative computation, **use the Pregel API** which correctly unpersists intermediate results
- Manual approach: materialize each iteration, then call `unpersistVertices` on previous graphs

## Optimized Representation

GraphX uses a **vertex-cut** approach: edges are assigned to partitions, vertices can span multiple machines. A routing table tracks where to broadcast vertex attributes for joins. This reduces communication overhead vs. edge-cut partitioning.
