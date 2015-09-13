__author__ = 'zpiao1'

tempLimit = float(input("Enter conversion limit for F: "))
while tempLimit < 32.0 or tempLimit > 1000.0:
    print("Warning: input value should range from 32 to 1000")
    tempLimit = float(input("Enter conversion limit for F:"))

print("\tFahrenheit\tCelsius")
print("\t----------\t-------")

fahren = 32.0
while fahren <= tempLimit:
    celsius = (fahren - 32.0) * 5.0 / 9.0
    print("\t  %5.1f\t\t %5.1f" % (fahren, celsius))
    fahren += 10