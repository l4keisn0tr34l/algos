"""
Problem: Merge Sort

Given an array of integers, sort it in ascending order using Merge Sort.

Example:
Input:  arr = [8, 3, 2, 9, 7, 1]
Output: [1, 2, 3, 7, 8, 9]

Idea:
Divide the array into two halves, sort both halves recursively, and merge the
sorted halves.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""


def merge(arr, low, mid, high):
    temp = []
    i, j = low, mid + 1

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= high:
        temp.append(arr[j])
        j += 1

    for k in range(low, high + 1):
        arr[k] = temp[k - low]


def merge_sort(arr, low, high):
    if low >= high:
        return

    mid = low + (high - low) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)
    merge(arr, low, mid, high)


if __name__ == "__main__":
    arr = [8, 3, 2, 9, 7, 1]
    merge_sort(arr, 0, len(arr) - 1)
    print(arr)
