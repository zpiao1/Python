__author__ = 'zpiao1'


def myFun(param):
    param.append(4)
    return param


myList = [1, 2, 3]
newList = myFun(myList)
print(myList, newList)