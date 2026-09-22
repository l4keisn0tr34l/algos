# 08 — Prim's Algorithm

## Purpose

Prim's algorithm finds a Minimum Spanning Tree of a connected, undirected, weighted graph.

---

## Greedy Choice

Start from any vertex. Repeatedly add the minimum weight edge that connects the current MST to a new vertex.

---

## Algorithm / Pseudocode

### Main Prim Algorithm

```text
Prim(G, start):
    MST = empty
    create empty min-priority queue Q

    for each vertex v:
        visited[v] = false

    visited[start] = true
    AddEdges(start, Q)

    while MST has fewer than V - 1 edges and Q is not empty:
        (u, v, w) = ExtractMin(Q)

        if visited[v] == true:
            continue

        add edge (u, v, w) to MST
        visited[v] = true

        AddEdges(v, Q)

    return MST
```

### Helper Function: AddEdges

```text
AddEdges(u, Q):
    for each edge (u, v, w) adjacent to u:
        if visited[v] == false:
            Insert(Q, (u, v, w))
```

### Helper Operation: ExtractMin

```text
ExtractMin(Q):
    remove and return edge with minimum weight from Q
```

In exams, `Insert` and `ExtractMin` can be written as min-priority queue operations.

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
