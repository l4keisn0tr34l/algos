"""
Problem: Bridges in an Undirected Graph

Given an undirected graph, find all bridges. A bridge is an edge whose removal
increases the number of connected components.

Example:
Graph: 0-1-2-3
Output: [(2, 3), (1, 2), (0, 1)]

Idea:
Use DFS discovery time and low value.
For DFS edge (u, v), if low[v] > disc[u], then (u, v) is a bridge.

Time Complexity: O(V + E)
Space Complexity: O(V)
"""


def dfs_bridge(u, adj, visited, disc, low, parent, bridges, timer):
    visited[u] = True
    disc[u] = low[u] = timer[0]
    timer[0] += 1

    for v in adj[u]:
        if not visited[v]:
            parent[v] = u
            dfs_bridge(v, adj, visited, disc, low, parent, bridges, timer)

            low[u] = min(low[u], low[v])

            if low[v] > disc[u]:
                bridges.append((u, v))

        elif v != parent[u]:
            low[u] = min(low[u], disc[v])


def find_bridges(adj):
    V = len(adj)
    visited = [False] * V
    disc = [0] * V
    low = [0] * V
    parent = [-1] * V
    bridges = []
    timer = [0]

    for i in range(V):
        if not visited[i]:
            dfs_bridge(i, adj, visited, disc, low, parent, bridges, timer)

    return bridges


if __name__ == "__main__":
    adj = [
        [1],       # 0
        [0, 2],    # 1
        [1, 3],    # 2
        [2]        # 3
    ]
    print(find_bridges(adj))
