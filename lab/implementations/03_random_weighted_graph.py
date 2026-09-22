"""
Lab 03: Random Weighted Undirected Simple Graph Generator
"""

import random


def generate_graph(n, density):
    max_edges = n * (n - 1) // 2
    e = int(density * max_edges)

    all_edges = []
    for u in range(n):
        for v in range(u + 1, n):
            all_edges.append((u, v))

    random.shuffle(all_edges)
    selected = all_edges[:e]

    matrix = [[0] * n for _ in range(n)]
    adj = [[] for _ in range(n)]

    weighted_edges = []
    for u, v in selected:
        w = random.randint(1, max(1, e))
        weighted_edges.append((u, v, w))
        matrix[u][v] = matrix[v][u] = w
        adj[u].append((v, w))
        adj[v].append((u, w))

    return weighted_edges, matrix, adj


if __name__ == "__main__":
    edges, matrix, adj = generate_graph(5, 0.6)

    print("Edges:")
    print(edges)

    print("\nAdjacency Matrix:")
    for row in matrix:
        print(row)

    print("\nAdjacency List:")
    for i, neighbors in enumerate(adj):
        print(i, ":", neighbors)
