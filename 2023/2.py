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
                reveal = reveal.split(' ')
                num = int(reveal[0])
                match reveal[1]:
                    case "red":
                        if num > 12:
                            possible = 0
                    case "green":
                        if num > 13:
                            possible = 0
                    case "blue":
                        if num >14:
                            possible = 0
                    case _:
                        next
        if possible == 1:
            answer += id
    return answer

def partb():
    answer = 0
    for game in data.splitlines():
        minBlue = 0
        minRed = 0
        minGreen = 0
        game = game.split(": ")
        for set in game[1].split("; "):
            for reveal in set.split(", "):
                reveal = reveal.split(' ')
                num = int(reveal[0])
                match reveal[1]:
                    case "red":
                        if num > minRed:
                            minRed = num
                    case "green":
                        if num > minGreen:
                            minGreen = num
                    case "blue":
                        if num > minBlue:
                            minBlue = num
                    case _:
                        next 
        answer += minBlue * minRed * minGreen
    return answer

submit(parta(), part="a")
submit(partb(), part="b")