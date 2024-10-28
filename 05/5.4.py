names = []
for i in range(5):
    name = input("Please enter the name of the city:")
    names.append(name)
for i in range(5):
    if i == 4:
        print(names[i],end="")
    else:
        print(names[i])