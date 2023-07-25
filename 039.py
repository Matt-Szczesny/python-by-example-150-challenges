num = int(input("Enter a number between 1 and 12: "))

if num < 1 or num > 12:
    print("Invalid number")
    quit()

for i in range(1,15):
    print(f"{num} * {i} = {num * i}")