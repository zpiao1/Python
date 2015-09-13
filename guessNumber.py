__author__ = 'zpiao1'
import random

# randomize a number
computer_num = random.randint(0, 50)
# print(computer_num)

# Get input
my_guess = int(input("Input your guess: "))

# Checking
if my_guess > computer_num:
    print("Your guess is too large")
elif my_guess < computer_num:
    print("Your guess is too small")
else:
    print("Bingo!!! Correct")