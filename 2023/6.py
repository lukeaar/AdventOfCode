# 2023 Day 6

from aocd import data
from aocd import submit

def parta():
    answer = 1
    
    times, records = [ list(map(int,line[9:].split())) 
                        for line in data.splitlines() ]
    for i in range(len(times)):
        num = 0
        for j in range(1,times[-1]):
            if (times[i]-j)*j > records[i]: num += 1
        answer *= num
        
    return answer

def partb():
    answer = 0
    
    time, record = [ int(line[9:].replace(' ',''))
                      for line in data.splitlines() ]
    for i in range(1,time):
        if (time-i)*i > record: answer+=1
    
    return answer

submit(parta(), part="a")
submit(partb(), part="b")