# 2023 Day 16

import aoc_tools as aoc
from aocd import data
from aocd import submit
from sys import setrecursionlimit

setrecursionlimit(1000000000)

energised = {}

def trace_light(x, y, x_increment, y_increment, grid):
    if x < 0 or x >= len(grid.rows()[0]) or y < 0 or y >= len(grid.rows()):
        return 0
    if (x,y,x_increment,y_increment) in energised.keys():
        return 0
    energised[(x,y,x_increment,y_increment)] = 1
    match grid.get(x,y):
        case '.':
            pass
        case '/':
            new_x_increment = 0 - y_increment
            new_y_increment = 0 - x_increment
            x_increment = new_x_increment
            y_increment = new_y_increment
        case '\\':
            new_x_increment = y_increment
            new_y_increment = x_increment
            x_increment = new_x_increment
            y_increment = new_y_increment
        case '|':
            if y_increment:
                pass
            else:
                trace_light(x,y-1,0,-1,grid)
                trace_light(x,y+1,0,1,grid)
                return 0
        case '-':
            if x_increment:
                pass
            else:
                trace_light(x-1,y,-1,0,grid)
                trace_light(x+1,y,1,0,grid)
                return 0
    x += x_increment
    y += y_increment
    trace_light(x,y,x_increment,y_increment,grid)
    return 0

def score():
    energised_clean = {}
    for value in energised.keys():
        energised_clean[(value[0],value[1])] = 1
    return sum(energised_clean.values())

def part_a():
    trace_light(0,0,1,0,aoc.Grid(data.splitlines(),str))
    return score()

def part_b():
    answer = 0
    grid = aoc.Grid(data.splitlines(),str)
    for x in range(len(grid.rows()[0])):
        energised.clear()
        trace_light(x,0,0,1,grid)
        answer = max(answer,score())
        energised.clear()
        trace_light(x,len(grid.rows())-1,0,-1,grid)
        answer = max(answer,score())
    for y in range(len(grid.rows())):
        energised.clear()
        trace_light(0,y,1,0,grid)
        answer = max(answer,score())
        energised.clear()
        trace_light(len(grid.rows()[0])-1,y,-1,0,grid)
        answer = max(answer,score())
    return answer

submit(part_a(), part="a")
submit(part_b(), part="b")