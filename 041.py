name = input("Enter your name: ")
num  = int(input("Enter number: ") or 0)

# if num < 10:
#     print((name + " ") * num)
# else:
#     print("Too high! " * 3)

if num < 10:
    for _ in range(0, num):
        print(name)
else:
    for _ in range(0, 3):
        print("Too high!")