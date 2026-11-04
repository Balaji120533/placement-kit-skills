# Debug mode — finds why your code fails, or walks through it, without rewriting it

Trigger: "My code gives TLE: [code]", "wrong answer on test 3", "Dry run this with [2,7,11,15]".

If the student reports a failure, follow **Failing code**. If they only want to understand the code, follow **Walkthrough**.

## Failing code

1. **Failing input:** a smallest input where the code misbehaves (or the input that triggers TLE, with n sized from the constraints). Actually run or hand-trace the code to confirm it fails; do not guess.
2. **Expected vs actual:** both values.
3. **Reason:** the logical cause in 1–3 sentences.
4. **Exact line:** line number and the offending expression.
5. **Fix hint:** one sentence on the direction. No rewritten code.

## Walkthrough

1. **State trace:** a table with one row per iteration, showing the variables that change. Use the student's input, or a small one if none is given. Run the code where possible so the trace is real.
2. **Complexity:** time and space derived line by line from the code.

## Rules

- Fixed code only if the student asks for it.
- For TLE: derive the complexity from the student's code, compare with the target in `../references/constraints.md`, name the hot line.
- For WA: check usual suspects (off-by-one, overflow, uninitialised state, empty/single input, duplicates, negative numbers).
- If the code is correct, say so and ask for the failing case.
- One question at most at the end, e.g. "Can you see why index i+1 is out of range?"
