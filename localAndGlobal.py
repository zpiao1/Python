__author__ = 'zpiao1'
myVar = 123  # global


def myFn(myVar=456):  # parameter is local
    yourVar = -10  # assignment is local
    print(myVar, yourVar)


myFn()  # prints 456 -10
myFn(500)  # prints 500 -10
print(myVar)  # prints 123
print(yourVar)  # ERROR