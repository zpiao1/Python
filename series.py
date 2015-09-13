__author__ = 'zpiao1'
# ask for x
x = float(input("Input x: "))

# initialization
total = term = 1.0

# computation
for divisor in range(1, 11):
    term = -term * x / divisor
    total += term
    # print(term)
print("total = ", total)