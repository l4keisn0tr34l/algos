# 02 — Binary Search

## 1. Intuition

Binary Search works on a **sorted array**. Instead of checking every element, it checks the middle element and discards half of the array each time.

---

## 2. Dry Run

Array:

```text
[2, 4, 7, 10, 15, 20]
```

Search `15`.

```text
low = 0, high = 5
mid = 2 → arr[2] = 7
15 > 7, search right half

low = 3, high = 5
mid = 4 → arr[4] = 15
found
```

---

## 3. Pseudocode

```text
BinarySearch(A, n, key):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) / 2

        if A[mid] == key:
            return mid
        else if key < A[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1
```

---

## 4. C++ Implementation

```cpp
int binarySearch(vector<int>& a, int key) {
    int low = 0, high = a.size() - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (a[mid] == key) return mid;
        else if (key < a[mid]) high = mid - 1;
        else low = mid + 1;
    }

    return -1;
}
```

---

## 5. Complexity

| Case | Complexity |
|---|---|
| Best | `O(1)` |
| Worst | `O(log n)` |
| Average | `O(log n)` |
| Space iterative | `O(1)` |
| Space recursive | `O(log n)` |

Why `O(log n)`? Because each comparison halves the search space.

---

## 6. Exam Perspective

Common questions:

- Write binary search algorithm.
- Apply binary search on a given array.
- Analyze its time complexity.
- Write recursive binary search.

---

## 7. Common Mistakes

- Using binary search on an unsorted array.
- Wrong loop condition: should usually be `low <= high`.
- Possible overflow with `(low + high) / 2`; safer: `low + (high-low)/2`.

---

## Practice

1. Search `23` in `[3, 5, 8, 12, 23, 40]` using binary search.
2. Write recursive binary search.
3. Why is binary search `O(log n)`?

---

## Practice Solutions

### 1. Search `23` in `[3, 5, 8, 12, 23, 40]`

```text
low = 0, high = 5
mid = 2 → A[2] = 8
23 > 8 → search right

low = 3, high = 5
mid = 4 → A[4] = 23
found at index 4
```

Answer:

```text
index = 4
```

### 2. Recursive binary search

```cpp
int binarySearch(vector<int>& a, int low, int high, int key) {
    if (low > high) return -1;

    int mid = low + (high - low) / 2;

    if (a[mid] == key) return mid;
    else if (key < a[mid]) return binarySearch(a, low, mid - 1, key);
    else return binarySearch(a, mid + 1, high, key);
}
```

### 3. Why binary search is `O(log n)`

At every step, binary search halves the search space:

```text
n → n/2 → n/4 → n/8 → ... → 1
```

Number of halvings needed is `log₂ n`, so complexity is:

```text
O(log n)
```

