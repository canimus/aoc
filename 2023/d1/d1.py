import numpy as np
from pathlib import Path

from operator import itemgetter as it
from operator import add
from operator import methodcaller as mc
from functools import reduce, partial
from toolz import compose, remove, juxt

raw = Path("input.txt").read_text().split("\n")

_c = compose(int, partial(reduce, add), it(0,-1), list, partial(remove, str.isalpha))
result = sum(map(_c, raw))
print(result)

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

def convert(word):
    indices = list(juxt(*[mc("find", o) for o in words])(word))
    A = np.array(indices)
    matches = np.sort(A[np.where(A >= 0)])
    for i in matches:
        position = indices.index(i)
        d = words[position]
        if d in word:
            word = word.replace(d, str(digits[d]),1)

    return word

#raw = Path("test2.txt").read_text().split("\n")
_w = compose(_c, convert)
print(sum(map(_w, raw)))
