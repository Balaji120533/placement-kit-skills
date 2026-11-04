# Dynamic programming basics

**Invariant:** `dp[i]` fully answers the subproblem for size/state i, and depends only on states already computed.

## Signals
- "Minimum/maximum/number of ways", with choices at each step
- Brute force recursion repeats the same subproblems (overlapping subproblems)
- Optimal substructure: the best answer is built from best answers of smaller states

## How to build a DP (in order)
1. Define the state in words ("fewest coins to make amount a").
2. Write the transition (try every last choice).
3. Set base cases.
4. Pick the order (smaller states first) or use memoised recursion.
5. Derive time = states × transitions per state; space = states (optimise later).

## Template (coin change, minimum coins) — verified
```python
def coin(coins, amt):
    INF = amt + 1                      # impossible marker
    dp = [0] + [INF] * amt             # dp[a] = fewest coins for amount a
    for a in range(1, amt + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amt] if dp[amt] < INF else -1
```
Time O(amt × len(coins)): two nested loops. Space O(amt).

## Dry run: coins = [1,2,5], amt = 11
| a | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| dp | 0 | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 3 | 3 | 2 | 3 |
Answer 3 (5 + 5 + 1). Greedy happens to work here but fails for coins like [1,3,4] with amount 6 (greedy 4+1+1 = 3 coins, optimal 3+3 = 2).

## Misconceptions
- Using greedy where the coin set is arbitrary.
- Wrong base case or INF overflow (`INF + 1` in languages with fixed ints).
- Not seeing that the state must contain everything the future depends on.
- Assuming DP is always O(n): count states × transitions.

## Ladder
Easy: Climbing Stairs → Medium: Coin Change / House Robber → Harder: Longest Increasing Subsequence / Edit Distance (all LeetCode).

## Interviewer twists
Count ways instead of minimum; reconstruct the actual coins; reduce space to O(1) or one row.
