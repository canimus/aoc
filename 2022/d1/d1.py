from collections import deque
from pathlib import Path
import sys

# Input
raw = Path("input.txt").read_text().split("\n")

# Part 1
q = deque(range(3),maxlen=3)

calories = 0
for i in raw:
    if i == '':
        if calories > min(q):
            q[q.index(min(q))] = calories

        calories = 0
    else:
        calories += int(i)

max(q)

# Part 2
sum(q)