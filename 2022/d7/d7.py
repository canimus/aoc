import numpy as np
from pathlib import Path

# Input
raw = Path("input.txt").read_text().split("\n")[0]

def search_signal(s, w=4):
    for i in range(len(s)-1):
        if len(set(list(s[i:i+w]))) == w:
            return i+w
# Part 1
print(search_signal(raw, w=4))

# Part 2
print(search_signal(raw, w=14))