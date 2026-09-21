"""
Problem: Dijkstra's Algorithm

Given a weighted graph with non-negative weights as adj[u] = [(v,w), ...], return
shortest distances from source.

Expected Complexity: O(E log V)
"""


def dijkstra(adj, source):
    # TODO: use min heap and relaxation
    pass


if __name__ == "__main__":
    adj = [
        [(1,4),(2,1)],
        [(3,1)],
        [(1,2),(3,5)],
        []
    ]
    assert dijkstra(adj, 0) == [0, 3, 1, 4]
    print("All tests passed")
