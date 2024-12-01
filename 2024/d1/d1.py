import numpy as np
from pathlib import Path
from typing import Tuple, List
from toolz import compose
from collections import Counter
from operator import methodcaller as mc
from icecream import ic
from pathlib import Path

# Load Data
raw = (Path(__file__).parent / "input.txt").read_text().split("\n")

def split(row: str) -> Tuple[int,int]:
    """Splits a row of two numbers into a tuple of ints"""
    return tuple(list(map(compose(int, str.strip), filter(None, row.split(" ")))))

def order(pairs: List) -> Tuple[List]:
    """Order pairs of tuples in sorted lists"""
    a = []
    b = []
    for x,y in pairs:
        a.append(x)
        b.append(y)

    return tuple([sorted(a), sorted(b)])

def distance(x: int, y: int) -> int:
    """Absolute distance between points L1"""
    return abs(y-x)

def similarity(l: np.array, r: np.array) -> int:
    """Search for instances of numbers on left in right and compute score"""
    _item = mc("item")
    scores = dict(Counter(map(_item, r)).items())
    return np.sum([x * scores.get(x, 0) for x in l]).item()

# Ordered Lists
a,b = map(np.array, order(map(split, raw)))

# Part 1
ic(np.abs(a-b).sum().item())

# Part: 2
ic(similarity(a,b))
