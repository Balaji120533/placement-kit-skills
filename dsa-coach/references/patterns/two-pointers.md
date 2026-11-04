# Two pointers

**Invariant:** everything outside `[l, r]` has already been ruled out. Each step moves one pointer inward and discards candidates that cannot be an answer.

## Signals
- Sorted array (or sortable) with a pair/triplet target sum
- "In-place", "O(1) extra space", partition, remove duplicates
- Palindrome check, merging two sorted arrays, container/area problems

## Template (pair with target sum in a sorted array) — verified
```python
def two_sum_sorted(a, t):
    l, r = 0, len(a) - 1
    while l < r:
        s = a[l] + a[r]
        if s == t:
            return [l, r]
        if s < t:
            l += 1      # need a bigger sum: only moving l right can help
        else:
            r -= 1      # need a smaller sum
    return []
```
Time O(n): `r - l` shrinks by 1 every iteration. Space O(1).

## Dry run: a = [1,2,4,7,11], t = 9
| step | l | r | a[l]+a[r] | action |
| --- | --- | --- | --- | --- |
| 1 | 0 | 4 | 12 | > 9, r-- |
| 2 | 0 | 3 | 8 | < 9, l++ |
| 3 | 1 | 3 | 9 | found [1,3] |

## Misconceptions
- Using it on an unsorted array without sorting first (sorting costs O(n log n) and loses original indices).
- Moving both pointers on a non-match. Only one side is provably useless.
- Skipping duplicate handling in 3Sum (gives repeated triplets).

## Ladder
Easy: Valid Palindrome (LeetCode) → Medium: 3Sum (LeetCode) → Harder: Trapping Rain Water (LeetCode).

## Interviewer twists
Return all pairs; count pairs; array is not sorted (hash map instead); k-sum generalisation.
