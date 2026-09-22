# PYQ Topic Index — What to Refer Where

This is a topic-wise index for using `pyqs/pyqs.pdf` along with our notes.

> Note: the PYQ PDF is scanned, so exact text search may not work. Page references below are approximate based on visual inspection of the PDF pages.

---

# Quick Navigation

## Main files to use

```text
pyqs/pyqs.pdf                     # original PYQ PDF
PYQ_POPULAR_SOLVED.md             # common PYQs with solutions
PYQ_DIFFICULT_ONCE_OVER.md        # tricky one-time revision sheet
PRACTICE_SETS_BY_TOPIC.md         # what to practice topic-wise
PRACTICE_SETS_SOLUTIONS.md        # compact solution templates
SYLLABUS_CHECKLIST.md             # ticklist for syllabus coverage
LAB_PROBLEMS.md                   # lab assignment checklist
```

## Notes folders

```text
notes/unit1/
notes/unit2/
notes/unit3/
```

## Practice folders

```text
python/unit2/problems/
python/unit2/solutions/
python/unit3/problems/
python/unit3/solutions/
lab/how_to_solve/
lab/implementations/
```

---

# Unit I — Analysis and Recurrences

## Asymptotic Notations

### PYQ PDF reference

Approx pages:

```text
page 2, page 43-ish
```

### What PYQs ask

- Define Big-O, Big-Omega, Big-Theta.
- Compare notations.
- RAM model may appear as short note.

### Refer notes

```text
PYQ_POPULAR_SOLVED.md
PRACTICE_SETS_BY_TOPIC.md
PRACTICE_SETS_SOLUTIONS.md
SYLLABUS_CHECKLIST.md
```

### What to memorize

```text
Formal definitions of O, Ω, Θ
Difference between upper, lower, tight bound
Common growth order
```

---

## Master Theorem

### PYQ PDF reference

Approx pages:

```text
page 3, pages 4-9, page 43-ish
```

### What PYQs ask

- Apply Master theorem to given recurrences.
- Identify cases.
- Sometimes use extended case with logs.

### Refer notes

```text
notes/unit1/02_masters_theorem.md
PYQ_DIFFICULT_ONCE_OVER.md
PRACTICE_SETS_SOLUTIONS.md
```

### What to memorize

```text
T(n) = aT(n/b) + f(n)
Compare f(n) with n^(log_b a)
Case 1, Case 2, Case 3
```

---

## Recursion Tree Method

### PYQ PDF reference

Approx pages:

```text
page 10, page 11, page 12
```

### What PYQs ask

- Solve recurrence using recursion tree.
- Show each level cost.
- Sometimes unequal recurrence like `T(n/3) + T(2n/3) + n`.

### Refer notes

```text
notes/unit1/01_recurrences.md
PYQ_DIFFICULT_ONCE_OVER.md
```

### What to practice

```text
T(n) = 2T(n/2) + n
T(n) = T(n/2) + n
T(n) = T(n/3) + T(2n/3) + n
```

---

# Unit II — Searching, Sorting, Divide and Conquer, Graph Basics

## Divide and Conquer Basics

### PYQ PDF reference

Approx pages:

```text
pages 13-19
```

### What PYQs ask

- Explain divide-and-conquer strategy.
- Derive recurrence from problem statement.
- Apply D&C to min/max.

### Refer notes

```text
notes/unit2/01_divide_and_conquer.md
PRACTICE_SETS_BY_TOPIC.md
```

---

## Binary Search + Variants

### PYQ PDF reference

Approx pages:

```text
pages 16, 18, 19
```

### What PYQs ask

- Recursive binary search.
- First `1` in sorted binary array.
- Search in circularly shifted / rotated sorted array.
- Fixed point `A[i] = i`.

### Refer notes

```text
notes/unit2/02_binary_search.md
notes/unit2/03_binary_search_variants.md
python/unit2/problems/01_binary_search.py
python/unit2/problems/02_first_one_binary_array.py
python/unit2/problems/03_search_rotated_sorted_array.py
python/unit2/problems/04_fixed_point.py
```

### What to memorize

```text
Binary Search pseudocode
FirstOne pseudocode
Rotated sorted array logic
Fixed point logic
```

---

## Merge Sort

### PYQ PDF reference

Approx pages:

```text
page 44, pages 13-18
```

### What PYQs ask

- Write Merge Sort algorithm.
- Write Merge helper.
- Apply on an array.
- Analyze recurrence.
- Lab: iterative Merge Sort.

### Refer notes

```text
notes/unit2/04_merge_sort.md
lab/how_to_solve/02_iterative_merge_sort.md
lab/implementations/02_iterative_merge_sort.py
python/unit2/problems/05_merge_sort.py
```

### What to memorize

```text
MergeSort
Merge helper
T(n) = 2T(n/2) + n = O(n log n)
```

---

## Inversion Count

### PYQ PDF reference

Approx pages:

```text
page 17
```

### What PYQs ask

- Count inversions using divide and conquer.
- Explain modified merge step.

### Refer notes

```text
notes/unit2/05_inversion_count.md
python/unit2/problems/06_inversion_count.py
PYQ_DIFFICULT_ONCE_OVER.md
```

### What to memorize

```text
If left[i] > right[j], add mid - i + 1 inversions
```

---

## Quick Sort

### PYQ PDF reference

Approx pages:

```text
pages 13, 14, 44
```

### What PYQs ask

- Write Quick Sort algorithm.
- Write Partition.
- Apply on given array.
- Derive best and worst case.
- Randomized Quick Sort may appear.

### Refer notes

```text
notes/unit2/06_quick_sort.md
python/unit2/problems/07_quick_sort.py
PYQ_POPULAR_SOLVED.md
```

### What to memorize

```text
QuickSort
Partition
Worst case recurrence T(n)=T(n-1)+n
Best case recurrence T(n)=2T(n/2)+n
```

---

## Heap / Heap Sort

### PYQ PDF reference

Approx pages:

```text
page 20, page 21
```

### What PYQs ask

- Build max heap.
- Insert/delete max.
- Apply Heap Sort step by step.
- Write MaxHeapify, BuildMaxHeap, HeapSort.

### Refer notes

```text
notes/unit2/07_heap_and_heap_sort.md
assets/heapsort_pseudocode.png
python/unit2/problems/08_heap_sort.py
python/unit2/problems/09_heap_insert_delete_max.py
```

### What to memorize

```text
MaxHeapify
BuildMaxHeap
HeapSort
Array index formulas
```

---

## Strassen Matrix Multiplication

### PYQ PDF reference

Approx pages:

```text
page 21, page 22
```

### What PYQs ask

- Explain Strassen.
- Write 7 products.
- Write recurrence.
- Analyze complexity.

### Refer notes

```text
notes/unit2/08_strassen_matrix_multiplication.md
PYQ_DIFFICULT_ONCE_OVER.md
```

### What to memorize

```text
T(n) = 7T(n/2) + O(n²)
O(n^2.807)
7 product formulas if time allows
```

---

## Graph Representations

### PYQ PDF reference

Approx pages:

```text
Unit II graph pages appear later in the PDF; also lab assignment 3
```

### What PYQs/labs ask

- Adjacency matrix.
- Adjacency list.
- Generate graph and store both ways.

### Refer notes

```text
notes/unit2/09_graph_representations.md
lab/how_to_solve/03_random_weighted_graph.md
lab/implementations/03_random_weighted_graph.py
python/unit2/problems/10_graph_representations.py
```

---

## BFS / DFS / Connected Components

### PYQ PDF reference

Approx pages:

```text
pages around Unit II graph section, page 52-ish for DFS edge types
```

### What PYQs ask

- Write BFS/DFS algorithm.
- Apply BFS/DFS on graph.
- Count connected components.
- DFS edge classification.

### Refer notes

```text
notes/unit2/10_dfs_bfs.md
notes/unit2/11_connected_components.md
notes/unit2/12_dfs_edge_classification.md
python/unit2/problems/11_bfs.py
python/unit2/problems/12_dfs.py
python/unit2/problems/13_connected_components.py
python/unit2/problems/14_dfs_edge_classification.py
```

### What to memorize

```text
BFS queue algorithm
DFS recursive algorithm
Tree/back/forward/cross edges
```

---

## Articulation Points and Bridges

### PYQ PDF reference

Approx pages:

```text
Not very frequent in sampled PYQs, but in syllabus
```

### What can be asked

- Define cut vertex / articulation point.
- Define bridge.
- Find them in a graph.
- State DFS conditions.

### Refer notes

```text
notes/unit2/13_articulation_points.md
notes/unit2/14_bridges.md
python/unit2/problems/15_articulation_points.py
python/unit2/problems/16_bridges.py
```

### What to memorize

```text
Articulation point:
root has >1 DFS child
non-root: low[child] >= disc[u]

Bridge:
low[v] > disc[u]
```

---

# Unit III — Greedy and Graph Algorithms

## Greedy Method Theory

### PYQ PDF reference

Approx pages:

```text
page 27, page 40, page 42
```

### What PYQs ask

- Define greedy method.
- Does greedy always give optimal solution?
- Greedy choice property.
- Optimal substructure.

### Refer notes

```text
notes/unit3/01_greedy_method.md
notes/unit3/13_greedy_pyq_patterns.md
PYQ_POPULAR_SOLVED.md
```

### What to memorize

```text
Greedy choice property
Optimal substructure
Counterexample: 0/1 knapsack
```

---

## Activity Selection

### PYQ PDF reference

Approx pages:

```text
Not strongly visible in sampled pages, but syllabus topic
```

### What can be asked

- Apply activity selection.
- Write algorithm.
- Explain earliest finish time rule.

### Refer notes

```text
notes/unit3/02_activity_selection.md
python/unit3/problems/01_activity_selection.py
```

---

## Fractional Knapsack

### PYQ PDF reference

Approx pages:

```text
page 29, lab assignment 9
```

### What PYQs ask

- Write algorithm for fractional knapsack.
- Solve table numerically.
- Compare with 0/1 knapsack.

### Refer notes

```text
notes/unit3/03_fractional_knapsack.md
python/unit3/problems/02_fractional_knapsack.py
lab/how_to_solve/09_fractional_knapsack.md
```

### What to memorize

```text
Sort by value/weight ratio
Take full item if possible, otherwise fraction
```

---

## Huffman Coding

### PYQ PDF reference

Approx pages:

```text
pages 25-28, lab assignment 7
```

### What PYQs ask

- Build Huffman tree.
- Assign codes.
- Compute average code length.
- Compare with fixed-length code.

### Refer notes

```text
notes/unit3/04_huffman_coding.md
python/unit3/problems/03_huffman_coding.py
lab/how_to_solve/07_huffman_coding.md
PYQ_DIFFICULT_ONCE_OVER.md
```

### What to memorize

```text
Repeatedly merge two least frequencies
GenerateCodes helper
Average length formula
```

---

## MST Basics

### PYQ PDF reference

Approx pages:

```text
pages 30-33, lab assignment 5
```

### What PYQs ask

- Define spanning tree.
- Define MST.
- Apply Kruskal or Prim.
- Sometimes ask all spanning trees for small graph.

### Refer notes

```text
notes/unit3/05_mst_basics.md
notes/unit3/14_comparisons.md
```

---

## DSU / Union-Find

### PYQ PDF reference

Approx pages:

```text
page 41
```

### What PYQs ask

- Describe DSU.
- Write Find and Union.
- Explain path compression.
- Use in Kruskal.

### Refer notes

```text
notes/unit3/06_disjoint_set_union.md
python/unit3/problems/04_disjoint_set_union.py
```

---

## Kruskal's Algorithm

### PYQ PDF reference

Approx pages:

```text
pages 30-33, lab assignment 5
```

### What PYQs ask

- Apply Kruskal on graph.
- Sort edges.
- Show selected/rejected edges.
- Write algorithm and complexity.

### Refer notes

```text
notes/unit3/07_kruskal.md
python/unit3/problems/05_kruskal_mst.py
lab/how_to_solve/05_mst_kruskal_prim.md
```

### What to memorize

```text
Kruskal main algorithm
MakeSet
Find
Union
```

---

## Prim's Algorithm

### PYQ PDF reference

Approx pages:

```text
pages 30-34, lab assignment 5
```

### What PYQs ask

- Apply Prim from given vertex.
- Show edge choices step by step.
- Explain greedy choice and optimal substructure.

### Refer notes

```text
notes/unit3/08_prim.md
python/unit3/problems/06_prim_mst.py
lab/how_to_solve/05_mst_kruskal_prim.md
```

---

## Dijkstra's Algorithm

### PYQ PDF reference

Approx pages:

```text
pages 34-37, lab assignment 6
```

### What PYQs ask

- Write Dijkstra algorithm.
- Apply on graph from source.
- Fill distance table.
- State limitation with negative edges.

### Refer notes

```text
notes/unit3/10_dijkstra.md
python/unit3/problems/07_dijkstra.py
lab/how_to_solve/06_dijkstra.md
PYQ_DIFFICULT_ONCE_OVER.md
```

### What to memorize

```text
Relaxation
Extract min distance vertex
No negative weights
```

---

## Bellman-Ford Algorithm

### PYQ PDF reference

Approx pages:

```text
Appears in syllabus, less prominent in sampled PYQs
```

### What can be asked

- Write Bellman-Ford.
- Compare with Dijkstra.
- Detect negative cycle.

### Refer notes

```text
notes/unit3/11_bellman_ford.md
notes/unit3/12_dijkstra_vs_bellman_ford.md
python/unit3/problems/08_bellman_ford.py
```

---

## Greedy PYQ Patterns

### PYQ PDF reference

Approx pages:

```text
page 40: gas station style problem
page 42: CD/song packing problem
lab assignment 8: optimal merge pattern
```

### What PYQs ask

- Design greedy algorithm.
- State greedy choice property.
- Analyze complexity.

### Refer notes

```text
notes/unit3/13_greedy_pyq_patterns.md
python/unit3/problems/09_min_gas_stops.py
python/unit3/problems/10_min_cds.py
lab/how_to_solve/08_optimal_merge_pattern.md
```

---

# Unit IV / Lab-Only Topics Appearing in Lab and PYQs

These are outside current Units I–III focus but appear in lab/PYQ PDF.

## 0/1 Knapsack DP

### PYQ PDF reference

Approx pages:

```text
page 55, lab assignment 10
```

### Refer files

```text
lab/how_to_solve/10_01_knapsack_dp.md
lab/implementations/10_01_knapsack_dp.py
PYQ_DIFFICULT_ONCE_OVER.md
```

### Need to know

```text
C[i][w] table
Keep[i][w] table
Selected item traceback
```

---

## LCS DP

### PYQ PDF reference

Approx pages:

```text
lab assignment 11; PYQ DP section later in PDF
```

### Refer files

```text
lab/how_to_solve/11_lcs_dp.md
lab/implementations/11_lcs_dp.py
PYQ_DIFFICULT_ONCE_OVER.md
```

---

# Most Important PYQ Practice Order

If time is limited, practice in this order:

```text
1. Master Theorem examples
2. Recursion tree T(n)=2T(n/2)+n
3. Quick Sort algorithm + trace
4. Heap Sort trace
5. Merge Sort + inversion count
6. Binary Search variants
7. Huffman Coding numerical
8. Fractional Knapsack numerical
9. Kruskal trace
10. Prim trace
11. Dijkstra table
12. Bellman-Ford comparison
13. Articulation Point vs Bridge definitions/conditions
14. Strassen recurrence/formulas
```

---

# What to Memorize vs What to Practice

## Memorize algorithms

```text
Binary Search
Merge Sort + Merge
Quick Sort + Partition
MaxHeapify + HeapSort
BFS
DFS
Activity Selection
Fractional Knapsack
Huffman + GenerateCodes
DSU Find/Union
Kruskal
Prim
Dijkstra
Bellman-Ford
```

## Practice dry runs

```text
Quick Sort partition
Heap Sort
Merge Sort
Huffman tree
Kruskal
Prim
Dijkstra table
Fractional Knapsack
Inversion Count
```

## Memorize theory/comparisons

```text
O vs Ω vs Θ
BFS vs DFS
Merge vs Quick vs Heap Sort
Kruskal vs Prim
Dijkstra vs Bellman-Ford
MST vs Shortest Path Tree
Articulation Point vs Bridge
Fractional vs 0/1 Knapsack
Greedy vs Divide-and-Conquer
```
