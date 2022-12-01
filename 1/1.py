#!/usr/bin/env python3
import sys

lines = list(map(str.strip, sys.stdin.readlines()))

print(lines)

elfs = []

curr = 0

for l in lines:
    if l == "":
        elfs.append(curr)
        curr = 0
    else:
        curr += int(l)

print(elfs)
print(max(elfs))

# 2

print(sum(sorted(elfs, reverse=True)[:3]))
