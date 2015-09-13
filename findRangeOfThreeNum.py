a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
if a > b:
    max = a
    min = b
else:
    max = b
    min = a
if c > max:
    max = c
elif c < min:
    min = c
print("The range is: ", max - min)
