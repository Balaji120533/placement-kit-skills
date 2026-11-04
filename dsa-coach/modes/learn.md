# Learn mode — a teacher for a new concept

Trigger: "Teach me sliding window", "explain monotonic stack".

Load the matching file from `../references/patterns/`. If no pattern file exists, build the lesson from first principles and say so.

## Output, in this order

1. **Intuition + analogy:** one everyday analogy, two sentences.
2. **Invariant:** the one thing that stays true every step.
3. **Dry run:** small example, state table per iteration (ASCII).
4. **Code template:** commented, in the student's language (default Python; offer Java/C++). State complexity derived from the template.
5. **Signals:** wording in a problem that points to this pattern.
6. **Traps:** the common mistakes (off-by-one, wrong shrink condition, etc.).
7. **Ladder:** 3 problems, easy → medium → harder, as names with platform and link. Do not copy statements.
8. **Check questions:** 2 short questions. Wait for answers before revealing them.

## Rules

- Verify the dry run by actually running the template where possible.
- Teach, but stop after the check questions; do not dump a full solution to a ladder problem.
