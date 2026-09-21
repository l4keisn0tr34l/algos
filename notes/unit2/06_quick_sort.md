# 06 — Quick Sort

## 1. Intuition

Quick Sort selects a pivot and partitions the array so that:

```text
left side ≤ pivot ≤ right side
```

Then it recursively sorts the left and right parts.

---

## 2. Pseudocode

```text
QuickSort(A, low, high):
    if low < high:
        p = Partition(A, low, high)
        QuickSort(A, low, p-1)
        QuickSort(A, p+1, high)
```

Partition using last element as pivot:

```text
Partition(A, low, high):
    pivot = A[high]
    i = low - 1

    for j = low to high-1:
        if A[j] <= pivot:
            i = i + 1
            swap A[i], A[j]

    swap A[i+1], A[high]
    return i + 1
```

---

## 3. Complexity

| Case | Condition | Complexity |
|---|---|---|
| Best | pivot divides array nearly equally | `O(n log n)` |
| Average | random-ish partitions | `O(n log n)` |
| Worst | pivot always smallest/largest | `O(n^2)` |

Space:

```text
Average: O(log n)
Worst: O(n)
```

---

## 4. Why Worst Case is O(n²)

If pivot is always smallest/largest:

```text
T(n) = T(n-1) + n
```

This becomes:

```text
n + (n-1) + (n-2) + ... + 1 = O(n^2)
```

---

## 5. Why Best Case is O(n log n)

If pivot splits array evenly:

```text
T(n) = 2T(n/2) + n
```

This gives:

```text
O(n log n)
```

---

## 6. C++ Implementation

```cpp
int partitionArray(vector<int>& a, int low, int high) {
    int pivot = a[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (a[j] <= pivot) {
            i++;
            swap(a[i], a[j]);
        }
    }

    swap(a[i + 1], a[high]);
    return i + 1;
}

void quickSort(vector<int>& a, int low, int high) {
    if (low < high) {
        int p = partitionArray(a, low, high);
        quickSort(a, low, p - 1);
        quickSort(a, p + 1, high);
    }
}
```

---

## 7. Exam Perspective

Very important PYQ topic.

Common questions:

- Write Quick Sort algorithm.
- Derive best and worst case complexity.
- Apply Quick Sort to given array.
- Explain randomized Quick Sort.
- Explain why average case is useful.

---

## Practice

1. Apply Quick Sort to `[4, 1, 6, 3, 9, 2, 7, 5]` using last element as pivot.
2. Derive worst-case recurrence.
3. Why is Quick Sort usually faster in practice than Merge Sort?

---

## Practice Solutions

### 1. Apply Quick Sort to `[4, 1, 6, 3, 9, 2, 7, 5]` using last element as pivot

Initial array:

```text
[4, 1, 6, 3, 9, 2, 7, 5]
```

Pivot = `5`.

After partition:

```text
[4, 1, 3, 2, 5, 6, 7, 9]
```

Now recursively sort left and right parts:

```text
Left:  [4, 1, 3, 2]
Right: [6, 7, 9]
```

Sorting left with pivot `2`:

```text
[1, 2, 3, 4]
```

Sorting right with pivot `9`:

```text
[6, 7, 9]
```

Final sorted array:

```text
[1, 2, 3, 4, 5, 6, 7, 9]
```

### 2. Worst-case recurrence

Worst case happens when pivot is always smallest or largest.

```text
T(n) = T(n-1) + n
```

Solving:

```text
T(n) = O(n^2)
```

### 3. Why Quick Sort is usually faster in practice than Merge Sort

Quick Sort is usually in-place and has good cache performance. Merge Sort needs extra array space for merging. Therefore Quick Sort often performs better in practice, although its worst case is `O(n²)`.

