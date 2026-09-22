"""
Problem: Kruskal MST

Given V vertices and weighted undirected edges (u, v, w), return total weight
and edges of a Minimum Spanning Tree.

Example:
Input: V=4, edges=[(0,1,10),(0,2,6),(0,3,5),(1,3,15),(2,3,4)]
Output weight: 19

Expected Complexity: O(E log E)
"""


class DSU:
    def __init__(self, n):
        # TODO: initialize parent and rank/size arrays
        pass

    def find(self, x):
        # TODO: return representative of x's set
        # Use path compression.
        pass

    def union(self, a, b):
        # TODO: merge sets of a and b
        # Return True if merge happened, False if already in same set.
        pass


def kruskal_mst(V, edges):
    # TODO:
    # 1. Sort edges by weight.
    # 2. Use DSU.find to check if an edge forms a cycle.
    # 3. Use DSU.union when adding an edge to MST.
    pass


if __name__ == "__main__":
    V = 4
    edges = [(0,1,10),(0,2,6),(0,3,5),(1,3,15),(2,3,4)]
    weight, mst = kruskal_mst(V, edges)
    assert weight == 19
    assert len(mst) == V - 1
    print("All tests passed")
