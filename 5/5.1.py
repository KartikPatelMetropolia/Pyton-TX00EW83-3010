import random
num = int(input("Enter the number of dice rolls"))
sum = 0
for i in range(num):
    roll = random.randint(1,6)
    sum += roll
print(f"The sum of all the rolls is {sum}")