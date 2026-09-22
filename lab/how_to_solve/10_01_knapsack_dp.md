# 10 — 0/1 Knapsack using Dynamic Programming

## Problem

Given items with weights and values, and capacity `W`, maximize value. Each item can either be taken fully or not taken.

## DP State

```text
C[i][w] = maximum value using first i items with capacity w
```

## Recurrence

If item `i` has weight `wt[i]` and value `val[i]`:

```text
if wt[i] > w:
    C[i][w] = C[i-1][w]
else:
    C[i][w] = max(C[i-1][w], val[i] + C[i-1][w - wt[i]])
```

## Keep Table

```text
Keep[i][w] = 1 if item i is included
Keep[i][w] = 0 otherwise
```

## Complexity

```text
Time: O(nW)
Space: O(nW)
```

## Finding selected items

Start from:

```text
i = n, w = W
```

If `Keep[i][w] == 1`, item `i` is selected. Then:

```text
w = w - weight[i]
i = i - 1
```

Otherwise:

```text
i = i - 1
```
