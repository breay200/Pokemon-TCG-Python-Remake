from classes.Lobby import Lobby
from classes.MainGameLoop import MainGameLoop
from classes.User import *
from classes.config import *
import tkinter as tk
from classes.Lobby import *
from tkinter import font

class MainMenu():
    def __init__(self, user):
        self.user = user

        width = Config.master.winfo_width()
        height = Config.master.winfo_height()
        self.width = width
        self.height = height

        self.main_menu_frame = tk.Frame(Config.master, width=self.width, height=self.height)

        font_height = 0 - int(self.height*0.05)
        banner_font = font.Font(family="Courier", size=font_height, weight="bold", underline=1)

        self.banner = tk.Label(self.main_menu_frame, text=f"WELCOME TO POKEMON TCG (PYTHON EDITION), {user.username.capitalize()}!", font=banner_font)
        self.banner.place(x=0,y=self.height*0.2)

        self.start_btn = tk.Button(self.main_menu_frame, text="JOIN LOBBY", command=self.start_game)
        self.start_btn.place()

        self.settings_btn = tk.Button(self.main_menu_frame, text="SETTINGS", command=self.settings)
        self.settings_btn.place()

        self.exit_btn = tk.Button(self.main_menu_frame, text="QUIT", command=self.quit)
        self.exit_btn.place()

        self.main_menu_frame.place(x=0,y=0)

    def start_game(self):
        self.game_frame.destroy()
        lobby = Lobby(self.user)
    
    def quit(self):
        Config.master.destroy()
    
    def settings(self):
        #should I create a settings class for creater seperation?

        self.main_frame.destroy()
        self.settings_frame = tk.Frame(Config.master, width=self.width, height=self.height)

        self.change_resolution_label = tk.Label(self.settings_frame, text="Change Resolution: ", bg="silver")
        
        self.default = tk.StringVar()
        self.default.set(Config.RESOLUTIONS[4])

        self.drop_down = tk.OptionMenu(self.settings_frame, self.default, *Config.RESOLUTIONS)

        self.apply_btn = tk.Button(self.settings_frame, text="Apply Changes", command=self.apply_settings)
        

        self.change_resolution_label.place(x=int(self.width*0.4), y=int(self.height*0.5))
        self.drop_down.place(x=int(self.width*0.5), y=int(self.height*0.5))
        self.apply_btn.place(x=int(self.width*0.5), y=int(self.height*0.6))
        self.settings_frame.place(x=0, y=0)