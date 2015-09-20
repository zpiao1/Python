__author__ = 'zpiao1'


def myFunction(paramList):
    paramList[0] = 100
    print(paramList)


argList = [1, 2, 3]
myFunction(argList)
print(argList)