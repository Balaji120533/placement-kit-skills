# Backtracking

**Invariant:** `cur` always holds a valid partial choice; after exploring a branch you undo the choice so the next branch starts clean.

## Signals
- "All subsets / permutations / combinations", n up to ~10–20 (see `../constraints.md`)
- Place items under constraints (N-Queens, Sudoku), generate valid strings (parentheses)
- Choose / explore / un-choose

## Template (all subsets) — verified
```python
def subsets(a):
    res, cur = [], []
    def go(i):
        if i == len(a):
            res.append(cur[:])      # copy, not a reference
            return
        go(i + 1)                   # skip a[i]
        cur.append(a[i])            # choose a[i]
        go(i + 1)
        cur.pop()                   # un-choose
    go(0)
    return res
```
Time O(n · 2^n): 2^n leaves, each copy costs up to n. Space O(n) recursion depth, excluding the output.

## Dry run: a = [1,2]
| call | cur | action |
| --- | --- | --- |
| go(0) | [] | skip 1 → go(1) |
| go(1) | [] | skip 2 → go(2): record [] |
| go(1) | [2] | choose 2 → go(2): record [2] |
| go(0) | [1] | choose 1 → go(1) |
| go(1) | [1] | skip 2 → record [1] |
| go(1) | [1,2] | choose 2 → record [1,2] |
Result: [], [2], [1], [1,2] (4 = 2^2 subsets).

## Misconceptions
- Appending `cur` instead of a copy (all results end up identical/empty).
- Forgetting to un-choose.
- Not pruning: add early exits (sum too large, column already used) to cut branches.
- Expecting polynomial time: output size alone can be exponential.

## Ladder
Easy: Subsets → Medium: Permutations / Combination Sum → Harder: N-Queens (all LeetCode).

## Interviewer twists
Duplicates in input (sort + skip equal siblings); count only; iterative bitmask version for subsets.
