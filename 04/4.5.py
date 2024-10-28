i = 0

while i <= 5:
    username = input("Enter the username:")
    password = input("Enter the password")
    if username == "python" and password == "rules":
        print("Welcome")
        exit()
    print("Please retry")
    i += 1
print("Access denied")