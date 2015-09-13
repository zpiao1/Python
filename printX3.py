__author__ = 'zpiao1'
Nlevels = int(input("How many levels: "))
Nspaces1 = Nlevels
for row in range(1, Nlevels + 1):
    for count in range(Nspaces1):
        print(" ", end="")
    print("X")
    Nspaces2 = Nspaces1 - row
    for count in range(1, Nspaces2 + 1):
        print(" ", end="")
    for count in range(1, row + 1):
        print("X", end="")
    print(" ", end="")
    for count in range(1, row + 1):
        print("X", end="")
    print()