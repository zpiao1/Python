# Get input
body_temperature = float(input("What is your body temperature?"))

# Checking
if body_temperature > 37.5:
    print("Fever!")
    print("Time to see doctor")
else:
    print("Normal!")