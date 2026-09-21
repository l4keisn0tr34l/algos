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

## 3. Algorithm / Formula

Divide matrices `A` and `B` into four submatrices each:

```text
A = [A11 A12]
    [A21 A22]

B = [B11 B12]
    [B21 B22]
```

Compute these 7 products:

```text
P1 = (A11 + A22)(B11 + B22)
P2 = (A21 + A22)B11
P3 = A11(B12 - B22)
P4 = A22(B21 - B11)
P5 = (A11 + A12)B22
P6 = (A21 - A11)(B11 + B12)
P7 = (A12 - A22)(B21 + B22)
```

Then compute result matrix `C`:

```text
C11 = P1 + P4 - P5 + P7
C12 = P3 + P5
C21 = P2 + P4
C22 = P1 - P2 + P3 + P6
```

---

## 4. Pseudocode

```text
Strassen(A, B, n):
    if n == 1:
        return A * B

    divide A into A11, A12, A21, A22
    divide B into B11, B12, B21, B22

    P1 = Strassen(A11 + A22, B11 + B22, n/2)
    P2 = Strassen(A21 + A22, B11, n/2)
    P3 = Strassen(A11, B12 - B22, n/2)
    P4 = Strassen(A22, B21 - B11, n/2)
    P5 = Strassen(A11 + A12, B22, n/2)
    P6 = Strassen(A21 - A11, B11 + B12, n/2)
    P7 = Strassen(A12 - A22, B21 + B22, n/2)

    C11 = P1 + P4 - P5 + P7
    C12 = P3 + P5
    C21 = P2 + P4
    C22 = P1 - P2 + P3 + P6

    combine C11, C12, C21, C22 into C
    return C
```

---

## 5. Recurrence

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

## 6. Exam Perspective

Common questions:

- Explain Strassen's matrix multiplication.
- Write the recurrence.
- Compare with normal `O(n³)` multiplication.
- Write the 7 products and final combinations.

---

## 7. Important Point

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

