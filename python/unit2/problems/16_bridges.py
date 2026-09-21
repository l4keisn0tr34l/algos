"""
Problem: Bridges in an Undirected Graph

Given an undirected graph, return all bridges. A bridge is an edge whose removal
increases the number of connected components.

Example:
Input graph: 0-1-2-3
Output: [(0,1), (1,2), (2,3)] in any DFS-valid order

Expected Complexity: O(V + E)
"""


def find_bridges(adj):
    # TODO: use DFS discovery time and low values
    pass


if __name__ == "__main__":
    adj = [[1], [0, 2], [1, 3], [2]]
    result = find_bridges(adj)
    assert set(tuple(sorted(e)) for e in result) == {(0, 1), (1, 2), (2, 3)}
    print("All tests passed")
