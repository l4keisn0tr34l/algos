"""
Problem: Disjoint Set Union

Implement DSU with find and union operations.

Expected Complexity: almost O(1) amortized per operation with path compression
and union by rank/size.
"""


class DSU:
    def __init__(self, n):
        # TODO: initialize parent and rank/size arrays
        pass

    def find(self, x):
        # TODO: return representative of x's set
        pass

    def union(self, a, b):
        # TODO: merge sets of a and b, return True if merged else False
        pass


if __name__ == "__main__":
    dsu = DSU(5)
    assert dsu.union(0, 1) is True
    assert dsu.union(1, 2) is True
    assert dsu.find(0) == dsu.find(2)
    assert dsu.union(0, 2) is False
    print("All tests passed")
