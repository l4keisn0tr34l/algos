# 11 — Connected Components

## 1. Definition

A connected component is a maximal group of vertices such that every vertex in the group is reachable from every other vertex in the group.

Only applies directly to undirected graphs.

---

## 2. Idea

Use DFS/BFS.

Every time we start DFS/BFS from an unvisited vertex, we discover one connected component.

---

## 3. Algorithm

```text
ConnectedComponents(G):
    mark all vertices unvisited
    count = 0

    for each vertex v:
        if v is not visited:
            count++
            DFS(v)

    return count
```

---

## 4. Complexity

```text
O(V + E)
```

---

## 5. Exam Perspective

Common questions:

- Define connected component.
- Find connected components in a graph.
- Write algorithm using DFS/BFS.
- Analyze complexity.

---

## Practice

1. Given a graph diagram, mark all connected components.
2. Write DFS-based algorithm to count components.
3. What does it mean if a graph has exactly one connected component?

---

## Practice Solutions

Consider graph:

```text
Component 1: 0-1-2
Component 2: 3-4
Component 3: 5
```

### 1. Connected components

```text
{0, 1, 2}
{3, 4}
{5}
```

Total components:

```text
3
```

### 2. DFS-based algorithm

```text
count = 0
mark all vertices unvisited

for each vertex v:
    if v is unvisited:
        count++
        DFS(v)
```

### 3. If graph has exactly one connected component

It means the graph is connected. Every vertex is reachable from every other vertex.

