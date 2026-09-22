# 04 — Priority Queue using MinHeap

## Problem

Implement a priority queue using MinHeap.

## MinHeap property

```text
parent <= children
```

The minimum element is always at index `0`.

## Helper formulas for 0-based indexing

```text
parent(i) = (i - 1) // 2
left(i) = 2i + 1
right(i) = 2i + 2
```

## Operations

### Insert

1. Add element at end.
2. Heapify up while parent is greater.

### Extract Min

1. Save root.
2. Replace root with last element.
3. Remove last element.
4. Heapify down.

## Complexity

| Operation | Complexity |
|---|---|
| Insert | `O(log n)` |
| Extract Min | `O(log n)` |
| Get Min | `O(1)` |
