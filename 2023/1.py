# 2023 Day 1

from aocd import data
from aocd import submit

import re

def parta():
    answer = 0

    for line in data.splitlines():
        digits = re.sub(r'\D', '', line)
        value = digits[0] + digits[-1]
        answer += int(value)
    
    return answer

def partb():
    answer = 0

    for line in data.splitlines():
        fLine = re.sub(r'(one)','o1e', line)
        fLine = re.sub(r'(two)', 't2o', fLine)
        fLine = re.sub(r'(three)','t3e', fLine)
        fLine = re.sub(r'(four)', 'f4r', fLine)
        fLine = re.sub(r'(five)', 'f5e', fLine)
        fLine = re.sub(r'(six)', 's6x', fLine)
        fLine = re.sub(r'(seven)', 's7n', fLine)
        fLine = re.sub(r'(eight)', 'e8t', fLine)
        fLine = re.sub(r'(nine)', 'n9e', fLine)
        #fLine = re.sub(r'(zero)', '0', fLine)
        digits = re.sub(r'\D', '', fLine)
        value = digits[0] + digits[-1]
        answer += int(value)
    
    return answer

submit(parta(), part="a")
submit(partb(), part="b")