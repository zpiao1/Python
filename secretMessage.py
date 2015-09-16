__author__ = 'zpiao1'
# The rule is to minus 15 from the ASCII
#  value of each character of the original
# string.

origin_str = input("Enter the message to be encrypted: ")
secret_str = ""
for ch in origin_str:
    secret_str += chr(ord(ch) - 15)
print("The secret message is: ", secret_str)
decrypted_str = ""
for ch in secret_str:
    decrypted_str += chr(ord(ch) + 15)
print("The decrypted message is: ", decrypted_str)