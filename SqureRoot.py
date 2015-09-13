# Inputs
x = 100.0
epsilon = 1e-14

# initialization
guess = x / 2.0
diff = guess * guess - x

# compute sqrt iteratively
while abs(diff) > epsilon:  # done?
    guess = (x / guess + guess) / 2.0
    diff = guess * guess - x

# compare with sqrt
print("result: ", guess)
