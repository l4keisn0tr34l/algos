"""
Problem: Prim MST

Given a weighted undirected graph as adjacency list adj[u] = [(v,w), ...], return
MST total weight and selected edges.

Expected Complexity: O(E log V)
"""


def prim_mst(adj, start=0):
    # TODO: use min heap to grow MST from start vertex
    pass


if __name__ == "__main__":
    adj = [
        [(1,10),(2,6),(3,5)],
        [(0,10),(3,15)],
        [(0,6),(3,4)],
        [(0,5),(1,15),(2,4)]
    ]
    weight, mst = prim_mst(adj, 0)
    assert weight == 19
    assert len(mst) == 3
    print("All tests passed")
