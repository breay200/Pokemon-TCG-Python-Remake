from ctypes import WINFUNCTYPE
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

        self.width = Config.master.winfo_width()
        self.height = Config.master.winfo_height()

        self.main_menu_frame = tk.Frame(Config.master, width=self.width, height=self.height)

        font_height = 0 - int(self.height*0.05)
        banner_font = font.Font(family="Courier", size=font_height, weight="bold", underline=1)

        self.banner = tk.Label(self.main_menu_frame, text=f"WELCOME TO POKEMON TCG (PYTHON EDITION), {user.username.capitalize()}!", font=banner_font)
        self.banner.place(x=0,y=0)

        btn_font = font.Font(family="Courier", size=(0 - int(self.height*0.04)), weight="bold")
        btn_width = int(self.width*0.4)
        btn_x_coordinate = ((self.width/2)-btn_width)
        btn_y_coordinates = [(self.height*0.3), (self.height*0.4), (self.height*0.5), (self.height*0.6)]

        self.lobby_btn = tk.Button(self.main_menu_frame, text="JOIN ONLINE LOBBY", command=self.go_to_lobby, bg="red", fg="white", font=btn_font)
        self.lobby_btn.place(x=btn_x_coordinate, y=btn_y_coordinates[0], width=btn_width)

        self.deck_btn = tk.Button(self.main_menu_frame, text="VIEW / EDIT DECKS", command=self.view_decks, bg="red", fg="white", font=btn_font)
        self.deck_btn.place(x=btn_x_coordinate, y=btn_y_coordinates[1], width=btn_width)

        self.search_btn = tk.Button(self.main_menu_frame, text="SEARCH THE CARD DATABASE", command=self.search_cards, bg="red", fg="white", font=btn_font)
        self.search_btn.place(x=btn_x_coordinate, y=btn_y_coordinates[2], width=btn_width)

        self.view_profile = tk.Button(self.main_menu_frame, text="VIEW PROFILE", command=self.view_profile)
        #self.view_profile.place()

        self.settings_btn = tk.Button(self.main_menu_frame, text="SETTINGS", command=self.settings)
        #self.settings_btn.place()

        self.quit_btn = tk.Button(self.main_menu_frame, text="QUIT", command=self.quit, bg="red", fg="white", font=btn_font)
        self.quit_btn.place(x=btn_x_coordinate, y=btn_y_coordinates[3], width=btn_width)

        self.main_menu_frame.place(x=0,y=0)

    def go_to_lobby(self):
        self.main_menu_frame.destroy()
        lobby = Lobby(self.user)
    
    def view_decks(self):
        pass
    
    def view_profile(self):
        pass

    def search_cards(self):
        pass

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