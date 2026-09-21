# 14 — Bridges

## 1. Definition

A bridge is an edge whose removal increases the number of connected components in an undirected graph.

Example:

```text
1 -- 2 -- 3
```

Removing edge `(2,3)` disconnects the graph, so `(2,3)` is a bridge.

---

## 2. Intuition

A bridge is a critical edge.

If there is no alternate path between its endpoints, it is a bridge.

---

## 3. DFS-Based Idea

Maintain:

```text
disc[u] = discovery time
low[u]  = earliest reachable discovery time from u's subtree
```

For DFS edge `(u, v)`, it is a bridge if:

```text
low[v] > disc[u]
```

This means `v`'s subtree cannot reach `u` or any ancestor of `u` without using edge `(u,v)`.

---

## 4. Complexity

```text
O(V + E)
```

---

## 5. Articulation Point vs Bridge

| Concept | Removal of | Effect |
|---|---|---|
| Articulation Point | vertex | increases connected components |
| Bridge | edge | increases connected components |

---

## 6. Exam Perspective

Common questions:

- Define bridge.
- Find bridges in a graph.
- Explain difference between bridge and articulation point.
- Explain DFS-based condition for bridge.

---

## Practice

1. Find bridges in path graph `1-2-3-4`.
2. Can an edge in a cycle be a bridge? Why/why not?
3. State the DFS condition for a bridge.

---

## Practice Solutions

### 1. Bridges in path graph `1-2-3-4`

Graph:

```text
1 -- 2 -- 3 -- 4
```

All edges are bridges:

```text
(1,2), (2,3), (3,4)
```

Removing any one of them disconnects the graph.

### 2. Can an edge in a cycle be a bridge?

No. If an edge lies in a cycle, there is an alternate path between its endpoints. Removing it will not disconnect the graph.

### 3. DFS condition for a bridge

For DFS tree edge `(u, v)`, it is a bridge if:

```text
low[v] > disc[u]
```

