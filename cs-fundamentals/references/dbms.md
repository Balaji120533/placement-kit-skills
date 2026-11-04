# DBMS and SQL — facts and worked examples

## Keys
- Super key: any set of attributes that uniquely identifies a row. Candidate key: a minimal super key. Primary key: the chosen candidate key (no NULLs). Foreign key: refers to a key in another table. Alternate key: candidate keys not chosen as primary.

## Normalization
- 1NF: atomic values, no repeating groups.
- 2NF: 1NF + no partial dependency (non-key attribute depending on part of a composite key).
- 3NF: 2NF + no transitive dependency (non-key → non-key).
- BCNF: for every non-trivial FD X → Y, X is a super key.
- Purpose: reduce redundancy and update/insert/delete anomalies.

## Transactions (ACID)
Atomicity, Consistency, Isolation, Durability.
Isolation anomalies: dirty read, non-repeatable read, phantom read. Levels from weakest: Read Uncommitted, Read Committed, Repeatable Read, Serializable.

## Joins
INNER (matching rows), LEFT/RIGHT (all rows of one side + matches, NULLs otherwise), FULL (all rows both sides), CROSS (every pair, m × n rows).

## SQL worked examples (verified on a scratch SQLite database)
Tables: `a(id) = {1,2,3}`, `b(id) = {2,3,4}`, `e(name, sal) = {(A,10),(B,20),(C,20),(D,30)}`.

| Query | Result |
| --- | --- |
| `SELECT a.id FROM a INNER JOIN b ON a.id=b.id` | 2, 3 |
| `SELECT COUNT(*) FROM a LEFT JOIN b ON a.id=b.id` | 3 |
| same, `WHERE b.id IS NULL` | 1 |
| `SELECT COUNT(*) FROM a, b` | 9 (cross join) |
| `SELECT COUNT(sal), COUNT(DISTINCT sal) FROM e` | 4, 3 |
| `SELECT MAX(sal) FROM e WHERE sal < (SELECT MAX(sal) FROM e)` | 20 (second highest) |

## Common MCQ traps
- `COUNT(*)` counts NULL rows; `COUNT(col)` skips NULLs.
- `WHERE` filters rows before grouping; `HAVING` filters groups.
- Comparing with NULL needs `IS NULL`; `= NULL` is never true.
- `UNION` removes duplicates; `UNION ALL` keeps them.
- DELETE (rows, can roll back, DML) vs TRUNCATE (all rows, DDL) vs DROP (table itself).
- Where a result depends on dialect, state the dialect.
