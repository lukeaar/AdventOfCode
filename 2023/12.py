# 2023 Day 12

import aoc_tools as aoc
from aocd import data
from aocd import submit
from functools import cache

@cache
def num_possible_arrangements(input:str, damaged_group_sizes:tuple) -> int:
    if len(damaged_group_sizes) == 0: return 1 if "#" not in input else 0

    group_size = damaged_group_sizes[0]
    count = 0
    for i in range(len(input)):
        if (
            i + group_size <= len(input) and
            all(spring != '.' for spring in input[i:i+group_size]) and
            (i == 0 or input[i-1] != '#') and
            (i + group_size == len(input) or input[i + group_size] != '#')
        ):
            count += num_possible_arrangements(input[i+group_size+1:],
                                               tuple(damaged_group_sizes[1:]))
        if input[i] == '#': break
        
    return count
    
def part_a():
    answer = 0
    
    for row in data.splitlines():
        spring_conditions, damaged_group_sizes = row.split()
        answer += num_possible_arrangements(spring_conditions,
            tuple(aoc.retype_sl(damaged_group_sizes.split(','))))
    
    return answer

def part_b():
    answer = 0
    
    for row in data.splitlines():
        spring_conditions, damaged_group_sizes = row.split()
        spring_conditions = ((spring_conditions + '?')*5)[:-1]
        answer += num_possible_arrangements(spring_conditions,
            tuple(aoc.retype_sl(damaged_group_sizes.split(','))*5))
    
    return answer

submit(part_a(), part="a")
submit(part_b(), part="b")