# 2️⃣ Merge Intervals Algorithm

(Range normalization — combining overlapping ranges into clean, non-overlapping ones)

### What it really is

You are given multiple numeric or time ranges.
Some of them overlap — and storing them as-is causes redundancy and confusion.

So you sort them and merge any that overlap so the final result contains minimal, non-overlapping ranges.

Think: normalize ranges so nothing overlaps.

### This matters when:

You’re handling calendar / appointment slots

Systems store time validity ranges

Databases optimize range partitions

Compilers / OS work with memory ranges

Security systems define firewall rule ranges

Bioinformatics tracks genomic spans

Anywhere ranges exist → merging is required.

### Workflow:

Sort intervals by start value

Initialize a list with the first interval

For each next interval:

If it overlaps with the last merged one → extend the range

If it does not overlap → append it as a new interval

Done — the list now contains normalized ranges

Overlap rule (most common):

current.start ≤ previous.end


If you want touching ranges like [1,2] & [2,3] not merged, change it to:

current.start < previous.end


Document the rule — ambiguity creates bugs.

### Example:
```
Input:
[1,3]
[2,6]
[8,10]
[9,11]

Output:
[1,6]
[8,11]

```
Because:

[1,3] and [2,6] overlap → merge into [1,6]

[8,10] and [9,11] overlap → merge into [8,11]

Usage (Python)
def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]

        if start <= last_end:   # overlaps
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return merged

Example run
print(merge_intervals([[1,3],[2,6],[8,10],[9,11]]))
 [[1, 6], [8, 11]]

### Edge cases:

Empty input

Single interval

Already merged ranges

Reverse-sorted input (sorting fixes it)

Fully contained interval

e.g., [1,10] and [2,3] → [1,10]

Touching intervals [1,2] & [2,3] — define whether they merge

Negative ranges (works fine)

Large numeric ranges

### Complexity:

Sorting: O(n log n)

Merge pass: O(n)

Total: O(n log n)

Memory: O(n)

If your data is already sorted → runtime becomes O(n).

### Where it’s actually used:

Calendar / booking & conflict resolution

CPU & memory segment allocation

Database index + range compression

Firewall / routing rule optimization

Time-series annotation

Pricing validity periods

Genome sequencing region mapping

Basically — whenever ranges overlap, normalize them.
