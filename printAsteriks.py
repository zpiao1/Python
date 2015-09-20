__author__ = 'zpiao1'
width = int(input("input pattern width: "))
print()
for row in range (1, 2 * width):
    print("*" * (width - abs(width - row)))