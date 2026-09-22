# 07 — Huffman Coding

## Problem

Given characters and frequencies, assign binary prefix codes with minimum average code length.

## Idea

Repeatedly combine two minimum-frequency nodes.

## Algorithm

```text
Huffman(chars, freq):
    create min heap of leaf nodes

    while heap has more than one node:
        x = extract minimum
        y = extract minimum
        z = new node with freq = x.freq + y.freq
        z.left = x
        z.right = y
        insert z into heap

    root = remaining node
    GenerateCodes(root, "")
```

## Helper

```text
GenerateCodes(node, code):
    if node is leaf:
        print character and code
    else:
        GenerateCodes(node.left, code + "0")
        GenerateCodes(node.right, code + "1")
```

## Complexity

```text
O(n log n)
```
