# 08 — Prim's Algorithm

## Purpose

Prim's algorithm finds a Minimum Spanning Tree of a connected, undirected, weighted graph.

---

## Greedy Choice

Start from any vertex. Repeatedly add the minimum weight edge that connects the current MST to a new vertex.

---

## Algorithm / Pseudocode

```text
Prim(G, start):
    MST = empty
    visited[start] = true
    push all edges from start into min-heap

    while MST has fewer than V - 1 edges:
        edge = extract minimum edge from heap

        if edge leads to already visited vertex:
            ignore it
        else:
            add edge to MST
            mark new vertex visited
            push all edges from new vertex to heap

    return MST
```

---

## Complexity

Using adjacency list + min heap:

```text
O(E log V)
```

Using adjacency matrix:

```text
O(V²)
```

---

## Dry Run Pattern

For exam:

1. Choose starting vertex.
2. List candidate edges crossing from selected vertices to unselected vertices.
3. Pick minimum edge.
4. Add new vertex.
5. Repeat until all vertices are included.

---

## Exam Perspective

Common PYQs:

- Apply Prim's algorithm step by step.
- Show MST construction at each step.
- State greedy choice and optimal substructure.
- Analyze complexity.

---

## Common Mistake

Do not select the globally smallest edge blindly. Prim selects the smallest edge that connects current tree to an unvisited vertex.
