# Sliding window

**Invariant:** the window `[l, r]` always satisfies the problem's validity condition after the shrink step. Each element enters once and leaves once.

## Signals
- Longest/shortest/count of contiguous subarray or substring
- Condition on a window: "at most k distinct", "no repeats", "sum ≥ target"
- Positive numbers only (for sum windows); negatives break the shrink logic

## Template (longest substring without repeating characters) — verified
```python
def longest_unique(s):
    seen = {}            # char -> last index
    l = best = 0
    for r, c in enumerate(s):
        if c in seen and seen[c] >= l:
            l = seen[c] + 1          # shrink past the previous copy
        seen[c] = r
        best = max(best, r - l + 1)
    return best
```
Time O(n): `r` moves once, `l` only moves forward. Space O(min(n, alphabet size)).

## Dry run: s = "abcabcbb"
| r | char | l after | window | best |
| --- | --- | --- | --- | --- |
| 0 | a | 0 | a | 1 |
| 1 | b | 0 | ab | 2 |
| 2 | c | 0 | abc | 3 |
| 3 | a | 1 | bca | 3 |
| 4 | b | 2 | cab | 3 |
| 5 | c | 3 | abc | 3 |
| 6 | b | 5 | cb | 3 |
| 7 | b | 7 | b | 3 |

## Misconceptions
- Forgetting `seen[c] >= l`: an old index outside the window must not move `l` backwards.
- Using this for sums with negative numbers (use prefix sums + hash map instead).
- Thinking nested while loops mean O(n²). Each pointer moves at most n times.

## Ladder
Easy: Maximum Average Subarray I → Medium: Longest Substring Without Repeating Characters → Harder: Minimum Window Substring (all LeetCode).

## Interviewer twists
Return the substring, not the length; at most k distinct characters; count windows instead of longest.
