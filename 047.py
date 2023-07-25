n1 = int(input("Enter number: "))
n2 = int(input("Enter another number: "))
total = n1 + n2
answer = "y"

while answer == "y":
    answer = input("Add another number? (y/n): ")
    if answer == "y":
        total += int(input("Enter another number: "))
else:
    print("Total:", total)



