"""
Problem: Heap Sort

Given an array of integers, sort it in ascending order using Heap Sort.

Example:
Input:  arr = [15, 19, 10, 7, 17, 6]
Output: [6, 7, 10, 15, 17, 19]

Idea:
Build a max heap. Repeatedly move the maximum element at root to the end and
heapify the reduced heap.

Time Complexity: O(n log n)
Space Complexity: O(1)
"""


def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)


def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)


def heap_sort(arr):
    n = len(arr)
    build_max_heap(arr)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, i, 0)


if __name__ == "__main__":
    arr = [15, 19, 10, 7, 17, 6]
    heap_sort(arr)
    print(arr)
