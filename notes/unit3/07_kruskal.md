# 07 — Kruskal's Algorithm

## Purpose

Kruskal's algorithm finds a Minimum Spanning Tree of a connected, undirected, weighted graph.

---

## Greedy Choice

Always choose the smallest weight edge that does not form a cycle.

Cycle detection is done using DSU.

---

## Algorithm / Pseudocode

```text
Kruskal(G):
    MST = empty
    sort all edges by increasing weight
    create DSU for all vertices

    for each edge (u, v, w) in sorted edges:
        if Find(u) != Find(v):
            add edge to MST
            Union(u, v)

        if MST has V - 1 edges:
            break

    return MST
```

---

## Complexity

Sorting edges dominates:

```text
O(E log E)
```

DSU operations are almost constant.

Since `E ≤ V²`, also written as:

```text
O(E log V)
```

---

## Dry Run Pattern

For exam:

1. Sort edges by weight.
2. Pick smallest edge.
3. If it forms cycle, reject.
4. Continue until `V-1` edges selected.
5. Sum selected edge weights.

---

## Exam Perspective

Common questions:

- Write Kruskal's algorithm.
- Apply Kruskal on graph.
- Show selected/rejected edges.
- Explain use of DSU.
- Analyze complexity.

---

## Kruskal vs Prim Short Hint

Kruskal chooses globally smallest safe edge.
Prim grows one tree from a starting vertex.
