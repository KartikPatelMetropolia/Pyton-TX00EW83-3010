talents = float(input("Etner talents:"))
pound = float(input("Enter pounds:"))
lots = float(input("Enter lots"))
total_grams = talents * 8512 + pound * 425.6 + lots * 13.3
kg = total_grams // 1000
grams = total_grams % 1000
print("The weight in modern units:")
print(kg,"kilograms and",round(grams,2),"grams.")