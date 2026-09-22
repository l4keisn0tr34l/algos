"""
Lab 11: Longest Common Subsequence using Dynamic Programming
Displays length table and direction table.
"""


def lcs(X, Y):
    m, n = len(X), len(Y)
    L = [[0] * (n + 1) for _ in range(m + 1)]
    direction = [[""] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                L[i][j] = 1 + L[i - 1][j - 1]
                direction[i][j] = "D"
            elif L[i - 1][j] >= L[i][j - 1]:
                L[i][j] = L[i - 1][j]
                direction[i][j] = "U"
            else:
                L[i][j] = L[i][j - 1]
                direction[i][j] = "L"

    # reconstruct LCS
    i, j = m, n
    result = []

    while i > 0 and j > 0:
        if direction[i][j] == "D":
            result.append(X[i - 1])
            i -= 1
            j -= 1
        elif direction[i][j] == "U":
            i -= 1
        else:
            j -= 1

    result.reverse()
    return L, direction, "".join(result)


def print_table(table, name):
    print(name)
    for row in table:
        print(row)
    print()


if __name__ == "__main__":
    X = "ABCBDAB"
    Y = "BDCABA"

    L, direction, ans = lcs(X, Y)

    print_table(L, "LCS Length Table:")
    print_table(direction, "Direction Table:")
    print("LCS length:", len(ans))
    print("LCS:", ans)
