"""
Problem: Activity Selection

Given activities as (start, finish), select the maximum number of non-overlapping
activities.

Example:
Input:  [(1,4), (3,5), (0,6), (5,7), (8,9), (5,9)]
Output: [(1,4), (5,7), (8,9)]

Expected Complexity: O(n log n)
"""


def activity_selection(activities):
    # TODO: sort by finish time and greedily select compatible activities
    pass


if __name__ == "__main__":
    acts = [(1,4), (3,5), (0,6), (5,7), (8,9), (5,9)]
    assert activity_selection(acts) == [(1,4), (5,7), (8,9)]
    print("All tests passed")
