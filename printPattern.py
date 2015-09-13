__author__ = 'zpiao1'
# get user input
Nlevels = int(input("How many levels: "))

for level in range(1, Nlevels + 1):

    # Skip the whitespace at each level
    skip = Nlevels - level
    while skip > 0:
        print(" ", end="")
        skip -= 1

    # Print the stars at each level
    num = 2 * level - 1
    while num > 0:
        print("*", end="")
        num -= 1

    # Next line
    print()