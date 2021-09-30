from classes.AccountCreator import *
from classes.Form import *
from misc_functions import check_in_file, check_password
import getpass
import hashlib

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
      