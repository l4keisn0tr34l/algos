"""
Problem: Count Connected Components

Given an undirected graph, count the number of connected components.

Example:
Graph components: 0-1-2, 3-4, 5
Output: 3

Expected Complexity: O(V + E)
"""


def count_components(adj):
    # TODO: run DFS/BFS from each unvisited vertex
    pass


if __name__ == "__main__":
    adj = [[1], [0, 2], [1], [4], [3], []]
    assert count_components(adj) == 3
    print("All tests passed")
