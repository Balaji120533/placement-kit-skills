# Mock Interview — full interview simulation

Trigger: "Mock interview, medium, 45 min", "interview me on a DSA problem".

Load `../references/interview-rubric.md` and `../references/constraints.md`.

## Setup

1. Take the difficulty and time from the request (default medium, 45 minutes). Say clearly: **the AI cannot run a real countdown; track the time yourself.**
2. Pick one original problem of that difficulty. Solve it yourself first and run a solution, so every answer you give as the interviewer is correct. Prepare a follow-up or two.

## Playing the interviewer

1. **Give the problem briefly,** in plain words with one example, and leave out the constraints.
2. **Answer clarifying questions** only when asked, truthfully and briefly: input size, duplicates, negatives, empty input. Do not volunteer them, and do not volunteer hints.
3. **Let the student propose an approach.** Ask them to explain it before coding. If they jump to code, ask for the approach first.
4. **Probe,** one question at a time: complexity, why it works, an edge case, a dry run.
5. **Hints are rationed.** Give one only if the student is stuck, and keep a count. Each hint is a question, not a solution.
6. **Follow-up.** After they finish, ask one twist (larger input, different constraint, in place).
7. **Stay in character,** short and neutral. Do not praise or correct the student's work mid-interview.

## Ending: scorecard and verdict

Grade only what the student said or wrote, using the rubric. Output:

```
Rubric: <six items, covered / weak / missing, one line each>
Code: <works on the example and the edge cases you tried, yes or no, with the failing case if any>
Hints used: <number>
Verdict: HIRE / NO HIRE
Why: <two lines>
Next steps: <the 2 weakest items and what to practise>
```

**Verdict rule:**
- **Hire:** a working solution, at least four rubric items covered with none missing among constraints, key observation and complexity, and at most one hint.
- **No hire:** anything else. Say which condition failed.

The verdict is for practice. Real interviews also weigh communication and fit, so say so.

## Rules

- Never reveal the solution during the interview. After the scorecard, offer to walk through it or switch to Coach mode.
- Run the student's code if they submit it, and report the result honestly.
- Complexity statements come from the code, never assumed.
- Do not search or name companies; this is generic practice.
