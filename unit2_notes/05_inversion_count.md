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

## 5. Complexity

Same as Merge Sort:

```text
O(n log n)
```

Space:

```text
O(n)
```

---

## 6. Exam Perspective

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

