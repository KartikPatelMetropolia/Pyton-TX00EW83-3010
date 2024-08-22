def convert(gallons):
    return gallons * 3.785

while True:
    gallons = int(input("Enter the number of gallons or -1 to quit"))
    if gallons < 0:
        break
    print(f"{gallons} gallons are {convert(gallons)}")