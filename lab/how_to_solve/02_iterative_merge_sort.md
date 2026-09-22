# 02 — Iterative Merge Sort

## Problem

Implement Merge Sort without recursion.

## Idea

Recursive Merge Sort splits array until size 1, then merges upward.

Iterative Merge Sort directly starts by merging blocks of size:

```text
1, 2, 4, 8, ...
```

## Algorithm

```text
IterativeMergeSort(A):
    n = length(A)
    size = 1

    while size < n:
        for left from 0 to n-1 in steps of 2*size:
            mid = min(left + size - 1, n - 1)
            right = min(left + 2*size - 1, n - 1)

            if mid < right:
                Merge(A, left, mid, right)

        size = size * 2
```

## Helper: Merge

Same as normal Merge Sort. Merge two sorted parts:

```text
A[left...mid]
A[mid+1...right]
```

## Complexity

```text
Time: O(n log n)
Space: O(n)
```
