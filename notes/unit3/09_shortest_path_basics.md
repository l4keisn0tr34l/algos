# 09 — Shortest Path Basics

## Single Source Shortest Path

Given a weighted graph and source vertex `s`, find shortest distance from `s` to every other vertex.

---

## Important Terms

### Relaxation

For edge `(u, v, w)`, if going through `u` gives a shorter path to `v`, update `dist[v]`.

```text
if dist[u] + w < dist[v]:
    dist[v] = dist[u] + w
```

---

## Algorithms

| Algorithm | Handles negative edges? | Detects negative cycle? |
|---|---|---|
| Dijkstra | No | No |
| Bellman-Ford | Yes | Yes |

---

## Negative Weight Edges

Dijkstra is unsafe with negative edge weights.

Bellman-Ford can handle negative edges, but not negative cycles as valid shortest paths.

---

## Negative Cycle

A cycle whose total weight is negative.

If reachable from source, shortest path is undefined because we can keep looping and reduce distance forever.

---

## MST vs Shortest Path

MST connects all vertices with minimum total edge cost.

Shortest path finds minimum distance from a source to other vertices.

They are different.
