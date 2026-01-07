# ⏩ Skip Lists — Deep Dive
(A probabilistic alternative to balanced binary search trees — with simpler logic and similar performance)
Core Problem They Solve

A plain sorted linked list has O(n) search because you must walk node-by-node.

Balanced BSTs fix this with O(log n) search — but rotations and invariants make them complex.

Skip lists give you the same asymptotic performance as balanced trees, but using probability instead of strict structural guarantees.

Translation:

We accept randomness → in exchange for dramatically simpler code.

And it works in practice — Redis uses skip lists for sorted sets. That’s a strong validation.

#### 1️⃣ Structure — What a Skip List Actually Looks Like

Imagine a sorted linked list:

1 → 3 → 5 → 7 → 9 → 13 → 15


Now add “express lanes” on top that skip nodes:

Level 3:      1 ------------ 9
Level 2:      1 ---- 5 ---- 9 ---- 15
Level 1:  1 → 3 → 5 → 7 → 9 → 13 → 15


#### Rules:

Level 1 has every node

Higher levels contain random subsets

Each node may exist in multiple levels

Highest level has very few nodes

So instead of scanning 15 elements linearly,
you jump ahead, then drop down.

#### 2️⃣ Searching — Step-by-Step Logic

Say we search for 9.

Start at the highest level, leftmost node.

Level 3
1 → 9


1 < 9 → move right
Next is 9 → stop here
Drop down to next level.

Level 2

We are already at 9 → drop down.

Level 1

We are on 9 → match

Done.

Why is this fast?

Because each level cuts the search space roughly in half.

Expected number of elements per level:

Level 0: n
Level 1: n/2
Level 2: n/4
Level 3: n/8
...


So expected height = O(log n)
And search = O(log n)

You didn’t “prove” it — but the intuition is strong enough.

#### 3️⃣ The Magic Trick — Random Promotion

When inserting a new node:

Insert into base level (like a normal sorted list)

Flip a coin

If heads → promote to next level

Flip again

If heads → promote again

Stop when tails OR hit max level

So probability of levels per node:

Level 0 → 100%
Level 1 → 50%
Level 2 → 25%
Level 3 → 12.5%
Level 4 → 6.25%
…


This is why lists “self-balance”.

No rotations.
No structural fix-ups.

Just probability.

#### 4️⃣ Insert — Real Walkthrough

Insert 6 into:

Level 2:  1 ---- 5 ---- 9
Level 1:  1 → 3 → 5 → 7 → 9

Step 1 — Search insertion position

Move like a search, but store the last node visited at each level:

We record:

Level 2 : stops at 5
Level 1 : stops at 5

Step 2 — Insert at level 1
1 → 3 → 5 → 6 → 7 → 9

Step 3 — Flip coin

Say it promotes → add at Level 2

Level 2: 1 ---- 5 -- 6 -- 9


Flip again:
Say tails → stop.

Done.

This update path storage is crucial — without it you’d need to restart.

#### 5️⃣ Delete — Straightforward

Search like normal.
If found → remove from all levels.
Done.

#### 6️⃣ Complexity — But Be Honest About It

Skip lists are probabilistic.
```
Expected:

Search: O(log n)
Insert: O(log n)
Delete: O(log n)
Space:  O(n)


Worst case (if all nodes promoted to all levels):

O(n)
```

But probability of that happening = practically zero.

So you get balanced-tree performance without the pain.

#### Edge cases:

Duplicate keys — decide policy

Very skewed randomness — still rare

Memory overhead — multiple pointers per node

Deterministic mode → replace randomness with fixed levels

#### Where it’s actually used:

Redis Sorted Sets (ZSET)

Concurrent maps (Java’s ConcurrentSkipListMap)

In-memory databases

Key-value index structures

Because:
✔ simpler than trees
✔ fast enough
✔ concurrency-friendly
