# 2023 Day 11

from aocd import data
from aocd import submit

grid = [[c for c in l] for l in data.splitlines()]

def expand(galaxies: list, factor=1) -> list:
    expansions = 0
    for y, row in enumerate(grid):
        if not '#' in row:
            for i, galaxy in enumerate(galaxies):
                if galaxy[1] > y + expansions * factor:
                    galaxies[i] = [galaxy[0], galaxy[1] + factor]
            expansions += 1
    expansions = 0
    for x, column in enumerate(
            [[r[i] for r in grid] for i in range(len(grid[0]))]):
        if not '#' in column:
            for i, galaxy in enumerate(galaxies):
                if galaxy[0] > x + expansions * factor:
                    galaxies[i] = [galaxy[0] + factor, galaxy[1]]
            expansions += 1
    return galaxies
    
def part_a():
    answer = 0
    
    galaxies = []
    for y, row in enumerate(grid):
        for x, element in enumerate(row):
            if element == '#': galaxies.append([x,y])
    for i, start in enumerate(expand(galaxies)):
        for end in galaxies[i+1:]:
            answer += abs(end[0] - start[0]) + abs(end[1] - start[1])
          
    return answer

def part_b():
    answer = 0
    
    galaxies = []
    for y, row in enumerate(grid):
        for x, element in enumerate(row):
            if element == '#': galaxies.append([x,y])        
    for i, start in enumerate(expand(galaxies, 999999)):
        for end in galaxies[i+1:]:
            answer += abs(end[0] - start[0]) + abs(end[1] - start[1])
    
    return answer

submit(part_a(), part="a")
submit(part_b(), part="b")