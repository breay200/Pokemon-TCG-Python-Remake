from classes.LoginForm import *

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