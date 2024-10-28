import random

def roll():
    return random.randint(1,6)
value = roll()
print(value)
while value != 6:
    value = roll()
    print(value)