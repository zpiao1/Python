# hangman.py -- a simplified version of hangman, with simple pattern to show the result
# Author: ZHAO JINGYI
# NTU Email: jzhao009@e.ntu.edu.sg
import random


# Given a string and the index, replace string[index] with the given character
def replace(string, char, i):
    string_list = list(string)
    string_list[i] = char
    return ''.join(string_list)


# Use a dictionary to store the topics, with keys to each topic being a list of words
word_dict = {'Fruits': ["APPLE", "BANANA", "PEAR", "ORANGE", "GRAPE"],
             'Animals': ["MOUSE", "CAT", "DOG", "ELEPHANT", "SNAKE"],
             'Subjects': ["ENGLISH", "MATHS", "CHINESE", "HISTORY", "COMPUTING"],
             'Sports': ["SOCCER", "BASKETBALL", "TENNIS", "SWIMMING", "TAEKWONDO"]}

# Randomly pick a topic and a word under that topic
topic = random.choice(list(word_dict.keys()))
print("The topic is: {}".format(topic))
word = random.choice(word_dict[topic])

# Initializations of variables
count_total = 0
guessed = '_' * len(word)
misses = ''
wrong = 0

# Use a string to store the picture or a hangman
pattern = "----------\n|    |\n|    O\n|   /|\\\n|   / \\\n|\n|         "

# If the guess is wrong, one of the char in pattern will be changed
# The indexes of chars to be changed are stored in char_indexes
char_indexes = [39, 37, 31, 30, 29, 23]

# The main part of the program, uses a infinite loop with break and continue inside
while True:
    # Prints the result of the last turn
    print("{:2d}\tWord: {}".format(count_total, guessed))
    print("  \tGuess: ", end='')
    # If wrong guess has accumulated to 6, the game ends and the guesser loses
    if wrong == 6:
        print("\n  \tMisses: {}".format(misses))
        print(pattern)
        print("Guesser loses - the answer was {}".format(word))
        break
    # If all the guessed chars combine into the correct word, the games ends and the guesser wins
    elif guessed == word:
        print("\n  \tMisses: {}".format(misses))
        print("Guesser wins - the answer was {}".format(word))
        break
    # The game goes on
    else:
        # Ask for input
        guess_char = input()
        # Prints the current state
        print("  \tMisses: {}".format(misses))
        print(pattern)
        # Indicates whether the char is found in the word
        found = False
        count_total += 1
        # If the user inputs the same wrong char, the program will give a prompt and ask for more input
        if guess_char.lower() in misses:
            print("You have guessed {} already".format(guess_char))
            continue
        else:
            # Loop through the correct word to see whether the user has inputted a correct char
            for index in range(0, len(word)):
                # If finds the char in the word, change the guessed word accordingly
                if word[index] == guess_char:
                    guessed = replace(guessed, guess_char, index)
                    found = True
            # If cannot find the char, the mark it as a wrong char
            if not found:
                pattern = replace(pattern, 'X', char_indexes[wrong])
                wrong += 1
                if misses == '':
                    misses += guess_char.lower()
                else:
                    misses += ',' + guess_char.lower()
