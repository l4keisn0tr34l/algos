# 12 — DFS Edge Classification

DFS edge classification is usually discussed for directed graphs.

When DFS runs, edges can be classified based on discovery/finish times.

---

## 1. Tree Edge

An edge used to discover a new vertex.

```text
u → v
```

If `v` was unvisited when explored from `u`, then `(u,v)` is a tree edge.

---

## 2. Back Edge

An edge from a vertex to one of its ancestors in the DFS tree.

Back edges indicate cycles in directed graphs.

---

## 3. Forward Edge

An edge from a vertex to a descendant in the DFS tree, but not a tree edge.

---

## 4. Cross Edge

An edge between vertices that do not have ancestor-descendant relationship in the DFS tree.

---

## 5. Exam Perspective

Common PYQ:

> What types of edges do you encounter when running DFS on a directed graph?

Answer:

```text
Tree edge, Back edge, Forward edge, Cross edge
```

Explain each in 1–2 lines.

---

## Practice

1. Define tree edge.
2. Which edge type indicates a cycle?
3. Differentiate forward edge and cross edge.

---

## Practice Solutions

### 1. Tree edge

A tree edge is an edge that discovers a new unvisited vertex during DFS.

```text
u → v
```

If `v` is unvisited when explored from `u`, then `(u, v)` is a tree edge.

### 2. Which edge type indicates a cycle?

```text
Back edge
```

A back edge goes from a vertex to one of its ancestors in the DFS tree, indicating a cycle in a directed graph.

### 3. Forward edge vs cross edge

| Edge type | Meaning |
|---|---|
| Forward edge | connects a vertex to its descendant but is not a tree edge |
| Cross edge | connects vertices with no ancestor-descendant relationship |

