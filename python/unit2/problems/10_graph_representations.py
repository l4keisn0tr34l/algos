"""
Problem: Build Graph Representations

Given number of vertices and a list of undirected edges, build:
1. Adjacency matrix
2. Adjacency list

Example:
Input: V = 4, edges = [(0,1), (0,2), (1,3)]
Output adjacency list:
[[1,2], [0,3], [0], [1]]

Expected Space:
Matrix: O(V^2)
List: O(V + E)
"""


def build_matrix(V, edges):
    # TODO: build adjacency matrix
    pass


def build_list(V, edges):
    # TODO: build adjacency list
    pass


if __name__ == "__main__":
    V = 4
    edges = [(0, 1), (0, 2), (1, 3)]
    assert build_matrix(V, edges) == [[0,1,1,0],[1,0,0,1],[1,0,0,0],[0,1,0,0]]
    assert build_list(V, edges) == [[1,2],[0,3],[0],[1]]
    print("All tests passed")
