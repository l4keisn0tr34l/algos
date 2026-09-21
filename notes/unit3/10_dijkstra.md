# 10 — Dijkstra's Algorithm

## Purpose

Find single-source shortest paths in a graph with non-negative edge weights.

---

## Greedy Choice

Repeatedly select the unvisited vertex with the smallest tentative distance.

Once selected, its shortest distance is finalized.

---

## Algorithm / Pseudocode

```text
Dijkstra(G, source):
    for each vertex v:
        dist[v] = infinity
    dist[source] = 0

    create min-priority queue Q
    insert (0, source) into Q

    while Q is not empty:
        (d, u) = ExtractMin(Q)

        if d > dist[u]:
            continue

        for each edge (u, v, w):
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                insert (dist[v], v) into Q

    return dist
```

---

## Complexity

Using adjacency list + min heap:

```text
O((V + E) log V)
```

Usually written:

```text
O(E log V)
```

Using adjacency matrix:

```text
O(V²)
```

---

## Exam Table Format

PYQs often require a table:

```text
Selected vertex | dist[A] dist[B] dist[C] ...
```

At each step:

1. Pick unvisited vertex with smallest distance.
2. Relax its outgoing edges.
3. Update table.

---

## Common Mistakes

- Using Dijkstra with negative edges.
- Confusing MST with shortest path.
- Forgetting to initialize source distance as 0.

---

## Exam Perspective

Common questions:

- Write Dijkstra's algorithm.
- Apply on graph from given source.
- Fill distance table.
- Compare with Bellman-Ford.
