text1 = open("differentText1.txt", 'r', encoding="utf-8")
text2 = open("differentText2.txt", 'r', encoding="utf-8")
outText = open("difference.txt", 'w', encoding="utf-8")

count = 0
text1List = text1.readlines()
text2List = text2.readlines()
print(text1List)
print(text2List)

for line in text1List:
    if line not in text2List:
        count += 1
        outText.write(line)

for line in text2List:
    if line not in text1List:
        count += 1
        outText.write(line)

print("There are totally {} different lines".format(count))
text1.close()
text2.close()
outText.close()
