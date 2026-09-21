"""
Problem: Minimum CDs for Songs in Given Order

Given song lengths in fixed order and CD capacity m, return minimum number of CDs
needed. Songs cannot be split and order must be preserved. Return -1 if any song
is longer than m.

Expected Complexity: O(n)
"""


def min_cds(songs, m):
    # TODO: greedily fill current CD, then move to next CD
    pass


if __name__ == "__main__":
    assert min_cds([4, 3, 5, 2, 1], 7) == 3
    assert min_cds([8, 1], 7) == -1
    print("All tests passed")
