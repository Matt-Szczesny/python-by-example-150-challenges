from random import randint

num = randint(1,5)
user = int(input("Enter number from 1 to 5: "))

if num == user:
    print("Well done")
else:
    print("Too high" if user > num else "Too low")
    user = int(input("Try again: "))
    
    if user == num:
        print("Correct!")
    else:
        print("You loose!")