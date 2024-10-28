import random

def roll(max):
    return random.randint(1,max)
max = int(input("Enter number of sides:"))
value = roll(max)
print(value)
while value != max:
    value = roll(max)
    print(value)