"""
Problem: Binary Search

Given a sorted array of integers and a target value, return the index of the
target if it exists. Otherwise, return -1.

Example:
Input:  arr = [3, 5, 8, 12, 23, 40], target = 23
Output: 4

Idea:
Repeatedly check the middle element and discard half of the search space.

Time Complexity: O(log n)
Space Complexity: O(1)
"""


def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


if __name__ == "__main__":
    arr = [3, 5, 8, 12, 23, 40]
    target = 23
    print(binary_search(arr, target))
