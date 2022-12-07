#!/usr/bin/env python3
import sys

lines = list(map(str.strip, sys.stdin.readlines()))

print(lines)

n = 0

for l in lines:
    # print(l)
    a, b = l.split(",")
    a = a.split("-")
    b = b.split("-")

    a = [int(x) for x in a]
    b = [int(x) for x in b]
    a, b = sorted([a, b])

    if a[0] == b[0]:
        a, b = sorted([a, b], key=lambda x: x[1], reverse=True)

    if a[1] >= b[0]:
        print(a, b)
        n += 1
    # else:
        # print(l)

print(n)
