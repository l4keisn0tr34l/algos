# 11 — Longest Common Subsequence using DP

## Problem

Given two strings `X` and `Y`, find the longest subsequence common to both.

Subsequence does not need to be contiguous.

## DP State

```text
L[i][j] = length of LCS of X[0...i-1] and Y[0...j-1]
```

## Recurrence

If characters match:

```text
X[i-1] == Y[j-1]
L[i][j] = 1 + L[i-1][j-1]
```

Otherwise:

```text
L[i][j] = max(L[i-1][j], L[i][j-1])
```

## Direction Table

Use a direction table to reconstruct LCS:

```text
D = diagonal match
U = came from up
L = came from left
```

## Complexity

```text
Time: O(mn)
Space: O(mn)
```
