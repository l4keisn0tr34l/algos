"""
Problem: Breadth First Search Traversal

Given an undirected graph and a source vertex, print BFS traversal from the
source.

Example:
Graph:
0: [1, 2]
1: [0, 3]
2: [0, 4]
3: [1]
4: [2]
Source: 0
Output: [0, 1, 2, 3, 4]

Idea:
Use a queue and visit vertices level by level.

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from collections import deque


def bfs(adj, source):
    V = len(adj)
    visited = [False] * V
    order = []
    q = deque()

    visited[source] = True
    q.append(source)

    while q:
        u = q.popleft()
        order.append(u)

        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)

    return order


if __name__ == "__main__":
    adj = [[1, 2], [0, 3], [0, 4], [1], [2]]
    print(bfs(adj, 0))
