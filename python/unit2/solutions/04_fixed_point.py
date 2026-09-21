"""
Problem: Fixed Point in Sorted Array

Given a sorted array of distinct integers, find an index i such that arr[i] == i.
If no such index exists, return -1.

Example:
Input:  arr = [-10, -5, 0, 3, 7]
Output: 3

Idea:
Use binary search. If arr[mid] > mid, search left. If arr[mid] < mid, search right.

Time Complexity: O(log n)
Space Complexity: O(1)
"""


def fixed_point(arr):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == mid:
            return mid
        elif arr[mid] > mid:
            high = mid - 1
        else:
            low = mid + 1

    return -1


if __name__ == "__main__":
    arr = [-10, -5, 0, 3, 7]
    print(fixed_point(arr))
