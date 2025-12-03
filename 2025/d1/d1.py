# %%
import numpy as np
from pathlib import Path
from collections import Counter
import chalk
# %%
raw = Path("input.txt").read_text().splitlines()
# %%
coords = list(map(lambda x: tuple([x[0], int(x[1:])]), raw))

# %%
p = 50
r1 = 0
r2 = 0
for i,j in coords:
    for _ in range(j):
        if i == 'L':
            p = (p-1+100)%100
        else:
            p = (p+1)%100
        if p == 0:
            r2 += 1
    if p == 0:
        r1 += 1


# %%
print(r1)
print(r2)


