try:
    print("Entering try suite")
    dividend = float(input("dividend: "))
    divisor = float(input("divisor: "))
    result = dividend / divisor
    print("{:2.2f} dividend by {:2.2f} = {:2.2f}". \
          format(dividend, divisor, result))

except ZeroDivisionError:
    print("Divide by 0 error")

except ValueError:
    print("Couldn't convert to a float")

print("Continuing with the rest of the program")
