from random import choice

coin = ["head","tail"]
valid = choice(coin)

choice = input("Head or tail? ")
if valid.startswith(choice.lower()):
    print("You win")
else:
    print("Bad luck, it was", valid)