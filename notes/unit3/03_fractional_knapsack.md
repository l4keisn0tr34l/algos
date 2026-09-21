# 03 — Fractional Knapsack

## Problem

Given items with weight and value, and a knapsack capacity `W`, maximize profit. You may take fractions of items.

---

## Greedy Choice

Choose items in decreasing order of:

```text
value / weight
```

This gives maximum value per unit weight.

---

## Algorithm / Pseudocode

```text
FractionalKnapsack(items, W):
    for each item:
        ratio = value / weight

    sort items by ratio in decreasing order
    profit = 0

    for each item:
        if item.weight <= W:
            take full item
            profit += item.value
            W -= item.weight
        else:
            take fraction W / item.weight
            profit += item.value * (W / item.weight)
            W = 0
            break

    return profit
```

---

## Complexity

```text
Sorting: O(n log n)
Loop:    O(n)
Total:   O(n log n)
```

Space:

```text
O(1) or O(n), depending on implementation
```

---

## Dry Run

Items:

```text
value weight ratio
60    10     6
100   20     5
120   30     4
```

Capacity `W = 50`.

Take:

```text
item1 full: profit = 60, W = 40
item2 full: profit = 160, W = 20
item3 20/30 fraction: profit += 120*(20/30) = 80
```

Total profit:

```text
240
```

---

## Fractional vs 0/1 Knapsack

| Feature | Fractional | 0/1 |
|---|---|---|
| Can take fraction? | Yes | No |
| Greedy works? | Yes | No generally |
| Common method | Greedy | Dynamic Programming / Branch & Bound |

---

## Exam Perspective

Common questions:

- Write fractional knapsack algorithm.
- Apply on given table.
- Why sort by value/weight?
- Compare with 0/1 knapsack.
