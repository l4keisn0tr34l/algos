# 13 — Greedy PYQ Patterns

These are extra PYQ-style greedy problems seen in previous papers.

---

## 1. Minimum Gas Stops Problem

### Problem

You travel along a road. Full tank lets you travel at most `m` distance. Given gas station positions, minimize number of stops.

### Greedy Choice

Go as far as possible before stopping.

### Algorithm

```text
MinStops(stations, m):
    stops = []
    current = start

    while destination not reachable:
        choose farthest station reachable from current
        if no station reachable:
            return impossible
        stop there
        current = chosen station

    return stops
```

### Complexity

```text
O(n)
```

---

## 2. CD / Song Packing in Given Order

### Problem

Songs must be stored in given order. Each CD has capacity `m`. Minimize number of CDs.

### Greedy Choice

Put as many consecutive songs as possible on current CD, then move to next CD.

### Algorithm

```text
MinCDs(songs, m):
    cds = 1
    remaining = m

    for song in songs:
        if song > m:
            return impossible

        if song <= remaining:
            remaining -= song
        else:
            cds += 1
            remaining = m - song

    return cds
```

### Complexity

```text
O(n)
```

---

## 3. Greedy Does Not Always Work

PYQ asks:

> Greedy approach guarantees optimal solution. True or false?

Answer:

```text
False
```

Reason: A locally optimal choice may block the globally optimal solution.

Examples:

- 0/1 Knapsack
- Travelling Salesman Problem
- Arbitrary coin change

---

## Exam Tip

For greedy PYQ proofs, mention:

```text
1. Greedy choice property
2. Optimal substructure
3. Exchange argument, if needed
```
