"""
Problem: First 1 in a Sorted Binary Array

Given a sorted binary array containing only 0s and 1s, find the index of the
first occurrence of 1. If 1 is not present, return -1.

Example:
Input:  arr = [0, 0, 0, 0, 1, 1]
Output: 4

Idea:
Use binary search. When arr[mid] == 1, store mid as possible answer and
continue searching left.

Time Complexity: O(log n)
Space Complexity: O(1)
"""


def first_one(arr):
    low, high = 0, len(arr) - 1
    ans = -1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == 1:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


if __name__ == "__main__":
    arr = [0, 0, 0, 0, 1, 1]
    print(first_one(arr))
