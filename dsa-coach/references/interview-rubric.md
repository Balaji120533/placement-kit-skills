# Interview rubric

Grades how a student explains an approach. Shared by Explain-back and, later, Mock Interview.

## The six items

| Item | Covered means the student said |
| --- | --- |
| Constraints | The input size and the complexity it demands |
| Brute force | The simple approach and its complexity |
| Key observation | What makes the optimal approach work, and why it removes the bottleneck |
| Complexity | Both time and space, with the reason for each |
| Edge cases | At least two cases that matter for this problem (empty, single element, duplicates, negatives, overflow) |
| Dry run | A small example walked through step by step |

## Grades

- **Covered:** stated, correct and with its reason.
- **Weak:** mentioned but vague, missing its reason, only partly done, or incorrect. Mark an incorrect claim "weak (incorrect)" and say what is wrong.
- **Missing:** not stated.

## Grading rules

- Grade only what the student wrote. Never credit an item because it can be inferred from their code or their other answers.
- Stating the approach is not the same as explaining it. "Use a hash map" alone is not a key observation.
- A correct answer with no reason is weak.
- Check every claim against your own solution. Derive the complexity from the approach the student described, not from the usual answer for this problem.
- The bar is an interviewer who has never seen this problem and needs convincing.

## Worked example

Problem: Two Sum, n up to 10^4.

Student: "I'd use a hash map. Store each number and check if target minus the number is there. It's O(n)."

| Item | Grade | Why |
| --- | --- | --- |
| Constraints | Missing | n is never mentioned |
| Brute force | Missing | The nested-loop O(n^2) approach is never mentioned |
| Key observation | Weak | Says what to do, not why it removes the inner scan |
| Complexity | Weak | Time only, no reason, no space |
| Edge cases | Missing | None named |
| Dry run | Missing | No example |

Model explanation: "n is up to 10^4, so O(n^2) would pass but O(n) is better. Brute force checks every pair, which is O(n^2). The bottleneck is scanning for the partner each time. If I remember each number I've seen in a hash map, I can look up target minus the current number in O(1) on average. One pass gives O(n) time and O(n) space. I check before inserting, so an element can't pair with itself, and duplicates like [3,3] with target 6 still work. On [2,7,11,15] with target 9: at 2 I need 7, not seen, so I store 2. At 7 I need 2, which is stored at index 0, so the answer is [0,1]."
