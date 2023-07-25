from random import randint

ans = 0
num = randint(1,10)

ans = int(input("Enter number: "))

while ans != num:
    print("Too high" if ans > num else "Too low")
    ans = int(input("Enter number: "))
