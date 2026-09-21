# 10 — DFS and BFS

# BFS — Breadth First Search

## 1. Intuition

BFS explores level by level using a queue.

```text
Start node
→ all neighbors
→ neighbors of neighbors
→ ...
```

## 2. Pseudocode

```text
BFS(G, source):
    mark source visited
    enqueue source

    while queue is not empty:
        u = dequeue
        visit u

        for each neighbor v of u:
            if v is not visited:
                mark v visited
                enqueue v
```

## 3. Complexity

```text
O(V + E)
```

---

# DFS — Depth First Search

## 1. Intuition

DFS goes as deep as possible before backtracking.

Usually implemented using recursion or stack.

## 2. Pseudocode

```text
DFS(u):
    mark u visited
    visit u

    for each neighbor v of u:
        if v is not visited:
            DFS(v)
```

## 3. Complexity

```text
O(V + E)
```

---

# BFS vs DFS

| Feature | BFS | DFS |
|---|---|---|
| Data structure | Queue | Stack/Recursion |
| Traversal | Level-wise | Depth-wise |
| Shortest path in unweighted graph | Yes | No guarantee |
| Used for | shortest path, levels | cycle detection, components, bridges |

---

## Exam Perspective

Common questions:

- Apply BFS/DFS on a graph.
- Write BFS/DFS algorithm.
- Compare BFS and DFS.
- Analyze complexity.

---

## Practice

1. Perform BFS from vertex 0 on a given graph.
2. Perform DFS from vertex 0 on the same graph.
3. Why is BFS used for shortest path in unweighted graphs?

---

## Practice Solutions

Use this graph:

```text
0: 1, 2
1: 0, 3
2: 0, 4
3: 1
4: 2
```

### 1. BFS from vertex 0

Queue order:

```text
0 → 1 → 2 → 3 → 4
```

BFS traversal:

```text
0, 1, 2, 3, 4
```

### 2. DFS from vertex 0

Assuming smaller-numbered neighbor is visited first:

```text
0 → 1 → 3 → 2 → 4
```

DFS traversal:

```text
0, 1, 3, 2, 4
```

### 3. Why BFS gives shortest path in unweighted graphs

BFS explores vertices level by level. The first time a vertex is reached, it is reached using the minimum number of edges from the source.

