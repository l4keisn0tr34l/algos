"""
Problem: Fractional Knapsack

Given items as (value, weight) and capacity W, maximize total value. You may take
fractions of items.

Example:
Input: items = [(60,10), (100,20), (120,30)], W = 50
Output: 240.0

Expected Complexity: O(n log n)
"""


def fractional_knapsack(items, W):
    # TODO: sort by value/weight ratio decreasing and take greedily
    pass


if __name__ == "__main__":
    items = [(60,10), (100,20), (120,30)]
    assert abs(fractional_knapsack(items, 50) - 240.0) < 1e-9
    print("All tests passed")
