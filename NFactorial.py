N = int(input("Input N: "))
if N <= 1:
    NFact = 1
else:
    NFact = 2
    for i in range(3, N + 1):
        NFact = NFact * i
print(NFact)
