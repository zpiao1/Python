__author__ = 'zpiao1'
words = puncts = 0
with open('text.txt', 'r', encoding='utf-8') as myFile:
    for line in myFile:
        lineList = line.split()
        for word in lineList:
            words += 1
            if '.' in word or ',' in word or '"' in word or '?' in word or '!' in word:
                puncts += 1

print("There are {} words and {} punctuations in the text.".format(words, puncts))
