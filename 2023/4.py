# 2023 Day 4

from aocd import data
from aocd import submit

def parta():
    answer = 0
    
    for card in data.splitlines():
        card = card.split(": ")[1]
        card = card.split(" | ")
        winningNumbers = card[0].split(' ')
        cardNumbers = card[1].split(' ')
        score = 0
        for number in cardNumbers:
            if number.isdigit() and number in winningNumbers:
                if score == 0:
                    score = 1
                else:
                    score = score * 2
        answer += score
    
    return answer

def partb():
    cards = data.splitlines()
    answer = len(cards)
    
    copyTable = [0] * len(cards)
    cardNumber = 0
    for card in cards:
        card = card.split(": ")[1]
        card = card.split(" | ")
        winningNumbers = card[0].split(' ')
        cardNumbers = card[1].split(' ')
        score = 0
        for number in cardNumbers:
            if number.isdigit() and number in winningNumbers:
                score += 1
        while score > 0:
            i = cardNumber + score
            if i < len(cards):
                copyTable[i] = copyTable[i] + 1 * (copyTable[cardNumber]+1)
            score -= 1
        cardNumber += 1
            
    answer = answer + sum(copyTable)
    
    return answer

submit(parta(), part="a")
submit(partb(), part="b")