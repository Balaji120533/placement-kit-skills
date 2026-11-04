# Hashing and prefix sums

**Invariant:** after processing index i, the map holds everything about prefixes up to i that a future index might need (counts of each prefix sum, last index of a value, etc.).

## Signals
- "Number of subarrays with sum k", "equal 0s and 1s", "divisible by k"
- Need O(1) lookup of "have I seen the complement/value before?"
- Negative numbers present (sliding window won't work)
- Frequency counting, grouping (anagrams), duplicates

## Template (count subarrays with sum k) — verified
```python
def subarray_sum_k(a, k):
    cnt = {0: 1}          # empty prefix has sum 0
    p = ans = 0
    for x in a:
        p += x                         # prefix sum up to this index
        ans += cnt.get(p - k, 0)       # earlier prefixes that make a sum-k subarray
        cnt[p] = cnt.get(p, 0) + 1
    return ans
```
Key identity: sum(i..j) = P[j] − P[i−1], so we need P[i−1] = P[j] − k.
Time O(n), one pass with O(1) average map operations. Space O(n) for the map.

## Dry run: a = [1,1,1], k = 2
| x | p | p−k | cnt[p−k] | ans | map after |
| --- | --- | --- | --- | --- | --- |
| – | 0 | – | – | 0 | {0:1} |
| 1 | 1 | −1 | 0 | 0 | {0:1,1:1} |
| 1 | 2 | 0 | 1 | 1 | {0:1,1:1,2:1} |
| 1 | 3 | 1 | 1 | 2 | {0:1,1:1,2:1,3:1} |

## Misconceptions
- Forgetting to seed `{0: 1}`: misses subarrays starting at index 0.
- Updating the map before the lookup (counts the empty subarray when k = 0).
- Storing a boolean instead of a count when duplicates matter.
- Calling hash operations O(1) worst case: it is O(1) average.

## Ladder
Easy: Two Sum → Medium: Subarray Sum Equals K → Harder: Longest Subarray with equal 0s and 1s variants / Subarray Sums Divisible by K (all LeetCode).

## Interviewer twists
No extra space allowed (sort, then two pointers); return the subarrays; streaming input.
