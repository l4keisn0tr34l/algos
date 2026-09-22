"""
Lab 04: Priority Queue using MinHeap
"""


class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            p = self.parent(i)
            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            i = p

    def get_min(self):
        if not self.heap:
            return None
        return self.heap[0]

    def extract_min(self):
        if not self.heap:
            return None

        minimum = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        if self.heap:
            self._heapify_down(0)

        return minimum

    def _heapify_down(self, i):
        n = len(self.heap)

        while True:
            smallest = i
            l = self.left(i)
            r = self.right(i)

            if l < n and self.heap[l] < self.heap[smallest]:
                smallest = l
            if r < n and self.heap[r] < self.heap[smallest]:
                smallest = r

            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest


if __name__ == "__main__":
    pq = MinHeap()
    for x in [5, 3, 8, 1, 2]:
        pq.insert(x)

    print("Heap:", pq.heap)
    print("Min:", pq.get_min())

    while pq.heap:
        print(pq.extract_min(), end=" ")
    print()
