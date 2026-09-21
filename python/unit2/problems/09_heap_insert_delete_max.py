"""
Problem: Insert and Delete-Max in Max Heap

Implement two operations on a max heap:
1. Insert a new key.
2. Delete and return the maximum key.

Example:
Input heap: [19, 17, 10, 7, 15, 6]
Insert: 20
Delete max returns: 20

Expected Complexity: O(log n) per operation
"""


def max_heapify(heap, n, i):
    # TODO: restore max-heap property at index i
    pass


def insert(heap, key):
    # TODO: insert key into max heap
    pass


def delete_max(heap):
    # TODO: delete and return maximum element
    pass


if __name__ == "__main__":
    heap = [19, 17, 10, 7, 15, 6]
    insert(heap, 20)
    assert heap[0] == 20
    assert delete_max(heap) == 20
    print("All tests passed")
