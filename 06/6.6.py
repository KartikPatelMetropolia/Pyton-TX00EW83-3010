def unitcalc(diameter,price):
    area = 3.14 * ((diameter / 2) ** 2)
    areainmeter = area / 10000
    return areainmeter / price

diameter1 = float(input("Enter the diameter of the first pizza:"))
price1 = float(input("Enter the price of the first pizza:"))
diameter2 = float(input("Enter the diameter of the second pizza:"))
price2 = float(input("Enter the price of the second pizza"))
unitprize1 = unitcalc(diameter1,price1)
unitprize2 = unitcalc(diameter2,price2)
if unitprize1 < unitprize2:
    print("First pizza has more unit per price")
else:
    print("Second pizza has more unit per price")
