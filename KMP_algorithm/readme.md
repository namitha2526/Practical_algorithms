# 🔍 KMP (Knuth–Morris–Pratt) Algorithm

(Fast substring search — avoids re-checking characters you already matched)

What it really is

KMP is a pattern-matching algorithm used to find a pattern P inside a text T in O(n + m) time.

Instead of restarting from the next character after a mismatch (like the naïve method), KMP remembers what part of the pattern already matched, so it doesn’t waste work.

### This matters when:

Text is large (logs, documents, DNA strings)

Pattern is repetitive (like "aaaaab")

You need predictable linear time

Searching happens frequently (editors, compilers, search tools)

Anywhere large strings exist → KMP is useful.

Workflow

### KMP has two main steps:

1️⃣ Build the LPS Array (Longest Prefix that is also Suffix)

For each position i in the pattern:
LPS[i] = length of the longest prefix of the pattern that is also a suffix ending at i

This allows the algorithm to know how far to “jump back” on mismatch.

2️⃣ Search Phase

Compare pattern with text:

If characters match → advance both pointers

If mismatch:

Don’t restart

Jump pattern index back using the LPS table

Continue until match is found or text ends

This prevents redundant comparisons.

### Example
Pattern:
A B A B A C
0 1 2 3 4 5   (index)

LPS Array:
0 0 1 2 3 0


Meaning at index 4 (pattern "ABABA")
→ the longest prefix "ABA" is also a suffix "ABA"
→ length = 3

So if mismatch happens here, jump back to length 3, not zero.

Usage (Python)
```
def build_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps



def kmp_search(text, pattern):
    if not pattern:
        return 0

    lps = build_lps(pattern)
    i = j = 0

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == len(pattern):
                return i - j
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1
```
### Example
kmp_search("ABABDABACDABABCABAB", "ABABCABAB")
returns 10


Pattern starts at index 10.

### Edge cases:

Empty pattern → match at index 0

Pattern longer than text → no match

All characters same (aaaaaa…)

Pattern appears multiple times

Case-sensitivity depends on input

### Complexity:

#### Time:

Build LPS → O(m)

Search → O(n)

Total = O(n + m)

#### Memory:

O(m) for LPS

This beats the naïve O(n·m) worst case.
