__author__ = 'zpiao1'
w1 = input("Enter the first word: ")
w2 = input("Enter the second word: ")
w1sorted = sorted(w1)
w2sorted = sorted(w2)

if w1sorted == w2sorted:
    print("Yes")
else:
    print("No")
