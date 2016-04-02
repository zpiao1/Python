__author__ = 'zpiao1'


def wordSorting(wordIn):
    wordOut = ''.join(sorted(list(wordIn)))
    return wordOut


# make a list containing words whose anagrams are to be search for
wordList = ['serve', 'rival', 'lovely', 'caveat', 'devote', 'irving', 'livery', \
            'serves', 'latvian', 'saviour', 'observe', 'octavian', 'dovetail', 'levantine']
# create the string which contains all letters of the word
anagramDict = {}
for word in wordList:
    sortedWord2Search = wordSorting(word)
    anagramDict[sortedWord2Search] = [word]

# print(anagramDict) # for testing
# create the dictionary with the key being the sortedWord
# and the value is a list containing all the anagrams
# print(anagramDict) # for testing
with open('word_list.txt', 'r') as myFile:
    for word in myFile:
        sortedWord = wordSorting(word.strip().lower())
        if sortedWord in anagramDict.keys() and (word[0] == 'v' or word[0] == 'V'):
            # print(word) # for testing
            anagramDict[sortedWord].append(word.strip())
# print(anagramDict) # for testing
for wordKey in anagramDict.keys():
    print("The anagram of {} is\\are: ".format(anagramDict[wordKey][0]), end='')
    for word in anagramDict[wordKey][1:]:
        print(word, end=' ')
    print()