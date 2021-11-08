import tkinter as tk
from classes.config import *
from classes.LoginForm import *

class MainApplication:
    def __init__(self) -> None:
        self.main_frame = tk.Frame(Config.master)

        self.start_button = tk.Button(self.main_frame, text="Start Game", command=self.start, width=25)
        self.start_button.grid(column=5, row=2)
        
        self.quit_button = tk.Button(self.main_frame, text="Quit Game", command=quit, width=25)
        self.quit_button.grid(column=2, row=2)

        self.main_frame.grid(column=0, row=0)

    def quit(self):
        Config.master.destroy()

    def start(self):
        self.main_frame.destroy()
        login_form = LoginForm()
