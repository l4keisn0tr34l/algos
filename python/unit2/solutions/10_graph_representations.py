"""
Problem: Build Graph Representations

Given number of vertices and a list of edges, build:
1. Adjacency matrix
2. Adjacency list

Example:
Input: V = 4, edges = [(0,1), (0,2), (1,3)]
Output adjacency list:
0: [1, 2]
1: [0, 3]
2: [0]
3: [1]

Idea:
For an undirected graph, add both u->v and v->u.

Matrix Space: O(V^2)
List Space: O(V + E)
"""


def build_matrix(V, edges):
    matrix = [[0] * V for _ in range(V)]

    for u, v in edges:
        matrix[u][v] = 1
        matrix[v][u] = 1

    return matrix


def build_list(V, edges):
    adj = [[] for _ in range(V)]

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    return adj


if __name__ == "__main__":
    V = 4
    edges = [(0, 1), (0, 2), (1, 3)]

    print("Adjacency Matrix:")
    for row in build_matrix(V, edges):
        print(row)

    print("Adjacency List:")
    adj = build_list(V, edges)
    for i in range(V):
        print(i, ":", adj[i])
