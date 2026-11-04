# Calendars

## Formulas
- Odd days = days left after dividing by 7. Day codes: 0 Sunday, 1 Monday … 6 Saturday.
- Normal year: 1 odd day. Leap year: 2 odd days.
- Leap year: divisible by 4; century years must be divisible by 400. So 2000 is a leap year, and 1900 and 2100 are not.
- Century odd days: 100 years 5, 200 years 3, 300 years 1, 400 years 0.

## Solved examples (verified against the real calendar)
1. **Day of the week on 15 Aug 1947.** 1600 years: 0. 300 years: 1. 46 years with 11 leap years: 57, so 1. Jan 1 to Aug 15: 227 days, so 3. Total 5: **Friday**.
2. **1 Jan 2024 was a Monday. What was 1 Jan 2025?** 2024 is a leap year, so +2: **Wednesday**.
3. **Which next year has the same calendar as 2023?** Add the odd days until they total a multiple of 7, and the leap status must also match: **2034**.

## Traps
- 1900 is not a leap year.
- A leap year only shifts dates after February in the same year; 1 Jan of the next year moves by 2.
- The same weekday on 1 Jan isn't enough: both years must be leap or both not.

## When generating
Check every date with code using a real calendar library. Keep dates after 1582 (the Gregorian calendar).
