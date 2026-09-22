"""
Lab 02: Iterative Merge Sort
"""


def merge(arr, left, mid, right):
    temp = []
    i, j = left, mid + 1

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1

    for k in range(left, right + 1):
        arr[k] = temp[k - left]


def iterative_merge_sort(arr):
    n = len(arr)
    size = 1

    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)

            if mid < right:
                merge(arr, left, mid, right)

        size *= 2


if __name__ == "__main__":
    arr = [8, 3, 2, 9, 7, 1]
    iterative_merge_sort(arr)
    print(arr)
