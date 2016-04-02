import random


def shuffleCards():
    cardList = [n for n in range(1, 11)]
    random.shuffle(cardList)
    return cardList


def simulateDesicion(currentNumber):
    global maxNum
    return currentNumber <= maxNum // 2


def playTurn(lst):
    playList = lst[:]
    while len(playList) > 1:
        if simulateDesicion(playList[0]):
            if playList[1] > playList[0]:
                print("Correct: {} is higher than {}".format(playList[1], playList[0]))
            else:
                print("Wrong: {} is not higher than {}".format(playList[1], playList[0]))
        else:
            if playList[1] < playList[0]:
                print("Correct: {} is lower than {}".format(playList[1], playList[0]))
            else:
                print("Wrong: {} is not lower than {}".format(playList[1], playList[0]))
        playList.remove(playList[0])

maxNum = 10
guessed = []
cards = shuffleCards()
playTurn(cards)
print(cards)
