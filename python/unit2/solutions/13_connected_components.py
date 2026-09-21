"""
Problem: Count Connected Components

Given an undirected graph, count the number of connected components.

Example:
Graph components: 0-1-2, 3-4, 5
Output: 3

Idea:
Run DFS from every unvisited vertex. Each new DFS call discovers one component.

Time Complexity: O(V + E)
Space Complexity: O(V)
"""


def dfs(u, adj, visited):
    visited[u] = True

    for v in adj[u]:
        if not visited[v]:
            dfs(v, adj, visited)


def count_components(adj):
    V = len(adj)
    visited = [False] * V
    count = 0

    for i in range(V):
        if not visited[i]:
            count += 1
            dfs(i, adj, visited)

    return count


if __name__ == "__main__":
    adj = [
        [1],       # 0
        [0, 2],    # 1
        [1],       # 2
        [4],       # 3
        [3],       # 4
        []         # 5
    ]
    print(count_components(adj))
