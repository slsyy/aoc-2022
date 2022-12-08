#!/usr/bin/env python3
import sys

lines = list(map(str.strip, sys.stdin.readlines()))
lines = [[int(c) for c in l] for l in lines]

h = len(lines)
w = len(lines[0])

count = 0


def iss(l):
    l = list(l)
    t = l[-1]

    c = 0
    rest = list(reversed(l[:-1]))
    for r in rest:
        c += 1
        if t <= r:
            break

    return c


def i(x, y):
    row = lines[y]
    column = [lines[yy][x] for yy in range(h)]

    score = 1
    score *= iss(row[:x + 1])
    score *= iss(reversed(row[x:]))

    score *= iss(column[:y + 1])
    score *= iss(reversed(column[y:]))

    return score


scores = []
for y in range(h):
    for x in range(w):
        scores.append(i(x, y))

print(scores)
print(max(scores))
