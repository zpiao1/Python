__author__ = 'zpiao1'
# get user input
Nlevels = int(input("How many levels: "))

for level in range(1, Nlevels + 1):

    # Skip the whitespace at each level
    skip = Nlevels - level
    for x in range(skip):
        print(" ", end="")

    # Print the stars at each level
    num = 2 * level - 1
    for x in range(num):
        print("*", end="")

    # Next line
    print()