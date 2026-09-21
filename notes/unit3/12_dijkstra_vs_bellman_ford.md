# 12 — Dijkstra vs Bellman-Ford

| Feature | Dijkstra | Bellman-Ford |
|---|---|---|
| Problem | Single-source shortest path | Single-source shortest path |
| Negative edges | Not safe | Allowed |
| Negative cycle detection | No | Yes |
| Main idea | Greedy selection of nearest unvisited vertex | Relax all edges repeatedly |
| Complexity | `O(E log V)` with heap | `O(VE)` |
| Faster? | Usually faster | Slower |
| Use when | all weights non-negative | negative edges may exist |

---

## Important Exam Line

Dijkstra fails with negative edges because once it finalizes a vertex, a later negative edge may reduce its distance, violating the greedy assumption.

---

## Practice

1. Which algorithm handles negative edges?
2. Which algorithm detects negative cycles?
3. Why is Dijkstra faster?

---

## Answers

1. Bellman-Ford.
2. Bellman-Ford.
3. Dijkstra uses a priority queue and does not repeatedly relax all edges `V-1` times.
