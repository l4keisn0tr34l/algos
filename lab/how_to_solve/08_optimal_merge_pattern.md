# 08 — Optimal Merge Pattern

## Problem

Given file sizes, merge all files into one file with minimum total cost.

Cost of merging two files:

```text
size1 + size2
```

## Greedy Idea

Always merge the two smallest files first.

## Algorithm

```text
OptimalMerge(files):
    insert all file sizes into min heap
    totalCost = 0

    while heap has more than one file:
        a = extract minimum
        b = extract minimum
        cost = a + b
        totalCost += cost
        insert cost into heap

    return totalCost
```

## Complexity

```text
O(n log n)
```

## Relation to Huffman

Very similar to Huffman coding: repeatedly combine two smallest weights.
