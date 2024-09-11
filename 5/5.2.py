from unittest.mock import numerics

numbers = list()
str = input("Enter the number:")
i = 0
while str != "":
    numbers.append(int(str))
    str = input("Enter the number:")
    i = i + 1
numbers.sort(reverse=True)
print(numbers[:5])