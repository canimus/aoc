# %%
import numpy as np
from pathlib import Path
from numpy.lib.stride_tricks import sliding_window_view


# %%
raw = Path("input.txt").read_text().split("\n")

# %%
data = np.array([list(c) for c in raw])
data

# %%
windows_v = sliding_window_view(data, 4, axis=0)
windows_h = sliding_window_view(data, 4, axis=1)
windows_d = sliding_window_view(data, (4,4))

v1,v2,_ = windows_v.shape
windows_v = windows_v.reshape(v1*v2, 4)

h1,h2,_ = windows_h.shape
windows_h = windows_h.reshape(h1*h2, 4)

d1,d2,_,_ = windows_d.shape
windows_d = windows_d.reshape(d1*d2, 4,4)

# %%
kernel = np.matrix(['X', 'M','A', 'S'])
kernel

# %%
kernel_1 = kernel
kernel_2 = np.flip(kernel_1)
kernel_3 = kernel_1.T
kernel_4 = kernel_2.T
kernel_5 = np.matrix([list(c) for c in 'X   ; M  ;  A ;   S'.split(";")])
kernel_6 = np.flip(kernel_5)
kernel_7 = kernel_5[::-1]
kernel_8 = np.flip(kernel_7)

# %%
counter_h = 0
for word in windows_h:
    if np.all(word == kernel_1) or np.all(word == kernel_2):
        counter_h += 1
            #print(f"OK: {counter}", word)
counter_h
            

# %%
counter_v = 0
for word in windows_v:
    if np.all(word.reshape(1,4) == kernel_3.A.flatten()) or np.all(word.reshape(1,4) == kernel_4.A.flatten()):
    #if np.all(word == kernel_3) or np.all(word == kernel_4):
        counter_v += 1
        #print(f"OK: {counter}", word)
counter_v

# %%
counter_d = 0
for word in windows_d:
    if np.all(np.diag(word == kernel_5)) or np.all(np.diag(word == kernel_6)):
        counter_d += 1
    if np.all(np.diag(((word == kernel_7)[::-1]))) or np.all(np.diag(((word == kernel_8)[::-1]))):
        counter_d += 1
        #print(f"OK {counter}:[{x},{y}]")

counter_d
            

# %%
# 2358: OK
counter_h + counter_v + counter_d

# %%
x_kernel_1 = np.array([['M', ' ', 'S'], [' ', 'A', ' '], ['M', ' ', 'S']])
x_kernel_2 = np.flip(x_kernel_1)
x_kernel_3 = np.array([['M', ' ', 'M'], [' ', 'A', ' '], ['S', ' ', 'S']])
x_kernel_4 = np.flip(x_kernel_3)

# %%
for i in range(1,5):
    print(eval(f"x_kernel_{i}"))

# %%
data2 = np.array([['M', 'P', 'M'],['P', 'A', 'P'],['S', 'P', 'S']])

# %%
windows = sliding_window_view(data, (3,3))

# %%
a,b,_,_ = windows.shape

# %%
windows_x = windows.reshape(a*b, 3,3)

# %%
counter_x = 0
for word in windows_x:
    if np.all(np.diag(word == x_kernel_1)) and np.all(np.diag((word == x_kernel_1)[::-1])):
        counter_x += 1
        continue
    if np.all(np.diag(word == x_kernel_2)) and np.all(np.diag((word == x_kernel_2)[::-1])):
        counter_x += 1
        continue
    if np.all(np.diag(word == x_kernel_3)) and np.all(np.diag((word == x_kernel_3)[::-1])):
        counter_x += 1
        continue
    if np.all(np.diag(word == x_kernel_4)) and np.all(np.diag((word == x_kernel_4)[::-1])):
        counter_x += 1
        continue


counter_x

# %%
# 1737


