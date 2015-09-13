__author__ = 'zpiao1'
Nlevels = int(input("How many levels: "))
for row in range(1, Nlevels + 1):
    for col in range(1, Nlevels + 1):
        print("XX  ", end="")
    print()
    for col in range(1, Nlevels + 1):
        print("  XX", end="")
    print()