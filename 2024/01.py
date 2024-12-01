# 2024 Day 1

import aoc_tools as aoc
from aocd import get_data, submit

data = get_data(day=1, year=2024).splitlines()

def part_a():
    lista = []
    listb = []
    for line in data:
        [a,b] = aoc.find_il(line)
        lista.append(a)
        listb.append(b)
    lista.sort()
    listb.sort()
    answer = 0
    for i in range(0,len(lista)): answer += abs(lista[i] - listb[i])
    return answer

def part_b():
    lista = []
    listb = []
    for line in data:
        [a,b] = aoc.find_il(line)
        lista.append(a)
        listb.append(b)
    answer = 0
    for num in lista: answer += num * listb.count(num)
    return answer

#submit(part_a(), part="a", day=1, year=2024)
submit(part_b(), part="b", day=1, year=2024)