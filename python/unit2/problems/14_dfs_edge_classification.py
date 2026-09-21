"""
Problem: DFS Edge Classification in Directed Graph

Given a directed graph, classify edges encountered during DFS as:
Tree Edge, Back Edge, Forward Edge, or Cross Edge.

Return a list of tuples:
(u, v, edge_type)

Expected Complexity: O(V + E)
"""


def classify_edges(adj):
    # TODO: use DFS colors and discovery times
    pass


if __name__ == "__main__":
    adj = [[1, 2], [2], [0, 3], []]
    result = classify_edges(adj)
    assert isinstance(result, list)
    print("Implement and inspect result:", result)
