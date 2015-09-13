import math

# Inputs
x = 4
epsilon = 1e-7

# initialization
guess = x / 2.0
diff = guess * guess - x

# compute sqrt iteratively
iter = 1
while abs(diff) > epsilon:  # done?
    print("iter#", iter, ": guess=", guess)
    guess = (x / guess + guess) / 2.0
    diff = guess * guess - x
    iter += 1

# compare with sqrt
print("result: ", guess)
print("sqrt(x): ", math.sqrt(x))
print("difference: ", (guess - math.sqrt(x)))
