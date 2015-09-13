result = 0

while True:
    # Read a math expression
    input_str = input("Enter a math. expression: ")

    # Execute the expression
    exec("result = " + input_str)

    # Print the result
    print("result=", result)
