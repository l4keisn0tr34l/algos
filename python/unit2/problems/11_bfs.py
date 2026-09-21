"""
Problem: Breadth First Search Traversal

Given an undirected graph and a source vertex, return BFS traversal from the
source.

Example:
Input: adj = [[1,2], [0,3], [0,4], [1], [2]], source = 0
Output: [0, 1, 2, 3, 4]

Expected Complexity: O(V + E)
"""


def bfs(adj, source):
    # TODO: implement BFS using queue
    pass


if __name__ == "__main__":
    adj = [[1, 2], [0, 3], [0, 4], [1], [2]]
    assert bfs(adj, 0) == [0, 1, 2, 3, 4]
    print("All tests passed")
