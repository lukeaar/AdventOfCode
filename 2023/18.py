# 2023 Day 18

import aoc_tools as aoc
from aocd import data, submit

def part_a():
    area = 0
    vertices = [(0,0)]
    perimeter = 0
    dirs = {
            'R' : (1,0),
            'D' : (0,1),
            'L' : (-1,0),
            'U' : (0,-1)
        }
    for line in data.splitlines():
        d, n, _ = line.split()
        n = int(n)
        perimeter += n
        vertices.append((vertices[-1][0] + (dirs[d][0]*n),
                         vertices[-1][1] + (dirs[d][1]*n)))
    for i in range(len(vertices)-1):
        area += (vertices[i][0]*vertices[i+1][1] -
                    vertices[i+1][0]*vertices[i][1])
    area = abs(area) / 2 - perimeter / 2 + 1
    
    return area + perimeter

def part_b():
    area = 0
    vertices = [(0,0)]
    perimeter = 0
    dirs = {
            '0' : (1,0),
            '1' : (0,1),
            '2' : (-1,0),
            '3' : (0,-1)
        }
    for line in data.splitlines():
        _, _, h = line.split()
        h = h[2:-1]
        d = h[-1:]
        n = int(h[:-1],16)
        perimeter += n
        vertices.append((vertices[-1][0] + (dirs[d][0]*n),
                         vertices[-1][1] + (dirs[d][1]*n)))
    for i in range(len(vertices)-1):
        area += (vertices[i][0]*vertices[i+1][1] -
                    vertices[i+1][0]*vertices[i][1])
    area = abs(area) / 2 - perimeter / 2 + 1
    
    return area + perimeter

submit(part_a(), part="a")
submit(part_b(), part="b")