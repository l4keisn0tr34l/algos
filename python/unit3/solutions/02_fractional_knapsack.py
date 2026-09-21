"""Reference solution: Fractional Knapsack"""

def fractional_knapsack(items, W):
    items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)
    profit = 0.0
    for value, weight in items:
        if W == 0:
            break
        if weight <= W:
            profit += value
            W -= weight
        else:
            profit += value * (W / weight)
            W = 0
    return profit

if __name__ == "__main__":
    items = [(60,10), (100,20), (120,30)]
    assert abs(fractional_knapsack(items, 50) - 240.0) < 1e-9
    print("All tests passed")
