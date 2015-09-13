import random

choices = {"Paper": 1, "Scissor": 2, "Rock": 3}
comp_choice = random.choice(list(choices))
print("Paper, Scissor, or Rock")
user_choice = choices[input("Enter your choice: ")]
if choices[comp_choice] == user_choice:
    print("Draw")
elif (user_choice - choices[comp_choice]) % 3 == 1:
    print("You win")
else:
    print("Computer wins")
print("The computer's choice is: " + comp_choice)