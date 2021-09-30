import getpass
from misc_functions import *

class Menu():
    def __init__(self):
        pass

    def main_menu(self):
        print("Welcome to Pokemon Trading Card Game - Python Edition!")
        login_form = LoginForm()
        username = login_form.check_account()
        menu = Menu()
        menu.game_menu()
        #print(username)

    def game_menu(self):
        print("Game Menu")

class Form():
    def __init__(self):
        pass
    
class LoginForm(Form):
    def __init__(self):
        pass

    def check_account(self):
        print("Enter a username to login or create an account!")
        while True:
            username = input("Enter username: ")
            try:
                str(username)
            except ValueError:
                print("Please enter a string value!")
            if check_in_file("passwd.txt", username):
                login_form = LoginForm()
                if login_form.login(username):
                    #return username and login status to create Player object?
                    return username
                else:
                    print("You did not login successfully.")
            else:
                #was unsure if I should put the create account function in this class or another class
                print("User does not exist. Prompt user to create account.")
                account_creator = AccountCreator()
                account_creator.create_account(username)
    
    def login(self, username):
        failed_logins = 0
        while True:
            print(f"Please enter the password for: {username}")
            password = getpass.getpass("Enter a password: ")
            try:
                str(password)
            except ValueError:
                print("Please enter a string value!")
            password_hash = hashlib.md5(str(password).encode('utf-8'))
            password = password_hash.hexdigest()
            if check_password(username, password):
                print("You have logged in successfully!")
                #return a True value if login success
                return True
            else:
                failed_logins += 1
                print("You have failed to login.")
                print(f"There are {3-failed_logins} attempts remaining")
                if failed_logins >= 3:
                    print("You have failed too many times. Account has been locked.")
                    #return a False value if login failed
                    return False
        

class AccountManager():
    def __init__(self):
        pass

    #gets password and validates that it matches
    def set_password(self, username):
        while True:
            print(f"Please enter a password for {username}")
            plain_password = input("Enter a password: ")
            hidden_password = getpass.getpass("Re-enter the password: ")
            try:
                str(plain_password)
                str(hidden_password)
            except ValueError:
                print("Please enter a valid response")
            if plain_password == hidden_password:
                hash_and_store(username, plain_password)
                break
            else:
                print("The passwords you entered don't match. Please try again.")


class AccountCreator(AccountManager):
    def __init__(self):
        pass
    
    def create_account(self, username):
        while True:
            print(f"Are you sure you want your username to be {username}?")
            response = input("Enter Y or N: ")
            try:
                str(response)
            except ValueError:
                print("Please enter a valid response!")
            if response is 'Y':
                print(response)
                account_creator = AccountCreator()
                account_creator.set_password(username)
                break
            elif response is 'N':
                print(response)
                print("Please enter a username")
                temp_username = input("Enter a username: ")
                try:
                    str(temp_username)
                except ValueError:
                    print("Please enter a valid response")
                #checking to see if the username already exists
                if check_in_file("usernames.txt", temp_username):
                    print("Username already exists")
                else:
                    print("Username is available")
                    username = temp_username
                    account_creator = AccountCreator()
                    account_creator.set_password(username)
                    break
            else:
                print("You did not enter a valid response.")









