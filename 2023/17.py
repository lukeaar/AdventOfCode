# 2023 Day 17

import aoc_tools as aoc
from aocd import data, submit
from collections import defaultdict
import heapq

def dijkstra(grid, min, max):
    heat_loss = defaultdict(lambda :float('inf'))
    previous = defaultdict(lambda :None)
    unvisited = [(0,(0,0),(1,0),0)]
    heapq.heapify(unvisited)
        
    heat_loss[((0,0),(1,0),0)] = 0
    target = (grid.row_len()-1,grid.column_len()-1)
    
    while len(unvisited):
        current = heapq.heappop(unvisited)[1:]
        if current[0] == target: return heat_loss[current]
        for dir in [(-1,0),(1,0),(0,-1),(0,1)]:
            if ((dir != current[1] and current[2] < min)
                    or ((-dir[0],-dir[1]) == current[1])):
                continue
            new_coord = (current[0][0] + dir[0], current[0][1] + dir[1])
            new_len = current[2]+1 if current[1] == dir else 1
            if (new_coord[0] < 0 or new_coord[1] < 0
                    or new_coord[0] >= grid.row_len()
                    or new_coord[1] >= grid.column_len()
                    or (new_len > max)):
                continue
            new_heat = heat_loss[current] + grid[new_coord]
            if new_heat < heat_loss[new_coord,dir,new_len]:
                heat_loss[new_coord,dir,new_len] = new_heat
                previous[new_coord,dir,new_len] = current
                heapq.heappush(unvisited,(new_heat,new_coord,dir,new_len))
    
def part_a():
    return(dijkstra(aoc.Grid(data.splitlines()),0,3))
    
def part_b():
    return(dijkstra(aoc.Grid(data.splitlines()),4,10))

submit(part_a(), part="a")
submit(part_b(), part="b")