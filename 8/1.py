#!/usr/bin/env python3
import sys

lines = list(map(str.strip, sys.stdin.readlines()))
lines = [[int(c) for c in l] for l in lines]

h = len(lines)
w = len(lines[0])

count = 0


def iss(l):
    l = list(l)
    if len(l) == 1:
        return True
    return max(l[:-1]) < l[-1]



def i(x, y):
    row = lines[y]
    column = [lines[yy][x] for yy in range(h)]

    if iss(row[:x + 1]):
        return True

    if iss(reversed(row[x:])):
        return True

    if iss(column[:y + 1]):
        return True

    if iss(reversed(column[y:])):
        return True

    return False


for y in range(h):
    for x in range(w):
        if i(x, y):
            print(y, x)
            count += 1

print(count)
