# 11 — Bellman-Ford Algorithm

## Purpose

Find single-source shortest paths even when graph has negative edge weights.

It can also detect negative weight cycles reachable from the source.

---

## Key Idea

Relax all edges `V - 1` times.

Why `V - 1`? A shortest simple path can contain at most `V - 1` edges.

---

## Algorithm / Pseudocode

### Main Bellman-Ford Algorithm

```text
BellmanFord(V, edges, source):
    for each vertex v:
        dist[v] = infinity
        parent[v] = NIL

    dist[source] = 0

    repeat V - 1 times:
        for each edge (u, v, w) in edges:
            Relax(u, v, w)

    for each edge (u, v, w) in edges:
        if dist[u] != infinity and dist[u] + w < dist[v]:
            report negative cycle
            return false

    return dist
```

### Helper Function: Relax

```text
Relax(u, v, w):
    if dist[u] != infinity and dist[u] + w < dist[v]:
        dist[v] = dist[u] + w
        parent[v] = u
```

### Negative Cycle Check Helper Idea

```text
HasNegativeCycle(edges):
    for each edge (u, v, w):
        if dist[u] != infinity and dist[u] + w < dist[v]:
            return true

    return false
```

---

## Complexity

```text
O(VE)
```

Space:

```text
O(V)
```

---

## Negative Cycle Detection

After `V - 1` relaxations, if any edge can still reduce a distance, then there is a negative cycle reachable from source.

---

## Exam Perspective

Common questions:

- Write Bellman-Ford algorithm.
- Apply on graph.
- Detect negative cycle.
- Compare with Dijkstra.

---

## Common Mistake

Bellman-Ford can handle negative edges, but if a negative cycle is reachable, shortest paths are not well-defined.
