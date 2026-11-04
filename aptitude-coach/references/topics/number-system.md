# Number system

## Formulas
- HCF × LCM = product of two numbers
- Factor count: if n = p^a × q^b …, factors = (a + 1)(b + 1) …
- Trailing zeros of n!: n/5 + n/25 + n/125 + … (whole parts only)
- Unit digits repeat in a cycle of at most 4

## Divisibility
3: digit sum divisible by 3. 4: last two digits. 8: last three digits. 9: digit sum divisible by 9. 11: alternating digit sum divisible by 11.

## Solved examples (verified)
1. **HCF and LCM of 12 and 18:** HCF **6**, LCM **36**. Check: 6 × 36 = 216 = 12 × 18.
2. **Unit digit of 7²³:** cycle 7, 9, 3, 1; 23 mod 4 = 3, so the third term, **3**.
3. **Factors of 360:** 2³ × 3² × 5, so 4 × 3 × 2 = **24**.
4. **Trailing zeros of 100!:** 20 + 4 = **24**.

## Traps
- HCF × LCM = product works for two numbers only.
- If the exponent mod 4 is 0, use the 4th term of the cycle, not the 0th.
- Trailing zeros need the 25s too (100/5 = 20 alone is wrong).

## Good wrong options
20 for trailing zeros; the first cycle term; exponents multiplied without adding 1.
