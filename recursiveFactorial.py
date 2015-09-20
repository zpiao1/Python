__author__ = 'zpiao1'
def f(n):
    if n == 1 or n == 0:
        return 1  # stopping point
    else:
        return n * f(n - 1)  # recursion

num = int(input("Enter an integer: "))
print("n! = {}".format(f(num)))