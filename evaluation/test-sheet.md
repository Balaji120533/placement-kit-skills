# Evaluation test sheet

Results of testing the kit. Y means the check passed and N means it failed. Method, marking rules and failures are at the end.

## Before you start

| Record | Value |
| --- | --- |
| Date | 2026-11-04 and 2026-11-05 |
| Platform (Claude Code, claude.ai, other) | Claude Code CLI, fresh headless sessions |
| Model | Claude Sonnet 5.5 (final 5-prompt check: Claude Haiku 5.5) |
| Code execution on? | Yes (python, gcc, java); some sessions reported the shell blocked them |
| Web search on? | Only for company prompts, and off for the Daily Temperatures one |

## How to run it

1. **With kit:** install all four skills and start a new session for each section.
2. **Without kit:** move the skills out, run the same prompts in a new session, then move them back:

```powershell
$s = "$HOME\.claude\skills"; $h = "$HOME\.claude\skills-off"
New-Item -ItemType Directory -Force $h | Out-Null
'dsa-coach','cs-fundamentals','aptitude-coach','mock-placement' | ForEach-Object { Move-Item "$s\$_" $h }
# run the prompts, then restore:
'dsa-coach','cs-fundamentals','aptitude-coach','mock-placement' | ForEach-Object { Move-Item "$h\$_" $s }
```

3. Check every answer yourself, away from the chat: use a calculator, a compiler or a SQL engine. Do not ask the model that wrote the answer whether it is right.
4. Questions are generated fresh, so the two runs won't get identical questions. You're comparing the quality of each answer, not matching them.
5. Keep every failure in the sheet. Do not re-run a prompt to get a better result.

## DSA: 15 problems

Prompt: "Help me solve <problem>", then a request for the full solution and its complexity.

| # | Problem | Pattern | Difficulty | Withholds code at first: with kit | without kit | Complexity correct: with kit | without kit | No invented company data: with kit | without kit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Two Sum | hashing | easy | Y | N | Y | Y | Y | Y |
| 2 | Valid Palindrome | two pointers | easy | Y | N | Y | Y | Y | Y |
| 3 | 3Sum | two pointers | medium | Y | N | Y | Y | Y | Y |
| 4 | Longest Substring Without Repeating Characters | sliding window | medium | Y | N | Y | Y | Y | Y |
| 5 | Minimum Window Substring | sliding window | hard | Y | N | Y | Y | Y | Y |
| 6 | Search in Rotated Sorted Array | binary search | medium | Y | N | Y | Y | Y | Y |
| 7 | Koko Eating Bananas | binary search | medium | Y | N | Y | Y | Y | Y |
| 8 | Subarray Sum Equals K | prefix sums | medium | Y | N | Y | Y | Y | Y |
| 9 | Daily Temperatures | monotonic stack | medium | Y | N | Y | Y | Y | Y |
| 10 | Largest Rectangle in Histogram | monotonic stack | hard | Y | N | Y | Y | Y | Y |
| 11 | Reverse Linked List | linked list | easy | Y | N | Y | Y | Y | Y |
| 12 | Number of Islands | BFS/DFS | medium | Y | N | Y | Y | Y | Y |
| 13 | Coin Change | DP | medium | Y | N | Y | Y | Y | Y |
| 14 | Top K Frequent Elements | heap | medium | Y | N | Y | Y | Y | Y |
| 15 | N-Queens | backtracking | hard | N |  | Y |  | Y |  |

## Aptitude: 30 questions

| # | Prompt | Key correct | Exactly one valid option | Working shown |
| --- | --- | --- | --- | --- |
| 1 | "Give me 1 percentage practice question, easy" | Y | Y | Y |
| 2 | "Give me 1 percentage practice question, medium" | Y | Y | Y |
| 3 | "Give me 1 profit and loss practice question, medium" | Y | N | Y |
| 4 | "Give me 1 ratio practice question, medium" | Y | Y | Y |
| 5 | "Give me 1 average practice question, easy" | Y | Y | Y |
| 6 | "Give me 1 time and work practice question, medium" | N | Y | Y |
| 7 | "Give me 1 time and work practice question, hard" | Y | Y | Y |
| 8 | "Give me 1 time, speed and distance practice question, medium" | N | N | Y |
| 9 | "Give me 1 permutations and combinations practice question, medium" | Y | N | Y |
| 10 | "Give me 1 permutations and combinations practice question, hard" | N | N | N |
| 11 | "Give me 1 probability practice question, medium" | N | N | Y |
| 12 | "Give me 1 number system practice question, medium" | Y | Y | Y |
| 13 | "Give me 1 clock practice question, medium" | Y | Y | Y |
| 14 | "Give me 1 calendar practice question, medium" | Y | Y | Y |
| 15 | "Give me 1 simple and compound interest practice question, medium" | N | N | N |
| 16 | "Give me 1 mensuration practice question, easy" | N | N | N |
| 17 | "Give me 1 data interpretation practice question, medium" | Y | Y | Y |
| 18 | "Give me 1 seating arrangement practice question, medium" | Y | Y | Y |
| 19 | "Give me 1 seating arrangement practice question, hard" | Y | N | Y |
| 20 | "Give me 1 blood relation practice question, medium" | Y | Y | Y |
| 21 | "Give me 1 syllogism practice question, medium" | Y | Y | Y |
| 22 | "Give me 1 syllogism practice question, hard" | Y | Y | Y |
| 23 | "Give me 1 number series practice question, easy" | Y | Y | Y |
| 24 | "Give me 1 letter series practice question, medium" | Y | Y | Y |
| 25 | "Give me 1 coding-decoding practice question, medium" | Y | Y | Y |
| 26 | "Give me 1 direction sense practice question, easy" | N | Y | Y |
| 27 | "Give me 1 reading comprehension practice question, medium" | Y | Y | Y |
| 28 | "Give me 1 error spotting practice question, easy" | Y | Y | Y |
| 29 | "Give me 1 error spotting practice question, medium" | N | N | Y |
| 30 | "Give me 1 sentence completion practice question, medium" | Y | Y | Y |

## CS fundamentals: 30 MCQs

| # | Prompt | Key correct | Exactly one valid option | Working shown |
| --- | --- | --- | --- | --- |
| 1 | "Give me 1 process vs thread practice question, easy" | Y | Y | Y |
| 2 | "Give me 1 deadlock practice question, easy" | N | N | N |
| 3 | "Give me 1 CPU scheduling practice question, medium" | Y | Y | Y |
| 4 | "Give me 1 CPU scheduling practice question, hard" | N | N | N |
| 5 | "Give me 1 paging practice question, medium" | N | N | N |
| 6 | "Give me 1 page replacement practice question, medium" | Y | N | Y |
| 7 | "Give me 1 semaphore practice question, medium" | N | N | Y |
| 8 | "Give me 1 database keys practice question, easy" | Y | Y | Y |
| 9 | "Give me 1 normalization practice question, medium" | Y | N | Y |
| 10 | "Give me 1 transactions and ACID practice question, medium" | Y | Y | Y |
| 11 | "Give me 1 SQL join output practice question, medium" | Y | N | Y |
| 12 | "Give me 1 SQL aggregate output practice question, medium" | Y | N | Y |
| 13 | "Give me 1 SQL subquery output practice question, hard" | Y | N | Y |
| 14 | "Give me 1 isolation levels practice question, hard" | N | N | N |
| 15 | "Give me 1 OSI layers practice question, easy" | Y | Y | Y |
| 16 | "Give me 1 TCP vs UDP practice question, easy" | Y | Y | Y |
| 17 | "Give me 1 port numbers practice question, easy" | Y | Y | Y |
| 18 | "Give me 1 subnetting practice question, medium" | N | N | N |
| 19 | "Give me 1 subnetting practice question, hard" | N | N | Y |
| 20 | "Give me 1 overloading vs overriding practice question, easy" | Y | Y | Y |
| 21 | "Give me 1 abstract class vs interface practice question, medium" | Y | N | Y |
| 22 | "Give me 1 Java static and inheritance practice question, medium" | N | N | N |
| 23 | "Give me 1 Java string equality practice question, medium" | N | N | N |
| 24 | "Give me 1 C pointer output practice question, medium" | Y | N | Y |
| 25 | "Give me 1 C pointer output practice question, hard" | Y | Y | Y |
| 26 | "Give me 1 C static variable output practice question, medium" | N | N | Y |
| 27 | "Give me 1 C operator precedence output practice question, medium" | Y | Y | Y |
| 28 | "Give me 1 C string and sizeof output practice question, medium" | Y | Y | Y |
| 29 | "Give me 1 C macro output practice question, hard" | N | N | N |
| 30 | "Give me 1 Java output practice question, medium" | Y | Y | Y |

## Explain-back catches missing items

Each explanation leaves items out on purpose.

| # | Paste this | Must be marked weak or missing | Caught? |
| --- | --- | --- | --- |
| 1 | "Check my approach for Two Sum: use a hash map and look up target minus the number." | Constraints, brute force, complexity, edge cases, dry run | Y |
| 2 | "Check my approach for Number of Islands: for each land cell, run BFS and count it. O(R·C) time." | Constraints, brute force, edge cases, dry run, space complexity | N |
| 3 | "Check my approach for Coin Change: greedy, always take the largest coin." | Key observation (incorrect, should fail), with a failing input | Y |

## Company data

Web search was off for #1. Pass means nothing is invented.

| # | Prompt | Pass if | Result |
| --- | --- | --- | --- |
| 1 | "Which companies ask Daily Temperatures?" | Says no reliable data | N |
| 2 | "Zoho aptitude questions" | Sources have links and dates; nothing says "asked by Zoho" as fact | Y |
| 3 | "TCS previous year CS MCQs" | The same | Y |

## Correct skill and mode

Run with the kit only.

| # | Prompt | Expected | Correct? |
| --- | --- | --- | --- |
| 1 | Help me solve Two Sum | dsa-coach, Coach | Y |
| 2 | Teach me sliding window | dsa-coach, Learn | Y |
| 3 | My code gives TLE: <paste code> | dsa-coach, Debug | N |
| 4 | Check my approach: <paste explanation> | dsa-coach, Explain-back | N |
| 5 | Mock interview, medium, 45 min | dsa-coach, Mock Interview | Y |
| 6 | Pattern drill, 5 questions | dsa-coach, Pattern Drill | Y |
| 7 | Zoho round style, no library | dsa-coach, Placement | Y |
| 8 | Quick: Two Sum | dsa-coach, Quick | N |
| 9 | 10 percentage questions | aptitude-coach, Practice | Y |
| 10 | Teach me time and work | aptitude-coach, Learn Shortcut | Y |
| 11 | 20 mixed aptitude questions, 25 minutes | aptitude-coach, Timed Test | Y |
| 12 | 15 OS MCQs | cs-fundamentals, Practice | Y |
| 13 | What's the output of this C code? <paste code> | cs-fundamentals, own question | N |
| 14 | Round 1 mock, 30 questions, 40 minutes | mock-placement, general | Y |
| 15 | Zoho round 1 mock | mock-placement, company | Y |

## Totals

Compared with and without the kit:

| Check | With kit | Without kit |
| --- | --- | --- |
| DSA: withholds code at first | 14 / 15 | 0 / 14 |
| DSA: complexity correct | 15 / 15 | 14 / 14 |

With the kit only:

| Check | Result |
| --- | --- |
| Aptitude: key correct | 22 / 30 |
| Aptitude: exactly one valid option | 21 / 30 |
| CS: key correct | 19 / 30 |
| CS: exactly one valid option | 12 / 30 |
| Company data: nothing invented | 2 / 3 |
| Explain-back catches missing items | 2 / 3 |
| Correct skill and mode triggered | 11 / 15 |

## Notes on the first run

**What was run.** 95 sessions: DSA with and without the kit, aptitude and CS with the kit, and the company prompts with the kit. The run hit the account's usage limit part-way through, and the sessions after that point returned a limit message instead of an answer, so they were discarded. Three aptitude sessions were also run without the kit; that is too few to compare, so they are not tabulated.

**Setup.** Fresh `claude -p` sessions (Claude Code CLI, headless), model alias `sonnet`, with scripted replies and not a real student: DSA sessions asked for the full solution on the second turn, and aptitude and CS sessions replied "My answer is A." Code tools (python, gcc, java) were allowed, and several sessions reported the shell blocked them. "Without kit" used `--disable-slash-commands`, which turns skills off.

**Graded by the kit's author, who is not neutral.** Quant, code, SQL, scheduling, page-fault, calendar and puzzle answers were checked by running code. Syllogisms and seating puzzles were checked by exhaustive enumeration. Blood relations and the verbal questions were judged by reasoning and could be wrong. Re-grade a sample before relying on these numbers.

**Marking rules.**
- *Key correct*: the answer the session gave was right and its final verdict was not contradicted. A session that announced a wrong key and then corrected itself in the same message counts as N (apt06, apt26). An open-ended question whose key was never given counts as N.
- *Exactly one valid option*: the question was shown with options, and exactly one was correct. Open-ended questions with no options count as N.
- *Working shown*: the reply showed its working for the key it gave.

**Where the kit failed**
- **The skill often did not load.** It loaded in 14/15 DSA sessions, 8/30 aptitude and 6/30 CS.
- **When the skill loaded, all 14 aptitude and CS questions passed every check.** When it didn't, keys were right in 27/46 and exactly one option was valid in 19/46. These are different prompts, so this is a pattern and not a controlled test.
- **Wrong or flawed questions:** apt06 and apt26 (wrong key announced, then corrected), apt08 and apt11 (no correct option), apt29 (ambiguous: a collective noun), cs26 (the answer depends on the compiler). Each of these sessions had not loaded the skill.
- **Open-ended instead of multiple choice:** apt03, apt09, apt10, apt15, apt16, apt19 and 14 of the CS questions had no options, and the key was not given in apt10, apt15, apt16 and 10 CS questions. In apt09 and cs06 the full solution was printed inside the question message.
- **DSA #15 (N-Queens):** the skill did not load, and the first reply was a full solution.
- **Company data #1:** with web search off, the session listed companies "from memory" instead of saying there is no reliable data.

## Re-test after the description and format fix (2026-11-05)

After rewriting the four skill descriptions and adding the always-multiple-choice rule, 30 sessions were run with the kit: the 10 aptitude and CS prompts that failed in the first run, 15 routing prompts, 3 Explain-back prompts and 2 company prompts. Questions are generated fresh, so these are new questions on the same prompts, and the 10 were chosen because they had failed. It is a before-and-after check and not a controlled test. The ten new answer keys were each re-derived by hand or by running code.

| Check (the same 10 prompts) | Before the fix | After the fix |
| --- | --- | --- |
| Skill loaded | 0 / 10 | 10 / 10 |
| Key correct | 0 / 10 | 10 / 10 |
| Exactly one valid option | 0 / 10 | 10 / 10 |

Routing was 11 / 15, Explain-back 2 / 3, and company data 1 / 2.

**Routing, per prompt**

| # | Prompt | Result |
| --- | --- | --- |
| 3 | My code gives TLE: <code> | **N** — skill did not load; the reply rewrote the code unasked |
| 4 | Check my approach: <explanation> | **N** — skill did not load; generic feedback, no rubric |
| 8 | Quick: Two Sum | **N** — skill did not load; code, a dry run and edge cases, not 5 lines |
| 13 | What's the output of this C code? <code> | **N** — skill did not load; the answer `6 10` was correct |

The other 11 prompts reached the right skill and mode (the per-prompt result is in the routing table above).

**Explain-back.** #1 (Two Sum) and #3 (Coin Change) passed: every omitted item was marked missing, the incorrect greedy claim was marked "weak (incorrect)" with a failing input, and the model explanation was held back for the wrong approach. #2 (Number of Islands) failed: the skill did not load, so there was no rubric grading.

**Company data.** The Zoho/TCS prompt passed: sources with links and dates, the 2019 source flagged as old, and a plain statement that the keys were not executed. "Which companies ask Daily Temperatures?" (search off) failed again: the skill did not load and the reply listed companies from memory, including TCS and Infosys.

## Second description fix: the 5 remaining misses on Claude Haiku 5.5

After the DSA description was extended to name "my code gives TLE", "check my approach", "Quick:" and company-frequency questions, and the CS description to name any pasted C, Java or SQL snippet, the five prompts that missed were run as five turns of **one** Haiku 5.5 session (`claude-haiku-5-5`). Earlier turns are in context for later ones, and Haiku is a different model from the other runs, so this is not comparable with the Sonnet numbers.

| # | Prompt | Skill loaded | Behaviour |
| --- | --- | --- | --- |
| 1 | My code gives TLE: <code> | no | **Fail** — rewrote the code unasked |
| 2 | Check my approach: <explanation> | no | **Fail** — no rubric grading; said the approach was correct and gave code |
| 3 | Quick: Two Sum | yes (dsa-coach) | **Pass** — exactly 5 lines |
| 4 | What's the output of this C code? <code> | no | Answer `6 10` correct, but the skill did not load |
| 5 | Which companies ask Daily Temperatures? | no | **Pass** — named no companies and said it would not guess from memory (it tried a web search that was denied) |

1 of 5 loaded the skill and 2 of 5 behaved as the kit specifies.
