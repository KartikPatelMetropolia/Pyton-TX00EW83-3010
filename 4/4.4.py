import random

ans = random.randint(1,10)
value = int(input("Enter a number"))
while(value != ans):
    if(value > ans):
        print("Too high")
    if(value < ans):
        print("Too low")
    value = int(input("Enter a number"))
print(f"Yay !! you have guessed it right {ans} is the answer")