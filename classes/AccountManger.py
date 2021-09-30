import getpass
from misc_functions import hash_and_store

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
