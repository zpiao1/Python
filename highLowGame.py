import random


def shuffleCards():
    cardList = []
    numOfCards = random.randint(1, 10)
    i = 1
    while i <= numOfCards:
        card = random.randint(1, 10)
        if card not in cardList:
            cardList.append(card)
            i += 1
    return cardList


def simulateDesicion(currentNumber):
    if currentNumber <= 5:
        return True
    else:
        return False


def playTurn(lst):
    playList = lst[:]
    while len(playList) > 1:
        if simulateDesicion(playList[0]):
            if playList[1] >= playList[0]:
                print("Correct: {} is higher than {}".format(playList[1], playList[0]))
            elif playList[1] <= playList[0]:
                print("Wrong: {} is not higher than {}".format(playList[1], playList[0]))
        else:
            if playList[1] <= playList[0]:
                print("Correct: {} is lower than {}".format(playList[1], playList[0]))
            elif playList[1] >= playList[0]:
                print("Wrong: {} is not lower than {}".format(playList[1], playList[0]))
        playList.remove(playList[0])


cardList = shuffleCards()
playTurn(cardList)
print(cardList)
