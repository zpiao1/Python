__author__ = 'zpiao1'
# average of a sum of integers in a given range
limit_str = input("range is from 1 to your input: ")

limit_int = int(limit_str)
count_int = 1
sum_int = 0

while count_int <= limit_int:
    sum_int += count_int
    count_int += 1

average = sum_int / (count_int - 1)

print("Average of sum of integers from 1 to", limit_int, \
      "is", average)