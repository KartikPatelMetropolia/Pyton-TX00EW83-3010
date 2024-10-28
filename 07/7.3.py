data = dict()
while True:
    choice = int(input("Menu\nPress 1 to add entry\nPress 2 to fetch information\nPress 3 to quit"))
    if choice == 1:
        icao = input("Enter the icao code of the airport:")
        name = input("Enter name of the airport:")
        data[icao] = name
    elif choice == 2:
        icao = input("Enter the icao code of the airport to fetch:")
        if icao in data:
            print(f"The name of the airport with {icao} is {data[icao]}")
        else:
            print("Please check the icao code of the airport or enter the data.")
    elif choice == 3:
        print("Closing the program.")
        break