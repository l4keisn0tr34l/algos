# 09 — Graph Representations

## 1. Basic Terms

A graph is:

```text
G = (V, E)
```

Where:

- `V` = set of vertices
- `E` = set of edges

---

## 2. Types of Graphs

| Type | Meaning |
|---|---|
| Undirected | edges have no direction |
| Directed | edges have direction |
| Weighted | edges have weights/costs |
| Unweighted | all edges treated equally |
| Connected | path exists between every pair of vertices |
| Cyclic | contains at least one cycle |
| Acyclic | contains no cycle |

---

## 3. Adjacency Matrix

Uses a `V × V` matrix.

```text
matrix[i][j] = 1 if edge exists from i to j
matrix[i][j] = 0 otherwise
```

For weighted graph:

```text
matrix[i][j] = weight
```

### Space

```text
O(V²)
```

### Good for

- dense graphs
- quick edge existence check

---

## 4. Adjacency List

Each vertex stores a list of its neighbors.

Example:

```text
0: 1, 2
1: 0, 3
2: 0
3: 1
```

### Space

```text
O(V + E)
```

### Good for

- sparse graphs
- DFS/BFS

---

## 5. Comparison

| Feature | Matrix | List |
|---|---|---|
| Space | `O(V²)` | `O(V+E)` |
| Check edge | `O(1)` | `O(degree)` |
| Iterate neighbors | `O(V)` | `O(degree)` |
| Best for | dense graph | sparse graph |

---

## Practice

1. Convert a small graph into adjacency matrix.
2. Convert the same graph into adjacency list.
3. Which representation is better for BFS and why?

---

## Practice Solutions

Consider graph edges:

```text
0-1, 0-2, 1-3
```

### 1. Adjacency matrix

```text
    0 1 2 3
0:  0 1 1 0
1:  1 0 0 1
2:  1 0 0 0
3:  0 1 0 0
```

### 2. Adjacency list

```text
0: 1, 2
1: 0, 3
2: 0
3: 1
```

### 3. Which representation is better for BFS and why?

Adjacency list is usually better for BFS because BFS needs to iterate over actual neighbors. With adjacency list, total traversal is:

```text
O(V + E)
```

With adjacency matrix, checking neighbors can take:

```text
O(V^2)
```

