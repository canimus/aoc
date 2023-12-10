import numpy as np
from pathlib import Path

from operator import itemgetter as it
from operator import add
from operator import methodcaller as mc
from functools import reduce, partial
from toolz import compose, remove, juxt, first, last

raw = Path("input.txt").read_text().split("\n")

_c = compose(int, partial(reduce, add), it(0,-1), list, partial(remove, str.isalpha))
print(sum(map(_c, raw)))

digits = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
}

words = list(digits.keys())
numbers = list(map(str, digits.values()))
tokens = words + numbers

def find_digit(word, side : str = "left"):
    if side == "left":
        fn = "find"
        take = first
    else:
        fn = "rfind"
        take = last
    indices = list(juxt(*[mc(fn, o) for o in tokens])(word))
    A = np.array(indices)
    match = take(np.sort(A[np.where(A >= 0)]))
    position = indices.index(match)
    if position > 8:
        value = numbers[position - 9]
    else:
        value = digits[words[position]]

    return str(value)

_l = lambda x: find_digit(x, "left")
_r = lambda x: find_digit(x, "right")

_w = compose(int, partial(reduce, add), juxt(_l, _r))
print(sum(map(_w, raw)))
