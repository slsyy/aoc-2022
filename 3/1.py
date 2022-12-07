#!/usr/bin/env python3
import sys

lines = list(map(str.strip, sys.stdin.readlines()))

print(lines)

score = 0

conficts = []

for l in lines:
    p = len(l) // 2
    a, b = l[:p], l[p:]

    conficts.extend(set(a) & set(b))


print(conficts)

def map(x):
    if 'a' <= x <= 'z':
        return ord(x) - ord('a') + 1
    else:
        return ord(x) - ord('A') + 27



m = [map(c) for c in conficts ]
print(m)
print(sum(m))