# 06 — Dijkstra Single Source Shortest Path

## Problem

Find shortest distance from a source vertex to all vertices in a weighted graph with non-negative weights.

## Idea

Use greedy method. Always finalize the unvisited vertex with minimum current distance.

## Algorithm

```text
Dijkstra(adj, source):
    dist[v] = infinity for all vertices
    dist[source] = 0
    minHeap = [(0, source)]

    while minHeap is not empty:
        (d, u) = extract minimum

        if d > dist[u]:
            continue

        for each edge (u, v, w):
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                insert (dist[v], v) into minHeap

    return dist
```

## Complexity

```text
O(E log V)
```

## Important

Dijkstra does not safely work with negative edge weights.
