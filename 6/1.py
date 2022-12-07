#!/usr/bin/env python3
import sys

lines = sys.stdin.readlines()

line = lines[0]

size = 14

for i, _ in enumerate(line):
    s = line[i:i + size]
    if len(s) == size and len(set(s)) == size:
        print(i + size)
        break
