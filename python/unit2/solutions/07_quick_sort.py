"""
Problem: Quick Sort

Given an array of integers, sort it in ascending order using Quick Sort.

Example:
Input:  arr = [4, 1, 6, 3, 9, 2, 7, 5]
Output: [1, 2, 3, 4, 5, 6, 7, 9]

Idea:
Choose a pivot, partition elements smaller than pivot to the left and greater
than pivot to the right, then recursively sort both sides.

Time Complexity:
Best/Average: O(n log n)
Worst: O(n^2)
Space Complexity: O(log n) average recursion stack, O(n) worst case
"""


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)


if __name__ == "__main__":
    arr = [4, 1, 6, 3, 9, 2, 7, 5]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
