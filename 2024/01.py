# 2024 Day 1

import aoc_tools as aoc
from aocd import get_data, submit

data = get_data(day=1, year=2024).splitlines()

def part_a():
    lista, listb = [], []
    for line in data:
        [a,b] = aoc.find_il(line)
        lista.append(a)
        listb.append(b)
    lista.sort()
    listb.sort()
    return sum(abs(lista[i] - listb[i]) for i in range(0,len(lista)))

def part_b():
    lista, listb = [], []
    for line in data:
        [a,b] = aoc.find_il(line)
        lista.append(a)
        listb.append(b)
    return sum(num * listb.count(num) for num in lista)

#submit(part_a(), part="a", day=1, year=2024)
submit(part_b(), part="b", day=1, year=2024)
