from pathlib import Path
import numpy as np
import pandas as pd
import toolz

# Input
raw = Path("input.txt").read_text().split("\n")

# Part 1
hand2 = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3
}

hand1 = {
    "A" : "X",  # Rock
    "B" : "Y",  # Paper
    "C" : "Z"   # Scissor
}

rules = {
    "XX" : "D",
    "YY" : "D",
    "ZZ" : "D",
    "XY" : "W",
    "XZ" : "L",
    "YX" : "L",
    "YZ" : "W",
    "ZX" : "W",
    "ZY" : "L"
}

game = {
    "W" : 6,
    "D" : 3,
    "L" : 0
}

result = {
    "X" : "L",
    "Y" : "D",
    "Z" : "W"
}

df = pd.DataFrame(list(map(lambda x: x.split(" "), raw)), columns=["Code", "Elf2"])
df["Elf1"] = df["Code"].map(hand1)
df["Game"] = df["Elf1"] + df["Elf2"]
df["Result"] = df["Game"].map(rules)
df["Score"] = df["Result"].map(game)
df["Extra"] = df["Elf2"].map(hand2)
df["Total"] = df["Score"] + df["Extra"]

# P1
df.Total.sum()

# Part 2
df["Predict"] = df["Elf2"].map(result)

def predict(outcome, hand):
    options = toolz.valfilter(lambda x: x == outcome, rules)
    return toolz.first(toolz.keyfilter(lambda x: x.startswith(hand), options).keys())[1]


df["Outcome"] = df[["Predict", "Elf1"]].apply(lambda x: predict(x.Predict, x.Elf1), axis=1)
df["Game2"] = df["Elf1"] + df["Outcome"]
df["Result2"] = df["Game2"].map(rules)
df["Score2"] = df["Result2"].map(game)
df["Extra2"] = df["Outcome"].map(hand2)
df["Total2"] = df["Score2"] + df["Extra2"]

# P2
df.Total2.sum()