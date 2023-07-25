name = input("Enter your first name: ")

if len(name) < 5:
    surname = input("Enter your surname: ")
    full = name + surname
    print(full.upper())
else:
    print(name.lower())