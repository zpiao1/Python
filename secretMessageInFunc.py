__author__ = 'zpiao1'
# The rule is to minus 15 from the ASCII
# value of each character of the original
# string.


def encryptString(string):
    encrypted = ""
    for ch in string:
        encrypted += chr(ord(ch) - 15)
    return encrypted


def decryptString(string):
    decrypted = ""
    for ch in string:
        decrypted += chr(ord(ch) + 15)
    return decrypted


origin_str = input("Enter the message to be encrypted: ")
secret_str = encryptString(origin_str)
print("The secret message is: ", secret_str)
decrypted_str = decryptString(secret_str)
print("The decrypted message is: ", decrypted_str)