# 13 — Articulation Points / Cut Vertices

## 1. Definition

An articulation point, also called a cut vertex, is a vertex whose removal increases the number of connected components in an undirected graph.

Example:

```text
1 -- 2 -- 3
```

If vertex `2` is removed, graph becomes disconnected.

So `2` is an articulation point.

---

## 2. Intuition

An articulation point is a critical connector vertex.

Removing it breaks communication between parts of the graph.

---

## 3. DFS-Based Idea

During DFS, maintain:

```text
disc[u] = discovery time of u
low[u]  = earliest discovered vertex reachable from u or its subtree
```

A non-root vertex `u` is articulation point if:

```text
low[child] >= disc[u]
```

A root vertex is articulation point if it has more than one DFS child.

---

## 4. Complexity

```text
O(V + E)
```

---

## 5. Exam Perspective

Common questions:

- Define cut vertex/articulation point.
- Find articulation points in a graph.
- Explain DFS-based algorithm.
- Compare articulation point and bridge.

---

## Practice

1. Find articulation points in path graph `1-2-3-4`.
2. Why is root treated differently in DFS articulation point algorithm?
3. What does `low[u]` represent?

---

## Practice Solutions

### 1. Articulation points in path graph `1-2-3-4`

Graph:

```text
1 -- 2 -- 3 -- 4
```

Removing `2` disconnects `1` from `3,4`.
Removing `3` disconnects `1,2` from `4`.

Answer:

```text
2 and 3
```

### 2. Why root is treated differently

In DFS, the root has no parent. It is an articulation point only if it has more than one DFS child, because multiple DFS children mean separate DFS subtrees that are connected only through the root.

### 3. Meaning of `low[u]`

`low[u]` is the earliest discovery time reachable from `u` or from any vertex in `u`'s DFS subtree, using tree edges and at most one back edge.

