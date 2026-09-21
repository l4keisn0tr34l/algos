"""
Problem: First 1 in a Sorted Binary Array

Given a sorted binary array containing only 0s and 1s, find the index of the
first occurrence of 1. If 1 is not present, return -1.

Example:
Input:  arr = [0, 0, 0, 0, 1, 1]
Output: 4

Expected Complexity: O(log n)
"""


def first_one(arr):
    low = 0
    high = len(arr)-1
    ans = -1
    while low<=high:
        mid = int(low + (high-low)/2)
        if arr[mid]==1:
            ans = mid
            high = mid -1
        else:
            low = mid +1
    return ans

if __name__ == "__main__":
    assert first_one([0, 0, 0, 0, 1, 1]) == 4
    assert first_one([0, 0, 0]) == -1
    print("All tests passed")
