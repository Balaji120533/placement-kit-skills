# Binary search

**Invariant:** the answer always lies in `[lo, hi)`. Each step discards half by testing a monotone yes/no condition.

## Signals
- Sorted array, "find first/last position", "insert position"
- n up to 10^5–10^9 and a target of O(log n)
- "Minimum value such that [condition holds]" (binary search on the answer: capacity, speed, days)
- Rotated sorted array

## Template (lower bound: first index with a[i] ≥ x) — verified
```python
def lower_bound(a, x):
    lo, hi = 0, len(a)        # hi is exclusive: answer may be len(a)
    while lo < hi:
        m = (lo + hi) // 2    # in Java/C++ use lo + (hi - lo) / 2 to avoid overflow
        if a[m] < x:
            lo = m + 1
        else:
            hi = m
    return lo
```
Time O(log n): the range halves each iteration. Space O(1).

## Dry run: a = [1,3,3,5], x = 3
| lo | hi | m | a[m] | action |
| --- | --- | --- | --- | --- |
| 0 | 4 | 2 | 3 | not < 3, hi = 2 |
| 0 | 2 | 1 | 3 | not < 3, hi = 1 |
| 0 | 1 | 0 | 1 | < 3, lo = 1 |
| 1 | 1 | – | – | stop, answer 1 |

## Binary search on the answer
Define `ok(v)` that is false…false true…true. Search the smallest `v` with `ok(v)`. Complexity = log(range) × cost of `ok`.

## Misconceptions
- Mixing `hi = n - 1` with `lo < hi` (infinite loop or missed element). Pick one convention and keep it.
- `lo = m` instead of `m + 1` when `m` is excluded: infinite loop.
- Integer overflow in `(lo + hi) / 2` in Java/C++.
- Applying it when the condition is not monotone.

## Ladder
Easy: Binary Search → Medium: Search in Rotated Sorted Array → Harder: Koko Eating Bananas / Capacity to Ship Packages (all LeetCode).

## Interviewer twists
Duplicates; first vs last occurrence; floating point answer (fixed iteration count); search in a 2D matrix.
