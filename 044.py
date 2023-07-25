guests = int(input("How many people do you want to invite?: "))

if guests < 10:
    for _ in range(0, guests):
        name = input("Guest's name: ")
        print(name, "has been invited!")
else:
    print("Too many people!")