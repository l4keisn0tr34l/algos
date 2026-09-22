"""
Lab 08: Optimal Merge Pattern
"""

import heapq


def optimal_merge(files):
    heap = files[:]
    heapq.heapify(heap)
    total_cost = 0
    steps = []

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        cost = a + b
        total_cost += cost
        steps.append((a, b, cost))
        heapq.heappush(heap, cost)

    return total_cost, steps


if __name__ == "__main__":
    files = [20, 30, 10, 5, 30]
    cost, steps = optimal_merge(files)
    print("Steps:")
    for step in steps:
        print(step)
    print("Minimum total cost:", cost)
