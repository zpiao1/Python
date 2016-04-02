__author__ = 'zpiao1'
input_str = input("Enter the string to be modified: ")
second_half_str = input_str[len(input_str) // 2:]
# print(second_half_str)
output_str = second_half_str.replace("a", "A")
output_str = output_str.replace("e", "E")
output_str = output_str.replace("i", "I")
output_str = output_str.replace("o", "O")
output_str = output_str.replace("u", "U")
output_str = input_str[:len(input_str) // 2] + output_str
print("The modified string is: " + output_str)
