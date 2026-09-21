# Unit I — Recurrence Relations Notes

## 1. What is a Recurrence Relation?

A **recurrence relation** expresses the running time of a recursive algorithm in terms of smaller input sizes.

Example:

```cpp
void solve(int n) {
    if (n <= 1) return;

    solve(n / 2);
    solve(n / 2);

    for (int i = 0; i < n; i++) {
        cout << i;
    }
}
```

This does:

- 2 recursive calls of size `n/2`
- `n` extra work outside recursion

So:

```text
T(n) = 2T(n/2) + n
```

---

## 2. How to Form a Recurrence

For recursive code, identify:

```text
1. Number of recursive calls
2. Size of each recursive call
3. Work done outside recursive calls
```

General divide-and-conquer form:

```text
T(n) = aT(n/b) + f(n)
```

| Symbol | Meaning |
|---|---|
| `a` | number of recursive calls |
| `n/b` | size of each subproblem |
| `f(n)` | non-recursive work |
| `T(1)` | base case, usually constant |

---

## 3. Examples of Forming Recurrences

### Example 1

```cpp
void f(int n) {
    if (n <= 1) return;

    f(n / 2);

    for (int i = 0; i < n; i++) {
        cout << i;
    }
}
```

One recursive call of size `n/2`, plus loop of `n`.

```text
T(n) = T(n/2) + n
```

---

### Example 2

```cpp
void f(int n) {
    if (n <= 1) return;

    f(n / 2);
    f(n / 2);

    for (int i = 0; i < n; i++) {
        cout << i;
    }
}
```

Two recursive calls of size `n/2`, plus loop of `n`.

```text
T(n) = 2T(n/2) + n
```

This is like Merge Sort.

---

### Example 3

```cpp
void f(int n) {
    if (n <= 1) return;

    f(n - 1);

    for (int i = 0; i < n; i++) {
        cout << i;
    }
}
```

One recursive call of size `n-1`, plus loop of `n`.

```text
T(n) = T(n-1) + n
```

This is not directly Master Theorem form because the input decreases by 1, not by division.

---

## 4. Methods to Solve Recurrences

Important methods for syllabus/PYQs:

```text
1. Expansion / substitution
2. Recursion tree method
3. Master theorem
```

This note starts with **expansion**.

---

# 5. Solving by Expansion

## Example A

```text
T(n) = T(n-1) + n
T(1) = 1
```

Expand:

```text
T(n) = T(n-1) + n
T(n-1) = T(n-2) + (n-1)
```

So:

```text
T(n) = T(n-2) + (n-1) + n
```

Again:

```text
T(n) = T(n-3) + (n-2) + (n-1) + n
```

Continue until base case:

```text
T(n) = T(1) + 2 + 3 + ... + n
```

Now:

```text
2 + 3 + ... + n = O(n^2)
```

Therefore:

```text
T(n) = O(n^2)
```

More precisely:

```text
T(n) = Θ(n^2)
```

---

## Example B

```text
T(n) = T(n/2) + 1
```

Expand:

```text
T(n) = T(n/2) + 1
T(n/2) = T(n/4) + 1
```

So:

```text
T(n) = T(n/4) + 2
```

Again:

```text
T(n) = T(n/8) + 3
```

After `k` steps:

```text
T(n) = T(n / 2^k) + k
```

Stop when:

```text
n / 2^k = 1
```

So:

```text
n = 2^k
k = log₂ n
```

Therefore:

```text
T(n) = T(1) + log n
T(n) = O(log n)
```

---

## Example C

```text
T(n) = T(n/2) + n
```

Expand:

```text
T(n) = T(n/2) + n
T(n/2) = T(n/4) + n/2
```

So:

```text
T(n) = T(n/4) + n/2 + n
```

Again:

```text
T(n) = T(n/8) + n/4 + n/2 + n
```

Eventually:

```text
T(n) = T(1) + n + n/2 + n/4 + n/8 + ...
```

This is a geometric series:

```text
n + n/2 + n/4 + ... < 2n
```

Therefore:

```text
T(n) = O(n)
```

More precisely:

```text
T(n) = Θ(n)
```

---

# 6. Common Recurrences to Remember

| Recurrence | Complexity |
|---|---|
| `T(n) = T(n-1) + 1` | `O(n)` |
| `T(n) = T(n-1) + n` | `O(n^2)` |
| `T(n) = T(n/2) + 1` | `O(log n)` |
| `T(n) = T(n/2) + n` | `O(n)` |
| `T(n) = 2T(n/2) + n` | `O(n log n)` — later by recursion tree/Master theorem |

---

# Practice Questions

Try these yourself before checking with me.

## Q1. Form recurrence and solve

```cpp
void f(int n) {
    if (n <= 1) return;
    f(n / 2);
}
```

Tasks:

```text
1. Form the recurrence.
2. Give final complexity.
```

---

## Q2. Form recurrence and solve

```cpp
void f(int n) {
    if (n <= 1) return;

    f(n - 1);

    for (int i = 0; i < n; i++) {
        cout << i;
    }
}
```

Tasks:

```text
1. Form the recurrence.
2. Give final complexity.
```

---

## Q3. Solve

```text
T(n) = T(n/2) + n
```

---

## Q4. Solve

```text
T(n) = T(n-1) + 1
```

---

## Q5. Form recurrence only

```cpp
void f(int n) {
    if (n <= 1) return;

    f(n / 3);
    f(n / 3);

    for (int i = 0; i < n * n; i++) {
        cout << i;
    }
}
```

Task:

```text
Form recurrence only.
```

---

# Answer Format

Send your answers like this:

```text
Q1: T(n) = ..., complexity = ...
Q2: T(n) = ..., complexity = ...
Q3: ...
Q4: ...
Q5: T(n) = ...
```
