#!/usr/bin/env python3
import re
import sys

lines = sys.stdin.readlines()

stacks = []


def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n + 1):
        yield l[i:i + n]


for l in lines:
    if '[' not in l:
        break

    s = [x for x in divide_chunks(l, 3)]
    print(s)

    for _ in range(len(s) - len(stacks)):
        stacks.append([])

    for i, x in enumerate(s):
        if x[1] != " ":
            stacks[i].insert(0, x[1])

print(stacks)

for l in lines:
    m = re.findall(r"move (\d+) from (\d+) to (\d+)", l)
    if not m:
        continue
    print(m)
    m = m[0]
    m = [int(x) for x in m]
    n, f, t = m

    stacks[t-1].extend(stacks[f-1][-n:])
    del stacks[f-1][-n:]

print()
for s in stacks:
    print(s[-1],end="")

