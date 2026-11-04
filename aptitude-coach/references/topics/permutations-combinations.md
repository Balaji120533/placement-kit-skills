# Permutations and combinations

## Formulas
- nPr = n! / (n − r)! (order matters)
- nCr = n! / (r! (n − r)!) (order does not matter)
- Repeated letters: n! / (p! q! …)
- Circular arrangements of n: (n − 1)!

## Shortcuts
- "At least one": total minus none.
- Order matters? Arrangement, use P. Order doesn't? Selection, use C.

## Solved examples (verified)
1. **Arrangements of LEVEL:** L and E each repeat: 5!/(2! 2!) = **30**.
2. **Committee of 3 from 5 men and 4 women, at least 1 woman:** C(9,3) − C(5,3) = 84 − 10 = **74**.
3. **6 people around a round table:** (6 − 1)! = **120**.

## Traps
- Forgetting to divide for repeats.
- Solving "at least one" by adding cases, which is slow and often double-counts.
- Using n! for a circular table.

## Good wrong options
5! = 120 with no repeat division; 6! = 720 for circular; C(4,1) × C(8,2), which double-counts.
