from classes.LoginForm import *
from classes.User import *
from classes.Deck import *
from classes.Game import *
from classes.main_application import *
from classes.config import *

class Menu():
    def __init__(self):
        pass

    def main_menu(self):
        print("Welcome to Pokemon Trading Card Game - Python Edition!")
        Config.master = tk.Tk()
        #width = Config.master.winfo_screenwidth() * 0.75
        #height = Config.master.winfo_screenheight() * 0.75
        #Config.master.geometry("%dx%d" % (width, height))
        Config.master.geometry("1920x1080")
        Config.master.title("TCG REMAKE")
        application = MainApplication()
        Config.master.mainloop()