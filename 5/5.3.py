num = int(input("Enter a number:"))
for i in range(2,num):
    if num % i == 0:
        print("The given number is not prime")
        exit()
print("The given number is prime")