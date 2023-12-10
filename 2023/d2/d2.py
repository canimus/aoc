import numpy as np
from pathlib import Path
import re
from dataclasses import dataclass
from toolz import first, valmap, compose
from typing import List
from operator import attrgetter as at


raw = Path("input.txt").read_text().split("\n")

@dataclass
class Draw():
    red: int = 0
    green: int = 0
    blue: int = 0

    def vector(self):
        return np.array([self.red, self.green, self.blue])

@dataclass
class Game():
    id: int
    draws: List[Draw]


constraint = np.array([12, 13, 14])

_draw = lambda x: Draw(**valmap(int, dict(map(reversed, re.findall(r"(\d+)\s(red|green|blue){1},?", x)))))
_valid = lambda y: np.all(list(map(lambda x: np.all(x.vector() <= constraint), y)))
_ok = compose(_valid, at("draws"))

games = []
for row in raw:
    game, splits = list(map(str.strip, row.split(":")))
    id = int(first(re.findall(r"Game\s(\d+)", game)))
    draws = list(map(str.strip, splits.split(";")))
    games.append(Game(id, list(map(_draw, draws))))    


result = sum(map(at("id"), list(filter(_ok, games))))
print(result)