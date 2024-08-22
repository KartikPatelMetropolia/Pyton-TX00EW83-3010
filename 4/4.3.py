value = input("Enter a value:")
if(value == ""):
    exit()
min = int(value)
max = int(value)
while(value != ""):
    value = int(value)
    if(value > max):
        max = value
    if(value < min):
        min = value
    value = input("Enter a value:")
print(f"The largest value out of the given number is {max} and the samllest is {min}")