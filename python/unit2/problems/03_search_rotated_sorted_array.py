"""
Problem: Search in Rotated Sorted Array

Given a sorted array that has been rotated at some pivot, find the index of a
target value. If target is not present, return -1.

Example:
Input:  arr = [35, 42, 5, 15, 27, 29], target = 15
Output: 3

Expected Complexity: O(log n)
"""


def search_rotated(arr, target):
    low = 0
    high = len(arr)-1

    while low<=high:
        mid = int(low + (high-low)/2)
        if arr[mid]==target:
            return mid
        if arr[low]>arr[mid]:
            if arr[low]<=target<arr[mid]:
                high = mid -1
            else: 
                low = mid +1

        else: 
            if arr[mid]<=target<arr[high]:
                low = mid +1
            else:
                high = mid -1
    return -1


if __name__ == "__main__":
    assert search_rotated([35, 42, 5, 15, 27, 29], 15) == 3
    assert search_rotated([35, 42, 5, 15, 27, 29], 100) == -1
    print("All tests passed")
