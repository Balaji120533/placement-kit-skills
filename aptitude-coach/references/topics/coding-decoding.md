# Coding-decoding

## Method
Write letter positions and compare the word with its code letter by letter. Common rules: fixed shift, reverse alphabet (A↔Z, position p becomes 27 − p), word reversal, sum of positions.

## Solved examples (verified)
1. **CAT is coded FDW. Code DOG.** Each letter +3: **GRJ**.
2. **Reverse alphabet code for GOOD:** G→T, O→L, O→L, D→W: **TLLW**.
3. **CAT = 24 (sum of positions). DOG = ?** 4 + 15 + 7 = **26**.

## Traps
- Shifts wrap around from Z to A.
- Checking only the first letter; the rule may vary by position.
- Two words with the same sum are not the same code.

## When generating
Generate the code with code. The example must have enough letters to rule out any other simple rule.
