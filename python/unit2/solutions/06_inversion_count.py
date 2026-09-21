"""
Problem: Count Inversions

Given an array, count the number of inversions. An inversion is a pair (i, j)
such that i < j and arr[i] > arr[j].

Example:
Input:  arr = [2, 4, 1, 3]
Output: 3
Explanation: (2,1), (4,1), (4,3)

Idea:
Modify Merge Sort. During merge, if left element > right element, then that
right element forms inversions with all remaining elements in the left half.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""


def merge_and_count(arr, low, mid, high):
    temp = []
    i, j = low, mid + 1
    count = 0

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            count += mid - i + 1
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= high:
        temp.append(arr[j])
        j += 1

    for k in range(low, high + 1):
        arr[k] = temp[k - low]

    return count


def count_inversions(arr, low, high):
    if low >= high:
        return 0

    mid = low + (high - low) // 2

    left = count_inversions(arr, low, mid)
    right = count_inversions(arr, mid + 1, high)
    cross = merge_and_count(arr, low, mid, high)

    return left + right + cross


if __name__ == "__main__":
    arr = [2, 4, 1, 3]
    print(count_inversions(arr, 0, len(arr) - 1))
