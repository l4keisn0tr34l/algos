"""
Problem: Fixed Point in Sorted Array

Given a sorted array of distinct integers, find an index i such that arr[i] == i.
If no such index exists, return -1.

Example:
Input:  arr = [-10, -5, 0, 3, 7]
Output: 3

Expected Complexity: O(log n)
"""


def fixed_point(arr):
    low = 0
    high = len(arr) - 1

    while low<=high:
        mid=int(low + (high-low)/2)
        if arr[mid]==mid:
            return mid
        if arr[mid]>arr[low]:
            low = mid +1

        else: 
            high = mid -1
    return -1

if __name__ == "__main__":
    assert fixed_point([-10, -5, 0, 3, 7]) == 3
    assert fixed_point([1, 2, 3, 4]) == -1
    print("All tests passed")
