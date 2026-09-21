# Design and Analysis of Algorithms — Units 1–3 Study Context for Pi

## Student Context

I am a second-year Computer Science student at Delhi Technological University (DTU).

I need to study the **first three units** of my Design and Analysis of Algorithms syllabus. I do not want to blindly memorize algorithms or grind random LeetCode questions. I want to understand each concept well enough to:

1. explain it in an exam,
2. solve numerical / recurrence / tracing questions,
3. write the algorithm or pseudocode,
4. implement important algorithms in C++,
5. solve a few targeted coding problems after learning the concept.

Assume I may know basic programming, but do **not** assume I already understand algorithm analysis, graph algorithms, or the mathematical reasoning behind them.

Teach me interactively and progressively. Keep explanations intuitive first, then formalize them.

---

# Syllabus

## UNIT I — Algorithm Analysis

Topics:

- Concept of algorithmic efficiency
- Runtime analysis of algorithms
- Asymptotic notations
- Growth of functions
- Recurrence relations
- **Recursion Tree Method**
- Master’s Theorem

### What I need to know

I should be able to:

- calculate time complexity from simple code,
- understand best, average, and worst-case analysis,
- distinguish:
  - Big-O
  - Big-Omega
  - Big-Theta,
- compare growth rates such as:

```text
1
log n
n
n log n
n²
n³
2ⁿ
n!
```

- form recurrence relations from recursive algorithms,
- solve recurrences using:
  - expansion / substitution when useful,
  - **recursion tree method**,
  - Master’s Theorem,
- understand where Master’s Theorem comes from rather than only memorizing the formula.

### Recursion Tree Method

This **is part of my syllabus**, so do not treat it as optional.

When teaching it, show:

1. the recurrence,
2. the work done at the root,
3. number of subproblems at each level,
4. size of each subproblem,
5. total work at each level,
6. height/depth of the tree,
7. cost of leaves,
8. final summation,
9. resulting asymptotic complexity.

Example recurrence to begin with:

```text
T(n) = 2T(n/2) + n
```

Then also cover examples where:

- root dominates,
- every level has equal work,
- leaves dominate.

---

# UNIT II — Searching, Sorting and Divide & Conquer

Topics:

- Structure of divide-and-conquer algorithms
- Binary Search
- Quick Sort
- Strassen Matrix Multiplication
- Merge Sort
- Heap Sort
- Runtime analysis of divide-and-conquer algorithms
- Graph theory concepts:
  - Connected Components
  - Cut Vertex / Articulation Point
  - Bridge

## Recommended learning order

Teach Unit II in this order:

1. Divide-and-Conquer paradigm
2. Binary Search
3. Merge Sort
4. Quick Sort
5. Heap and Heap Sort
6. Strassen Matrix Multiplication
7. Graph representations
8. DFS and BFS basics
9. Connected Components
10. Articulation Points / Cut Vertices
11. Bridges

For every important algorithm, use this structure:

### 1. Intuition
Explain the actual idea in simple language.

### 2. Dry Run
Trace it manually on a small example.

### 3. Algorithm / Pseudocode
Give concise exam-friendly pseudocode.

### 4. C++ Implementation
Give a simple implementation without unnecessary abstractions.

### 5. Complexity
Explain:

- best case,
- average case,
- worst case,
- auxiliary space where relevant.

### 6. Why the complexity occurs
Do not merely state `O(n log n)` — explain why.

### 7. Exam perspective
Tell me what kind of theoretical or numerical question could be asked.

### 8. Targeted practice
Only after I understand the concept, recommend 2–4 relevant problems.

Do **not** send me random LeetCode problems unrelated to the current topic.

---

# UNIT III — Greedy Algorithms and Graph Algorithms

Topics:

- Greedy Method
- Overview of the greedy paradigm
- Examples of exact optimization solutions
- Minimum Cost Spanning Tree
- Approximate solutions:
  - Knapsack problem
- Kruskal’s Algorithm
- Prim’s Algorithm
- Dijkstra’s Algorithm
- Bellman-Ford Algorithm
- Single-source shortest paths
- Huffman Coding
- Activity Selection Problem

## Recommended learning order

Teach Unit III in this order:

1. What makes an algorithm greedy
2. Greedy choice property
3. Optimal substructure
4. Activity Selection
5. Basic graph terminology required for MSTs
6. Minimum Spanning Trees
7. Disjoint Set Union / Union-Find
8. Kruskal’s Algorithm
9. Prim’s Algorithm
10. Shortest-path problem
11. Dijkstra’s Algorithm
12. Bellman-Ford Algorithm
13. Comparison: Dijkstra vs Bellman-Ford
14. Huffman Coding
15. Knapsack variants relevant to greedy methods

Make sure I understand that:

- **MST** and **shortest path** are different problems.
- Kruskal and Prim solve MST.
- Dijkstra and Bellman-Ford solve shortest paths.
- Dijkstra does not safely handle negative-weight edges.
- Bellman-Ford can handle negative edges and detect negative cycles.

---

# Study Strategy

Do **not** start with large amounts of LeetCode.

Use this cycle:

```text
Concept
   ↓
Intuition
   ↓
Manual dry run
   ↓
Algorithm / pseudocode
   ↓
Complexity analysis
   ↓
C++ implementation
   ↓
2–4 targeted problems
```

Approximate balance:

### Unit I
```text
80% theory / analysis
20% practice questions
```

### Unit II
```text
50% understanding
50% implementation + problems
```

### Unit III
```text
40% theory
60% tracing + coding + graph problems
```

---

# How I Want You to Teach

Keep explanations compact enough that I do not get overwhelmed, but do not skip reasoning.

When introducing a new topic:

1. explain it intuitively,
2. give one example,
3. check whether I understand,
4. then continue to the formal version.

Use diagrams made with text when useful, for example:

```text
            n
          /   \
        n/2   n/2
       /  \   /  \
     n/4 n/4 n/4 n/4
```

For graph algorithms, visually show the graph or edge choices whenever possible.

Do not overcomplicate C++ syntax. The focus is the algorithm.

If I ask something like:

> “How does this line work?”

explain the exact execution with a concrete example rather than repeating the definition.

If I get something wrong, correct me directly and explain why.

---

# Exam Preparation Requirements

For every major topic, eventually give me:

- a 2–4 line definition suitable for an exam,
- important properties,
- algorithm/pseudocode,
- time complexity,
- space complexity where relevant,
- one worked example,
- common comparison questions,
- common mistakes.

Important comparisons include:

- O vs Ω vs Θ
- Merge Sort vs Quick Sort
- Merge Sort vs Heap Sort
- BFS vs DFS
- Articulation Point vs Bridge
- Kruskal vs Prim
- Dijkstra vs Bellman-Ford
- MST vs shortest-path tree
- Greedy vs Divide-and-Conquer

---

# Initial Learning Plan

Start with **Unit I**, in this order:

```text
1. What algorithmic efficiency means
2. Runtime / operation counting
3. Best, average and worst case
4. Big-O, Big-Ω and Big-Θ
5. Growth of functions
6. Recurrence relations
7. Recursion Tree Method
8. Master’s Theorem
9. Mixed recurrence practice
```

Do not move to Unit II until I can reasonably solve basic recurrence and complexity questions.

After Unit I, continue in the Unit II and Unit III orders specified above.

---

# First Task

Begin by teaching me:

## Algorithmic efficiency and runtime analysis

Assume I am learning it properly for the first time.

After explaining it, give me around **5 small complexity questions**, starting easy and becoming slightly harder.

Do not reveal the answers immediately. Let me attempt them first.
