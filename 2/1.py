#!/usr/bin/env python3
import sys

lines = list(map(str.strip, sys.stdin.readlines()))

print(lines)

score = 0

for l in lines:
    opponent, me = l.split(" ")

    opponent = {
        "A": "X",
        "B": "Y",
        "C": "Z",
    }[opponent]

    score += ["X", "Y", "Z"].index(me)+1

    if opponent == me:
        score += 3

    if me == "X" and opponent == "Z":
        score += 6

    if me == "Y" and opponent == "X":
        score += 6

    if me == "Z" and opponent == "Y":
        score += 6

print(score)

