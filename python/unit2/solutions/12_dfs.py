"""
Problem: Depth First Search Traversal

Given an undirected graph and a source vertex, print DFS traversal from the
source.

Example:
Graph:
0: [1, 2]
1: [0, 3]
2: [0, 4]
3: [1]
4: [2]
Source: 0
Output: [0, 1, 3, 2, 4]

Idea:
Use recursion to go as deep as possible before backtracking.

Time Complexity: O(V + E)
Space Complexity: O(V)
"""


def dfs_util(u, adj, visited, order):
    visited[u] = True
    order.append(u)

    for v in adj[u]:
        if not visited[v]:
            dfs_util(v, adj, visited, order)


def dfs(adj, source):
    V = len(adj)
    visited = [False] * V
    order = []
    dfs_util(source, adj, visited, order)
    return order


if __name__ == "__main__":
    adj = [[1, 2], [0, 3], [0, 4], [1], [2]]
    print(dfs(adj, 0))
