# 2023 Day 7

from functools import cmp_to_key

from aocd import data
from aocd import submit

def typeScoreA(hand: str):
    counts = sorted([hand.count(c) for c in hand], reverse=True)
    match max(counts):
        case 5: return 0
        case 4: return 1
        case 3: return 3 - (counts[3] - 1)
        case 2: return 5 - (counts[2] - 1)
        case _: return 6
        
def compareHandsA(a,b):
    cardList = "AKQJT98765432"
    typeScoreDif = typeScoreA(a[:5]) - typeScoreA(b[:5])
    if typeScoreDif: return typeScoreDif
    cardScoreDif = 0
    for i in range(5):
        cardScoreDif = cardList.index(a[i]) - cardList.index(b[i])
        if cardScoreDif: break
    return cardScoreDif

def typeScoreB(hand: str):
    counts = sorted([hand.count(c) for c in hand], reverse=True)
    jokers = hand.count('J')
    match jokers:
        case 5 | 4: return 0
        case 3: return 1 - (counts[3] - 1)
        case 2:
            match max(counts):
                case 3: return 0
                case 2: return 3 - 2*(counts[1] - 1)
        case 1:
            match max(counts):
                case 4: return 0
                case 3: return 1
                case 2: return 3 - (counts[2] - 1)
                case 1: return 5
    match max(counts):
        case 5: return 0
        case 4: return 1
        case 3: return 3 - (counts[3] - 1)
        case 2: return 5 - (counts[2] - 1)
        case _: return 6

def compareHandsB(a,b):
    cardList = "AKQT98765432J"
    typeScoreDif = typeScoreB(a[:5]) - typeScoreB(b[:5])
    if typeScoreDif: return typeScoreDif
    cardScoreDif = 0
    for i in range(5):
        cardScoreDif = cardList.index(a[i]) - cardList.index(b[i])
        if cardScoreDif: break
    return cardScoreDif

def parta():
    answer = 0
    
    hands = sorted(data.splitlines(), key=cmp_to_key(compareHandsA))
    handNumber = len(hands)
    for i in range(handNumber):
        answer += int(hands[i][6:])*(handNumber-i)

    return answer

def partb():
    answer = 0
    
    hands = sorted(data.splitlines(), key=cmp_to_key(compareHandsB))
    handNumber = len(hands)
    for i in range(handNumber):
        answer += int(hands[i][6:])*(handNumber-i)
    
    return answer

submit(parta(), part="a")
submit(partb(), part="b")