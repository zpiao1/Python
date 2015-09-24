# calculator example from Module 4

result = 0
while True:
    try:
        # Read a math expression
        input_str = input("Enter a math expression: ")

        # execute the expression
        exec("result = " + input_str)

    except NameError:
        print("Please provide a correct expression")

    except ZeroDivisionError:
        print("Denominator should not be zero")

    else:
        # print the result
        print("Result = ", result)
