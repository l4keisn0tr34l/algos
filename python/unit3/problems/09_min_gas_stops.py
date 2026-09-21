"""
Problem: Minimum Gas Stops

A car can travel at most m distance on a full tank. Given sorted station positions
including start 0 and destination, return minimum stops needed between start and
destination. Return -1 if impossible.

Example:
Input: stations=[0,10,20,30,60], m=30
Output: 1   # stop at 30

Expected Complexity: O(n)
"""


def min_gas_stops(stations, m):
    # TODO: greedily jump to farthest reachable station
    pass


if __name__ == "__main__":
    assert min_gas_stops([0,10,20,30,60], 30) == 1
    assert min_gas_stops([0,10,45], 30) == -1
    print("All tests passed")
