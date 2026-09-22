# 00 — MinHeap Helper Functions

MinHeap is used in:

- Prim's Algorithm
- Dijkstra's Algorithm
- Huffman Coding
- Optimal Merge Pattern

A **MinHeap** is a complete binary tree where every parent is smaller than or equal to its children.

```text
parent <= children
```

So the minimum element is always at the root.

---

## Array Representation

For 0-based indexing:

```text
left(i)   = 2i + 1
right(i)  = 2i + 2
parent(i) = floor((i - 1) / 2)
```

For 1-based indexing:

```text
left(i)   = 2i
right(i)  = 2i + 1
parent(i) = floor(i / 2)
```

---

## Helper Function: MinHeapify

Used when a node may violate min-heap property, but its left and right subtrees are already min-heaps.

```text
MinHeapify(A, n, i):
    smallest = i
    left = 2i + 1
    right = 2i + 2

    if left < n and A[left] < A[smallest]:
        smallest = left

    if right < n and A[right] < A[smallest]:
        smallest = right

    if smallest != i:
        swap A[i], A[smallest]
        MinHeapify(A, n, smallest)
```

Complexity:

```text
O(log n)
```

---

## Helper Function: Insert

Insert a new element into MinHeap.

```text
Insert(A, key):
    add key at the end of A
    i = index of key

    while i > 0 and A[parent(i)] > A[i]:
        swap A[i], A[parent(i)]
        i = parent(i)
```

Complexity:

```text
O(log n)
```

---

## Helper Function: ExtractMin

Remove and return the smallest element.

```text
ExtractMin(A):
    if heap is empty:
        return error

    minValue = A[0]
    A[0] = A[last]
    remove last element

    MinHeapify(A, heapSize, 0)

    return minValue
```

Complexity:

```text
O(log n)
```

---

## Helper Function: GetMin

Return the minimum element without removing it.

```text
GetMin(A):
    if heap is empty:
        return error

    return A[0]
```

Complexity:

```text
O(1)
```

---

## Helper Function: DecreaseKey

Used in some versions of Dijkstra and Prim.

```text
DecreaseKey(A, i, newKey):
    if newKey > A[i]:
        return error

    A[i] = newKey

    while i > 0 and A[parent(i)] > A[i]:
        swap A[i], A[parent(i)]
        i = parent(i)
```

Complexity:

```text
O(log n)
```

---

## Build MinHeap

```text
BuildMinHeap(A, n):
    for i = floor(n/2) - 1 downto 0:
        MinHeapify(A, n, i)
```

Complexity:

```text
O(n)
```

---

## Exam Usage

In algorithm pseudocode, instead of writing the full heap implementation every time, you may write:

```text
Insert(Q, item)
ExtractMin(Q)
DecreaseKey(Q, item, newValue)
```

But if the question specifically asks for priority queue / MinHeap implementation, write the helper functions above.
