"""
Lab 09: Fractional Knapsack
"""


def fractional_knapsack(items, capacity):
    # item = (value, weight)
    items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)
    profit = 0.0
    taken = []

    for value, weight in items:
        if capacity == 0:
            break

        if weight <= capacity:
            profit += value
            capacity -= weight
            taken.append((value, weight, 1.0))
        else:
            fraction = capacity / weight
            profit += value * fraction
            taken.append((value, weight, fraction))
            capacity = 0

    return profit, taken


if __name__ == "__main__":
    items = [(60, 10), (100, 20), (120, 30)]
    profit, taken = fractional_knapsack(items, 50)
    print("Profit:", profit)
    print("Taken:", taken)
