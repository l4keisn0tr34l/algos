# DAA Syllabus Checklist

Use this file to track what you have covered.

## How to mark ticks in Markdown

Unchecked item:

```md
- [ ] Topic name
```

Checked item:

```md
- [x] Topic name
```

So change:

```md
- [ ] Binary Search
```

to:

```md
- [x] Binary Search
```

---

# Unit I — Algorithm Analysis

## Basics

- [x] Concept of algorithmic efficiency
- [x] Runtime analysis of algorithms
- [x] Operation counting from code
- [ ] Best case analysis
- [ ] Average case analysis
- [x] Worst case analysis

## Asymptotic Notations

- [x] Big-O notation
- [ ] Big-Omega notation
- [ ] Big-Theta notation
- [ ] Difference between `O`, `Ω`, and `Θ`

## Growth of Functions

- [ ] Compare common growth rates
- [ ] `1`
- [ ] `log n`
- [ ] `n`
- [ ] `n log n`
- [ ] `n²`
- [ ] `n³`
- [ ] `2ⁿ`
- [ ] `n!`

## Recurrences

- [x] Form recurrence relations from recursive algorithms
- [x] Expansion / substitution method
- [ ] Recursion tree method
- [x] Master theorem
- [ ] Runtime analysis of divide-and-conquer algorithms
- [ ] Mixed recurrence practice

---

# Unit II — Searching, Sorting, Divide and Conquer, Graph Basics

## Divide and Conquer

- [ ] Structure of divide-and-conquer algorithms
- [ ] Divide, conquer, combine idea
- [ ] Writing recurrence for divide-and-conquer algorithms

## Binary Search

- [x] Binary Search intuition
- [x] Binary Search dry run
- [x] Binary Search pseudocode
- [x] Binary Search implementation
- [x] Binary Search complexity

## Binary Search PYQ Variants

- [x] First `1` in sorted binary array
- [x] Search in rotated sorted array
- [x] Fixed point problem: `A[i] = i`

## Merge Sort
- [x] Merge Sort intuition
- [x] Merge Sort dry run
- [ ] Merge algorithm
- [ ] Merge Sort pseudocode
- [x] Merge Sort implementation
- [x] Merge Sort recurrence: `T(n) = 2T(n/2) + n`
- [x] Merge Sort complexity

## Inversion Count

- [ ] Definition of inversion
- [ ] Brute force inversion count
- [ ] Merge-sort-based inversion count
- [ ] Inversion count implementation
- [ ] Inversion count complexity

## Quick Sort

- [ ] Quick Sort intuition
- [ ] Partition algorithm
- [ ] Quick Sort dry run
- [ ] Quick Sort pseudocode
- [ ] Quick Sort implementation
- [ ] Best case complexity
- [ ] Average case complexity
- [ ] Worst case complexity
- [ ] Randomized Quick Sort idea

## Heap and Heap Sort

- [ ] Heap definition
- [ ] Max heap
- [ ] Min heap
- [ ] Array representation of heap
- [ ] Max-Heapify
- [ ] Build Max Heap
- [ ] Insert in heap
- [ ] Delete max
- [ ] Heap Sort
- [ ] Heap Sort implementation
- [ ] Heap Sort complexity

## Strassen Matrix Multiplication

- [ ] Normal matrix multiplication complexity
- [ ] Strassen idea
- [ ] 7 Strassen products
- [ ] Final matrix combinations
- [ ] Strassen recurrence: `T(n) = 7T(n/2) + O(n²)`
- [ ] Strassen complexity: `O(n^2.807)`

## Graph Basics

- [ ] Graph terminology
- [ ] Directed vs undirected graph
- [ ] Weighted vs unweighted graph
- [ ] Adjacency matrix
- [ ] Adjacency list
- [ ] Matrix vs list comparison

## BFS and DFS

- [ ] BFS intuition
- [ ] BFS algorithm
- [ ] BFS implementation
- [ ] BFS complexity
- [ ] DFS intuition
- [ ] DFS algorithm
- [ ] DFS implementation
- [ ] DFS complexity
- [ ] BFS vs DFS comparison

## Connected Components

- [ ] Connected component definition
- [ ] Connected components using DFS/BFS
- [ ] Connected components implementation
- [ ] Connected components complexity

## DFS Edge Classification

- [ ] Tree edge
- [ ] Back edge
- [ ] Forward edge
- [ ] Cross edge
- [ ] DFS edge classification algorithm

## Articulation Points / Cut Vertices

- [ ] Cut vertex definition
- [ ] Discovery time and low value
- [ ] Root condition
- [ ] Non-root condition: `low[child] >= disc[u]`
- [ ] Articulation point algorithm
- [ ] Articulation point implementation

## Bridges

- [ ] Bridge definition
- [ ] Discovery time and low value
- [ ] Bridge condition: `low[v] > disc[u]`
- [ ] Bridge algorithm
- [ ] Bridge implementation
- [ ] Articulation point vs bridge comparison

---

# Unit III — Greedy and Graph Algorithms

## Greedy Method

- [ ] Greedy algorithm definition
- [ ] Greedy choice property
- [ ] Optimal substructure
- [ ] When greedy works
- [ ] When greedy fails
- [ ] Greedy vs divide-and-conquer
- [ ] Greedy vs dynamic programming

## Activity Selection

- [ ] Activity selection problem statement
- [ ] Greedy rule: earliest finish time
- [ ] Activity selection algorithm
- [ ] Activity selection implementation
- [ ] Activity selection complexity
- [ ] Activity selection dry run

## Fractional Knapsack

- [ ] Fractional knapsack problem statement
- [ ] Greedy rule: highest value/weight ratio
- [ ] Fractional knapsack algorithm
- [ ] Fractional knapsack implementation
- [ ] Fractional knapsack complexity
- [ ] Fractional vs 0/1 knapsack comparison

## Huffman Coding

- [ ] Huffman coding problem statement
- [ ] Prefix-free codes
- [ ] Greedy rule: merge two minimum frequencies
- [ ] Huffman tree construction
- [ ] Huffman coding algorithm
- [ ] Huffman coding implementation
- [ ] Assigning binary codes
- [ ] Average code length calculation
- [ ] Fixed-length vs Huffman coding comparison

## Minimum Spanning Tree Basics

- [ ] Spanning tree definition
- [ ] MST definition
- [ ] MST properties
- [ ] Cut property
- [ ] Cycle property
- [ ] MST vs shortest path tree

## Disjoint Set Union / Union-Find

- [ ] DSU purpose
- [ ] Make Set
- [ ] Find operation
- [ ] Path compression
- [ ] Union operation
- [ ] Union by rank / size
- [ ] DSU implementation
- [ ] DSU amortized complexity

## Kruskal's Algorithm

- [ ] Kruskal problem statement
- [ ] Greedy rule: smallest safe edge
- [ ] Sorting edges
- [ ] Cycle detection using DSU
- [ ] Kruskal algorithm
- [ ] Kruskal implementation
- [ ] Kruskal dry run
- [ ] Kruskal complexity

## Prim's Algorithm

- [ ] Prim problem statement
- [ ] Greedy rule: smallest edge from current tree to outside vertex
- [ ] Prim algorithm
- [ ] Prim implementation using heap
- [ ] Prim dry run
- [ ] Prim complexity with heap
- [ ] Prim complexity with adjacency matrix

## Shortest Path Basics

- [ ] Single-source shortest path definition
- [ ] Relaxation
- [ ] Negative edge
- [ ] Negative cycle
- [ ] Shortest path vs MST

## Dijkstra's Algorithm

- [ ] Dijkstra problem statement
- [ ] Non-negative edge requirement
- [ ] Greedy rule: nearest unvisited vertex
- [ ] Dijkstra algorithm
- [ ] Dijkstra implementation
- [ ] Dijkstra dry run table
- [ ] Dijkstra complexity
- [ ] Why Dijkstra fails with negative edges

## Bellman-Ford Algorithm

- [ ] Bellman-Ford problem statement
- [ ] Relax all edges `V-1` times
- [ ] Bellman-Ford algorithm
- [ ] Bellman-Ford implementation
- [ ] Bellman-Ford dry run table
- [ ] Negative cycle detection
- [ ] Bellman-Ford complexity

## Comparisons

- [ ] Kruskal vs Prim
- [ ] Dijkstra vs Bellman-Ford
- [ ] MST vs shortest path tree
- [ ] Fractional vs 0/1 knapsack
- [ ] Greedy vs divide-and-conquer

## PYQ Greedy Patterns

- [ ] Greedy correctness / counterexample question
- [ ] Minimum gas stops problem
- [ ] CD/song packing in given order
- [ ] Writing greedy choice and optimal substructure in answers

---

# Practical Coding Checklist

## Unit II Python Practice

- [ ] Binary Search
- [ ] First 1 in sorted binary array
- [ ] Search in rotated sorted array
- [ ] Fixed Point
- [ ] Merge Sort
- [ ] Inversion Count
- [ ] Quick Sort
- [ ] Heap Sort
- [ ] Heap Insert/Delete-Max
- [ ] Graph Representations
- [ ] BFS
- [ ] DFS
- [ ] Connected Components
- [ ] DFS Edge Classification
- [ ] Articulation Points
- [ ] Bridges

## Unit III Python Practice

- [ ] Activity Selection
- [ ] Fractional Knapsack
- [ ] Huffman Coding
- [ ] Disjoint Set Union
- [ ] Kruskal MST
- [ ] Prim MST
- [ ] Dijkstra
- [ ] Bellman-Ford
- [ ] Minimum Gas Stops
- [ ] Minimum CDs
