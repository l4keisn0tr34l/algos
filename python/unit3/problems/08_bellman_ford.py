"""
Problem: Bellman-Ford Algorithm

Given V vertices and directed weighted edges (u, v, w), return shortest distances
from source. If a negative cycle is reachable, return None.

Expected Complexity: O(VE)
"""


def bellman_ford(V, edges, source):
    # TODO: relax all edges V-1 times, then check negative cycle
    pass


if __name__ == "__main__":
    V = 5
    edges = [(0,1,-1),(0,2,4),(1,2,3),(1,3,2),(1,4,2),(3,2,5),(3,1,1),(4,3,-3)]
    assert bellman_ford(V, edges, 0) == [0, -1, 2, -2, 1]
    print("All tests passed")
