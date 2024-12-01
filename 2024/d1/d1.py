import numpy as np
from pathlib import Path
from typing import Tuple, List
from toolz import compose, first, last, juxt
from toolz.curried import map as map_curried
from collections import Counter
from operator import methodcaller as mc
from icecream import ic

# Load Data
raw = (Path(__file__).parent / "input.txt").read_text().split("\n")


def split(row: str) -> Tuple[int, int]:
    """Splits a row of two numbers into a tuple of ints"""
    return tuple(list(map(compose(int, str.strip), filter(None, row.split(" ")))))


def order(pairs: List) -> Tuple[List]:
    """Order pairs of tuples in sorted lists"""
    first_list = compose(sorted, map_curried(first))
    second_list = compose(sorted, map_curried(last))
    return tuple(
        juxt(first_list, second_list)(pairs)
    )


def similarity(left: np.array, right: np.array) -> int:
    """Search for instances of numbers on left in right and compute score"""
    _item = mc("item")
    scores = dict(Counter(map(_item, right)).items())
    return np.sum([x * scores.get(x, 0) for x in left]).item()


# Ordered Lists
a, b = map(np.array, order(map(split, raw)))

# Part 1
ic(np.abs(a - b).sum().item())

# Part: 2
ic(similarity(a, b))
