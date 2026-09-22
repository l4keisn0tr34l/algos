"""
Lab 10: 0/1 Knapsack using Dynamic Programming
Displays C[][] and Keep[][] tables.
"""


def knapsack_01(weights, values, capacity):
    n = len(weights)
    C = [[0] * (capacity + 1) for _ in range(n + 1)]
    Keep = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        wt = weights[i - 1]
        val = values[i - 1]

        for w in range(capacity + 1):
            if wt <= w and val + C[i - 1][w - wt] > C[i - 1][w]:
                C[i][w] = val + C[i - 1][w - wt]
                Keep[i][w] = 1
            else:
                C[i][w] = C[i - 1][w]
                Keep[i][w] = 0

    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if Keep[i][w] == 1:
            selected.append(i - 1)
            w -= weights[i - 1]

    selected.reverse()
    return C, Keep, C[n][capacity], selected


def print_table(table, name):
    print(name)
    for row in table:
        print(row)
    print()


if __name__ == "__main__":
    weights = [4, 7, 5, 3]
    values = [40, 42, 25, 12]
    capacity = 16

    C, Keep, max_value, selected = knapsack_01(weights, values, capacity)

    print_table(C, "C Table:")
    print_table(Keep, "Keep Table:")
    print("Maximum value:", max_value)
    print("Selected item indices:", selected)
