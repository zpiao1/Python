x = int(input("Enter the value of x: "))
list = []
for count in range(0, x + 1):
    if count % 3 == 0:
        list.append(count * count)

print(list)