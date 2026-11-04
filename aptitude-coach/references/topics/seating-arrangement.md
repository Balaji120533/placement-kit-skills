# Seating arrangement

## Method
1. Draw the positions first.
2. Place the fixed clues first ("in the middle", "at the end").
3. Then the adjacent clues, then the negative clues.
4. If a clue allows two cases, draw both and let later clues eliminate one.

## Direction rule
- Row facing north, drawn with north at the top: a person's left is the left of the page.
- Circle facing the centre: your left is the clockwise direction.

## Solved examples (verified: exactly one arrangement survives)
1. **Row of 5 facing north, A to E:** C is in the middle. A is immediately left of C. E is at the right end. D is not at an end. → **B A C D E**.
2. **Circle of 5 facing the centre:** B is immediately left of A. C is second to the right of A. E is not next to A. → clockwise from A: **A B E C D**.
3. **Floors 1 to 4, W X Y Z:** X is on an even floor. Z is immediately above X. W is below Y. → floor 1 to 4: **W X Z Y**. (X on floor 4 would put Z on floor 5.)

## Traps
- Left and right flip for people facing the opposite way.
- "Immediately left" is not "somewhere to the left".
- A puzzle with too few clues has more than one answer.

## When generating
Enumerate every arrangement with code. Exactly one must fit all the clues, or the question asked must have the same answer in every surviving case. State the facing direction every time.
