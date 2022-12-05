from pathlib import Path
from functools import partial
from toolz import first, compose
import numpy as np
import re

# Input
raw = Path("test.txt").read_text().split("\n")

# Clean Data
clean_fn = compose(first, partial(re.subn, "[\[\]]", " "))

# Data Split
stack = list(filter(lambda x: not x.startswith("move") and x != '', raw))[:-1]
moves = list(filter(lambda x: x.startswith("move"), raw))

horizontal = []
for row in map(clean_fn, stack):
    mask = range(0, len(row), 4)
    horizontal.append(np.array(list(row)[1:-1])[mask])

rows = np.array(horizontal)

vertical = []
for i in range(rows.shape[1]):
    vertical.append(rows[:,i:i+1])


global crates
crates = []
def reset_crates():    
    for c in vertical:
        crates.append(list(reversed(list(filter(lambda x: x != ' ', c.flatten())))))

def move_instruction(s):
    return map(int, first(re.findall(r"move (\d+) from (\d+) to (\d)+", s)))

def move_action(a,b,c):
    x = crates[b-1]
    y = crates[c-1]
    for i in range(a):
        y.append(x.pop())

for m in moves:
    move_action(*move_instruction(m))

# # P1
# print("".join(list(map(lambda x: x[-1], crates))))

# def move_multiple(a,b,c):
#     x = crates[b-1]
#     y = crates[c-1]
#     y += x[len(x)-a:]
#     [x.pop() for _ in range(a)]

# crates = reset_crates()

# # P2
# for m in moves:
#     move_multiple(*move_instruction(m))

# # P2
# print("".join(list(map(lambda x: x[-1], crates))))