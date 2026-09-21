# 01 — Greedy Method

## Intuition

A greedy algorithm builds a solution step by step by choosing the locally best option at each step.

```text
At each step: choose what looks best right now
```

Greedy does **not** always give optimal answers. It works only for problems with certain properties.

---

## Two Required Properties

### 1. Greedy Choice Property

A globally optimal solution can be reached by making a locally optimal choice.

### 2. Optimal Substructure

An optimal solution to the whole problem contains optimal solutions to subproblems.

---

## Generic Greedy Algorithm

```text
Greedy(problem):
    solution = empty

    while problem is not finished:
        choose the best available option according to greedy rule
        if choice is feasible:
            add it to solution

    return solution
```

---

## Examples Where Greedy Works

- Activity Selection
- Fractional Knapsack
- Huffman Coding
- Kruskal's MST
- Prim's MST
- Dijkstra's shortest path for non-negative edges

---

## Examples Where Greedy Does Not Always Work

- 0/1 Knapsack
- Travelling Salesman Problem
- General coin change with arbitrary coin denominations

---

## Exam Definition

A greedy algorithm is an algorithmic technique that constructs a solution incrementally by selecting the locally optimal choice at each step, hoping to obtain a globally optimal solution. It is correct when the problem has greedy choice property and optimal substructure.

---

## Common PYQ Questions

1. Does greedy always produce optimal solution? Justify.
2. Define greedy choice property and optimal substructure.
3. Compare greedy with divide-and-conquer/dynamic programming.

---

## Practice

1. State two properties needed for greedy correctness.
2. Give one example where greedy works and one where it fails.
3. Why does greedy fail for 0/1 knapsack?

---

## Practice Solutions

1. Greedy choice property and optimal substructure.
2. Works: Activity Selection. Fails: 0/1 Knapsack.
3. In 0/1 knapsack, choosing highest value/weight item may block a better combination of whole items later.
