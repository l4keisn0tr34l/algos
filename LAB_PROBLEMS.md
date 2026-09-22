# DAA Lab Problems Checklist

These are the lab assignments shared in class.

## Assignment 1 — Execution Time Measurement

- [ ] Learn how to measure execution time of a program
- [ ] Use time/date related libraries in C/C++
- [ ] Run same algorithm on different input sizes
- [ ] Record and compare execution time

**Topic mapping:** Unit I — runtime analysis / algorithmic efficiency

---

## Assignment 2 — Iterative Merge Sort

- [ ] Understand recursive Merge Sort
- [ ] Understand bottom-up / iterative Merge Sort
- [ ] Implement iterative Merge Sort
- [ ] Test on different arrays
- [ ] Analyze complexity

**Topic mapping:** Unit II — Merge Sort / Divide and Conquer

---

## Assignment 3 — Random Weighted Graph Generator

Design an algorithm to randomly generate a weighted, undirected, simple graph.

Given:

```text
n = number of vertices
d = density percentage
```

Maximum possible edges in undirected simple graph:

```text
n(n - 1) / 2
```

Number of edges to generate:

```text
e = d × n(n - 1) / 2
```

Requirements:

- [ ] Randomly generate `e` unique undirected edges
- [ ] No self-loops
- [ ] No duplicate edges
- [ ] Assign random weight to each edge in range `1...e`
- [ ] Store graph as adjacency matrix
- [ ] Store graph as adjacency list

**Topic mapping:** Unit II — graph representation

---

## Assignment 4 — Priority Queue using Min Heap

- [ ] Implement MinHeap
- [ ] Insert element
- [ ] Extract minimum
- [ ] Get minimum
- [ ] Heapify up
- [ ] Heapify down
- [ ] Use it as a priority queue

**Topic mapping:** Unit II / III — Heap, Prim, Dijkstra, Huffman

---

## Assignment 5 — MST Algorithms

Implement:

- [ ] Kruskal's Algorithm
- [ ] Prim's Algorithm

For Kruskal:

- [ ] Sort edges by weight
- [ ] Implement DSU / Union-Find
- [ ] Implement `Find`
- [ ] Implement `Union`
- [ ] Select edges without forming cycle

For Prim:

- [ ] Use adjacency list
- [ ] Use min-priority queue
- [ ] Select minimum edge from current tree to unvisited vertex

**Topic mapping:** Unit III — MST

---

## Assignment 6 — Dijkstra Single Source Shortest Path

- [ ] Implement Dijkstra's algorithm
- [ ] Use graph adjacency list or matrix
- [ ] Maintain distance array
- [ ] Use relaxation
- [ ] Use priority queue if required
- [ ] Print shortest distances from source

**Topic mapping:** Unit III — shortest path

---

## Assignment 7 — Huffman Coding

- [ ] Build min heap of characters/frequencies
- [ ] Repeatedly merge two minimum frequency nodes
- [ ] Build Huffman tree
- [ ] Generate binary codes
- [ ] Display codes
- [ ] Compute average code length if required

**Topic mapping:** Unit III — greedy / Huffman coding

---

## Assignment 8 — Optimal Merge Pattern

- [ ] Given file sizes, repeatedly merge two smallest files
- [ ] Add merge cost to total cost
- [ ] Insert merged file size back into min heap
- [ ] Continue until one file remains

**Topic mapping:** Greedy + min heap. This is not in the listed Unit III syllabus, but appears in lab.

---

## Assignment 9 — Fractional Knapsack

- [ ] Compute value/weight ratio
- [ ] Sort items by decreasing ratio
- [ ] Take full item if possible
- [ ] Take fractional part if remaining capacity is smaller
- [ ] Compute maximum profit

**Topic mapping:** Unit III — greedy / knapsack

---

## Assignment 10 — 0/1 Knapsack using Dynamic Programming

Requirements:

- [ ] Implement 0/1 Knapsack using DP
- [ ] Display `C[][]` table
- [ ] Display `Keep[][]` table
- [ ] Display final selected items and maximum profit

**Topic mapping:** Unit IV — Dynamic Programming, but lab includes it.

---

## Assignment 11 — Longest Common Subsequence using Dynamic Programming

Requirements:

- [ ] Implement LCS using DP
- [ ] Display all constructed tables
- [ ] Display final LCS length
- [ ] Display one final LCS string

**Topic mapping:** Unit IV — Dynamic Programming, but lab includes it.

---

# Priority for Current Study

Since we are currently focusing on Units II and III, prioritize:

1. Iterative Merge Sort
2. Random weighted graph generator
3. MinHeap priority queue
4. Kruskal and Prim
5. Dijkstra
6. Huffman Coding
7. Optimal Merge Pattern
8. Fractional Knapsack

Then later do DP labs:

9. 0/1 Knapsack
10. LCS
