# 06 — Disjoint Set Union / Union-Find

## Purpose

DSU maintains a collection of disjoint sets and supports:

```text
Find(x)   → representative/root of x's set
Union(x,y) → merge sets containing x and y
```

Used in Kruskal's algorithm to detect cycles.

---

## Operations

### Make Set

```text
parent[x] = x
rank[x] = 0
```

### Find with Path Compression

```text
Find(x):
    if parent[x] != x:
        parent[x] = Find(parent[x])
    return parent[x]
```

### Union by Rank

```text
Union(x, y):
    rootX = Find(x)
    rootY = Find(y)

    if rootX == rootY:
        return

    if rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    else if rank[rootX] > rank[rootY]:
        parent[rootY] = rootX
    else:
        parent[rootY] = rootX
        rank[rootX]++
```

---

## Complexity

With path compression + union by rank:

```text
Almost O(1) amortized
```

More formally:

```text
O(α(n))
```

where `α(n)` is inverse Ackermann function, extremely slow-growing.

---

## Exam Perspective

Common questions:

- Describe DSU.
- Write Find and Union algorithms.
- Explain path compression.
- Use DSU in Kruskal's algorithm.
