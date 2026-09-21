"""
Problem: DFS Edge Classification in Directed Graph

Given a directed graph, classify edges encountered during DFS as:
1. Tree Edge
2. Back Edge
3. Forward Edge
4. Cross Edge

Idea:
Use DFS colors:
WHITE = unvisited
GRAY = currently in recursion stack
BLACK = fully processed

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

WHITE, GRAY, BLACK = 0, 1, 2


def dfs_classify(u, adj, color, disc, finish, timer):
    color[u] = GRAY
    disc[u] = timer[0]
    timer[0] += 1

    for v in adj[u]:
        if color[v] == WHITE:
            print(f"{u} -> {v}: Tree Edge")
            dfs_classify(v, adj, color, disc, finish, timer)
        elif color[v] == GRAY:
            print(f"{u} -> {v}: Back Edge")
        else:
            if disc[u] < disc[v]:
                print(f"{u} -> {v}: Forward Edge")
            else:
                print(f"{u} -> {v}: Cross Edge")

    color[u] = BLACK
    finish[u] = timer[0]
    timer[0] += 1


def classify_edges(adj):
    V = len(adj)
    color = [WHITE] * V
    disc = [0] * V
    finish = [0] * V
    timer = [0]

    for i in range(V):
        if color[i] == WHITE:
            dfs_classify(i, adj, color, disc, finish, timer)


if __name__ == "__main__":
    adj = [
        [1, 2],
        [2],
        [0, 3],
        []
    ]
    classify_edges(adj)
