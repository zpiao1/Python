# A strong password should be at least 8 characters long and include at least one digit,
# one uppercase letter, one lowercase letter, and one special character.

password = input("Enter your password to check whether it is strong enough: ")

if len(password) < 8:
    print("Not strong enough!")
else:
    digits = lower = upper = special = ""
    for char in password:
        asciiCode = ord(char)
        if char.isdigit():
            digits += char
        elif char.isupper():
            upper += char
        elif char.islower():
            lower += char
        elif 33 <= asciiCode <= 126:  # range between 33 and 123 are numbers, letters and
            special += char  # special characters. If a char is neither a digit nor a
            # letter, then it must be a special character
    if len(digits) * len(upper) * len(lower) * len(special) == 0:
        print("Not strong enough!")
    else:
        print("Congratulations! Your password is strong!")
