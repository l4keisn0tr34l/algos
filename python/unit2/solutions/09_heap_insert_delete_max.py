"""
Problem: Insert and Delete-Max in Max Heap

Implement two operations on a max heap:
1. Insert a new key.
2. Delete and return the maximum key.

Example:
Input heap: [19, 17, 10, 7, 15, 6]
Insert: 20
Heap after insert: [20, 17, 19, 7, 15, 6, 10]
Delete max returns: 20

Idea:
Insert: add at the end and bubble up.
Delete max: replace root with last element and heapify down.

Time Complexity: O(log n) per insert/delete
Space Complexity: O(1) auxiliary
"""


def max_heapify(heap, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and heap[left] > heap[largest]:
        largest = left

    if right < n and heap[right] > heap[largest]:
        largest = right

    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        max_heapify(heap, n, largest)


def insert(heap, key):
    heap.append(key)
    i = len(heap) - 1

    while i > 0:
        parent = (i - 1) // 2
        if heap[parent] >= heap[i]:
            break
        heap[parent], heap[i] = heap[i], heap[parent]
        i = parent


def delete_max(heap):
    if not heap:
        return None

    max_value = heap[0]
    heap[0] = heap[-1]
    heap.pop()

    if heap:
        max_heapify(heap, len(heap), 0)

    return max_value


if __name__ == "__main__":
    heap = [19, 17, 10, 7, 15, 6]
    insert(heap, 20)
    print(heap)
    print(delete_max(heap))
    print(heap)
