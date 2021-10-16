from classes.LoginForm import *
from classes.User import *
from classes.Deck import *
from classes.Game import *
from classes.main_application import *

class Menu():
    def __init__(self):
        pass

    def main_menu(self):
        print("Welcome to Pokemon Trading Card Game - Python Edition!")
        
        root = tk.Tk()
        width = root.winfo_screenwidth() * 0.75
        height = root.winfo_screenheight() * 0.75
        root.geometry("%dx%d" % (width, height))
        root.title("TCG REMAKE")
        application = MainApplication(root)
        root.mainloop()
        
        #self.game_menu(username)


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
                    decks = deck.get_decks("data/set1.json")
                    deck.set_active_deck(decks)
                    deck.load_deck("data/set1.json")
            elif response == 3:
                    if check_in_file("data/player_data.txt", username):
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
                