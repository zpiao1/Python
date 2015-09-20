__author__ = 'zpiao1'


def enclosing():
    myVariable = 'defined by enclosing'

    def enclosed():
        print('scope: ' + myVariable)

    enclosed()


enclosing()