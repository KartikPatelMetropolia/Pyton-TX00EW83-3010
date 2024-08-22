
def exist(list,name):
    if name in list:
        return 1
    return 0
set = set()
name = input("Enter name:")
while name != "":
    if exist(set,name):
        print("Existing name")
    else:
        print("New name")
    set.add(name)
    name = input("Enter name:")
for i in set:
    print(i)