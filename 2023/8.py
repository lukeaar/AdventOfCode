# 2023 Day 8

import numpy as np
from aocd import data
from aocd import submit

def part_a():
    directions, network = data.split("\n\n")
    network_dict = {l[:3] : (l[7:10],l[12:15]) for l in network.splitlines()}
    current = "AAA"
    step = 1
    while step:
        if directions[(step-1)%len(directions)] == 'L':
            current = network_dict[current][0]
        else:
            current = network_dict[current][1]
        if current == "ZZZ": return step
        step += 1
        
def part_b():
    directions, network = data.split("\n\n")
    network_dict = {l[:3] : (l[7:10],l[12:15]) for l in network.splitlines()}
    step = 1
    nodes = [[n,-1,0] for n in network_dict.keys() if n.endswith('A')]
    while step:
        for i, n in enumerate(nodes):
            if directions[(step-1)%len(directions)] == 'L':
                nodes[i][0] = network_dict[n[0]][0]
            else:
                nodes[i][0] = network_dict[n[0]][1]
            if nodes[i][0].endswith('Z'):
                match n[1]:
                    case -1:
                        nodes[i][1] = 0
                        nodes[i][2] = step
                    case 0:
                        nodes[i][1] = 1
                        nodes[i][2] = step - nodes[i][2]
        all_looped = True
        i = 0
        while all_looped and i < len(nodes):
            all_looped = nodes[i][1] == 1
            i += 1
        if all_looped:
            loop_lengths = [n[2] for n in nodes]
            return np.lcm.reduce(loop_lengths)
        step += 1

submit(part_a(), part="a")
submit(part_b(), part="b")