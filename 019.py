num = int(input("Enter 1, 2 or 3: "))

match num:
    case 1:
        print("Thank you!")
    case 2:
        print("Well done")
    case 3:
        print("Correct")
    case _:
        print("Error message")