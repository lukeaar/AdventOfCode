# 2023 Day 10

import aoc_tools as aoc
from aocd import data
from aocd import submit

data_split = data.splitlines()
pipes = aoc.forge_grid(data_split,str)
xlen = len(data_split[0])
ylen = len(data_split)

def part_a():
    x, y = list(pipes.keys())[list(pipes.values()).index("S")]
    last = [(x,y),(x,y)]
    current = []
    if y > 0 and pipes[x,y-1] in ["|","7","F"]:
        current.append((x,y-1))
        pipes[x,y] = "^"
    if x > 0 and pipes[x-1,y] in ["-","L","F"]:
        current.append((x-1,y))
    if x < xlen - 1 and pipes[x+1,y] in ["-","J","7"]:
        current.append((x+1,y))
    if y < ylen - 1 and pipes[x,y+1] in ["|","L","J"]:
        current.append((x,y+1))
        
    step = 1
    while(step):
        step += 1
        for i in range(2):
            x = current[i][0]
            y = current[i][1]
            match pipes[current[i]]:
                case "|":
                    y += y - last[i][1]
                    pipes[current[i]] = "^"
                case "-":
                    x += x - last[i][0]
                    pipes[current[i]] = "S"
                case "L":
                    if x - last[i][0]: y -= 1
                    else: x += 1
                    pipes[current[i]] = "^"
                case "J":
                    if x - last[i][0]: y -= 1
                    else: x -= 1
                    pipes[current[i]] = "^"
                case "7":
                    if x - last[i][0]: y += 1
                    else: x -= 1
                    pipes[current[i]] = "S"
                case "F":
                    if x - last[i][0]: y += 1
                    else: x += 1
                    pipes[current[i]] = "S"
            last[i] = current[i]
            current[i] = (x,y)
        if current[0] == current[1]: return step

def part_b():
    for y in range(ylen):
        vert_count = 0
        for x in range(xlen):
            match pipes[x,y]:
                case "^": vert_count += 1
                case "S": continue
                case _: pipes[x,y] = str(vert_count%2)
    return list(pipes.values()).count("1")

submit(part_a(), part="a")
submit(part_b(), part="b")