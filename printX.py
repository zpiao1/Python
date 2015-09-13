__author__ = 'zpiao1'
Nlevels = int(input("How many levels: "))
Nspaces = 0
for row in range(1, Nlevels + 1):
    for count in range(1, Nspaces + 1):
        print(" ", end="")

    for count in range(1, row + 1):
        print("X", end="")
    print()
    Nspaces += row
