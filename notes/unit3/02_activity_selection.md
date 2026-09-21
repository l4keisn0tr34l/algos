# 02 — Activity Selection Problem

## Problem

Given activities with start and finish times, select the maximum number of non-overlapping activities.

---

## Greedy Choice

Choose the activity that finishes earliest.

Why? The earlier an activity finishes, the more room remains for future activities.

---

## Algorithm / Pseudocode

Assume activities are sorted by finish time.

```text
ActivitySelection(activities):
    sort activities by finish time
    selected = []
    lastFinish = -infinity

    for each activity (start, finish):
        if start >= lastFinish:
            add activity to selected
            lastFinish = finish

    return selected
```

---

## Python-like Code

```python
def activity_selection(activities):
    activities.sort(key=lambda x: x[1])
    selected = []
    last_finish = float('-inf')

    for start, finish in activities:
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish

    return selected
```

---

## Complexity

| Step | Complexity |
|---|---|
| Sorting | `O(n log n)` |
| Selection scan | `O(n)` |
| Total | `O(n log n)` |

If already sorted by finish time:

```text
O(n)
```

---

## Dry Run

Activities:

```text
(1,4), (3,5), (0,6), (5,7), (8,9), (5,9)
```

Sorted by finish:

```text
(1,4), (3,5), (0,6), (5,7), (8,9), (5,9)
```

Select:

```text
(1,4) → select
(3,5) → reject
(0,6) → reject
(5,7) → select
(8,9) → select
(5,9) → reject
```

Answer:

```text
(1,4), (5,7), (8,9)
```

---

## Exam Perspective

Common questions:

- Write activity selection algorithm.
- Apply on given start/finish times.
- Prove/explain greedy choice.
- Analyze complexity.

---

## Common Mistake

Do not sort by start time or duration. The correct greedy rule is earliest finish time.
