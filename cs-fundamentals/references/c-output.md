# C / Java output prediction

## Rules for generating output questions
1. Write the program, compile and **run it** (e.g. `gcc`) before showing the question. Use that output as the key.
   **If you cannot run C** (no compiler, no code execution, or a C-less sandbox), do not guess:
   - Try another tool you do have (a Java or Python run can check Java questions or the arithmetic, but not C-specific behaviour such as `unsigned` wraparound or pointer arithmetic).
   - Otherwise trace the program by hand, one statement at a time, writing out every variable's value. Check the result a second time with a different method (for example, recompute from the end).
   - Limit questions to constructs whose behaviour you are certain of, and prefer the verified examples in the table below.
   - Tell the student the key was hand-traced and not executed, and that they can run it on an online compiler to confirm.
   - If you are not certain of an answer, drop the question and write a different one.
2. Avoid undefined behaviour (e.g. `a++ + ++a`, `i = i++`, unsequenced modifications, signed overflow, reading uninitialised variables, out-of-bounds access) unless the correct answer is "undefined behaviour".
3. Avoid implementation-defined output (e.g. `sizeof(int)` assumptions) unless stated.
4. Show the working: evaluate step by step.

## Verified examples (compiled and run with gcc)

| Code | Output | Why |
| --- | --- | --- |
| `int x=10; printf("%d", x++ * 2);` | 20 | post-increment uses the old value in the expression |
| `int a[]={10,20,30}; int *p=a; printf("%d\n", *p++); printf("%d\n", *p);` | 10, then 20 | `*p++` yields the old element, then `p` moves on. (Putting both in one `printf` would be unsequenced; keep them separate.) |
| `static int c=0; int f(int n){c+=n; return c;}` called as `f(1)` then `f(2)` | 1, then 3 | `static` keeps its value between calls |
| `char s[]="hello"; sizeof(s)` / `strlen(s)` | 6 / 5 | `sizeof` includes the `'\0'` |
| `7/2`, `-7/2`, `-7%3`, `7/2.0` | 3, -3, -1, 3.500000 | integer division truncates toward zero; `%` takes the dividend's sign |
| `int i=0; if(i=5) printf("assigned %d", i);` | assigned 5 | `=` is assignment, which evaluates to 5 (true) |
| `unsigned char u=255; u++; printf("%d", u);` | 0 | unsigned wraps around modulo 256 |
| `printf("%d", 5>3>1);` | 0 | parsed as `(5>3)>1` → `1>1` → 0 |
| `int k=3; printf("%d", k<<2);` | 12 | left shift by 2 multiplies by 4 |

## Topics to cover
Pointers and pointer arithmetic, operator precedence and associativity, increment/decrement, loops with `break`/`continue`, recursion, `static`, strings and `\0`, arrays vs pointers (`sizeof` differs), integer division, type promotion, bitwise operators, `switch` fall-through, macros (`#define SQ(x) x*x` with `SQ(2+3)` → `2+3*2+3` = 11).

## Java notes
- String `==` compares references; `.equals` compares content. Literals are interned, `new String("a") == "a"` is false.
- Integer division and `%` behave like C. `char + int` promotes to `int`.
- `static` blocks run once at class load; instance initialisation order: fields → constructor.
- Run the code with `java` before using it as a question.

## Traps worth teaching
Precedence of `&&` over `||`, short-circuit evaluation, missing `break` in `switch`, `sizeof` of an array parameter (a pointer), the dangling `;` after `if` or `for`.
