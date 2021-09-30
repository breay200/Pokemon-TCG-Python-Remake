from classes.AccountManger import *
from misc_functions import check_in_file

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









