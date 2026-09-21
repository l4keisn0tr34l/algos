"""
Problem: Depth First Search Traversal

Given an undirected graph and a source vertex, return DFS traversal from the
source. Visit neighbors in the order given in adjacency list.

Example:
Input: adj = [[1,2], [0,3], [0,4], [1], [2]], source = 0
Output: [0, 1, 3, 2, 4]

Expected Complexity: O(V + E)
"""


def dfs(adj, source):
    # TODO: implement recursive or iterative DFS
    pass


if __name__ == "__main__":
    adj = [[1, 2], [0, 3], [0, 4], [1], [2]]
    assert dfs(adj, 0) == [0, 1, 3, 2, 4]
    print("All tests passed")
