rainy = input("Is to raining? (yes/no) ")

if rainy.lower() == "yes":
    windy = input("Is it windy? (yes/no) ")
    if windy.lower() == "yes":
        print("It is too windy for an umbrella!")
    else:
        print("Take an unbrella!")
else:
    print("Enjoy the day!")