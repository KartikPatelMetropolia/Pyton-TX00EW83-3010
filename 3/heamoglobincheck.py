gender = input("Enter your gender:(m/f)")
g = gender.lower()
if(g == "m"):
    value = float(input("Enter the value of hemoglobin you have:"))
    if(value >= 134 and value <= 167):
        print("Your hemoglobin is normal")
    elif(value < 134):
        print("Your hemoglobin is lower than expected")
    else:
        print("Your hemoglobin is higher than expected")
elif(g == "f"):
    value = float(input("Enter the value of hemoglobin you have:"))
    if(value >= 117 and value <= 155):
        print("Your hemoglobin is normal")
    elif(value < 117):
        print("Your hemoglobin is lower than expected")
    else:
        print("Your hemoglobin is higher than expected")
else:
    print("Please enter a valid input")