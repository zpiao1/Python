# Tutorial 2: Pandovan Sequence
a = b = c = 1
while a < 1000:
    print(a)
    a, b, c = b, c, a + b
