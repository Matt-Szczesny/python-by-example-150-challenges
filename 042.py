total = 0

for i in range(0, 5):
    n = int(input(f"Enter {i+1} number: "))
    if "y" == input("Do you want to include that number? (y/n): "):
        total += n

print("Total:", total)