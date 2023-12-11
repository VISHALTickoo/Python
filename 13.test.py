import getpass
import msvcrt
from datetime import datetime
from colorama import Fore, Style, init


init(autoreset=True)  # Initialize colorama

# User details dictionary
users = {
    "user1": {"name": "User 1", "password": "pass1", "balance": 5000},
    "user2": {"name": "User 2", "password": "pass2", "balance": 5000},
    "user3": {"name": "User 3", "password": "pass3", "balance": 5000},
    "user4": {"name": "User 4", "password": "pass4", "balance": 5000},
    "user5": {"name": "User 5", "password": "pass5", "balance": 5000}
}

# Admin details
admin = {"userid": "admin", "password": "adminpass", "balance": 1000000}


def print_welcome_message():
    print(Fore.BLUE + Style.BRIGHT)
    print(Fore.BLUE + Style.BRIGHT + "                                                                  ╔═══════════════════════════════════════════╗")
    print(Fore.BLUE + Style.BRIGHT + "                                                                  ║                                           ║")
    print(Fore.BLUE + Style.BRIGHT + "                                                                  ║                                           ║")
    print(Fore.BLUE + Style.BRIGHT + "                                                                  ║                                           ║")
    print(Fore.BLUE + Style.BRIGHT + "                                                                  ║          Welcome to ABC Bank ATM          ║")
    print(Fore.BLUE + Style.BRIGHT + "                                                                  ║                                           ║")
    print(Fore.BLUE + Style.BRIGHT + "                                                                  ║           Select an option:               ║")
    print(Fore.BLUE + Style.BRIGHT + "                                                                  ║             1. Admin Login                ║")
    print(Fore.BLUE + Style.BRIGHT + "                                                                  ║             2. User Login                 ║")
    print(Fore.BLUE + Style.BRIGHT + "                                                                  ║                                           ║")
    print(Fore.BLUE + Style.BRIGHT + "                                                                  ║                                           ║")
    print(Fore.BLUE + Style.BRIGHT + "                                                                  ╚═══════════════════════════════════════════╝" + Style.RESET_ALL)

def print_success(message):
    print(Fore.GREEN + f"✓ {message}" + Style.RESET_ALL)


def print_error(message):
    print(Fore.RED + f"✗ {message}" + Style.RESET_ALL)


# Login user function
def login_users(userid, password):
    if userid in users:
        if password == users[userid]["password"]:
            print_success("Login successful!")
            return True
        else:
            print_error("Invalid password!")
    else:
        print_error("Invalid userid!")
    return False


# Deposit function
def deposit(userid, amount):
    if amount > 100000:
        print_error("Deposit amount exceeds the limit of 1 lakh. Please deposit a lower amount.")
    else:
        users[userid]["balance"] += amount
        transaction_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print_success(f"Deposit successful! Transaction time: {transaction_time}")


# Withdraw function
def withdraw(userid, amount):
    if amount > 50000:
        print_error("Withdrawal amount exceeds the limit of 50,000. Please withdraw a lower amount.")
    elif amount > users[userid]["balance"]:
        print_error("Insufficient balance!")
    else:
        users[userid]["balance"] -= amount
        transaction_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print_success(f"Withdrawal successful! Transaction time: {transaction_time}")


# Balance function
def check_balance(userid):
    transaction_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print_success(f"Balance: {users[userid]['balance']} | Transaction time: {transaction_time}")


# Change userid or password
def change_credentials_menu(userid):
    while True:
        print(Fore.BLUE + Style.BRIGHT + "\n***** Change Userid or Password Menu *****")
        print(Fore.BLUE + Style.BRIGHT + "1. Change Userid")
        print(Fore.BLUE + Style.BRIGHT + "2. Change Password")
        print(Fore.BLUE + Style.BRIGHT + "3. Go back")

        change_choice = input("\nEnter your choice: ")

        if change_choice == '1':
            new_userid = input("Enter new userid: ")
            change_user_credentials(userid, new_userid=new_userid)
        elif change_choice == '2':
            new_password = getpass_windows("Enter new password: ")
            change_user_credentials(userid, new_password=new_password)
        elif change_choice == '3':
            break  # Go back to the main user menu
        else:
            print_error("Invalid choice!")


def change_user_credentials(userid, new_userid=None, new_password=None):
    if userid in users:
        # Backup the user details in case changes cannot be made
        backup_user = users[userid].copy()

        # Check for conflicts with new_userid
        if new_userid is not None:
            if new_userid != userid and new_userid not in users:
                users[new_userid] = users.pop(userid)
                print_success(f"Userid changed to: {new_userid}")
            else:
                print_error(f"Cannot change userid to '{new_userid}'. It either matches the current userid or already exists.")
                # Restore original user details
                users[userid] = backup_user
                return "No changes made"

        # Update the password if new_password is provided
        if new_password is not None:
            users[userid]["password"] = new_password
            print_success("Password changed successfully")

        return "User credentials changed successfully"
    else:
        return "Invalid userid!"


# Admin menu function
def admin_menu():
    while True:
        print(Fore.BLUE + Style.BRIGHT + "\n***** Admin Menu *****")
        print(Fore.BLUE + Style.BRIGHT + "1. Check Total Balance")
        print(Fore.BLUE + Style.BRIGHT + "2. Deposit Cash")
        print(Fore.BLUE + Style.BRIGHT + "3. Logout")

        choice = input(Fore.BLUE + Style.BRIGHT + "\nEnter your choice: ")

        if choice == "1":
            total = admin["balance"]
            for user in users.values():
                total += user["balance"]
            print_success(f"Total balance: {total}")

        elif choice == "2":
            amount = int(input("Enter amount to deposit: "))
            admin["balance"] += amount
            print_success("Deposit successful!")

        elif choice == "3":
            print_success("Logout successfully")
            break

        else:
            print_error("Invalid choice!")


# User menu function
def user_menu(userid):
    while True:

        print(Fore.BLUE + Style.BRIGHT + "\n***** User Menu *****")

        print(Fore.BLUE + Style.BRIGHT + "1. Deposit Cash")
        print(Fore.BLUE + Style.BRIGHT + "2. Withdraw Cash")
        print(Fore.BLUE + Style.BRIGHT + "3. Check Balance")
        print(Fore.BLUE + Style.BRIGHT + "4. Change userid or password")
        print(Fore.BLUE + Style.BRIGHT + "5. Logout")

        choice = input(Fore.BLUE + Style.BRIGHT + "\nEnter your choice: ")

        if choice == "1":

            amount = int(input("Enter amount to deposit: "))
            deposit(userid, amount)

        elif choice == "2":
            amount = int(input("Enter amount to withdraw: "))
            withdraw(userid, amount)

        elif choice == "3":

            check_balance(userid)

        elif choice == "4":
            change_credentials_menu(userid)

        elif choice == "5":
            print_success("Logout successfully")
            break

        else:
            print_error("Invalid choice!")


def getpass_windows(prompt="Enter password: "):
    password = ""
    print(prompt, end='', flush=True)
    while True:
        char = msvcrt.getch()
        if char == b'\r' or char == b'\n':
            print('')
            break
        elif char == b'\x08':
            if password:
                password = password[:-1]
                print('\b \b', end='', flush=True)
        else:
            password += char.decode('utf-8')
            print('*', end='', flush=True)
    return password


# Main menu
while True:

    print_welcome_message()

    choice = input(Fore.BLUE + Style.BRIGHT + "\nEnter your choice: ")

    if choice == "1":
        userid = input("Enter admin userid: ")

        password = getpass_windows("Enter password: ")
        if login_users(userid, password):
            admin_menu()
        else:
            print_error("Invalid userid or password!")

    elif choice == "2":
        userid = input("Enter userid: ")
        password = getpass_windows("Enter password: ")

        if login_users(userid, password):
            user_menu(userid)
        else:
            print_error("Invalid userid or password!")

    else:
        print_error("Invalid choice!")


















































