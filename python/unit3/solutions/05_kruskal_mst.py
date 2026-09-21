"""Reference solution: Kruskal MST"""
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

def kruskal_mst(V, edges):
    dsu = DSU(V)
    total = 0
    mst = []
    for u, v, w in sorted(edges, key=lambda x: x[2]):
        if dsu.union(u, v):
            mst.append((u, v, w))
            total += w
            if len(mst) == V - 1:
                break
    return total, mst

if __name__ == "__main__":
    V = 4
    edges = [(0,1,10),(0,2,6),(0,3,5),(1,3,15),(2,3,4)]
    weight, mst = kruskal_mst(V, edges)
    assert weight == 19 and len(mst) == V - 1
    print("All tests passed")
