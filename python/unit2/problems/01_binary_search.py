"""
Problem: Binary Search

Given a sorted array of integers and a target value, return the index of the
target if it exists. Otherwise, return -1.

Example:
Input:  arr = [3, 5, 8, 12, 23, 40], target = 23
Output: 4

Expected Complexity: O(log n)
"""


def binary_search(arr, target):
    low = 0
    high = len(arr)

    while low<=high :
        mid = int(low + (high-low)/2)
        if arr[mid]==target:
            return mid
        elif target > arr[mid]:
            low = mid + 1
        else: 
            high = mid - 1
    return -1
    

if __name__ == "__main__":
    assert binary_search([3, 5, 8, 12, 23, 40], 23) == 4
    assert binary_search([3, 5, 8, 12, 23, 40], 7) == -1
    print("All tests passed")
