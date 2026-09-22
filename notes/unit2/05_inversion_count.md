# 05 — Inversion Count using Merge Sort

## 1. What is an Inversion?

An inversion is a pair `(i, j)` such that:

```text
i < j and A[i] > A[j]
```

Example:

```text
A = [2, 4, 1, 3]
```

Inversions:

```text
(2,1), (4,1), (4,3)
```

Total inversions = `3`.

---

## 2. Brute Force

Check all pairs.

```text
O(n^2)
```

---

## 3. Efficient Idea

Use Merge Sort.

While merging two sorted halves:

- If left element <= right element, no new inversion.
- If left element > right element, then that right element forms inversions with all remaining elements in left half.

---

## 4. Key Formula During Merge

If:

```text
left[i] > right[j]
```

Then inversions added:

```text
mid - i + 1
```

Because all elements from `i` to `mid` in left half are greater than `right[j]`.

---

## 5. Algorithm / Pseudocode

### Main Algorithm: CountInversions

```text
CountInversions(A, low, high):
    if low >= high:
        return 0

    mid = (low + high) / 2

    leftCount  = CountInversions(A, low, mid)
    rightCount = CountInversions(A, mid + 1, high)
    crossCount = MergeAndCount(A, low, mid, high)

    return leftCount + rightCount + crossCount
```

### Helper Function: MergeAndCount

```text
MergeAndCount(A, low, mid, high):
    i = low
    j = mid + 1
    count = 0
    temp = empty array

    while i <= mid and j <= high:
        if A[i] <= A[j]:
            append A[i] to temp
            i = i + 1
        else:
            append A[j] to temp
            count = count + (mid - i + 1)
            j = j + 1

    while i <= mid:
        append A[i] to temp
        i = i + 1

    while j <= high:
        append A[j] to temp
        j = j + 1

    copy temp back to A[low ... high]
    return count
```

---

## 6. C++ Implementation

```cpp
long long mergeAndCount(vector<int>& a, int low, int mid, int high) {
    vector<int> temp;
    int i = low, j = mid + 1;
    long long count = 0;

    while (i <= mid && j <= high) {
        if (a[i] <= a[j]) {
            temp.push_back(a[i++]);
        } else {
            temp.push_back(a[j++]);
            count += (mid - i + 1);
        }
    }

    while (i <= mid) temp.push_back(a[i++]);
    while (j <= high) temp.push_back(a[j++]);

    for (int k = low; k <= high; k++) {
        a[k] = temp[k - low];
    }

    return count;
}

long long countInversions(vector<int>& a, int low, int high) {
    if (low >= high) return 0;

    int mid = low + (high - low) / 2;

    long long left = countInversions(a, low, mid);
    long long right = countInversions(a, mid + 1, high);
    long long cross = mergeAndCount(a, low, mid, high);

    return left + right + cross;
}
```

---

## 7. Complexity

Same as Merge Sort:

```text
O(n log n)
```

Space:

```text
O(n)
```

---

## 8. Exam Perspective

Common PYQ:

> Using divide and conquer, count number of inversions in an array.

You should write:

1. definition of inversion
2. merge-sort-based algorithm
3. explain counting during merge
4. complexity

---

## Practice

1. Count inversions in `[2, 4, 1, 3]`.
2. Count inversions in `[5, 4, 3, 2, 1]`.
3. Why does merge step count cross inversions efficiently?

---

## Practice Solutions

### 1. Count inversions in `[2, 4, 1, 3]`

Pairs:

```text
(2, 1)
(4, 1)
(4, 3)
```

Answer:

```text
3 inversions
```

### 2. Count inversions in `[5, 4, 3, 2, 1]`

This array is reverse sorted. Every pair is an inversion.

For `n = 5`:

```text
number of inversions = n(n-1)/2 = 5×4/2 = 10
```

Answer:

```text
10 inversions
```

### 3. Why merge step counts cross inversions efficiently

During merge, both halves are already sorted. If:

```text
left[i] > right[j]
```

then all remaining elements from `left[i]` to `left[mid]` are also greater than `right[j]`. So we add:

```text
mid - i + 1
```

inversions at once instead of checking one by one.

