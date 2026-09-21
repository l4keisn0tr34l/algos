"""
Problem: Articulation Points / Cut Vertices

Given an undirected graph, find all articulation points. A vertex is an
articulation point if removing it increases the number of connected components.

Example:
Graph: 0-1-2-3
Output: [1, 2]

Idea:
Use DFS discovery time and low value.
A non-root u is articulation point if low[child] >= disc[u].
A root is articulation point if it has more than one DFS child.

Time Complexity: O(V + E)
Space Complexity: O(V)
"""


def dfs_ap(u, adj, visited, disc, low, parent, is_ap, timer):
    visited[u] = True
    disc[u] = low[u] = timer[0]
    timer[0] += 1
    children = 0

    for v in adj[u]:
        if not visited[v]:
            parent[v] = u
            children += 1
            dfs_ap(v, adj, visited, disc, low, parent, is_ap, timer)

            low[u] = min(low[u], low[v])

            if parent[u] == -1 and children > 1:
                is_ap[u] = True

            if parent[u] != -1 and low[v] >= disc[u]:
                is_ap[u] = True

        elif v != parent[u]:
            low[u] = min(low[u], disc[v])


def articulation_points(adj):
    V = len(adj)
    visited = [False] * V
    disc = [0] * V
    low = [0] * V
    parent = [-1] * V
    is_ap = [False] * V
    timer = [0]

    for i in range(V):
        if not visited[i]:
            dfs_ap(i, adj, visited, disc, low, parent, is_ap, timer)

    return [i for i in range(V) if is_ap[i]]


if __name__ == "__main__":
    adj = [
        [1],       # 0
        [0, 2],    # 1
        [1, 3],    # 2
        [2]        # 3
    ]
    print(articulation_points(adj))
