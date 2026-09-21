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

## 4. Algorithm / Pseudocode

```text
FindArticulationPoints(G):
    mark all vertices unvisited
    parent[v] = NIL for all vertices
    disc[v] = 0, low[v] = 0
    articulation[v] = false
    time = 0

    for each vertex u:
        if u is unvisited:
            DFS_AP(u)
```

```text
DFS_AP(u):
    mark u visited
    disc[u] = low[u] = ++time
    children = 0

    for each neighbor v of u:
        if v is not visited:
            parent[v] = u
            children = children + 1
            DFS_AP(v)

            low[u] = min(low[u], low[v])

            // Case 1: root with more than one DFS child
            if parent[u] == NIL and children > 1:
                articulation[u] = true

            // Case 2: non-root where child cannot reach ancestor of u
            if parent[u] != NIL and low[v] >= disc[u]:
                articulation[u] = true

        else if v != parent[u]:
            low[u] = min(low[u], disc[v])
```

---

## 5. C++ Implementation

```cpp
void dfsAP(int u, vector<vector<int>>& adj, vector<int>& disc,
           vector<int>& low, vector<int>& parent,
           vector<bool>& isAP, vector<bool>& visited, int& timer) {

    visited[u] = true;
    disc[u] = low[u] = ++timer;
    int children = 0;

    for (int v : adj[u]) {
        if (!visited[v]) {
            parent[v] = u;
            children++;
            dfsAP(v, adj, disc, low, parent, isAP, visited, timer);

            low[u] = min(low[u], low[v]);

            if (parent[u] == -1 && children > 1) {
                isAP[u] = true;
            }

            if (parent[u] != -1 && low[v] >= disc[u]) {
                isAP[u] = true;
            }
        }
        else if (v != parent[u]) {
            low[u] = min(low[u], disc[v]);
        }
    }
}

vector<int> articulationPoints(vector<vector<int>>& adj) {
    int V = adj.size();
    vector<int> disc(V, 0), low(V, 0), parent(V, -1);
    vector<bool> visited(V, false), isAP(V, false);
    int timer = 0;

    for (int i = 0; i < V; i++) {
        if (!visited[i]) {
            dfsAP(i, adj, disc, low, parent, isAP, visited, timer);
        }
    }

    vector<int> result;
    for (int i = 0; i < V; i++) {
        if (isAP[i]) result.push_back(i);
    }
    return result;
}
```

---

## 6. Complexity

```text
O(V + E)
```

---

## 7. Exam Perspective

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

