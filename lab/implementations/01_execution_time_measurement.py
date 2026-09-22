"""
Lab 01: Execution Time Measurement

Measures running time of a sample algorithm using time.perf_counter().
"""

import time


def sample_algorithm(n):
    total = 0
    for i in range(n):
        total += i
    return total


if __name__ == "__main__":
    n = 1_000_000

    start = time.perf_counter()
    result = sample_algorithm(n)
    end = time.perf_counter()

    print("Result:", result)
    print("Execution time:", end - start, "seconds")
