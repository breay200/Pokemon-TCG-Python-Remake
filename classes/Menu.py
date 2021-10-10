from classes.LoginForm import *
from classes.User import *
from classes.Deck import *
from classes.Game import *

class Menu():
    def __init__(self):
        pass

    def main_menu(self):
        print("Welcome to Pokemon Trading Card Game - Python Edition!")
        login_form = LoginForm()
        username = login_form.check_account()
        self.game_menu(username)
        #print(username)

    def game_menu(self, username):
        user = User(username)
        deck = Deck()
        print("Game Menu")
        shouldContinue = True
        while shouldContinue:
            print(f"Welcome {username}! Your current deck is {deck.active_deck} Please select an option from the menu.")
            print("1. Start New Match")
            print("2. Change Deck")
            print("3. Update Account Information")
            print("4. Quit Game")
            response = input("Enter 1, 2 or 3: ")
            try:
                response = int(response)
            except ValueError:
                print("You did not enter a valid number!")
            if response == 1:
                    game = Game(user)
                    game.main_game_loop()
            elif response == 2:
                    decks = deck.get_decks("set1.json")
                    deck.set_active_deck(decks)
                    deck.load_deck("set1.json")
            elif response == 3:
                    if check_in_file("player_data.txt", username):
                        user.load_user_data()
                        print(user)
                    else:
                        user.create_user_data(deck)
                        print(user)
            elif response == 4:
                    print("Quitting Program")
                    shouldContinue = False
            else:
                pass
                