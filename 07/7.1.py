seasons = ("spring", "summer", "autumn", "winter")
month = int(input("Enter the current month:"))

index = -1
if month in (3,4,5):
    index = 0
elif month in (6,7,8):
    index = 1
elif month in (9,10,11):
    index = 2
elif month in (12,1,2):
    index = 3
else:
    print("Invalid month")
    exit()
print(f"The current season is {seasons[index]}")