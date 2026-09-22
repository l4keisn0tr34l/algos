# DAA Popular PYQs with Solutions

This file contains high-frequency PYQ-style questions from Units I–III with exam-ready solutions.

---

# Unit I — Analysis and Recurrences

## 1. Define Big-O, Big-Omega and Big-Theta

### Answer

**Big-O:** upper bound on growth.

```text
f(n) = O(g(n)) if there exist constants c > 0 and n0 such that
0 <= f(n) <= c g(n) for all n >= n0
```

**Big-Omega:** lower bound on growth.

```text
f(n) = Ω(g(n)) if there exist constants c > 0 and n0 such that
0 <= c g(n) <= f(n) for all n >= n0
```

**Big-Theta:** tight bound.

```text
f(n) = Θ(g(n)) if f(n) = O(g(n)) and f(n) = Ω(g(n))
```

---

## 2. Solve using Master Theorem

```text
T(n) = 2T(n/2) + n
```

### Solution

```text
a = 2, b = 2, f(n) = n
n^(log_b a) = n^(log_2 2) = n
```

Since:

```text
f(n) = Θ(n^(log_b a))
```

Case 2 applies:

```text
T(n) = Θ(n log n)
```

---

## 3. Solve using Master Theorem

```text
T(n) = 4T(n/2) + n
```

### Solution

```text
a = 4, b = 2, f(n) = n
n^(log_b a) = n^(log_2 4) = n²
```

Since:

```text
f(n) = O(n²⁻ε)
```

Case 1:

```text
T(n) = Θ(n²)
```

---

## 4. Solve using recursion tree

```text
T(n) = 2T(n/2) + n
```

### Solution

At level 0:

```text
work = n
```

At level 1:

```text
2 subproblems of size n/2
work = 2 × n/2 = n
```

At level 2:

```text
4 subproblems of size n/4
work = 4 × n/4 = n
```

Every level costs `n`.

Height:

```text
n / 2^k = 1
k = log₂ n
```

Total:

```text
n + n + ... log n times = n log n
```

Answer:

```text
T(n) = Θ(n log n)
```

---

# Unit II — Searching, Sorting, Divide and Conquer

## 5. Write Binary Search algorithm and analyze complexity

### Algorithm

```text
BinarySearch(A, n, key):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) / 2

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

---

## 6. Find first 1 in sorted binary array

Example:

```text
A = [0, 0, 0, 0, 1, 1]
```

### Algorithm

```text
FirstOne(A, n):
    low = 0
    high = n - 1
    ans = -1

    while low <= high:
        mid = low + (high - low) / 2

        if A[mid] == 1:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans
```

### Answer for example

```text
index = 4
```

Complexity:

```text
O(log n)
```

---

## 7. Search in rotated sorted array

Example:

```text
A = [35, 42, 5, 15, 27, 29], target = 15
```

### Algorithm

```text
SearchRotated(A, target):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) / 2

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

### Answer

```text
15 is at index 3
```

Complexity:

```text
O(log n)
```

---

## 8. Write Merge Sort algorithm and recurrence

### Algorithm

```text
MergeSort(A, low, high):
    if low >= high:
        return

    mid = (low + high) / 2
    MergeSort(A, low, mid)
    MergeSort(A, mid + 1, high)
    Merge(A, low, mid, high)
```

### Helper

```text
Merge(A, low, mid, high):
    i = low
    j = mid + 1
    temp = empty array

    while i <= mid and j <= high:
        if A[i] <= A[j]:
            append A[i] to temp
            i++
        else:
            append A[j] to temp
            j++

    copy remaining elements from left half
    copy remaining elements from right half
    copy temp back to A[low...high]
```

### Recurrence

```text
T(n) = 2T(n/2) + n
```

### Complexity

```text
Best = Average = Worst = O(n log n)
Space = O(n)
```

---

## 9. Count inversions using divide and conquer

### Definition

An inversion is a pair `(i, j)` such that:

```text
i < j and A[i] > A[j]
```

### Algorithm

Use modified Merge Sort.

```text
CountInversions(A, low, high):
    if low >= high:
        return 0

    mid = (low + high) / 2
    left = CountInversions(A, low, mid)
    right = CountInversions(A, mid + 1, high)
    cross = MergeAndCount(A, low, mid, high)

    return left + right + cross
```

### Key line

During merge, if:

```text
A[i] > A[j]
```

then inversions added:

```text
mid - i + 1
```

### Complexity

```text
O(n log n)
```

---

## 10. Write Quick Sort algorithm and best/worst complexity

### Algorithm

```text
QuickSort(A, low, high):
    if low < high:
        p = Partition(A, low, high)
        QuickSort(A, low, p - 1)
        QuickSort(A, p + 1, high)
```

### Partition

```text
Partition(A, low, high):
    pivot = A[high]
    i = low - 1

    for j = low to high - 1:
        if A[j] <= pivot:
            i++
            swap A[i], A[j]

    swap A[i+1], A[high]
    return i + 1
```

### Complexity

```text
Best: O(n log n)
Average: O(n log n)
Worst: O(n²)
```

Worst case occurs when pivot is always smallest/largest.

---

## 11. Heap Sort algorithm

### Algorithm

```text
HeapSort(A, n):
    BuildMaxHeap(A, n)

    for i = n - 1 downto 1:
        swap A[0], A[i]
        MaxHeapify(A, i, 0)
```

### Helper

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

### Complexity

```text
Build heap: O(n)
Heap sort: O(n log n)
Space: O(1)
```

---

## 12. Strassen Matrix Multiplication recurrence

### Answer

Strassen reduces 8 recursive multiplications to 7.

```text
T(n) = 7T(n/2) + O(n²)
```

Using Master Theorem:

```text
T(n) = O(n^log₂7) = O(n^2.807)
```

Normal matrix multiplication:

```text
O(n³)
```

---

## 13. BFS vs DFS

| Feature | BFS | DFS |
|---|---|---|
| Data structure | Queue | Stack / Recursion |
| Traversal | Level-wise | Depth-wise |
| Shortest path in unweighted graph | Yes | No guarantee |
| Complexity | `O(V+E)` | `O(V+E)` |

---

## 14. Articulation Point vs Bridge

| Concept | Removal of | Effect |
|---|---|---|
| Articulation Point | Vertex | increases connected components |
| Bridge | Edge | increases connected components |

Conditions:

```text
Articulation point: low[child] >= disc[u]
Bridge: low[v] > disc[u]
```

---

# Unit III — Greedy and Graph Algorithms

## 15. Define Greedy Method

### Answer

A greedy algorithm builds a solution step by step by choosing the locally optimal option at each step. It works when the problem has:

```text
1. Greedy choice property
2. Optimal substructure
```

Greedy does not always guarantee optimal solution.

---

## 16. Activity Selection

### Greedy Rule

Choose the activity with earliest finishing time.

### Algorithm

```text
ActivitySelection(activities):
    sort activities by finish time
    selected = empty
    lastFinish = -infinity

    for each activity (start, finish):
        if start >= lastFinish:
            add activity to selected
            lastFinish = finish

    return selected
```

### Complexity

```text
O(n log n)
```

---

## 17. Fractional Knapsack

### Greedy Rule

Sort by decreasing:

```text
value / weight
```

### Algorithm

```text
FractionalKnapsack(items, W):
    sort items by value/weight decreasing
    profit = 0

    for each item:
        if item.weight <= W:
            take full item
            profit += item.value
            W -= item.weight
        else:
            take fraction W / item.weight
            profit += item.value * W / item.weight
            break

    return profit
```

### Complexity

```text
O(n log n)
```

---

## 18. Huffman Coding

### Greedy Rule

Repeatedly merge two least frequent nodes.

### Algorithm

```text
Huffman(chars, freq):
    create min heap Q

    for each character:
        insert leaf node into Q

    while Q has more than one node:
        x = ExtractMin(Q)
        y = ExtractMin(Q)
        z = new node with freq = x.freq + y.freq
        z.left = x
        z.right = y
        Insert(Q, z)

    root = ExtractMin(Q)
    GenerateCodes(root, "")
```

### Helper

```text
GenerateCodes(node, code):
    if node is leaf:
        print node.character and code
    else:
        GenerateCodes(node.left, code + "0")
        GenerateCodes(node.right, code + "1")
```

### Complexity

```text
O(n log n)
```

---

## 19. Kruskal's Algorithm

### Algorithm

```text
Kruskal(G):
    sort all edges by increasing weight
    MST = empty

    for each vertex v:
        MakeSet(v)

    for each edge (u, v, w):
        if Find(u) != Find(v):
            add edge to MST
            Union(u, v)

        if MST has V - 1 edges:
            break

    return MST
```

### Complexity

```text
O(E log E)
```

---

## 20. Prim's Algorithm

### Algorithm

```text
Prim(G, start):
    MST = empty
    visited[start] = true
    insert all edges of start into min heap

    while MST has fewer than V-1 edges:
        edge = ExtractMin(heap)

        if edge goes to unvisited vertex:
            add edge to MST
            mark new vertex visited
            insert its outgoing edges into heap

    return MST
```

### Complexity

```text
O(E log V)
```

---

## 21. Dijkstra's Algorithm

### Use

Single-source shortest paths with non-negative weights.

### Algorithm

```text
Dijkstra(G, source):
    dist[v] = infinity for all vertices
    dist[source] = 0
    create min heap Q
    Insert(Q, (0, source))

    while Q is not empty:
        (d, u) = ExtractMin(Q)

        if d > dist[u]:
            continue

        for each edge (u, v, w):
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                Insert(Q, (dist[v], v))

    return dist
```

### Complexity

```text
O(E log V)
```

---

## 22. Bellman-Ford Algorithm

### Use

Single-source shortest paths with negative edges and negative cycle detection.

### Algorithm

```text
BellmanFord(V, edges, source):
    dist[v] = infinity for all vertices
    dist[source] = 0

    repeat V - 1 times:
        for each edge (u, v, w):
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for each edge (u, v, w):
        if dist[u] + w < dist[v]:
            report negative cycle

    return dist
```

### Complexity

```text
O(VE)
```

---

## 23. Dijkstra vs Bellman-Ford

| Feature | Dijkstra | Bellman-Ford |
|---|---|---|
| Negative edges | No | Yes |
| Negative cycle detection | No | Yes |
| Complexity | `O(E log V)` | `O(VE)` |
| Method | Greedy | Relax all edges repeatedly |

---

## 24. MST vs Shortest Path Tree

| Feature | MST | Shortest Path Tree |
|---|---|---|
| Goal | minimum total connection cost | minimum distance from source |
| Source needed? | No | Yes |
| Algorithms | Prim, Kruskal | Dijkstra, Bellman-Ford |

