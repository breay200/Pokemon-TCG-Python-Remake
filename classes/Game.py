from classes.User import *
from classes.config import *
from classes.MainGameLoop import *

class Game():
    def __init__(self, user):
        self.user = user

        self.game_frame = tk.Frame(Config.master)

        self.welcome_label = tk.Label(self.game_frame, text=f"HEY {user.username}\nWELCOME TO POKEMON TCG - PYTHON EDITION")
        self.welcome_label.grid(column=0, row=0, columnspan=5)

        self.start_btn = tk.Button(self.game_frame, text="Start New Match", command=self.start_game)
        self.start_btn.grid(column=0,row=1)

        self.settings_btn = tk.Button(self.game_frame, text="Settings")
        self.settings_btn.grid(column=0, row=2)

        self.exit_btn = tk.Button(self.game_frame, text="Quit Game")
        self.exit_btn.grid(column=0, row=3)

        self.game_frame.grid(column=0, row=0)

    def start_game(self):
        self.game_frame.destroy()  
        mgl = MainGameLoop(self.user)      

        
