# %%
import numpy as np
from pathlib import Path
import enum

# %%
raw = Path("input.txt").read_text().split("\n")

# %%
A = np.array([[i for i in c] for c in raw])
w,h = A.shape
y,x = np.where(A == "^")
y,x = x.item(), y.item()

# %%
y,x

# %%
class Direction(enum.Enum):
    N = 'N'
    S = 'S'
    E = 'E'
    W = 'W'

# %%
def is_available(a,b,M):    
    if (p := M[a,b]) in ['.', '^']:
        return True
    return False
    
def is_block(a,b,M):
    if (p := M[a,b]) == '#':
        return True
    return False

# %%
movement = [tuple([x,y])]
direction = Direction.N
is_exit = False
print(f"Start: {x},{y}")

while not is_exit:
    try:
        match direction:
            case Direction.N:
                if is_available(x-1,y,A):
                    A[x,y] = '.'
                    A[x-1,y] = '^'
                    x -= 1
                elif is_block(x-1,y, A):
                    direction = Direction.E
                    A[x,y] = '>'
            case Direction.S:
                if is_available(x+1,y,A):
                    A[x,y] = '.'
                    A[x+1,y] = 'v'
                    x += 1
                elif is_block(x+1,y, A):
                    direction = Direction.W
                    A[x,y] = '<'
            case Direction.E:
                if is_available(x,y+1,A):
                    A[x,y] = '.'
                    A[x,y+1] = '>'
                    y += 1
                elif is_block(x,y+1, A):
                    direction = Direction.S
                    A[x,y] = 'v'
            case Direction.W:
                if is_available(x,y-1,A):
                    A[x,y] = '.'
                    A[x,y-1] = '<'
                    y -= 1
                elif is_block(x,y-1, A):
                    direction = Direction.N
                    A[x,y] = '^'

        movement.append(tuple([x,y]))
        if (x <= 0) or (x >= w):
            is_exit = True
        if (y <= 0) or (y >= h):
            is_exit = True

        #print(f"D:{direction.value}|<{x},{y}>|M{len(set(movement))}")
        #print(A)
    except Exception as e:
        break

print(len(set(movement)))

# %%
# 5329: OK

# %%



