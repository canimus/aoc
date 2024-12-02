# %%
import numpy as np
from pathlib import Path

# %%
raw = (Path(__file__).parent / "input.txt").read_text().split("\n")

# %%
data = [list(map(int, r.split())) for r in raw]
len(data)

# %%
def condition_a(row: np.ndarray, wor: np.ndarray) -> bool:
    return (np.all(row[:-1] <= row[1:])) or (np.all(wor[:-1] <= wor[1:]))

def condition_b(row: np.ndarray, wor: np.ndarray) -> bool:
    diff_a = row[1:] - row[:-1]
    diff_b = wor[1:] - wor[:-1]
    return (np.all((diff_a >= 1) & (diff_a <= 3))) or (np.all((diff_b >= 1) & (diff_b <= 3)))

# %%
reports = 0
for arr in data:
    row = np.array(arr)
    wor = row[::-1]
    cond_a = condition_a(row, wor)
    cond_b = condition_b(row, wor)
    if cond_a and cond_b:
        reports += 1

# Part 1: 559
print(reports)


reports = 0
for arr in data:
    row = np.array(arr)
    wor = row[::-1]
    cond_a = condition_a(row, wor)
    cond_b = condition_b(row, wor)
    if cond_a and cond_b:
        reports += 1
    else:
        for fix in range(len(arr)):
            row_prime = np.delete(arr, fix)
            wor_prime = row_prime[::-1]
            cond_a = condition_a(row_prime, wor_prime)
            cond_b = condition_b(row_prime, wor_prime)
            if cond_a and cond_b:
                reports += 1
                break

# Part 2: 601
print(reports)

# %%



