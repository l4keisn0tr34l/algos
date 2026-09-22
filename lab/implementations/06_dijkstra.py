"""
Lab 06: Dijkstra Single Source Shortest Path
"""

import heapq


def dijkstra(adj, source):
    V = len(adj)
    dist = [float("inf")] * V
    parent = [-1] * V
    dist[source] = 0

    heap = [(0, source)]

    while heap:
        d, u = heapq.heappop(heap)

        if d > dist[u]:
            continue

        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(heap, (dist[v], v))

    return dist, parent


if __name__ == "__main__":
    adj = [
        [(1, 4), (2, 1)],
        [(3, 1)],
        [(1, 2), (3, 5)],
        []
    ]

    dist, parent = dijkstra(adj, 0)
    print("Distances:", dist)
    print("Parents:", parent)
