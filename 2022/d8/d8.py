from pathlib import Path
import re
import toolz
from collections import defaultdict

# Input
raw = Path("input.txt").read_text().split("\n")

# Part 1
stack = []
inventory = defaultdict(int)
edges = {}
counter = 0
dirs = 0

def dname():
    return ".".join(stack)

for i in raw:
    if i.startswith("$"):
        if "cd" in i:
            _,_,path = i.split(" ")
            if path == "..":
                stack.pop()
            else:
                stack += [path]
        elif "ls" in i:
            # inventory[dname()] += 0
            edges[dname()] = []
    elif re.match(r"^\d+\s.*", i):
        counter += 1
        fsize, fname = i.split(" ")
        # inventory[dname()].update([tuple([fname, int(fsize)])])
        inventory[dname()] += int(fsize)
    else:
        dirs += 1
        d = i.split(" ")[1]
        edges[dname()] += [f"{dname()}.{d}"]


def total_inside(key, acc=0):
    if len(edges[key]) == 0:
        return acc
    else:
        return acc + sum([total_inside(i, inventory[i]) for i in edges[key]])

total = defaultdict(int)
for e in edges.keys():
    base = 0
    base += total_inside(e, inventory[e])
    total[e] += base

target = toolz.valfilter(lambda x: x<=100000, total).values()

# P1
print(sum(target))

# Part 2
FS = 70000000
UPDATE = 30000000

requirement = UPDATE - (FS - total["/"])
freeup = toolz.valfilter(lambda x: x >= requirement, total).values()

# P2
print(toolz.first(sorted(freeup)))
