# 03 — Random Weighted Graph Generator

## Problem

Generate a random weighted, undirected, simple graph.

Given:

```text
n = number of vertices
d = density percentage
```

Maximum possible edges:

```text
n(n-1)/2
```

Number of edges:

```text
e = d × n(n-1)/2
```

If `d = 0.6`, use 60% of possible edges.

## Conditions

- no self-loops
- no duplicate edges
- undirected edge `(u, v)` is same as `(v, u)`
- random weight from `1...e`

## Algorithm

```text
Generate all possible edges (u, v), where u < v
Shuffle all edges
Pick first e edges
Assign random weights
Build adjacency matrix
Build adjacency list
```

## Complexity

Generating possible edges takes:

```text
O(n²)
```
