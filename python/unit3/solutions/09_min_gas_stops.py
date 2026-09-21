"""Reference solution: Minimum Gas Stops"""
def min_gas_stops(stations, m):
    n = len(stations)
    stops = 0
    current = 0
    while current < n - 1:
        last = current
        while current + 1 < n and stations[current + 1] - stations[last] <= m:
            current += 1
        if current == last:
            return -1
        if current < n - 1:
            stops += 1
    return stops

if __name__ == "__main__":
    assert min_gas_stops([0,10,20,30,60], 30) == 1
    assert min_gas_stops([0,10,45], 30) == -1
    print("All tests passed")
