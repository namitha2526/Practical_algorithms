1️⃣ Control Break Algorithm

(Streaming group-wise processing — not the toy “group by” you see online)

What it really is

You process sorted data record-by-record and detect when the “group key” changes.
At the boundary, you finalize the previous group’s aggregation — without storing everything in memory.

This matters when:

Data is huge (logs, ETL pipelines, mainframes, streaming batch jobs)

You can’t load everything at once

Sorting is cheap / already guaranteed (DB output, MapReduce shuffle, etc.)

If your input is not sorted — the algorithm breaks. Document that clearly.

Workflow

Read first record → initialize group accumulator

For each next record:

If key == current group key → keep aggregating

If key changes → output result for old group → reset accumulator

At end → flush last group

Think: group-by but memory-safe.
Example

Input (sorted by department):
```
(dept=A, salary=10)
(dept=A, salary=20)
(dept=B, salary=50)
(dept=B, salary=10)
(dept=B, salary=40)
```
Output (sum salary per dept):
```
A → 30
B → 100
```
Usage 
```
records = [
    ("A", 10),
    ("A", 20),
    ("B", 50),
    ("B", 10),
    ("B", 40)
]

result = list(
    control_break(
        records,
        key_fn=lambda r: r[0],
        agg_fn=lambda acc, r: acc + r[1],
        initial_value=0
    )
)

print(result)
# [('A', 30), ('B', 100)]
```
Edge cases you MUST mention

Input must be sorted by key

Empty input

Single record

Group with only one record

Reset logic bug — beginners always mess this up

Complexity

Time: O(n)

Memory: O(1) (huge win vs storing all groups)

Where it’s actually used

ETL / data warehousing

MapReduce reduce phase

Bank / telecom batch processing

Log aggregation

Stream processing when ordering exists
