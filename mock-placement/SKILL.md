---
name: mock-placement
description: Runs full timed placement round-1 mock tests, general or company-specific, with a section-wise report.
---

# Mock Placement

Runs a full timed round-1 test that mixes aptitude and technical MCQs, then reports where to improve.

## Test type

| User wording | Type | Load |
| --- | --- | --- |
| "Round 1 mock, 30 questions, 40 minutes" | General mock | `references/test-blueprints.md` + `references/question-rules.md` |
| "Zoho round 1 mock", "TCS mock test" | Company mock | The same two files + `references/company-search.md` |

A single-topic test belongs to Aptitude Coach or CS Fundamentals. If neither is installed, run it here with one section.

## Flow

1. **Set up.** Take the count and time from the request, or use the blueprint default. For a company mock, follow `references/company-search.md` first and show a short source list with links, dates and reliability.
2. **State the rules.** Give the question count, time limit and sections. Say clearly: **the AI cannot run a real countdown in chat; track the time yourself.**
3. **Prepare.** Solve and check every question using `references/question-rules.md`.
4. **Show the whole test at once,** grouped by section and numbered, with options A–D. No answers, hints or working.
5. **Collect answers.** Ask for replies like `1-A, 2-C, 3-skip`. Accept partial answers.
6. **Mark.** Solve every question again from the start, with code where possible, without showing this step. If a question turns out to be flawed, leave it out of the score and say so.
7. **Report,** using the format below.

## Report

```
Score: <right> / <counted>   (<skipped> skipped, <removed> removed as flawed)
Section-wise: <section: right / total>
Weak topics: <ranked by mistakes>
Next 3 things to practise: <specific>
Time: <what the student reports, or "not reported">
```

Then list each wrong answer with the correct option and the working. Offer a closer look at any question.

## Non-negotiable rules

- Answers only at the end. Do not reveal them if the student asks mid-test; offer to end the test instead.
- A skipped question scores 0. No negative marking unless the student asks for it.
- A general mock is labelled "Practice mix", never as any company's pattern.
- In a company mock, label each section "Based on questions reported by <source>" or "In the reported pattern". Never say a company asked a question as fact.
- Original questions only. Never invent company names, frequencies or test patterns. No source → "no reliable data".
- Search only for a company mock or a request for real/previous-year questions.
