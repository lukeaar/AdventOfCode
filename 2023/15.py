# 2023 Day 15

from aocd import data
from aocd import submit
from collections import defaultdict

def hash_algorithm(input:str) -> int:
    value = 0
    for char in input: value = ((value + ord(char)) * 17) % 256
    return value

def part_a():
    answer = 0
    sequence = data.replace('\n','').split(',')
    for step in sequence: answer += hash_algorithm(step)
    return answer

def return_empty():
    return []

def part_b():
    answer = 0
    
    boxes = defaultdict(return_empty)
    lenses = {}
    sequence = data.replace('\n','').split(',')
    for step in sequence:
        if step[-1] == '-':
            label = step[:-1]
            hash_value = hash_algorithm(label)
            if label in boxes[hash_value]:
                boxes[hash_value].remove(label)
        else:
            label, focal_length = step.split('=')
            lenses[label] = int(focal_length)
            hash_value = hash_algorithm(label)
            if label not in boxes[hash_value]:
                boxes[hash_value] += [label]
    for i in range (256):
        for j, lens in enumerate(boxes[i]):
            answer += (1 + i) * (1 + j) * lenses[lens]
    
    return answer

submit(part_a(), part="a")
submit(part_b(), part="b")