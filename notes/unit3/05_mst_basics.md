# 05 — Minimum Spanning Tree Basics

## Spanning Tree

A spanning tree of a connected undirected graph is a subgraph that:

- contains all vertices
- is connected
- has no cycle
- has exactly `V - 1` edges

---

## Minimum Spanning Tree

A Minimum Spanning Tree (MST) is a spanning tree with minimum total edge weight.

---

## Important Properties

For a graph with `V` vertices:

```text
Any spanning tree has V - 1 edges
```

MST applies to:

```text
connected, undirected, weighted graph
```

---

## Cut Property

For any cut in the graph, the minimum-weight edge crossing that cut is safe to include in an MST.

This supports Prim and Kruskal.

---

## Cycle Property

In any cycle, the maximum-weight edge cannot be part of some MST if there is a cheaper alternative.

---

## MST vs Shortest Path Tree

MST minimizes total weight of connecting all vertices.

Shortest path tree minimizes distance from a source to every other vertex.

They are different problems.

---

## Algorithms

| Algorithm | Purpose |
|---|---|
| Kruskal | MST |
| Prim | MST |
| Dijkstra | Shortest path |
| Bellman-Ford | Shortest path |

---

## Exam Perspective

Common questions:

- Define spanning tree and MST.
- State properties of MST.
- Compare MST and shortest path tree.
- Apply Prim/Kruskal on graph.
