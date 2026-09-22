# DAA Practice Sets by Unit / Topic

Use this to know:

- what kind of questions to practice
- where you must memorize/write algorithms
- where you only need concepts/comparisons
- where numerical/dry-run practice is important

Legend:

```text
[A] = Memorize algorithm/pseudocode
[D] = Practice dry run / tracing
[N] = Numerical / recurrence / table question
[T] = Theory / definition / comparison
[C] = Coding practice useful
```

---

# Unit I — Algorithm Analysis

## 1. Runtime Analysis / Operation Counting

### Practice Questions

1. Find complexity of single loop, nested loop, and dependent nested loop. `[N]`
2. Find complexity of loops where variable doubles/halves. `[N]`
3. Find complexity of code with two separate loops. `[N]`
4. Find best/worst case of linear search. `[T/N]`

### Need to memorize algorithm?

No. Focus on solving complexity questions.

---

## 2. Asymptotic Notations

### Practice Questions

1. Define Big-O, Big-Omega, Big-Theta. `[T]`
2. Prove or disprove: `3n² + 5n + 2 = O(n²)`. `[N]`
3. Compare growth rates: `log n`, `n`, `n log n`, `n²`, `2ⁿ`, `n!`. `[T/N]`
4. Difference between `O`, `Ω`, and `Θ`. `[T]`

### Need to memorize?

Yes, memorize definitions.

---

## 3. Recurrences

### Practice Questions

1. Form recurrence from recursive code. `[N]`
2. Solve `T(n) = T(n-1) + n`. `[N]`
3. Solve `T(n) = T(n/2) + n`. `[N]`
4. Solve `T(n) = 2T(n/2) + n` using recursion tree. `[N]`
5. Solve Master Theorem examples. `[N]`
6. Identify when Master Theorem cannot apply. `[T/N]`

### Need to memorize?

Memorize Master Theorem cases and recursion tree format.

---

# Unit II — Searching, Sorting, Divide and Conquer, Graph Basics

## 1. Divide and Conquer

### Practice Questions

1. Explain divide, conquer, combine. `[T]`
2. Write recurrence for an algorithm with 2 subproblems of size `n/2` and `n` combine work. `[N]`
3. Give examples of divide-and-conquer algorithms. `[T]`

### Need to memorize algorithm?

No specific algorithm, but memorize the structure.

---

## 2. Binary Search

### Practice Questions

1. Write iterative binary search algorithm. `[A]`
2. Write recursive binary search algorithm. `[A]`
3. Apply binary search on a given sorted array. `[D]`
4. Derive recurrence `T(n)=T(n/2)+1`. `[N]`

### Must memorize pseudocode?

Yes.

---

## 3. Binary Search Variants

### Practice Questions

1. Find first `1` in sorted binary array. `[A/D]`
2. Search in rotated sorted array. `[A/D]`
3. Find fixed point `A[i] = i`. `[A/D]`

### Must memorize pseudocode?

Yes, especially first `1` and rotated sorted array.

---

## 4. Merge Sort

### Practice Questions

1. Write Merge Sort algorithm. `[A]`
2. Write Merge helper function. `[A]`
3. Apply Merge Sort on an array. `[D]`
4. Derive recurrence and complexity. `[N]`
5. Explain why Merge Sort needs `O(n)` space. `[T]`

### Must memorize pseudocode?

Yes. Memorize both `MergeSort` and `Merge`.

---

## 5. Inversion Count

### Practice Questions

1. Define inversion. `[T]`
2. Count inversions manually for small array. `[D/N]`
3. Write merge-sort-based inversion count algorithm. `[A]`
4. Explain why `mid - i + 1` inversions are added. `[T/N]`

### Must memorize pseudocode?

Yes, if PYQ asks divide-and-conquer inversion count.

---

## 6. Quick Sort

### Practice Questions

1. Write Quick Sort algorithm. `[A]`
2. Write Partition algorithm. `[A]`
3. Apply Quick Sort on given array. `[D]`
4. Derive worst-case recurrence. `[N]`
5. Explain best, average, worst case. `[T/N]`
6. Explain randomized Quick Sort. `[T]`

### Must memorize pseudocode?

Yes. Very important.

---

## 7. Heap and Heap Sort

### Practice Questions

1. Convert array into max heap. `[D]`
2. Write MaxHeapify. `[A]`
3. Write BuildMaxHeap. `[A]`
4. Write HeapSort. `[A]`
5. Perform delete-max and insert. `[D/A]`
6. Explain why BuildHeap is `O(n)`. `[T]`

### Must memorize pseudocode?

Yes: `MaxHeapify`, `BuildMaxHeap`, `HeapSort`.

---

## 8. Strassen Matrix Multiplication

### Practice Questions

1. Write Strassen recurrence. `[N]`
2. State why Strassen is faster than normal multiplication. `[T]`
3. Write 7 products and final matrix combinations. `[A/T]`
4. Solve complexity using Master Theorem. `[N]`

### Must memorize pseudocode?

Not full code, but memorize recurrence and preferably formulas.

---

## 9. Graph Representations

### Practice Questions

1. Convert graph to adjacency matrix. `[D]`
2. Convert graph to adjacency list. `[D]`
3. Compare matrix vs list. `[T]`
4. Build graph representation from edge list. `[C]`

### Must memorize algorithm?

Basic construction only.

---

## 10. BFS and DFS

### Practice Questions

1. Write BFS algorithm. `[A]`
2. Write DFS algorithm. `[A]`
3. Apply BFS on graph. `[D]`
4. Apply DFS on graph. `[D]`
5. Compare BFS and DFS. `[T]`
6. Explain why BFS gives shortest path in unweighted graph. `[T]`

### Must memorize pseudocode?

Yes.

---

## 11. Connected Components

### Practice Questions

1. Define connected component. `[T]`
2. Find components in graph. `[D]`
3. Write DFS/BFS algorithm to count components. `[A]`

### Must memorize algorithm?

Yes, short DFS-based algorithm.

---

## 12. DFS Edge Classification

### Practice Questions

1. Define tree, back, forward, cross edge. `[T]`
2. Classify edges in a DFS traversal. `[D]`
3. Which edge indicates cycle? `[T]`

### Must memorize algorithm?

Mostly definitions; algorithm optional.

---

## 13. Articulation Points / Cut Vertices

### Practice Questions

1. Define cut vertex/articulation point. `[T]`
2. Find articulation points in graph. `[D]`
3. Explain `disc[]` and `low[]`. `[T]`
4. Write DFS condition for articulation point. `[A/T]`
5. Compare articulation point and bridge. `[T]`

### Must memorize algorithm?

Memorize conditions. Full pseudocode if aiming high.

---

## 14. Bridges

### Practice Questions

1. Define bridge. `[T]`
2. Find bridges in graph. `[D]`
3. Explain bridge condition `low[v] > disc[u]`. `[T]`
4. Compare with articulation point. `[T]`

### Must memorize algorithm?

Memorize condition. Full pseudocode useful.

---

# Unit III — Greedy and Graph Algorithms

## 1. Greedy Method

### Practice Questions

1. Define greedy method. `[T]`
2. Explain greedy choice property. `[T]`
3. Explain optimal substructure. `[T]`
4. Does greedy always give optimal solution? Justify. `[T]`
5. Give example where greedy fails. `[T]`

### Must memorize algorithm?

No. Memorize definitions and examples.

---

## 2. Activity Selection

### Practice Questions

1. Write activity selection algorithm. `[A]`
2. Apply on start/finish time table. `[D]`
3. Explain why earliest finish time works. `[T]`
4. Analyze complexity. `[T]`

### Must memorize pseudocode?

Yes.

---

## 3. Fractional Knapsack

### Practice Questions

1. Solve numerical fractional knapsack. `[D/N]`
2. Write algorithm. `[A]`
3. Sort by value/weight ratio. `[D]`
4. Compare fractional and 0/1 knapsack. `[T]`

### Must memorize pseudocode?

Yes.

---

## 4. Huffman Coding

### Practice Questions

1. Build Huffman tree from frequencies. `[D]`
2. Assign binary codes. `[D]`
3. Compute average code length. `[N]`
4. Compare Huffman with fixed-length encoding. `[T/N]`
5. Write Huffman algorithm. `[A]`

### Must memorize pseudocode?

Yes. Very important.

---

## 5. Minimum Spanning Tree Basics

### Practice Questions

1. Define spanning tree. `[T]`
2. Define MST. `[T]`
3. State properties of MST. `[T]`
4. Explain cut property. `[T]`
5. Compare MST and shortest path tree. `[T]`

### Must memorize algorithm?

No, but memorize definitions/properties.

---

## 6. Disjoint Set Union

### Practice Questions

1. Write MakeSet, Find, Union. `[A]`
2. Explain path compression. `[T]`
3. Explain union by rank. `[T]`
4. Use DSU to detect cycle. `[D/T]`

### Must memorize pseudocode?

Yes, especially for Kruskal.

---

## 7. Kruskal's Algorithm

### Practice Questions

1. Write Kruskal algorithm. `[A]`
2. Write DSU helpers. `[A]`
3. Apply Kruskal on weighted graph. `[D]`
4. Show selected/rejected edges. `[D]`
5. Analyze complexity. `[T]`

### Must memorize pseudocode?

Yes. Very important.

---

## 8. Prim's Algorithm

### Practice Questions

1. Write Prim algorithm. `[A]`
2. Apply Prim from given source. `[D]`
3. Show MST construction step by step. `[D]`
4. Analyze complexity using heap and matrix. `[T]`
5. Explain greedy choice. `[T]`

### Must memorize pseudocode?

Yes. Very important.

---

## 9. Shortest Path Basics

### Practice Questions

1. Define single-source shortest path. `[T]`
2. Explain relaxation. `[T]`
3. Explain negative edge and negative cycle. `[T]`
4. Compare shortest path with MST. `[T]`

### Must memorize algorithm?

No, but relaxation formula is essential.

---

## 10. Dijkstra's Algorithm

### Practice Questions

1. Write Dijkstra algorithm. `[A]`
2. Apply on graph using distance table. `[D]`
3. Explain why negative edges are not allowed. `[T]`
4. Analyze complexity. `[T]`
5. Reconstruct shortest path using parent array. `[D]`

### Must memorize pseudocode?

Yes. Very important.

---

## 11. Bellman-Ford Algorithm

### Practice Questions

1. Write Bellman-Ford algorithm. `[A]`
2. Apply relaxations on graph. `[D]`
3. Detect negative cycle. `[D/T]`
4. Compare with Dijkstra. `[T]`
5. Analyze complexity. `[T]`

### Must memorize pseudocode?

Yes.

---

## 12. Greedy PYQ Patterns

### Practice Questions

1. Minimum gas stops problem. `[A/D]`
2. CD/song packing in given order. `[A/D]`
3. Optimal merge pattern. `[A/D]`
4. Greedy always optimal? True/false. `[T]`

### Must memorize pseudocode?

Memorize greedy rule and simple algorithm.

---

# Lab / Extra Important Practice

## 1. Iterative Merge Sort

### Practice Questions

1. Write bottom-up merge sort. `[A/C]`
2. Compare recursive and iterative merge sort. `[T]`

### Memorize?

Only if lab exam asks implementation.

---

## 2. Random Weighted Graph Generator

### Practice Questions

1. Generate `e = d × n(n-1)/2` edges. `[C]`
2. Avoid duplicate edges and self-loops. `[C]`
3. Store in adjacency matrix and list. `[C]`

### Memorize?

Understand steps; no need for exam pseudocode unless lab.

---

## 3. MinHeap Priority Queue

### Practice Questions

1. Insert in MinHeap. `[A/C]`
2. Extract minimum. `[A/C]`
3. Heapify up/down. `[A/C]`

### Memorize?

Yes for lab and useful for Huffman/Prim/Dijkstra.

---

## 4. 0/1 Knapsack DP

### Practice Questions

1. Fill DP table. `[N]`
2. Write recurrence. `[A/T]`
3. Display `C[][]` and `Keep[][]`. `[D/C]`
4. Trace selected items. `[D]`

### Memorize?

For lab yes. For current Units I–III, lower priority.

---

## 5. LCS DP

### Practice Questions

1. Fill LCS table. `[N]`
2. Write recurrence. `[A/T]`
3. Trace final LCS. `[D]`

### Memorize?

For lab yes. For current Units I–III, lower priority.

---

# Highest Priority Algorithms to Memorize

## Unit II

```text
Binary Search
First 1 in binary array
Rotated sorted array search
Merge Sort + Merge
Inversion Count + MergeAndCount
Quick Sort + Partition
MaxHeapify + BuildMaxHeap + HeapSort
BFS
DFS
Connected Components
Articulation Point condition
Bridge condition
```

## Unit III

```text
Activity Selection
Fractional Knapsack
Huffman Coding + GenerateCodes
DSU: MakeSet, Find, Union
Kruskal
Prim
Dijkstra
Bellman-Ford
Optimal Merge Pattern
```

---

# Highest Priority Dry Runs / Numericals

```text
Merge Sort on array
Quick Sort partition trace
Heap Sort trace
Huffman tree + average code length
Fractional Knapsack table
Kruskal edge selection
Prim MST construction
Dijkstra distance table
Bellman-Ford relaxation table
Recursion tree for T(n)=2T(n/2)+n
Master theorem examples
```

---

# Highest Priority Theory Comparisons

```text
O vs Ω vs Θ
Merge Sort vs Quick Sort
Merge Sort vs Heap Sort
BFS vs DFS
Articulation Point vs Bridge
Kruskal vs Prim
Dijkstra vs Bellman-Ford
MST vs Shortest Path Tree
Fractional vs 0/1 Knapsack
Greedy vs Divide-and-Conquer
```
