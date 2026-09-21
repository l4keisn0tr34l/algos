# 08 — Strassen Matrix Multiplication

## 1. Normal Matrix Multiplication

For two `n × n` matrices, normal multiplication takes:

```text
O(n^3)
```

Because each of `n²` entries takes `n` multiplications/additions.

---

## 2. Strassen's Idea

For two `2 × 2` block matrices:

```text
A = [A11 A12]
    [A21 A22]

B = [B11 B12]
    [B21 B22]
```

Normal divide-and-conquer uses 8 recursive multiplications.

Strassen reduces this to **7 recursive multiplications**, at the cost of more additions/subtractions.

---

## 3. Recurrence

```text
T(n) = 7T(n/2) + O(n^2)
```

Using Master Theorem:

```text
T(n) = O(n^log₂7)
```

Since:

```text
log₂7 ≈ 2.807
```

Complexity:

```text
O(n^2.807)
```

---

## 4. Exam Perspective

Common questions:

- Explain Strassen's matrix multiplication.
- Write the recurrence.
- Compare with normal `O(n³)` multiplication.
- Write the 7 products and final combinations.

---

## 5. Important Point

Strassen is faster asymptotically for large matrices, but for small matrices normal multiplication may be better due to overhead.

---

## Practice

1. What is the recurrence of Strassen's algorithm?
2. Why is it better than normal multiplication?
3. What is `log₂7` approximately?

---

## Practice Solutions

### 1. Recurrence of Strassen's algorithm

```text
T(n) = 7T(n/2) + O(n^2)
```

### 2. Why it is better than normal multiplication

Normal divide-and-conquer matrix multiplication uses 8 recursive multiplications of size `n/2`.

Strassen uses only 7 recursive multiplications, reducing complexity from:

```text
O(n^3)
```

to:

```text
O(n^2.807)
```

### 3. Approximate value of `log₂7`

```text
log₂7 ≈ 2.807
```

