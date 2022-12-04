from pathlib import Path

# Input
raw = Path("input.txt").read_text().split("\n")

# Part 1

def srange(s):
    x,y = list(map(int,s.split(",")))
    return set(range(x,y+1))

def split(e):
    a,b = e.replace(",","|").replace("-",",").split("|")
    return srange(a),srange(b)

def overlap(a,b):
    if a.issuperset(b) or b.issuperset(a):
        return 1
    else:
        return 0

def intersect(a,b):
    if len(a.intersection(b)) > 0:
        return 1
    else:
        return 0

# P1: 550
sum([overlap(*split(i)) for i in raw])


# P2: 931
sum([intersect(*split(i)) for i in raw])