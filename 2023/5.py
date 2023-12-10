# 2023 Day 5

from sys import maxsize
import aoc_tools as aoc
from aocd import data
from aocd import submit

def parta():
    answer = maxsize
    
    almanac = data.split("\n\n")
    for seed in aoc.retype_sl(almanac.pop(0)[7:].split()):
        num = int(seed)
        for map in almanac:
            map = map.splitlines()
            map.pop(0)
            for line in map:
                line = line.split()
                dst = int(line[0])
                src = int(line[1])
                if num >= src and num < src + int(line[2]):
                    num = dst + (num - src)
                    break
        answer = min(answer,num)
    
    return answer

def partb():
    almanac = data.split("\n\n")
    ranges = aoc.retype_sl(almanac.pop(0)[7:].split())
    untransformed = []
    for i in range(0,len(ranges),2):
        untransformed.append((ranges[i], ranges[i]+ranges[i+1]-1))
    
    for map in almanac:
        map = map.splitlines()
        map.pop(0)
        transformed = []
        for line in map:
            d_start, s_start, size = [int(i) for i in line.split()]
            s_end = s_start + size - 1
            transformation = d_start - s_start
            for i, i_tuple in enumerate(untransformed):
                i_start, i_end = i_tuple
                if i_end < s_start or i_start > s_end:
                    continue
                elif i_start < s_start and i_end <= s_end:
                    untransformed.pop(i)
                    untransformed.append((i_start,s_start-1))
                    transformed.append((s_start+transformation,
                                        i_end+transformation))
                elif i_start <= s_end and i_end > s_end:
                    untransformed.pop(i)
                    untransformed.append((s_end+1,i_end))
                    transformed.append((i_start+transformation,
                                        s_end+transformation))
                elif i_start >= s_start and i_end <= s_end:
                    untransformed.pop(i)
                    transformed.append((i_start+transformation,
                                        i_end+transformation))
                elif i_start < s_start and i_end > s_end:
                    untransformed.pop(i)
                    untransformed.append((i_start,s_start-1))
                    untransformed.append((s_end+1,i_end))
                    transformed.append((s_start+transformation,
                                        s_end+transformation))
        untransformed += transformed
    return min(untransformed)[0]

submit(parta(), part="a")
submit(partb(), part="b")