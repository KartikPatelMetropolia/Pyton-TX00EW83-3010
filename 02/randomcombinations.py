import random

three = random.randint(0,9)
threestr = str(three)
for i in range(2):
    threestr += str(random.randint(0,9))
four = random.randint(1,6)
fourstr = str(four)
for i in range(3):
    fourstr += str(random.randint(1,6))
print("The two random combinations are",threestr,"and",fourstr)
print("The overall combination is",threestr + fourstr)