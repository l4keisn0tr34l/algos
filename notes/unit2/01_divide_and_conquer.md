# 01 — Divide and Conquer Paradigm

## 1. Intuition

Divide and Conquer solves a problem by breaking it into smaller subproblems, solving them recursively, and combining their answers.

```text
Divide → Conquer → Combine
```

Example: Merge Sort divides the array into halves, sorts both halves, then merges them.

---

## 2. General Structure

```text
DNC(problem):
    if problem is small enough:
        solve directly
    divide problem into smaller subproblems
    solve each subproblem recursively
    combine subproblem answers
```

---

## 3. Generic Algorithm / Pseudocode

```text
DivideAndConquer(problem):
    if problem is small enough:
        solve directly
        return answer

    divide problem into smaller subproblems

    answer1 = DivideAndConquer(subproblem1)
    answer2 = DivideAndConquer(subproblem2)
    ...

    finalAnswer = Combine(answer1, answer2, ...)
    return finalAnswer
```

Example recurrence format:

```text
T(n) = aT(n/b) + f(n)
```

Where:

- `a` = number of recursive subproblems
- `n/b` = size of each subproblem
- `f(n)` = divide/combine work done outside recursion

---

## 4. Common Examples

| Algorithm | Divide | Combine |
|---|---|---|
| Binary Search | Choose one half | No major combine |
| Merge Sort | Split into two halves | Merge sorted halves |
| Quick Sort | Partition around pivot | No major combine |
| Strassen | Split matrices | Combine 7 products |
| Min/Max D&C | Split array | Compare min/max |

---

## 5. Recurrence Form

Many divide-and-conquer algorithms have recurrence:

```text
T(n) = aT(n/b) + f(n)
```

Where:

| Symbol | Meaning |
|---|---|
| `a` | number of subproblems |
| `n/b` | size of each subproblem |
| `f(n)` | work outside recursion |

---

## 6. Exam Definition

A divide-and-conquer algorithm solves a problem by dividing it into smaller subproblems, recursively solving them, and combining their solutions to obtain the final answer.

---

## 7. Common Mistakes

- Forgetting the combine step.
- Thinking every recursive algorithm is divide and conquer.
- Confusing divide-and-conquer with greedy.
- Not writing recurrence while analyzing complexity.

---

## Practice

1. Write the three steps of divide and conquer.
2. Explain why Merge Sort is divide and conquer.
3. For an algorithm that solves 2 subproblems of size `n/2` and does `n` extra work, write the recurrence.

---

## Practice Solutions

### 1. Three steps of divide and conquer

```text
Divide → Conquer → Combine
```

- Divide: break problem into smaller subproblems.
- Conquer: solve subproblems recursively.
- Combine: merge subproblem answers to get final answer.

### 2. Why Merge Sort is divide and conquer

Merge Sort divides the array into two halves, recursively sorts both halves, and combines them by merging the sorted halves.

### 3. Recurrence

If an algorithm solves 2 subproblems of size `n/2` and does `n` extra work:

```text
T(n) = 2T(n/2) + n
```

