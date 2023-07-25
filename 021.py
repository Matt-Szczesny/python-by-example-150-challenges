name = input("Enter your name: ")
surname = input("Enter your surname: ")

full = name + " " + surname
# full = " ".join([name, surname])
# full = f"{name} {surname}"

print(f"{full} (Length: {len(full)})")
