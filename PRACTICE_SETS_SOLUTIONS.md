# DAA Practice Sets — Solution Key / Answer Templates

This file gives compact solutions or answer templates for the practice questions in `PRACTICE_SETS_BY_TOPIC.md`.

---

# Unit I — Algorithm Analysis

## Runtime Analysis / Operation Counting

### Common answers

```text
Single loop from 1 to n: O(n)
Nested n × n loop: O(n²)
Loop doubling i = i * 2: O(log n)
Loop halving i = i / 2: O(log n)
Two separate loops O(n) + O(n²): O(n²)
Dependent loop 1 + 2 + ... + n: O(n²)
Geometric sum 1 + 2 + 4 + ... + n: O(n)
```

### Linear search

```text
Best case: O(1)       key at first position
Worst case: O(n)      key last or absent
Average case: O(n)    about n/2 comparisons
```

---

## Asymptotic Notations

### Big-O

```text
f(n) = O(g(n)) if there exist c > 0 and n0 such that
0 <= f(n) <= c g(n) for all n >= n0.
```

### Big-Omega

```text
f(n) = Ω(g(n)) if there exist c > 0 and n0 such that
0 <= c g(n) <= f(n) for all n >= n0.
```

### Big-Theta

```text
f(n) = Θ(g(n)) if f(n) = O(g(n)) and f(n) = Ω(g(n)).
```

### Example proof

For:

```text
3n² + 5n + 2 = O(n²)
```

For `n >= 1`:

```text
3n² + 5n + 2 <= 3n² + 5n² + 2n² = 10n²
```

So choose:

```text
c = 10, n0 = 1
```

---

## Growth Order

From slowest to fastest:

```text
1 < log n < n < n log n < n² < n³ < 2ⁿ < n!
```

---

## Recurrences

### Common results

```text
T(n) = T(n-1) + 1       => O(n)
T(n) = T(n-1) + n       => O(n²)
T(n) = T(n/2) + 1       => O(log n)
T(n) = T(n/2) + n       => O(n)
T(n) = 2T(n/2) + n      => O(n log n)
T(n) = 4T(n/2) + n      => O(n²)
T(n) = 2T(n/2) + n²     => O(n²)
T(n) = 2T(n/2) + n log n => O(n log² n)
```

### Master Theorem template

For:

```text
T(n) = aT(n/b) + f(n)
```

Steps:

```text
1. Find a, b, f(n)
2. Compute n^(log_b a)
3. Compare f(n) with n^(log_b a)
4. Apply case
```

---

# Unit II — Searching, Sorting, D&C, Graph Basics

## Divide and Conquer

### Definition

Divide and conquer solves a problem by dividing it into smaller subproblems, solving them recursively, and combining the answers.

```text
Divide → Conquer → Combine
```

### Recurrence example

2 subproblems of size `n/2` and `n` combine work:

```text
T(n) = 2T(n/2) + n
```

---

## Binary Search

### Algorithm

```text
BinarySearch(A, n, key):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high-low)/2

        if A[mid] == key:
            return mid
        else if key < A[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1
```

### Complexity

```text
Best: O(1)
Worst: O(log n)
Space: O(1)
```

### Recurrence

```text
T(n) = T(n/2) + 1 = O(log n)
```

---

## Binary Search Variants

### First 1 in binary array

```text
FirstOne(A):
    low = 0, high = n-1, ans = -1

    while low <= high:
        mid = low + (high-low)/2

        if A[mid] == 1:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans
```

### Rotated sorted array

```text
SearchRotated(A, target):
    low = 0, high = n-1

    while low <= high:
        mid = low + (high-low)/2

        if A[mid] == target:
            return mid

        if A[low] <= A[mid]:
            if A[low] <= target < A[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if A[mid] < target <= A[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1
```

### Fixed point

```text
FixedPoint(A):
    low = 0, high = n-1

    while low <= high:
        mid = low + (high-low)/2

        if A[mid] == mid:
            return mid
        else if A[mid] > mid:
            high = mid - 1
        else:
            low = mid + 1

    return -1
```

---

## Merge Sort

### Main algorithm

```text
MergeSort(A, low, high):
    if low >= high:
        return

    mid = (low + high)/2
    MergeSort(A, low, mid)
    MergeSort(A, mid+1, high)
    Merge(A, low, mid, high)
```

### Helper

```text
Merge(A, low, mid, high):
    i = low
    j = mid + 1
    temp = empty

    while i <= mid and j <= high:
        if A[i] <= A[j]:
            append A[i]
            i++
        else:
            append A[j]
            j++

    copy remaining left elements
    copy remaining right elements
    copy temp back to A[low...high]
```

### Complexity

```text
T(n) = 2T(n/2) + n = O(n log n)
Space = O(n)
```

---

## Inversion Count

### Definition

```text
(i, j) is inversion if i < j and A[i] > A[j]
```

### Key formula

During merge, if:

```text
A[i] > A[j]
```

then add:

```text
mid - i + 1
```

### Complexity

```text
O(n log n)
```

---

## Quick Sort

### Main

```text
QuickSort(A, low, high):
    if low < high:
        p = Partition(A, low, high)
        QuickSort(A, low, p-1)
        QuickSort(A, p+1, high)
```

### Partition

```text
Partition(A, low, high):
    pivot = A[high]
    i = low - 1

    for j = low to high-1:
        if A[j] <= pivot:
            i++
            swap A[i], A[j]

    swap A[i+1], A[high]
    return i+1
```

### Complexity

```text
Best: O(n log n)
Average: O(n log n)
Worst: O(n²)
```

Worst case recurrence:

```text
T(n) = T(n-1) + n = O(n²)
```

---

## Heap / Heap Sort

### MaxHeapify

```text
MaxHeapify(A, n, i):
    largest = i
    left = 2i + 1
    right = 2i + 2

    if left < n and A[left] > A[largest]:
        largest = left
    if right < n and A[right] > A[largest]:
        largest = right

    if largest != i:
        swap A[i], A[largest]
        MaxHeapify(A, n, largest)
```

### Build heap

```text
BuildMaxHeap(A, n):
    for i = n/2 - 1 downto 0:
        MaxHeapify(A, n, i)
```

### Heap sort

```text
HeapSort(A, n):
    BuildMaxHeap(A, n)

    for i = n-1 downto 1:
        swap A[0], A[i]
        MaxHeapify(A, i, 0)
```

### Complexity

```text
BuildHeap: O(n)
HeapSort: O(n log n)
Space: O(1)
```

---

## Strassen Matrix Multiplication

### Recurrence

```text
T(n) = 7T(n/2) + O(n²)
```

### Complexity

```text
O(n^log₂7) = O(n^2.807)
```

### Key idea

Strassen uses 7 recursive multiplications instead of 8.

---

## Graph Representations

### Adjacency matrix

```text
matrix[u][v] = 1 or weight if edge exists
```

Space:

```text
O(V²)
```

### Adjacency list

```text
adj[u] contains neighbors of u
```

Space:

```text
O(V + E)
```

---

## BFS

```text
BFS(G, source):
    mark source visited
    enqueue source

    while queue not empty:
        u = dequeue
        visit u

        for each neighbor v:
            if v not visited:
                mark visited
                enqueue v
```

Complexity:

```text
O(V + E)
```

---

## DFS

```text
DFS(u):
    mark u visited
    visit u

    for each neighbor v:
        if v not visited:
            DFS(v)
```

Complexity:

```text
O(V + E)
```

---

## Connected Components

```text
ConnectedComponents(G):
    count = 0
    mark all unvisited

    for each vertex v:
        if v not visited:
            count++
            DFS(v)

    return count
```

---

## DFS Edge Classification

```text
Tree edge: discovers new vertex
Back edge: goes to ancestor
Forward edge: goes to descendant but not tree edge
Cross edge: unrelated DFS branches
```

Back edge indicates cycle in directed graph.

---

## Articulation Point

A vertex whose removal increases number of connected components.

Conditions:

```text
Root: children > 1
Non-root: low[child] >= disc[u]
```

---

## Bridge

An edge whose removal increases number of connected components.

Condition:

```text
low[v] > disc[u]
```

---

# Unit III — Greedy and Graph Algorithms

## Greedy Method

### Definition

Greedy builds a solution by choosing the locally best option at each step.

Works when:

```text
1. Greedy choice property
2. Optimal substructure
```

Greedy does not always work. Example: 0/1 knapsack.

---

## Activity Selection

Exam-friendly version without using `-infinity`:

```text
ActivitySelection(activities):
    sort activities by increasing finish time

    selected = empty list

    add activities[1] to selected
    lastFinish = finish time of activities[1]

    for i = 2 to n:
        if start time of activities[i] >= lastFinish:
            add activities[i] to selected
            lastFinish = finish time of activities[i]

    return selected
```

Complexity:

```text
O(n log n)
```

Note: If array indexing starts from 0 in code, use first activity as `activities[0]` and loop from index `1`.

---

## Fractional Knapsack

```text
FractionalKnapsack(items, W):
    sort by value/weight decreasing
    profit = 0

    for each item:
        if item.weight <= W:
            take full
            profit += value
            W -= weight
        else:
            take fraction W/item.weight
            profit += value * W/item.weight
            break

    return profit
```

Complexity:

```text
O(n log n)
```

---

## Huffman Coding

```text
Huffman(chars, freq):
    create min heap Q

    for each char:
        insert leaf node

    while Q has more than one node:
        x = ExtractMin(Q)
        y = ExtractMin(Q)
        z = new node with freq x.freq + y.freq
        z.left = x
        z.right = y
        Insert(Q, z)

    root = ExtractMin(Q)
    GenerateCodes(root, "")
```

Helper:

```text
GenerateCodes(node, code):
    if node is leaf:
        print character and code
    else:
        GenerateCodes(node.left, code + "0")
        GenerateCodes(node.right, code + "1")
```

Complexity:

```text
O(n log n)
```

Average length:

```text
Σ(freq × code length) / Σ(freq)
```

---

## MST Basics

```text
Spanning tree: connected acyclic subgraph containing all vertices
MST: spanning tree with minimum total edge weight
Any spanning tree has V-1 edges
```

MST is not the same as shortest path tree.

---

## DSU

```text
MakeSet(x):
    parent[x] = x
    rank[x] = 0
```

```text
Find(x):
    if parent[x] != x:
        parent[x] = Find(parent[x])
    return parent[x]
```

```text
Union(x, y):
    rx = Find(x)
    ry = Find(y)

    if rx == ry:
        return

    attach smaller rank tree under larger rank tree
```

---

## Kruskal

```text
Kruskal(G):
    sort edges by weight
    MST = empty

    for each vertex:
        MakeSet(vertex)

    for each edge (u, v, w):
        if Find(u) != Find(v):
            add edge to MST
            Union(u, v)

    return MST
```

Complexity:

```text
O(E log E)
```

---

## Prim

```text
Prim(G, start):
    MST = empty
    visited[start] = true
    insert all edges of start into min heap

    while MST has fewer than V-1 edges:
        edge = ExtractMin(heap)

        if edge goes to unvisited vertex:
            add edge to MST
            mark vertex visited
            insert its outgoing edges

    return MST
```

Complexity:

```text
O(E log V)
```

---

## Dijkstra

```text
Dijkstra(G, source):
    dist[v] = infinity for all v
    dist[source] = 0
    minHeap = [(0, source)]

    while heap not empty:
        (d, u) = ExtractMin(heap)

        if d > dist[u]:
            continue

        for each edge (u, v, w):
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                Insert(heap, (dist[v], v))

    return dist
```

Complexity:

```text
O(E log V)
```

Does not work safely with negative edges.

---

## Bellman-Ford

```text
BellmanFord(V, edges, source):
    dist[v] = infinity for all v
    dist[source] = 0

    repeat V-1 times:
        for each edge (u, v, w):
            if dist[u] != infinity and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for each edge (u, v, w):
        if dist[u] != infinity and dist[u] + w < dist[v]:
            report negative cycle

    return dist
```

Complexity:

```text
O(VE)
```

---

## Important Comparisons

### Kruskal vs Prim

| Kruskal | Prim |
|---|---|
| Sorts all edges | Starts from vertex |
| Uses DSU | Uses priority queue |
| Chooses globally smallest safe edge | Chooses smallest edge from tree to outside |

### Dijkstra vs Bellman-Ford

| Dijkstra | Bellman-Ford |
|---|---|
| No negative edges | Handles negative edges |
| Faster | Slower |
| No negative cycle detection | Detects negative cycle |

### Fractional vs 0/1 Knapsack

| Fractional | 0/1 |
|---|---|
| Can split items | Cannot split items |
| Greedy works | Greedy does not always work |

---

# Lab / Extra Solutions

## Iterative Merge Sort

```text
IterativeMergeSort(A):
    size = 1

    while size < n:
        for left = 0 to n-1 step 2*size:
            mid = min(left + size - 1, n-1)
            right = min(left + 2*size - 1, n-1)

            if mid < right:
                Merge(A, left, mid, right)

        size = size * 2
```

---

## Random Weighted Graph

```text
Generate all possible edges (u, v), u < v
Shuffle edges
Pick first e edges
Assign random weights
Build adjacency matrix and adjacency list
```

Number of edges:

```text
e = d × n(n-1)/2
```

---

## MinHeap Priority Queue

```text
Insert(x):
    add x at end
    heapify up
```

```text
ExtractMin():
    save root
    replace root with last element
    delete last
    heapify down
```

Complexity:

```text
Insert: O(log n)
ExtractMin: O(log n)
GetMin: O(1)
```

---

## 0/1 Knapsack DP

State:

```text
C[i][w] = max value using first i items with capacity w
```

Recurrence:

```text
if wt[i] > w:
    C[i][w] = C[i-1][w]
else:
    C[i][w] = max(C[i-1][w], val[i] + C[i-1][w-wt[i]])
```

Complexity:

```text
O(nW)
```

---

## LCS DP

State:

```text
L[i][j] = length of LCS of X[0...i-1] and Y[0...j-1]
```

Recurrence:

```text
if X[i-1] == Y[j-1]:
    L[i][j] = 1 + L[i-1][j-1]
else:
    L[i][j] = max(L[i-1][j], L[i][j-1])
```

Complexity:

```text
O(mn)
```
