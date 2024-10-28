inclass = input("Please enter the cabin class")
if(inclass == "LUX"):
    print("upper-deck cabin with a balcony.")
elif(inclass == "A"):
    print("above the car deck, equipped with a window.")
elif(inclass == "B"):
    print("windowless cabin above the car deck.")
elif(inclass == "C"):
    print("windowless cabin below the car deck.")
else:
    print("Invalid cabin class")