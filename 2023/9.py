# 2023 Day 9

from aocd import data
from aocd import submit

def extrapolate(sequence: list) -> int:
    differences = [(int(sequence[i]) - int(sequence[i-1]))
                   for i in range(1,len(sequence))]
    if any(differences): return int(sequence[-1]) + extrapolate(differences)
    return int(sequence[-1])
        
def part_a():
    return sum([extrapolate(line.split()) for line in data.splitlines()])

def part_b():
    return sum([extrapolate(list(reversed(line.split())))
                for line in data.splitlines()])

submit(part_a(), part="a")
submit(part_b(), part="b")