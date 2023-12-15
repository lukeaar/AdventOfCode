# 2023 Day 14

import aoc_tools as aoc
from aocd import data
from aocd import submit

def part_a():
    platform = aoc.Grid(data.splitlines(),str)
    answer = 0
    for column in platform.columns():
        stop_pos = 0
        for i, space in enumerate(column):
            if space == 'O':
                answer += len(column) - stop_pos
                stop_pos += 1
            elif space == '#':
                stop_pos = i + 1
    return answer

def spin(platform:aoc.Grid):
    for x, column in enumerate(platform.columns()):
        stop_pos = 0
        for y, space in enumerate(column):
            if space == 'O':
                platform.set(x,y,'.')
                platform.set(x,stop_pos,'O')
                stop_pos += 1
            elif space == '#':
                stop_pos = y + 1
    for y, row in enumerate(platform.rows()):
        stop_pos = 0
        for x, space in enumerate(row):
            if space == 'O':
                platform.set(x,y,'.')
                platform.set(stop_pos,y,'O')
                stop_pos += 1
            elif space == '#':
                stop_pos = x + 1
    for x, column in enumerate(platform.columns()):
        stop_pos = len(column) - 1
        for y, space in reversed(list(enumerate(column))):
            if space == 'O':
                platform.set(x,y,'.')
                platform.set(x,stop_pos,'O')
                stop_pos -= 1
            elif space == '#':
                stop_pos = y - 1
    for y, row in enumerate(platform.rows()):
        stop_pos = len(row) - 1
        for x, space in reversed(list(enumerate(row))):
            if space == 'O':
                platform.set(x,y,'.')
                platform.set(stop_pos,y,'O')
                stop_pos -= 1
            elif space == '#':
                stop_pos = x - 1
    return platform

def part_b():
    answer = 0
    
    platform = aoc.Grid(data.splitlines(),str)
    states = []
    states.append(hash(platform))
    loop_found = False
    i = 0
    while i < 1000000000:
        platform = spin(platform)
        plat_hash = hash(platform)
        i += 1
        if not loop_found and plat_hash in states:
            loop_found = True
            loop_length = i - states.index(plat_hash)
            i += loop_length * ((1000000000 - i) // loop_length)
        states.append(plat_hash)

    for column in platform.columns():
        for i, space in enumerate(column):
            if space == 'O': answer += len(column) - i

    return answer

submit(part_a(), part="a")
submit(part_b(), part="b")