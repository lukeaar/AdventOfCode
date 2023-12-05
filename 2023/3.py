# 2023 Day 3

from aocd import data
from aocd import submit

def parta():
    answer = 0

    schematic = data.splitlines()
    rows = len(schematic)
    columns = len(schematic[0])
    
    for i in range(rows):
        n = ""
        partFlag = 0
        for j in range(columns):
            char = schematic[i][j]
            isDigit = char.isdigit()
            if isDigit:
                n += char
                for x in range(i-1,i+2):
                    for y in range(j-1,j+2):
                        if x >= 0 and x < rows and y >= 0 and y < columns:
                            test = schematic[x][y]
                            if not test.isdigit() and test != '.':
                                partFlag = 1
            if j == columns-1 or not isDigit and n != "":
                if partFlag:
                    answer += int(n)
                partFlag = 0
                n = ""

    return answer

def partb():
    answer = 0
    
    schematic = data.splitlines()
    rows = len(schematic)
    columns = len(schematic[0])
    
    for i in range(rows):
        for j in range(columns):
            if schematic[i][j] == '*':
                n1, n2 = 0, 0
                overgear = 0
                for x in range(i-1,i+2):
                    for y in range(j-1,j+2):
                        num = schematic[x][y]
                        if (x >= 0 and x < rows and y >= 0 and y < columns 
                                and num.isdigit()):
                            z = y - 1
                            while z >= 0 and schematic[x][z].isdigit():
                                num = schematic[x][z] + num
                                z -= 1
                            z = y + 1
                            while z < columns and schematic[x][z].isdigit():
                                num = num + schematic[x][z]
                                z += 1
                            num = int(num)
                            if n1 == 0:
                                n1 = num
                            elif n1 != num and n2 == 0:
                                n2 = num
                            elif n1 != num and n2 != num:
                                overgear = 1
                if not overgear:
                    answer += n1 * n2
                    
    return answer

submit(parta(), part="a")
submit(partb(), part="b")
