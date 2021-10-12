from classes.AccountManger import *
from misc_functions import check_in_file

class AccountCreator(AccountManager):
    def __init__(self):
        pass
    
    def create_account(self, username):
        while True:
            print(f"Are you sure you want your username to be {username}?")
            response = input("Enter y or n: ")
            try:
                str(response)
            except ValueError:
                print("Please enter a valid response!")
            if response is 'y':
                print(response)
                self.set_password(username)
                break
            elif response is 'n':
                print(response)
                print("Please enter a username")
                temp_username = input("Enter a username: ")
                try:
                    str(temp_username)
                except ValueError:
                    print("Please enter a valid response")
                #checking to see if the username already exists
                #THIS FILE DOES NOT EXIST!
                if check_in_file("/data/usernames.txt", temp_username):
                    print("Username already exists")
                else:
                    print("Username is available")
                    username = temp_username
                    self.set_password(username)
                    break
            else:
                print("You did not enter a valid response.")









