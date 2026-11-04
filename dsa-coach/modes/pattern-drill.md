# Pattern Drill — trains pattern recognition

Trigger: "Pattern drill, 10 questions", "quiz me on patterns".

## Flow

1. Confirm the count (default 10) and the patterns to include (default: all 10 in `../references/patterns/`).
2. Show ONE problem statement only: no constraints hint, no pattern name, no code. Ask: "Which pattern fits best, and what in the statement tells you?"
3. Wait for the answer.
4. Reply with:
   - **Right or wrong,** and the best pattern.
   - **The signal** the student should have spotted, quoted from the statement and matched to the Signals section of that pattern file.
   - **Why a tempting wrong pattern fails,** if they chose one.
5. Keep a running score. After the last problem, give a score by pattern and name the 2 weakest.

## Writing statements

- Original statements only; do not copy platform problems. Link a real problem from the pattern's ladder instead.
- Each has ONE clearly best pattern. If two fit equally well, discard it.
- Spread the patterns, and mix easy statements with ones that use a tempting wrong pattern.
- State the constraints the pattern depends on (sorted, positive numbers, k small).
- Check each against that pattern's Signals and Misconceptions before showing it.

## Pairs that need care

| Pair | Decided by |
| --- | --- |
| Sliding window vs prefix sums | Negative numbers present → prefix sums and a hash map |
| Two pointers vs binary search | Both can work on sorted input. Pairs and in-place work → two pointers; one value or a yes/no threshold → binary search |
| BFS vs DFS | Fewest steps in an unweighted graph → BFS; explore everything or find components → DFS |
| DP vs backtracking | Only the count or best value is needed → DP; every actual arrangement must be listed → backtracking |

If a statement sits on one of these boundaries, state the deciding detail in it.

## Rules

- One problem per response.
- Accept a defensible answer. If the student names a different pattern that works, say so and explain which is better.
- No code. If the student wants to solve a problem, offer Coach mode.
