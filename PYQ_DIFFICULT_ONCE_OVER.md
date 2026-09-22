# DAA Difficult PYQs — One-Time Revision Sheet

This file is for questions that are easy to forget or make mistakes in. Read this close to exam.

---

# 1. Recursion Tree: `T(n) = T(n/3) + T(2n/3) + n`

## Why difficult?

Subproblem sizes are unequal, so normal Master Theorem does not directly apply.

## Recursion tree idea

At each node, total subproblem size remains:

```text
n/3 + 2n/3 = n
```

So total work per level is about:

```text
n
```

Height is dominated by larger branch:

```text
n -> 2n/3 -> (2/3)^2 n -> ... -> 1
```

So:

```text
(2/3)^k n = 1
k = log_{3/2} n
```

Total work:

```text
n × log n = Θ(n log n)
```

Answer:

```text
T(n) = Θ(n log n)
```

---

# 2. Recurrence: `T(n) = 2T(n/2) + n log n`

## Solution

```text
a = 2, b = 2, f(n) = n log n
n^(log_b a) = n
```

Here:

```text
f(n) = n log n = Θ(n log¹ n)
```

Master Theorem extended Case 2:

```text
T(n) = Θ(n log² n)
```

Common mistake: writing `O(n log n)`.

---

# 3. Recurrence: `T(n) = 3T(n/2) + n²`

## Solution

```text
a = 3, b = 2
n^(log_b a) = n^(log₂3) ≈ n^1.585
f(n) = n²
```

Since:

```text
n² grows faster than n^1.585
```

Case 3:

```text
T(n) = Θ(n²)
```

---

# 4. Binary Search in Rotated Sorted Array

## Key observation

At every `mid`, at least one half is sorted.

## Algorithm

```text
SearchRotated(A, target):
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low)/2

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

Complexity:

```text
O(log n)
```

Common mistake: not checking which half is sorted.

---

# 5. Fixed Point `A[i] = i`

Given sorted distinct array.

## Algorithm

```text
FixedPoint(A):
    low = 0
    high = n - 1

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

Why?

- If `A[mid] > mid`, fixed point can only be on left.
- If `A[mid] < mid`, fixed point can only be on right.

Complexity:

```text
O(log n)
```

---

# 6. Inversion Count using Merge Sort

## Key condition

During merge, if:

```text
left[i] > right[j]
```

Then add:

```text
mid - i + 1
```

because all remaining elements in left half are greater than `right[j]`.

## Algorithm skeleton

```text
CountInv(A, low, high):
    if low >= high:
        return 0

    mid = (low + high)/2
    left = CountInv(A, low, mid)
    right = CountInv(A, mid+1, high)
    cross = MergeAndCount(A, low, mid, high)

    return left + right + cross
```

Complexity:

```text
O(n log n)
```

Common mistake: adding only `1` instead of `mid-i+1`.

---

# 7. Build Heap is `O(n)`, not `O(n log n)`

## Explanation

Although one heapify can take `O(log n)`, most nodes are near leaves and move very little.

Total work:

```text
number of nodes at height h ≈ n / 2^(h+1)
work per node = O(h)
```

Total:

```text
Σ (n / 2^(h+1)) × h = O(n)
```

So:

```text
BuildMaxHeap = O(n)
HeapSort = O(n log n)
```

---

# 8. Quick Sort Worst Case Derivation

Worst case occurs when pivot is always smallest/largest.

Recurrence:

```text
T(n) = T(n-1) + n
```

Expansion:

```text
T(n) = n + (n-1) + (n-2) + ... + 1
```

So:

```text
T(n) = Θ(n²)
```

Best case:

```text
T(n) = 2T(n/2) + n = Θ(n log n)
```

---

# 9. Strassen Formula Set

For:

```text
A = [A11 A12]
    [A21 A22]

B = [B11 B12]
    [B21 B22]
```

Seven products:

```text
P1 = (A11 + A22)(B11 + B22)
P2 = (A21 + A22)B11
P3 = A11(B12 - B22)
P4 = A22(B21 - B11)
P5 = (A11 + A12)B22
P6 = (A21 - A11)(B11 + B12)
P7 = (A12 - A22)(B21 + B22)
```

Result:

```text
C11 = P1 + P4 - P5 + P7
C12 = P3 + P5
C21 = P2 + P4
C22 = P1 - P2 + P3 + P6
```

Recurrence:

```text
T(n) = 7T(n/2) + O(n²)
```

Complexity:

```text
O(n^2.807)
```

---

# 10. DFS Edge Classification

For directed graphs:

| Edge | Meaning |
|---|---|
| Tree edge | discovers a new vertex |
| Back edge | goes to ancestor |
| Forward edge | goes to descendant but not tree edge |
| Cross edge | between unrelated DFS branches |

Back edge indicates cycle in directed graph.

Color logic:

```text
WHITE → unvisited
GRAY → in recursion stack
BLACK → fully processed
```

```text
WHITE neighbor = Tree edge
GRAY neighbor = Back edge
BLACK descendant = Forward edge
BLACK unrelated = Cross edge
```

---

# 11. Articulation Point Conditions

Maintain:

```text
disc[u] = discovery time
low[u] = earliest discovery time reachable from u's subtree
```

## Root condition

Root is articulation point if it has more than one DFS child.

```text
children(root) > 1
```

## Non-root condition

A non-root `u` is articulation point if:

```text
low[child] >= disc[u]
```

Meaning child subtree cannot reach an ancestor of `u`.

---

# 12. Bridge Condition

For DFS tree edge `(u, v)`:

```text
if low[v] > disc[u]:
    (u, v) is a bridge
```

Difference from articulation:

```text
Articulation: low[child] >= disc[u]
Bridge:       low[v] > disc[u]
```

Common mistake: using `>=` for bridge. Bridge requires strictly `>`.

---

# 13. Huffman Coding Average Length

## Steps

1. Build Huffman tree by merging two smallest frequencies.
2. Assign codes using left = 0, right = 1.
3. Compute:

If frequencies:

```text
Average length = Σ(freq × code_length) / Σ(freq)
```

If probabilities:

```text
Average length = Σ(prob × code_length)
```

Common mistake: forgetting to divide by total frequency.

---

# 14. Fractional vs 0/1 Knapsack

| Feature | Fractional | 0/1 |
|---|---|---|
| Can split item? | Yes | No |
| Greedy works? | Yes | No generally |
| Method | sort by value/weight | DP / Branch and Bound |

Common exam trap:

```text
Greedy by value/weight does not guarantee optimal answer for 0/1 knapsack.
```

---

# 15. Kruskal Algorithm with DSU Helpers

## Main

```text
Kruskal(G):
    sort edges by weight
    for each vertex v:
        MakeSet(v)

    for each edge (u, v, w):
        if Find(u) != Find(v):
            add edge to MST
            Union(u, v)
```

## Find

```text
Find(x):
    if parent[x] != x:
        parent[x] = Find(parent[x])
    return parent[x]
```

## Union

```text
Union(x, y):
    rx = Find(x)
    ry = Find(y)

    if rx == ry:
        return

    attach smaller rank tree under larger rank tree
```

Complexity:

```text
O(E log E)
```

---

# 16. Prim vs Kruskal

| Feature | Prim | Kruskal |
|---|---|---|
| Grows | one tree | forest merging into MST |
| Chooses | min edge from tree to outside | globally smallest safe edge |
| Uses | min heap | DSU |
| Complexity | `O(E log V)` | `O(E log E)` |

---

# 17. Dijkstra Table Method

At each step:

1. Select unvisited vertex with smallest `dist`.
2. Mark it finalized.
3. Relax all outgoing edges.
4. Update distance table.

Relaxation:

```text
if dist[u] + w < dist[v]:
    dist[v] = dist[u] + w
```

Dijkstra fails with negative edges because a finalized distance may later become smaller.

---

# 18. Bellman-Ford Negative Cycle Detection

Run relaxation `V-1` times.

Then check once more:

```text
for each edge (u, v, w):
    if dist[u] + w < dist[v]:
        negative cycle exists
```

Why?

After `V-1` rounds, all shortest simple paths should be finalized. If improvement is still possible, there is a cycle reducing distance.

Complexity:

```text
O(VE)
```

---

# 19. MST vs Shortest Path Tree

Very common confusion.

| Feature | MST | Shortest Path Tree |
|---|---|---|
| Source required? | No | Yes |
| Objective | minimize total edge weight | minimize distance from source |
| Algorithms | Prim, Kruskal | Dijkstra, Bellman-Ford |

They are not the same.

---

# 20. Optimal Merge Pattern

Even though not in core Unit III list, it appeared in lab.

## Greedy rule

Repeatedly merge two smallest files.

## Algorithm

```text
OptimalMerge(files):
    insert all file sizes into min heap
    cost = 0

    while heap has more than one file:
        a = ExtractMin(heap)
        b = ExtractMin(heap)
        merged = a + b
        cost += merged
        Insert(heap, merged)

    return cost
```

Complexity:

```text
O(n log n)
```

Same greedy structure as Huffman.

---

# 21. 0/1 Knapsack DP Table

Lab/PYQ-style DP topic.

State:

```text
C[i][w] = max value using first i items with capacity w
```

Recurrence:

```text
if weight[i] > w:
    C[i][w] = C[i-1][w]
else:
    C[i][w] = max(C[i-1][w], value[i] + C[i-1][w-weight[i]])
```

Keep table:

```text
Keep[i][w] = 1 if item i is selected
Keep[i][w] = 0 otherwise
```

Complexity:

```text
O(nW)
```

---

# 22. LCS DP Table

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

Traceback:

- diagonal if characters match
- move up/left depending on larger value

Complexity:

```text
O(mn)
```

---

# Final One-Liners to Memorize

```text
Merge Sort: T(n)=2T(n/2)+n = O(n log n)
Quick Sort worst: T(n)=T(n-1)+n = O(n²)
Heap Sort: O(n log n), O(1) space
Build Heap: O(n)
Strassen: T(n)=7T(n/2)+n² = O(n^2.807)
BFS/DFS: O(V+E)
Kruskal: O(E log E)
Prim: O(E log V)
Dijkstra: O(E log V), no negative edges
Bellman-Ford: O(VE), handles negative edges
Huffman: O(n log n)
Fractional Knapsack: O(n log n), greedy works
0/1 Knapsack: greedy fails, DP works
```
