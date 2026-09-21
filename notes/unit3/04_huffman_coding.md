# 04 — Huffman Coding

## Problem

Given characters and their frequencies, construct variable-length prefix codes such that average code length is minimized.

High-frequency characters should get shorter codes.

---

## Greedy Choice

Repeatedly merge the two nodes with lowest frequencies.

---

## Algorithm / Pseudocode

```text
Huffman(characters, frequencies):
    create a min-priority queue Q

    for each character c:
        create leaf node for c
        insert node into Q using frequency as key

    while Q has more than one node:
        x = ExtractMin(Q)
        y = ExtractMin(Q)

        z = new internal node
        z.freq = x.freq + y.freq
        z.left = x
        z.right = y

        insert z into Q

    return ExtractMin(Q) as root of Huffman tree
```

Assign:

```text
left edge  = 0
right edge = 1
```

Code of a character is path from root to leaf.

---

## Complexity

For `n` characters:

```text
O(n log n)
```

Because there are `n-1` merge operations and priority queue operations cost `O(log n)`.

---

## Average Code Length

If frequency counts are given:

```text
Average code length = Σ(freq[i] × codeLength[i]) / Σ(freq[i])
```

If probabilities are given:

```text
Average code length = Σ(prob[i] × codeLength[i])
```

---

## Dry Run Pattern

For frequencies:

```text
a: 5, b: 9, c: 12, d: 13, e: 16, f: 45
```

Merge smallest repeatedly:

```text
5 + 9 = 14
12 + 13 = 25
14 + 16 = 30
25 + 30 = 55
45 + 55 = 100
```

Then assign 0/1 along tree edges to get codes.

Note: Codes may differ depending on left/right choice, but total cost remains same.

---

## Exam Perspective

Very important PYQ topic.

Common questions:

- Build Huffman tree.
- Assign binary codes.
- Compute average code length.
- Compare with fixed-length encoding.
- Write algorithm and complexity.

---

## Common Mistakes

- Merging largest frequencies instead of smallest.
- Forgetting prefix-free property.
- Thinking Huffman codes are unique. They are not necessarily unique.
