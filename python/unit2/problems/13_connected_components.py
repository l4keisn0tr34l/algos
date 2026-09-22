"""
Problem: Count Connected Components

Given an undirected graph, count the number of connected components.

Example:
Graph components: 0-1-2, 3-4, 5
Output: 3

Expected Complexity: O(V + E)
"""


def dfs_component(u, adj, visited):
    # TODO: helper DFS to mark all vertices in one component
    pass


def count_components(adj):
    # TODO:
    # 1. Create visited array.
    # 2. For each unvisited vertex, increment count and call dfs_component.
    # 3. Return count.
    pass


if __name__ == "__main__":
    adj = [[1], [0, 2], [1], [4], [3], []]
    assert count_components(adj) == 3
    print("All tests passed")
