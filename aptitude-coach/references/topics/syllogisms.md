# Syllogisms

## Method
Draw Venn diagrams. A conclusion follows only if it is true in **every** diagram that fits the statements.

- "All A are B": A sits inside B.
- "Some A are B": A and B overlap.
- "No A are B": no overlap.
- "Some A are not B": part of A is outside B.

## Solved examples (verified by checking every possible Venn model)
1. **All A are B. All B are C.** "All A are C": **follows**. "All C are A": **does not follow**. "Some C are A": **follows**.
2. **All A are B. Some B are C.** "Some A are C": **does not follow**. "No A are C": **does not follow**. "Either some A are C or no A are C": **follows** (complementary pair).
3. **Some A are B. No B are C.** "Some A are not C": **follows**. "No A are C": **does not follow**.

## Traps
- Real-world knowledge doesn't count; use only the statements.
- "All A are B" does not give "All B are A".
- "Some" with "some" gives no conclusion.
- "Some" and "no" on the same two terms form an either-or pair even when neither follows alone.

## When generating
Check each conclusion against every model with code, assuming each term names something. Say so if a question depends on that assumption.
