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

## 5. Edge Classification Algorithm

Use DFS colors:

```text
WHITE = unvisited
GRAY  = currently in recursion stack
BLACK = completely processed
```

For an edge `(u, v)` during DFS:

```text
if color[v] == WHITE:
    edge is Tree Edge

else if color[v] == GRAY:
    edge is Back Edge

else if color[v] == BLACK:
    if discovery[u] < discovery[v]:
        edge is Forward Edge
    else:
        edge is Cross Edge
```

---

## 6. Pseudocode

```text
DFS(u):
    color[u] = GRAY
    discovery[u] = time
    time = time + 1

    for each v in Adj[u]:
        if color[v] == WHITE:
            print Tree Edge (u, v)
            DFS(v)
        else if color[v] == GRAY:
            print Back Edge (u, v)
        else:
            if discovery[u] < discovery[v]:
                print Forward Edge (u, v)
            else:
                print Cross Edge (u, v)

    color[u] = BLACK
    finish[u] = time
    time = time + 1
```

---

## 7. C++ Implementation Sketch

```cpp
vector<int> color, disc, finish;
int timer = 0;

void dfsClassify(int u, vector<vector<int>>& adj) {
    color[u] = 1; // GRAY
    disc[u] = timer++;

    for (int v : adj[u]) {
        if (color[v] == 0) {
            cout << u << " -> " << v << " : Tree Edge\n";
            dfsClassify(v, adj);
        } else if (color[v] == 1) {
            cout << u << " -> " << v << " : Back Edge\n";
        } else {
            if (disc[u] < disc[v]) {
                cout << u << " -> " << v << " : Forward Edge\n";
            } else {
                cout << u << " -> " << v << " : Cross Edge\n";
            }
        }
    }

    color[u] = 2; // BLACK
    finish[u] = timer++;
}
```

---

## 8. Exam Perspective

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

