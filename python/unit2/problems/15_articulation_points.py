"""
Problem: Articulation Points / Cut Vertices

Given an undirected graph, return all articulation points. A vertex is an
articulation point if removing it increases the number of connected components.

Example:
Input graph: 0-1-2-3
Output: [1, 2]

Expected Complexity: O(V + E)
"""


def articulation_points(adj):
    # TODO: use DFS discovery time and low values
    pass


if __name__ == "__main__":
    adj = [[1], [0, 2], [1, 3], [2]]
    assert articulation_points(adj) == [1, 2]
    print("All tests passed")
