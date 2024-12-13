# %%
import numpy as np
from pathlib import Path
from toolz import groupby, valmap, compose
from operator import not_
from collections import defaultdict, deque

# %%
raw = Path("input.txt").read_text().split("\n")

# %%
rules = list(filter(lambda x: "|" in x, raw))
order = list(filter(lambda x: "," in x, raw))
edges = list(map(lambda x: tuple(map(int, x.split("|"))), rules))

# %%
pages = groupby(lambda x: x[0], [tuple(map(int, x.split("|"))) for x in rules])
valid = valmap(lambda y: list(map(lambda x: x[1], y)), pages)

# %%
page_order = list(map(lambda x: list(map(int, x.split(","))), order))

# %%
def check_page(arr):
    for page in range(len(t:=arr)):
        s = valid.get(t[page], [])
        # Checks if the remaining pages should be printed before current page
        # if there is at least one page that should be printed before => False
        x = set(t[page+1:]).difference(s)
        if len(x) > 0:
            yield False
        else:
            yield True

# %%
is_good = compose(all, check_page)

# %%
are_valid = list(map(is_good, page_order))

# %%
entries = [b for a,b in zip(are_valid, page_order) if a]

# %%
# 5248
sum([b[a] for a,b in zip(list(map(lambda x: len(x) // 2, entries)), entries)])

# %%
are_invalid = list(map(not_, are_valid))

# %%
entries_invalid = [b for a,b in zip(are_invalid, page_order) if a]

# %%


def sort_with_rules(numbers, rules):
    # Build a graph and in-degree dictionary
    graph = defaultdict(list)
    in_degree = {num: 0 for num in numbers}

    # Parse the rules and update the graph and in-degrees
    for before,after in edges:
        if after in numbers and before in numbers:  # Only consider numbers in the list
            graph[before].append(after)
            in_degree[after] += 1

    # Perform a topological sort using Kahn's algorithm
    queue = deque([num for num in numbers if in_degree[num] == 0])
    sorted_list = []

    while queue:
        current = queue.popleft()
        sorted_list.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if sorting is valid (no cycles)
    if len(sorted_list) != len(numbers):
        raise ValueError("The rules contain a cycle and cannot be resolved.")

    return sorted_list

# Example usage
#numbers = [30, 20, 10]
#rules = ["10|20", "20|30"]
fixed = []
for e in entries_invalid:
    fixed.append(sort_with_rules(e, rules))


# %%
sum([b[a] for a,b in zip(list(map(lambda x: len(x) // 2, fixed)), fixed)])

# %%
# 4568 KO => +
# 4507 OK

# %%



