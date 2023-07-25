count = 1
compnum = 50
num = 0

while num != compnum:
    num = int(input("Enter a number: "))
    if num > compnum:
        print("Too high...")
        count += 1
    elif num < compnum:
        print("Too low...")
        count += 1
else:
    print(f"Well done, you took {count} attempts!")