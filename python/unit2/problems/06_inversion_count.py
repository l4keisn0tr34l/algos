"""
Problem: Count Inversions

Given an array, count the number of inversions. An inversion is a pair (i, j)
such that i < j and arr[i] > arr[j].

Example:
Input:  arr = [2, 4, 1, 3]
Output: 3

Expected Complexity: O(n log n)
"""


def merge_and_count(arr, low, mid, high):
    # TODO: merge while counting cross inversions
    pass


def count_inversions(arr, low, high):
    # TODO: implement modified merge sort
    pass


if __name__ == "__main__":
    arr = [2, 4, 1, 3]
    assert count_inversions(arr, 0, len(arr) - 1) == 3
    arr = [5, 4, 3, 2, 1]
    assert count_inversions(arr, 0, len(arr) - 1) == 10
    print("All tests passed")
