# Placement rounds: no-library programming problems

Reported Indian campus programming rounds often ask for plain-C or Java solutions without built-in collections or library helpers. The exact rules differ by company and drive, so never state them as fact. Say "reported" and follow `company-search.md` when a company is named.

## Default rules for Placement mode

- Language: C by default, Java on request.
- Allowed: loops, arrays, `printf` or `System.out`, and your own helper functions.
- Not allowed: library helpers that do the work (`strrev`, `strcat`, `sort`, `qsort`, collections, streams, regex).
- Reading input with `scanf` or `Scanner` is fine. Tell the student if input is hard-coded for the sample.
- Prefer one clear method over a clever one. State complexity from the code.

## Problem types

| Type | Examples |
| --- | --- |
| Strings | reverse words, remove duplicates in place, palindrome, anagram check, count vowels |
| Matrix | spiral print, rotate 90°, row and column sums, transpose |
| Patterns | pyramid, diamond, number triangle |
| Numbers | palindrome, Armstrong, prime, GCD, digit sums |

## Verified solutions (compiled and run with gcc)

### Reverse the words in a string
Input `the sky is blue` → output `blue is sky the`.
```c
void rev(char *s, int i, int j) {
    while (i < j) { char t = s[i]; s[i] = s[j]; s[j] = t; i++; j--; }
}
void reverse_words(char *s) {
    int n = 0; while (s[n]) n++;
    rev(s, 0, n - 1);                          /* reverse everything */
    int start = 0;
    for (int i = 0; i <= n; i++) {
        if (s[i] == ' ' || s[i] == '\0') {     /* reverse each word back */
            rev(s, start, i - 1);
            start = i + 1;
        }
    }
}
```
Time O(n): each character is swapped at most twice. Space O(1). Assumes single spaces.

### Remove duplicate characters in place (keep the first)
Input `programming` → output `progamin`.
```c
void dedupe(char *s) {
    int seen[256] = {0}, w = 0;
    for (int r = 0; s[r]; r++) {
        unsigned char c = s[r];
        if (!seen[c]) { seen[c] = 1; s[w++] = c; }
    }
    s[w] = '\0';
}
```
Time O(n). Space O(1): the 256-entry table does not grow with n.

### Spiral order of a 3×4 matrix
Input `{{1,2,3,4},{5,6,7,8},{9,10,11,12}}` → `1 2 3 4 8 12 11 10 9 5 6 7`.
```c
void spiral(int a[3][4], int R, int C) {
    int top = 0, bot = R - 1, l = 0, r = C - 1;
    while (top <= bot && l <= r) {
        for (int j = l; j <= r; j++) { printf("%d ", a[top][j]); }
        top++;
        for (int i = top; i <= bot; i++) { printf("%d ", a[i][r]); }
        r--;
        if (top <= bot) {                      /* guard: single remaining row */
            for (int j = r; j >= l; j--) { printf("%d ", a[bot][j]); }
            bot--;
        }
        if (l <= r) {                          /* guard: single remaining column */
            for (int i = bot; i >= top; i--) { printf("%d ", a[i][l]); }
            l++;
        }
    }
}
```
Time O(R·C): every cell is printed once. Space O(1). The two guards stop a row or column printing twice.

### Rotate a 3×3 matrix 90° clockwise in place
Input `{{1,2,3},{4,5,6},{7,8,9}}` → `{{7,4,1},{8,5,2},{9,6,3}}`.
```c
void rotate(int a[3][3]) {
    for (int i = 0; i < 3; i++)                /* transpose */
        for (int j = i + 1; j < 3; j++) { int t = a[i][j]; a[i][j] = a[j][i]; a[j][i] = t; }
    for (int i = 0; i < 3; i++) {              /* reverse each row */
        int l = 0, r = 2;
        while (l < r) { int t = a[i][l]; a[i][l] = a[i][r]; a[i][r] = t; l++; r--; }
    }
}
```
Time O(n²) for an n×n matrix. Space O(1).

### Number checks
`is_pal(12321)` → 1, `is_pal(1231)` → 0, `armstrong(153)` → 1, `armstrong(154)` → 0, `is_prime(97)` → 1, `is_prime(91)` → 0 (91 = 7 × 13).
```c
int is_pal(int n) { int o = n, r = 0; while (n > 0) { r = r * 10 + n % 10; n /= 10; } return o == r; }
int armstrong(int n) {
    int o = n, d = 0, t = n;
    while (t) { d++; t /= 10; }
    int s = 0;
    while (n) { int x = n % 10, p = 1; for (int k = 0; k < d; k++) p *= x; s += p; n /= 10; }
    return s == o;
}
int is_prime(int n) { if (n < 2) return 0; for (int i = 2; i * i <= n; i++) if (n % i == 0) return 0; return 1; }
```
`is_pal`: O(log n). `armstrong`: O(d²) for d digits. `is_prime`: O(√n).

### Pattern printing
Pyramid of height 4: row i prints `4 − i` spaces then `2i − 1` stars.
```
   *
  ***
 *****
*******
```
Number triangle of height 4: row i prints `1` to `i`.
```
1
12
123
1234
```

## Timed follow-ups to ask
Handle multiple spaces; use no extra array; make it work for n × m; reduce it from O(n²) to O(n). Give the student a time limit and let them track it; the AI cannot run a countdown.

## Traps
- Off-by-one on string ends and the `'\0'`.
- Forgetting the single-row or single-column guards in spiral.
- Reversing a word using the wrong end index when it is last in the string.
- Integer overflow in Armstrong or palindrome checks for large inputs.
