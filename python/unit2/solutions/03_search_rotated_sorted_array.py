"""
Problem: Search in Rotated Sorted Array

Given a sorted array that has been rotated at some pivot, find the index of a
target value. If target is not present, return -1.

Example:
Input:  arr = [35, 42, 5, 15, 27, 29], target = 15
Output: 3

Idea:
At every mid, at least one side is sorted. Decide which side is sorted and
check whether the target lies in that side.

Time Complexity: O(log n)
Space Complexity: O(1)
"""


def search_rotated(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid

        # Left half is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


if __name__ == "__main__":
    arr = [35, 42, 5, 15, 27, 29]
    target = 15
    print(search_rotated(arr, target))
