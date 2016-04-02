__author__ = 'zpiao1'
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
range1 = abs(a - b)
range2 = abs(b - c)
range3 = abs(a - c)
print("The range is: ", (range1 + range2 + range3) // 2)
