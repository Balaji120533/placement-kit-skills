---
name: cs-fundamentals
description: Technical MCQ trainer for OS, DBMS, SQL, networks, OOP and C/Java output prediction.
---

# CS Fundamentals MCQ

Covers the technical MCQ part of placement round 1. C/Java output prediction is a priority (Zoho-style first rounds typically include C output questions). This file is a router: detect the mode and topic, then load only the files needed.

## Mode detection

| User wording | Mode | Load |
| --- | --- | --- |
| "Teach me deadlock", "explain normalization" | Learn Shortcut | `modes/learn-shortcut.md` + topic file |
| "10 OS MCQs, medium" | Practice | `modes/practice.md` + topic file |
| "20 questions, 25 minutes" | Timed Test | `modes/timed-test.md` + topic files |
| "Explain my mistakes" | Mistake Review | `modes/mistake-review.md` |
| "Zoho CS questions", "TCS previous year" | Company Pattern | `modes/company-pattern.md` + `../shared/company-search.md` |

## Topic files (`references/`)

`os.md`, `dbms.md`, `cn.md`, `oop.md`, `c-output.md`. Load only the topics requested.

## Non-negotiable rules

- **Solve before showing:** generate the question, solve it fully, and confirm exactly one option is correct before showing it.
- **Verify with code** where the platform allows: run C/Java output questions, run SQL on a scratch database. If code can't be run, follow the fallback in `references/c-output.md` (hand-trace twice, stick to certain constructs, tell the student the key was not executed).
- **Output questions:** avoid undefined behaviour (e.g. `a++ + ++a`) unless the answer is "undefined behaviour".
- **Show the working** in every explanation.
- **Original questions only.** Link copyrighted banks (IndiaBix, PrepInsta); never reproduce them.
- **Never invent company names or frequencies.** No source → "no reliable data".
- Search only when a company or real/previous-year questions are requested; otherwise generate.
