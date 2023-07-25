num = int(input("Enter number below 50: "))

if num >= 50:
    print("Invalid number")
    quit()

for i in range(num, 0, -1):
    print(i)