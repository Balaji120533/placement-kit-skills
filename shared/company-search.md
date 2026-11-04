# Company search rule (shared by all Placement Kit skills)

## When to search

Search only when the user names a company or asks for real, previous-year or "asked in" questions. Everything else is generated: original, solved and verified.

| User says | Do |
| --- | --- |
| "10 percentage questions" | Generate original questions. No search. |
| "15 OS MCQs" | Generate. No search. |
| "Zoho aptitude questions" | Search Zoho round-1 patterns, then build a practice set in that pattern, with source links. |
| "TCS previous year CS MCQs" | Search, give sources, then a practice set. |
| "Real questions asked in Amazon OA" | Search, then link to the actual problems (LeetCode etc.). |

Companies rarely repeat exact questions; the pattern is what repeats. Do not search every request.

## Where to look

- Interview-experience posts: GFG, LeetCode Discuss, blogs.
- Public GitHub company-wise problem lists.

## Rules

1. Always show the source link and its date. Mark any source older than 2 years as "older than 2 years".
2. Link copyrighted content (IndiaBix, PrepInsta, paid banks). Never reproduce whole question sets. Reuse GitHub content only if its license allows.
3. Re-solve any answer found online before trusting it.
4. Say how reliable the source looks. Many "previous year" posts are recycled.
5. Never invent company names, frequencies or tags. If there is no source, say "no reliable data" and show the pattern family plus similar problems.
6. If search is unavailable, say so and generate original questions instead.
7. Company questions: rewrite a reported question in your own words with new numbers, then solve it yourself. Label it "Based on a question reported by <source>", with the link. Never say a question was "asked by <company>" as fact, and never copy one word for word.

## Output shape

```
Sources found:
- <title> — <url> — <date> — <reliability note>
Pattern seen: <what repeats>
Company questions: <one at a time, each labelled as based on a reported question or in the reported pattern>
```
