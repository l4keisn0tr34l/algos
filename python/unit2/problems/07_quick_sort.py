"""
Problem: Quick Sort

Given an array of integers, sort it in ascending order using Quick Sort.
Modify the array in-place.

Example:
Input:  arr = [4, 1, 6, 3, 9, 2, 7, 5]
Output: [1, 2, 3, 4, 5, 6, 7, 9]

Expected Complexity: Average O(n log n), Worst O(n^2)
"""


def partition(arr, low, high):
    # TODO: partition using arr[high] as pivot
    pass


def quick_sort(arr, low, high):
    # TODO: implement quick sort
    pass


if __name__ == "__main__":
    arr = [4, 1, 6, 3, 9, 2, 7, 5]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 9]
    print("All tests passed")
