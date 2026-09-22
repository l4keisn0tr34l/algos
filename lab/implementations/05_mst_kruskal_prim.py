"""
Lab 05: MST Algorithms — Kruskal and Prim
"""

import heapq


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False

        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1

        return True


def kruskal(V, edges):
    dsu = DSU(V)
    mst = []
    total = 0

    for u, v, w in sorted(edges, key=lambda x: x[2]):
        if dsu.union(u, v):
            mst.append((u, v, w))
            total += w
            if len(mst) == V - 1:
                break

    return total, mst


def prim(adj, start=0):
    V = len(adj)
    visited = [False] * V
    heap = [(0, start, -1)]
    mst = []
    total = 0

    while heap and len(mst) < V - 1:
        w, u, parent = heapq.heappop(heap)

        if visited[u]:
            continue

        visited[u] = True
        total += w

        if parent != -1:
            mst.append((parent, u, w))

        for v, wt in adj[u]:
            if not visited[v]:
                heapq.heappush(heap, (wt, v, u))

    return total, mst


if __name__ == "__main__":
    V = 4
    edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]

    adj = [[] for _ in range(V)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    print("Kruskal:", kruskal(V, edges))
    print("Prim:", prim(adj, 0))
