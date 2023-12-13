# 2023 Day 13

from aocd import data
from aocd import submit

def part_a():
    answer = 0
    
    patterns = [pattern.splitlines() for pattern in data.split("\n\n")]
    for pattern in patterns:
        reflection = True
        for i in range(1,len(pattern)):
            r = i
            for l in range(i-1,-1,-1):
                if pattern[l] != pattern[r]:
                    reflection = False
                    break
                r += 1
                if r == len(pattern) or not reflection: break
            if reflection:
                answer += 100 * i
                break
            reflection = True
        reflection = True
        for i in range(1,len(pattern[0])):
            r = i
            for l in range(i-1,-1,-1):
                if ([pattern[j][l] for j in range(len(pattern))] != 
                        [pattern[j][r] for j in range(len(pattern))]):
                    reflection = False
                    break
                r += 1
                if r == len(pattern[0]) or not reflection: break
            if reflection:
                answer += i
                break
            reflection = True
    
    return answer

def part_b():
    answer = 0
    
    patterns = [pattern.splitlines() for pattern in data.split("\n\n")]
    for pattern in patterns:
        count = 0
        for i in range(1,len(pattern)):
            r = i
            for l in range(i-1,-1,-1):
                for n in range(len(pattern[l])):
                    if pattern[l][n] != pattern[r][n]: count += 1
                    if count > 1: break
                r +=1
                if r == len(pattern) or count >1: break
            if count == 1:
                answer += 100 * i
                break
            count = 0
        count = 0
        for i in range(1,len(pattern[0])):
            r = i
            for l in range(i-1,-1,-1):
                for n in range(len(pattern)):
                    if pattern[n][l] != pattern[n][r]: count +=1
                    if count > 1: break
                r += 1
                if r == len(pattern[0]) or count > 1: break
            if count == 1:
                answer += i
                break
            count = 0
    
    return answer

submit(part_a(), part="a")
submit(part_b(), part="b")