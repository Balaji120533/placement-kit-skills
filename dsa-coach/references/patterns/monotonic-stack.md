# Stack and monotonic stack

**Invariant:** the stack holds indices whose answer is still unknown, kept in monotone order of value. A new element resolves every smaller (or larger) element on top.

## Signals
- "Next greater/smaller element", "days until warmer"
- Largest rectangle in histogram, trapping rain water
- Matching brackets, nested structure, undo behaviour

## Template (next greater element to the right) — verified
```python
def next_greater(a):
    res = [-1] * len(a)
    st = []                          # indices, values strictly decreasing
    for i, x in enumerate(a):
        while st and a[st[-1]] < x:  # x is the next greater for these
            res[st.pop()] = x
        st.append(i)
    return res
```
Time O(n): every index is pushed once and popped at most once, so the inner while is O(n) in total. Space O(n).

## Dry run: a = [2,1,2,4,3]
| i | x | pops (index→value) | stack after (indices) |
| --- | --- | --- | --- |
| 0 | 2 | – | [0] |
| 1 | 1 | – | [0,1] |
| 2 | 2 | 1→2 | [0,2] |
| 3 | 4 | 2→4, 0→4 | [3] |
| 4 | 3 | – | [3,4] |
Result: [4,2,4,−1,−1]; indices left on the stack have no greater element.

## Misconceptions
- Believing the nested loop is O(n²).
- Strict vs non-strict comparison: `<` vs `<=` changes how equal values behave. Decide from the problem.
- Storing values instead of indices when distances are needed.
- Circular arrays: iterate 2n times.

## Ladder
Easy: Valid Parentheses → Medium: Daily Temperatures / Next Greater Element II → Harder: Largest Rectangle in Histogram (all LeetCode).

## Interviewer twists
Next smaller to the left; circular array; compute the answer in one pass for both sides.
