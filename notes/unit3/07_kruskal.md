# 07 — Kruskal's Algorithm

## Purpose

Kruskal's algorithm finds a Minimum Spanning Tree of a connected, undirected, weighted graph.

---

## Greedy Choice

Always choose the smallest weight edge that does not form a cycle.

Cycle detection is done using DSU.

---

## Algorithm / Pseudocode

### Main Kruskal Algorithm

```text
Kruskal(G):
    MST = empty
    sort all edges by increasing weight

    for each vertex v in G:
        MakeSet(v)

    for each edge (u, v, w) in sorted edges:
        if Find(u) != Find(v):
            add edge (u, v, w) to MST
            Union(u, v)

        if MST has V - 1 edges:
            break

    return MST
```

### Helper Function: MakeSet

```text
MakeSet(x):
    parent[x] = x
    rank[x] = 0
```

### Helper Function: Find with Path Compression

```text
Find(x):
    if parent[x] != x:
        parent[x] = Find(parent[x])

    return parent[x]
```

### Helper Function: Union by Rank

```text
Union(x, y):
    rootX = Find(x)
    rootY = Find(y)

    if rootX == rootY:
        return

    if rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    else if rank[rootX] > rank[rootY]:
        parent[rootY] = rootX
    else:
        parent[rootY] = rootX
        rank[rootX] = rank[rootX] + 1
```

### Why Find/Union is needed

Kruskal adds edges in increasing weight order. Before adding an edge `(u, v)`, we check:

```text
Find(u) != Find(v)
```

If true, `u` and `v` are in different components, so adding the edge will not form a cycle. If false, adding it would form a cycle, so reject it.

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
