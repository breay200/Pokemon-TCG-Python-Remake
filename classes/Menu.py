from classes.LoginForm import *
from classes.User import *
from classes.Deck import *

class Menu():
    def __init__(self):
        pass

    def main_menu(self):
        print("Welcome to Pokemon Trading Card Game - Python Edition!")
        login_form = LoginForm()
        username = login_form.check_account()
        menu = Menu()
        menu.game_menu(username)
        #print(username)

    def game_menu(self, username):
        print("Game Menu")
        while True:
            print(f"Welcome {username}! Please select an option from the menu.")
            print("1. Start New Match")
            print("2. Change Deck")
            print("3. Update Account Information")
            print("4. Quit Game")
            response = input("Enter 1, 2, 3 or 4: ")
            try:
                response = int(response)
            except ValueError:
                print("You did not enter a valid number!")
            if response == 1:
                #start match method
                print(1)
                break
            elif response == 2:
                #change deck method
                deck = Deck()
                deck.get_decks("set1.json")
                break
            elif response == 3:
                user = User(username)
                if check_in_file("player_data.txt", username):
                    user.load_user_data()
                    print(user)
                else:
                    user.create_user_data()
                    print(user)
            elif response == 4:
                print("Quitting Program")
                quit()
            else:
                pass
                