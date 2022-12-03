from pathlib import Path
from toolz import first
import numpy as np
from functools import reduce

# Input
raw = Path("input.txt").read_text().split("\n")

# Part 1
def priority(c):
    o = ord(c)
    if o > 96:
        v = o - 96
    else:
        v = o - 38
    return v

def split(x):
    l = len(x)
    a,b = x[:l//2], x[l//2:]
    i = first(set(a).intersection(b))
    
    return priority(i)

# P1
sum(map(split, raw))


# Part 2
data = np.array_split(raw, len(raw)//3)

def group(d):
    v = reduce(lambda a,b: a.intersection(b), [set(x) for x in d])
    return priority(first(v))

# P2
sum([group(p) for p in data])