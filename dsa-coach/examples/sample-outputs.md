# Sample outputs

What good output looks like in each built mode. These show shape and length, not text to repeat. For Explain-back, see the worked example in `../references/interview-rubric.md`.

## Coach, first turn

**Student:** Help me solve Two Sum.

**Coach:**

> This is LeetCode 1. n goes up to 10^4, so O(n^2) is about 10^8 operations and borderline; aim for O(n) or O(n log n).
>
> What is your brute force, and what is its bottleneck?

Shows the constraints and one question. No pattern name, no similar problems, no code.

## Coach, after "I don't know"

**Coach:**

> No problem. Pick the first number in the array. How would you find its partner, and how much work does that take?

A nudge is a question, one rung up the hint ladder. It does not mention a hash map.

## Debug, failing code

**Student:** My code gives wrong answer for longest substring without repeating characters.

```python
1  def longest(s):
2      seen = {}
3      l = best = 0
4      for r, c in enumerate(s):
5          if c in seen:
6              l = seen[c] + 1
7          seen[c] = r
8          best = max(best, r - l + 1)
9      return best
```

**Debug:**

> **Failing input:** `"abba"`
> **Expected vs actual:** expected 2, got 3.
> **Reason:** at the last `a`, `seen['a']` is 0, which is already outside the window. The code still moves `l`, and it moves it backwards from 2 to 1.
> **Exact line:** line 6, `l = seen[c] + 1`, because the check on line 5 doesn't test whether that index is inside the window.
> **Fix hint:** only move `l` when the previous copy is inside the current window.

No rewritten code.

## Debug, walkthrough

**Student:** Dry run this with [2,7,11,15], target 9.

```python
1  def two_sum(a, t):
2      seen = {}
3      for i, x in enumerate(a):
4          if t - x in seen:
5              return [seen[t - x], i]
6          seen[x] = i
```

**Debug:**

> | i | x | t - x | seen before | action |
> | --- | --- | --- | --- | --- |
> | 0 | 2 | 7 | {} | not found, store 2 |
> | 1 | 7 | 2 | {2:0} | found, return [0,1] |
>
> **Time:** O(n). The loop on line 3 runs at most n times, and lines 4 and 6 are O(1) on average.
> **Space:** O(n). `seen` holds at most n entries.

## Quick

**Student:** Quick: Two Sum

**Quick:**

> **Pattern:** hashing
> **Key observation:** for each number, its partner is exactly target minus that number.
> **Approach:** scan once, look up the partner in a hash map, then store the current number.
> **Time:** O(n), one pass with O(1) average lookups.
> **Space:** O(n), the map holds up to n numbers.

Exactly 5 lines.
