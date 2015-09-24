def createList(classIndex, className):
    print("Input the grades of class", classIndex)
    inGrade = int(input())
    while inGrade != -1:
        className.append(inGrade)
        inGrade = int(input())
    return className


class1 = class2 = []

# ask for input of grades, using -1 as sentinel value
class1 = createList(1, class1)
class2 = createList(2, class2)

# find the max as well as the max of the class
ave1 = sum(class1) / len(class1)
ave2 = sum(class2) / len(class2)
max1 = max(class1)
max2 = max(class2)

epsilon = 1e-7
if ave1 - ave2 > epsilon:
    print("Class 1 has higher average score: {:.2f}".format(ave1))
elif ave2 - ave1 > epsilon:
    print("Class 2 has higher average score: {.2f}".format(ave2))
else:
    print("Both class have the same average score: {:.2f}".format(ave1))

if max1 > max2:
    print("Class 1 has higher maximum score: {:.2f}".format(max1))
elif max1 == max2:
    print("Both class have the same maximum score: {:.2f}".format(max1))
else:
    print("Class 2 has higher maximum score: {.2f}".format(max2))
