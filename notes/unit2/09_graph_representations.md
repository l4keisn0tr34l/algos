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

## 5. Algorithms to Build Representations

### Build Adjacency Matrix

For an undirected unweighted graph:

```text
BuildMatrix(V, edges):
    create V × V matrix initialized with 0

    for each edge (u, v):
        matrix[u][v] = 1
        matrix[v][u] = 1

    return matrix
```

For directed graph, only do:

```text
matrix[u][v] = 1
```

For weighted graph, store weight instead of `1`.

---

### Build Adjacency List

For an undirected graph:

```text
BuildList(V, edges):
    create array/list adj of size V

    for each edge (u, v):
        add v to adj[u]
        add u to adj[v]

    return adj
```

For directed graph, only do:

```text
add v to adj[u]
```

---

## 6. C++ Implementation

```cpp
vector<vector<int>> buildMatrix(int V, vector<pair<int,int>>& edges) {
    vector<vector<int>> matrix(V, vector<int>(V, 0));

    for (auto edge : edges) {
        int u = edge.first;
        int v = edge.second;
        matrix[u][v] = 1;
        matrix[v][u] = 1;  // remove this line for directed graph
    }

    return matrix;
}

vector<vector<int>> buildList(int V, vector<pair<int,int>>& edges) {
    vector<vector<int>> adj(V);

    for (auto edge : edges) {
        int u = edge.first;
        int v = edge.second;
        adj[u].push_back(v);
        adj[v].push_back(u);  // remove this line for directed graph
    }

    return adj;
}
```

---

## 7. Comparison

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

