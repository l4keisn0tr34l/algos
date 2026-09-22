# 09 — Fractional Knapsack

## Problem

Given values, weights, and capacity, maximize profit. Fractions of items are allowed.

## Greedy Rule

Sort by decreasing ratio:

```text
value / weight
```

## Algorithm

```text
FractionalKnapsack(items, W):
    compute ratio for every item
    sort items by decreasing ratio
    profit = 0

    for item in sorted items:
        if item.weight <= W:
            take full item
            profit += item.value
            W -= item.weight
        else:
            take W / item.weight fraction
            profit += item.value * W / item.weight
            break

    return profit
```

## Complexity

```text
O(n log n)
```
