# 04 — Merge Sort

## 1. Intuition

Merge Sort divides the array into two halves, sorts each half recursively, and then merges the two sorted halves.

```text
Divide → Sort left → Sort right → Merge
```

---

## 2. Dry Run

Array:

```text
[4, 1, 6, 3]
```

Divide:

```text
[4, 1, 6, 3]
→ [4, 1] and [6, 3]
→ [4], [1], [6], [3]
```

Merge:

```text
[4] + [1] → [1, 4]
[6] + [3] → [3, 6]
[1, 4] + [3, 6] → [1, 3, 4, 6]
```

---

## 3. Pseudocode

```text
MergeSort(A, low, high):
    if low >= high:
        return

    mid = (low + high) / 2
    MergeSort(A, low, mid)
    MergeSort(A, mid+1, high)
    Merge(A, low, mid, high)
```

---

## 4. Recurrence

```text
T(n) = 2T(n/2) + n
```

Reason:

- two recursive calls of size `n/2`
- merging takes `n` time

---

## 5. Complexity

| Case | Complexity |
|---|---|
| Best | `O(n log n)` |
| Average | `O(n log n)` |
| Worst | `O(n log n)` |
| Space | `O(n)` |

Why? There are `log n` levels and each level does total `n` merging work.

---

## 6. C++ Implementation

```cpp
void mergeArray(vector<int>& a, int low, int mid, int high) {
    vector<int> temp;
    int i = low, j = mid + 1;

    while (i <= mid && j <= high) {
        if (a[i] <= a[j]) temp.push_back(a[i++]);
        else temp.push_back(a[j++]);
    }

    while (i <= mid) temp.push_back(a[i++]);
    while (j <= high) temp.push_back(a[j++]);

    for (int k = low; k <= high; k++) {
        a[k] = temp[k - low];
    }
}

void mergeSort(vector<int>& a, int low, int high) {
    if (low >= high) return;

    int mid = low + (high - low) / 2;
    mergeSort(a, low, mid);
    mergeSort(a, mid + 1, high);
    mergeArray(a, low, mid, high);
}
```

---

## 7. Exam Perspective

Common questions:

- Write Merge Sort algorithm.
- Trace Merge Sort on an array.
- Derive recurrence and complexity.
- Compare Merge Sort with Quick Sort / Heap Sort.

---

## Practice

1. Apply Merge Sort to `[8, 3, 2, 9, 7, 1]`.
2. Write recurrence of Merge Sort.
3. Why does Merge Sort need `O(n)` extra space?

---

## Practice Solutions

### 1. Apply Merge Sort to `[8, 3, 2, 9, 7, 1]`

Divide:

```text
[8, 3, 2, 9, 7, 1]
→ [8, 3, 2] and [9, 7, 1]
→ [8], [3, 2] and [9], [7, 1]
→ [8], [3], [2] and [9], [7], [1]
```

Merge:

```text
[3] + [2] → [2, 3]
[8] + [2, 3] → [2, 3, 8]

[7] + [1] → [1, 7]
[9] + [1, 7] → [1, 7, 9]

[2, 3, 8] + [1, 7, 9] → [1, 2, 3, 7, 8, 9]
```

Final sorted array:

```text
[1, 2, 3, 7, 8, 9]
```

### 2. Recurrence of Merge Sort

```text
T(n) = 2T(n/2) + n
```

### 3. Why Merge Sort needs `O(n)` extra space

During merging, temporary arrays are used to store sorted elements before copying them back. At a level, the temporary storage can be proportional to `n`, so auxiliary space is:

```text
O(n)
```

