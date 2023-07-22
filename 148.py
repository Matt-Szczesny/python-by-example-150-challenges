import os
import re
import csv 

FILE = "./148-users.csv"

data = {}
data["users"] = {}

class Password():

    def measure_strength(self, password):
        strength = 0

        if len(password) >= 8:
            strength += 1

        if re.search(r'[A-Z]', password):
            strength += 1

        if re.search(r'[a-z]', password):
            strength += 1

        if re.search(r'[0-9]', password):
            strength += 1

        if re.search(r'[!$%&<*@]', password):
            strength += 1

        return strength
    
    def validate(self, password):
        while True:
            os.system("clear")
            strength = self.measure_strength(password)

            if strength < 3:
                print("Password is too weak, please try again")
                password = input("Enter new password: ")
                continue
            elif strength < 5:
                repeat = input("Password is moderate and can be improved. Try again? (y/n): ")
                if repeat == "y":
                    password = input("Enter new password: ")
                    continue

            return password

def ensure_file_exists():
    if not os.path.isfile(FILE):
        os.system(f"touch {FILE}")

def count_records():
    ensure_file_exists()

    with open(FILE, "r") as file:
        return sum(1 for row in file)

def load_csv():
    ensure_file_exists()
    data["users"] = {}

    with open(FILE, "r") as file:
        reader = csv.reader(file)
        for user, password in reader:
            data["users"][user] = password

def update_csv():
    with open(FILE, "w") as file:
        writer = csv.writer(file)
        for key, value in data["users"].items():
            writer.writerow([key, value])

def create_user():
    p = Password()

    while True:
        name = input("User ID: ")
        if name in data["users"].keys():
            input("User with this ID already exists!")
            continue

        password = p.validate(input("Enter new password: "))

        data["users"][name] = password
        update_csv()
        return input("User has been created!")

def change_password():
    user = input("Enter User ID: ")

    if user in data["users"].keys():
        p = Password()
        password = p.validate(input("Enter new password: "))

        data["users"][user] = password
        input("Password has been updated")
        update_csv()
    else:
        input("Invalid user id")

def exit_program():
    print("Bye!")
    quit()

def list_users():
    os.system("clear")
    if count_records() == 0:
        print("No users found")
    else:
        i = 1
        for key, value in data["users"].items():
            print(i, key)
            i += 1
    input("\nHit ENTER to continue")

def main():
    load_csv()

    while True:
        os.system("clear")
        print("Menu")
        print("1) Create a new User ID")
        print("2) Change a password")
        print("3) Display all User IDs")
        print("4) Quit")
        
        choice = int(input("Your choice: "))

        match choice:
            case 1: create_user()
            case 2: change_password()
            case 3: list_users()
            case 4: exit_program()

try:
    main()
except KeyboardInterrupt:
    exit_program()