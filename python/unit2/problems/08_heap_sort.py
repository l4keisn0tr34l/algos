"""
Problem: Heap Sort

Given an array of integers, sort it in ascending order using Heap Sort.
Modify the array in-place.

Example:
Input:  arr = [15, 19, 10, 7, 17, 6]
Output: [6, 7, 10, 15, 17, 19]

Expected Complexity: O(n log n)
"""


def max_heapify(arr, n, i):
    # TODO: restore max-heap property at index i
    pass


def build_max_heap(arr):
    # TODO: convert array into max heap
    pass


def heap_sort(arr):
    # TODO: implement heap sort
    pass


if __name__ == "__main__":
    arr = [15, 19, 10, 7, 17, 6]
    heap_sort(arr)
    assert arr == [6, 7, 10, 15, 17, 19]
    print("All tests passed")
