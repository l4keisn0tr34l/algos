# 01 — Execution Time Measurement

## Problem

Measure execution time of a program/algorithm.

## How to solve

1. Choose an algorithm/function to test.
2. Record start time before function call.
3. Run the function.
4. Record end time after function call.
5. Compute:

```text
elapsed time = end time - start time
```

## Python approach

Use:

```python
import time
start = time.perf_counter()
# algorithm call
end = time.perf_counter()
print(end - start)
```

## C++ equivalent

Use:

```cpp
#include <chrono>
```

and `chrono::high_resolution_clock`.

## Complexity note

Execution time depends on machine, compiler/interpreter, OS, and input size. Theoretical time complexity is still more important for DAA.
