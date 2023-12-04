# 2023 Day 2

from aocd import data
from aocd import submit

def parta():
    answer = 0
    
    for game in data.splitlines():
        possible = 1
        game = game.split(": ")
        id = int(game[0].split(' ')[1])
        for set in game[1].split("; "):
            for reveal in set.split(", "):
                num = int(reveal.split(' ')[0])
                match reveal[1]:
                    case "red":
                        possible = num <= 12
                    case "green":
                        possible = num <= 13
                    case "blue":
                        possible = num <= 14
        if possible:
            answer += id
            
    return answer

def partb():
    answer = 0
    
    for game in data.splitlines():
        minBlue, minRed, minGreen = 0, 0, 0
        game = game.split(": ")[1].split("; ")
        for set in game:
            for reveal in set.split(", "):
                num = int(reveal.split(' ')[0])
                match reveal[1]:
                    case "red":
                        minRed = max(minRed, num)
                    case "green":
                        minGreen = max(minGreen, num)
                    case "blue":
                        minBlue = max(minBlue, num)
        answer += minBlue * minRed * minGreen
        
    return answer

submit(parta(), part="a")
submit(partb(), part="b")
