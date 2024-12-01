import numpy as np
from pathlib import Path
from typing import List, Tuple
from collections import Counter

# Load Data
raw = (Path(__file__).parent / "input.txt").read_text().split("\n")

def split(row: str) -> Tuple[int, int]:
    """Splits a row of two numbers into a tuple of ints."""
    return tuple(map(int, row.split()))

def order(pairs: List[Tuple[int, int]]) -> Tuple[np.ndarray, np.ndarray]:
    """Order pairs of tuples in sorted numpy arrays."""
    # Use numpy array operations for efficient sorting
    pairs_array = np.array(pairs)
    return np.sort(pairs_array[:, 0]), np.sort(pairs_array[:, 1])

def similarity(left: np.ndarray, right: np.ndarray) -> int:
    """Search for instances of numbers on left in right and compute score."""
    # Use numpy's efficient indexing and counting
    right_counts = Counter(right)
    return sum(val * right_counts.get(val, 0) for val in left)

# Convert raw input to pairs
pairs = [split(row) for row in raw if row.strip()]

# Ordered Lists
a, b = order(pairs)

# Part 1: Absolute difference sum
print(np.abs(a - b).sum())

# Part 2: Similarity score
print(similarity(a, b))
