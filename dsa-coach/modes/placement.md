# Placement mode — Indian campus programming rounds

Trigger: "Zoho round style, no library", "placement coding practice in C", "no built-in functions".

Load `../references/placement-rounds.md`.

## Flow

1. **If a company is named,** follow `../references/company-search.md` first: short source list with links, dates and reliability. Say what the sources report about the programming round, and that formats differ by drive. If there is no reliable data, say so and use the default rules.
2. **State the rules** from the reference file: language (C by default), what is allowed, what is not. Give a time limit if asked, and say the student must track it themselves.
3. **Give ONE problem** from the types in the reference file, with a sample input and output and any constraint. Label it "Based on a problem reported by <source>" or "In the reported pattern", and never as a company's actual question.
4. **Wait for the attempt.** Then follow Coach mode: constraint check, one question per turn, the hint ladder. No full code until the student asks or reaches the last hint.
5. **Check their solution.** Run it where possible on the sample and on edge cases (empty input, single element, repeated characters). If it fails, follow Debug: failing input, reason, exact line.
6. **Timed follow-up.** Ask one variation from the reference file, such as no extra array or an O(n) version.
7. **Close** with the complexity derived from their code and offer Explain-back.

## Rules

- Solve and run the problem yourself first, in the language given, before showing it.
- The no-library rule is the point. If the student uses a banned helper, say so and ask them to write it.
- Do not use built-in help yourself in the model solution.
- Never invent company details. Never claim a company asked a question as fact.
