count = 0
invite = "y"

while invite == "y":
    name = input("Who do you want to invite? ")
    print(name, "has been invited!")
    count += 1
    invite = input("Do you want to invide somebody else? (y/n): ")
else:
    print(count, "guests" if count > 1 else "guest", "has been invited!")