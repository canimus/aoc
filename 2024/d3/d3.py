# %%
from pathlib import Path
import re
from operator import mul
from itertools import starmap
import chalk

# %%
data = (Path(__file__).parent / "input.txt").read_text().split("\n")


# %%
_i = lambda x: tuple(map(int, x.split(",")))
results = []
for row in data:
    result = sum(starmap(mul, map(_i, re.findall(r"mul\((\d{1,3},\d{1,3})\)", row))))
    results.append(result)

# %%
# Part 1: 167090022
print(sum(results))

# %%
x = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

# %%
pattern = r"(do\(\)|don't\(\))"

# %%
results = []
flag = True
for row in data:
    for part in re.split(pattern, row):
        if "don't()" == part:
            flag = False
            continue
        if "do()" == part:
            flag = True

        if flag:
            matches = re.findall(r"mul\((\d{1,3},\d{1,3})\)", part)
            if matches:
                results.append(sum(starmap(mul, (map(lambda x: tuple(map(int, x.split(","))), matches)))))
        else:
            continue
            
    


# %%
print(sum(results))


