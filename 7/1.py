#!/usr/bin/env python3
import json
import re
import sys

lines = list(map(str.strip, sys.stdin.readlines()))

root = {}
curr = None


def parent(root, n):
    for c in root.values():
        if c is n:
            return root

    for c in root.values():
        if isinstance(c, dict):
            if found := parent(c, n):
                return found

    return None


while lines:
    l = lines[0]

    if m := re.findall(r'\$ cd (.*)', l):
        m = m[0]
        match m:
            case "/":
                curr = root
            case "..":
                curr = parent(root, curr)
            case _:
                curr = curr[m]

        lines = lines[1:]
    elif l == "$ ls":
        lines = lines[1:]
        while lines and not lines[0].startswith("$"):
            l = lines[0]
            lines = lines[1:]

            if m := re.findall(r'dir (.*)', l):
                curr[m[0]] = {}
            elif m := re.findall(r'(\d+) (.*)', l):
                m = m[0]
                curr[m[1]] = int(m[0])

    else:
        raise RuntimeError("unhandled")

print(json.dumps(root, indent=2))

sizes = []

def rec(n):
    size = 0

    # print(n)

    for c in n.values():
        if isinstance(c, int):
            size += c
        if isinstance(c, dict):
            size += rec(c)

    sizes.append(size)
    return size



rec(root)
print(sizes)
print(sum([s for s in sizes if s <=100000]))

# 2

needed = 30000000 - (70000000 - max(sizes))

print(sorted([s for s in sizes if s >= needed])[0])


