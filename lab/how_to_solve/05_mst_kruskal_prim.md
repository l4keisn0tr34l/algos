# 05 — MST Algorithms: Kruskal and Prim

## MST

A Minimum Spanning Tree connects all vertices with minimum total edge weight and has exactly `V-1` edges.

---

# Kruskal

## Idea

Sort all edges by weight. Pick the smallest edge that does not form a cycle.

## Helpers

Use DSU:

```text
Find(x)
Union(x, y)
```

## Algorithm

```text
Kruskal(V, edges):
    sort edges by weight
    create DSU
    MST = empty

    for each edge (u, v, w):
        if Find(u) != Find(v):
            add edge to MST
            Union(u, v)

    return MST
```

## Complexity

```text
O(E log E)
```

---

# Prim

## Idea

Start from one vertex. Repeatedly choose the minimum edge from visited vertices to an unvisited vertex.

## Algorithm

```text
Prim(adj, start):
    visited[start] = true
    push edges of start into min heap

    while MST has less than V-1 edges:
        extract minimum edge
        if it goes to unvisited vertex:
            add it
            push new vertex edges
```

## Complexity

```text
O(E log V)
```
