# Constraint → target complexity

Read the input limit first. It tells you which complexity will pass (about 10^8 simple operations per second).

| n up to | Target complexity |
| --- | --- |
| ~10 | O(n!) |
| ~20 | O(2^n) |
| ~500 | O(n^3) |
| ~5,000 | O(n^2) |
| ~10^5 to 10^6 | O(n log n) or O(n) |
| larger | O(log n) or O(1) |

## How to use it

1. Find n in the constraints and read off the target.
2. Compare it with the brute force. If brute force is O(n^2) and n = 10^5, name that as the bottleneck.
3. Ask which observation removes the repeated work (sorting, hashing, a window, a stack, memoisation).

## Cautions

- Multiple inputs (n and m, or n and k) change the target; use the product or sum that appears.
- Hidden factors count: a sort inside a loop, string concatenation in a loop, or recursion depth near 10^5.
- The table is a guide. Always derive the final complexity from the actual code, never assume it.
