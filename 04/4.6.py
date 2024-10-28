import random

def isinside(x,y):
    if(x*x + y*y < 1):
        return 1
    return 0
n = 0
N = int(input("Enter how many random numbers you want to generate:"))
i = 0
while(i <= N):
    x = random.uniform(0.0,1.0)
    y = random.uniform(0.0,1.0)
    if(isinside(x,y)):
        n += 1
    i += 1
print("The approximate value of pi is", 4 * n / N)