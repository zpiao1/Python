vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

inFile = open('tolkien.txt', mode='r', encoding='utf-8')
outFile = open('Output.txt', mode='w', encoding='utf-8')

print(type(inFile))

for line in inFile:
    for letter in line:
        if letter in vowels:
            line = line.replace(letter, '')
    outFile.write(line)  # written to the output file

inFile.close()
outFile.close()
