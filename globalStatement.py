__author__ = 'zpiao1'
myVar = 100


def myFn():
    global myVar
    myVar = -1


myFn()
print(myVar)