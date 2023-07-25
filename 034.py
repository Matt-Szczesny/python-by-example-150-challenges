print("1) Square")
print("2) Triangle")

select = int(input("Selection: "))

if select == 1:
    side = int(input("Enter side's length: "))
    
    print("Square's area equals:", side**2)
elif select == 2:
    base = int(input("Triangle's base length: "))
    height = int(input("Triangle's height: "))
    
    print("Triangle's area equals:", (base * height) / 2)
else:
    print("Invalid option selected")