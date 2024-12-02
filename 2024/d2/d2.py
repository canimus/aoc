reports = 0
for row in data:
    wor = row[::-1]
    cond_a = (np.all(row[:-1] <= row[1:])) or (np.all(wor[:-1] <= wor[1:]))
    diff_a = row[1:] - row[:-1]
    diff_b = wor[1:] - wor[:-1]
    cond_b = (np.all((diff_a >= 1) & (diff_a <= 3))) or (np.all((diff_b >= 1) & (diff_b <= 3)))
    if cond_a and cond_b:
        reports += 1

reports