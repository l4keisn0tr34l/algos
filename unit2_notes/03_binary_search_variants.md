# 03 — Binary Search Variants

PYQs often ask binary search in disguised form.

---

# Variant 1: First 1 in a Sorted 0/1 Array

Given:

```text
[0, 0, 0, 1, 1, 1]
```

Find the first index containing `1`.

## Idea

If `A[mid] == 1`, answer may be `mid`, but there may be an earlier `1` on the left.

If `A[mid] == 0`, first `1` must be on the right.

## Pseudocode

```text
FirstOne(A, n):
    low = 0, high = n - 1
    ans = -1

    while low <= high:
        mid = low + (high-low)/2

        if A[mid] == 1:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans
```

## C++ Implementation

```cpp
int firstOne(vector<int>& a) {
    int low = 0, high = a.size() - 1;
    int ans = -1;

    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (a[mid] == 1) {
            ans = mid;
            high = mid - 1;   // try to find earlier 1
        } else {
            low = mid + 1;
        }
    }

    return ans;
}
```

## Complexity

```text
O(log n)
```

---

# Variant 2: Search in Rotated Sorted Array

Example:

```text
[35, 42, 5, 15, 27, 29]
```

This was sorted but circularly shifted.

## Idea

At every `mid`, at least one side is sorted.

- If left side is sorted, check whether target lies there.
- Otherwise search right.
- If right side is sorted, check whether target lies there.

## Pseudocode

```text
SearchRotated(A, n, target):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) / 2

        if A[mid] == target:
            return mid

        // left half is sorted
        if A[low] <= A[mid]:
            if A[low] <= target < A[mid]:
                high = mid - 1
            else:
                low = mid + 1

        // right half is sorted
        else:
            if A[mid] < target <= A[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1
```

## C++ Implementation

```cpp
int searchRotated(vector<int>& a, int target) {
    int low = 0, high = a.size() - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (a[mid] == target) return mid;

        // left half is sorted
        if (a[low] <= a[mid]) {
            if (a[low] <= target && target < a[mid]) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        // right half is sorted
        else {
            if (a[mid] < target && target <= a[high]) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
    }

    return -1;
}
```

## Dry Run

Search `15` in:

```text
[35, 42, 5, 15, 27, 29]
```

```text
low = 0, high = 5
mid = 2 → A[mid] = 5
A[low] = 35, A[mid] = 5
left half is not sorted, so right half must be sorted
15 lies between A[mid]=5 and A[high]=29
so low = mid + 1 = 3

low = 3, high = 5
mid = 4 → A[mid] = 27
left half [15, 27] is sorted
15 lies between A[low]=15 and A[mid]=27
so high = mid - 1 = 3

low = 3, high = 3
mid = 3 → A[mid] = 15
found at index 3
```

## Complexity

```text
O(log n)
```

---

# Variant 3: Fixed Point `A[i] = i`

Given sorted array of distinct integers, find index `i` such that:

```text
A[i] = i
```

Example:

```text
[-10, -5, 0, 3, 7]
```

Here:

```text
A[3] = 3
```

## Idea

Use binary search:

- if `A[mid] == mid`, found.
- if `A[mid] > mid`, search left.
- if `A[mid] < mid`, search right.

## Pseudocode

```text
FixedPoint(A, n):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) / 2

        if A[mid] == mid:
            return mid
        else if A[mid] > mid:
            high = mid - 1
        else:
            low = mid + 1

    return -1
```

## C++ Implementation

```cpp
int fixedPoint(vector<int>& a) {
    int low = 0, high = a.size() - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (a[mid] == mid) return mid;
        else if (a[mid] > mid) high = mid - 1;
        else low = mid + 1;
    }

    return -1;
}
```

## Dry Run

Array:

```text
[-10, -5, 0, 3, 7]
```

```text
low = 0, high = 4
mid = 2 → A[2] = 0
A[mid] < mid, so fixed point must be on right
low = 3

low = 3, high = 4
mid = 3 → A[3] = 3
found fixed point at index 3
```

## Complexity

```text
O(log n)
```

---

## Exam Perspective

Common PYQ wording:

- Find smallest index with 1 in sorted binary array.
- Search element in circularly shifted sorted array.
- Find index `i` where `A[i] = i`.

---

## Practice

1. Find first 1 in `[0, 0, 0, 0, 1, 1]`.
2. Search `15` in `[35, 42, 5, 15, 27, 29]`.
3. Find fixed point in `[-10, -5, 0, 3, 7]`.

---

## Practice Solutions

### 1. First 1 in `[0, 0, 0, 0, 1, 1]`

```text
low = 0, high = 5
mid = 2 → A[2] = 0 → go right

low = 3, high = 5
mid = 4 → A[4] = 1 → possible answer, go left
ans = 4

low = 3, high = 3
mid = 3 → A[3] = 0 → go right

low = 4, high = 3 → stop
```

Answer:

```text
first 1 is at index 4
```

---

### 2. Search `15` in `[35, 42, 5, 15, 27, 29]`

```text
low = 0, high = 5
mid = 2 → A[2] = 5
left side [35, 42, 5] is not sorted
right side [15, 27, 29] is sorted
15 lies in right side → low = 3

low = 3, high = 5
mid = 4 → A[4] = 27
left side [15, 27] is sorted
15 lies in left side → high = 3

low = 3, high = 3
mid = 3 → A[3] = 15
found
```

Answer:

```text
15 is at index 3
```

---

### 3. Fixed point in `[-10, -5, 0, 3, 7]`

Check indices:

```text
A[0] = -10
A[1] = -5
A[2] = 0
A[3] = 3
A[4] = 7
```

Answer:

```text
fixed point = 3
```

Because:

```text
A[3] = 3
```

