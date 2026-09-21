# 14 — Important Unit III Comparisons

## Kruskal vs Prim

| Feature | Kruskal | Prim |
|---|---|---|
| Solves | MST | MST |
| Approach | chooses smallest safe edge globally | grows tree from a start vertex |
| Data structure | DSU | Priority queue |
| Better for | sparse graphs | dense graphs with matrix or connected graphs |
| Complexity | `O(E log E)` | `O(E log V)` with heap |

---

## MST vs Shortest Path Tree

| Feature | MST | Shortest Path Tree |
|---|---|---|
| Goal | minimize total cost connecting all vertices | minimize distance from source |
| Algorithms | Kruskal, Prim | Dijkstra, Bellman-Ford |
| Source vertex needed? | No | Yes |
| Same result? | Not necessarily | Not necessarily |

---

## Dijkstra vs Bellman-Ford

| Feature | Dijkstra | Bellman-Ford |
|---|---|---|
| Negative edges | No | Yes |
| Negative cycle detection | No | Yes |
| Complexity | faster, `O(E log V)` | slower, `O(VE)` |

---

## Fractional vs 0/1 Knapsack

| Feature | Fractional | 0/1 |
|---|---|---|
| Can split items? | Yes | No |
| Greedy works? | Yes | No generally |
| Method | Greedy | DP / Branch and Bound |

---

## Greedy vs Divide and Conquer

| Feature | Greedy | Divide and Conquer |
|---|---|---|
| Strategy | local best choice | divide problem into subproblems |
| Combines subanswers? | usually no | yes |
| Examples | Prim, Kruskal, Huffman | Merge Sort, Binary Search |
