from ctypes import WINFUNCTYPE
from classes.Lobby import Lobby
from classes.MainGameLoop import MainGameLoop
from classes.User import *
from classes.config import *
import tkinter as tk
from classes.Lobby import *
from tkinter import font
from PIL import Image, ImageTk

class MainMenu():
    def __init__(self, user):
        self.user = user

        self.width = Config.master.winfo_width()
        self.height = Config.master.winfo_height()
        self.view_profile_frame = None
        self.main_menu_frame = tk.Frame(Config.master, width=self.width, height=self.height)

        font_height = 0 - int(self.height*0.05)
        self.banner_font = font.Font(family="Courier", size=font_height, weight="bold", underline=1)

        self.banner = tk.Label(self.main_menu_frame, text=f"WELCOME TO POKEMON TCG (PYTHON EDITION), {user.username.capitalize()}!", font=self.banner_font)
        self.banner.place(x=0,y=0)

        self.btn_font = font.Font(family="Courier", size=(0 - int(self.height*0.04)), weight="bold")
        btn_width = int(self.width*0.4)
        btn_x_coordinate = ((self.width/2)-btn_width)
        btn_y_coordinates = [(self.height*0.3), (self.height*0.4), (self.height*0.5), (self.height*0.6), (self.height*0.7)]

        self.lobby_btn = tk.Button(self.main_menu_frame, text="JOIN ONLINE LOBBY", command=self.go_to_lobby, bg="red", fg="white", font=self.btn_font)
        self.lobby_btn.place(x=btn_x_coordinate, y=btn_y_coordinates[0], width=btn_width)

        self.deck_btn = tk.Button(self.main_menu_frame, text="VIEW / EDIT DECKS", command=self.view_decks, bg="red", fg="white", font=self.btn_font)
        self.deck_btn.place(x=btn_x_coordinate, y=btn_y_coordinates[1], width=btn_width)

        self.search_btn = tk.Button(self.main_menu_frame, text="SEARCH THE CARD DATABASE", command=self.search_cards, bg="red", fg="white", font=self.btn_font)
        self.search_btn.place(x=btn_x_coordinate, y=btn_y_coordinates[2], width=btn_width)

        self.profile_img = Image.open("images/406.png").resize((int(self.width*0.10), int(self.height*0.16)))
        self.profile_img = ImageTk.PhotoImage(self.profile_img)
        self.view_profile = tk.Button(self.main_menu_frame, text="VIEW PROFILE", command=self.view_profile, image=self.profile_img, highlightthickness=2, highlightbackground = "red")
        self.view_profile.place(x=self.width*0.89, y=self.height*0.02, width=self.width*0.10, height=self.height*0.16)

        self.settings_btn = tk.Button(self.main_menu_frame, text="SETTINGS", command=self.settings, bg="red", fg="white", font=self.btn_font)
        self.settings_btn.place(x=btn_x_coordinate, y=btn_y_coordinates[3], width=btn_width)

        self.quit_btn = tk.Button(self.main_menu_frame, text="QUIT", command=self.quit, bg="red", fg="white", font=self.btn_font)
        self.quit_btn.place(x=btn_x_coordinate, y=btn_y_coordinates[4], width=btn_width)

        self.main_menu_frame.place(x=0,y=0)

    def go_to_lobby(self):
        self.main_menu_frame.destroy()
        lobby = Lobby(self.user, self)
    
    def view_decks(self):
        pass
    
    def view_profile(self):
        if self.view_profile_frame is None:
            self.view_profile_frame = tk.Frame(self.main_menu_frame, width=int(self.width*0.8), height=int(self.height*0.5), bg="red") 
            self.view_profile_frame.place(x=self.width*0.1, y=self.height*0.3)
        else:
            self.view_profile_frame.destroy()
            self.view_profile_frame = None

    def search_cards(self):
        pass

    def quit(self):
        Config.master.destroy()

    def apply_settings(self):
        pass
    
    def settings(self):
        self.settings_width = int(self.width*0.8)
        self.settings_height = int(self.height*0.5)
        self.settings_frame = tk.Frame(self.main_menu_frame, width=self.settings_width, height=self.settings_height, bg="red") 
        self.settings_frame.place(x=self.width*0.1, y=self.height*0.3)

        self.settings_label = tk.Label(self.settings_frame, text="SETTINGS", bg="red", fg="white", font=self.banner_font)
        self.settings_label.place(x=(self.settings_width*0.45), y=0)

        self.change_resolution_label = tk.Label(self.settings_frame, text="CHANGE DISPLAY RESOLUTION: ", bg="red", fg="white", font=self.btn_font)
        self.change_resolution_label.place(x=0, y=self.height*0.1)
        
        self.default = tk.StringVar()
        self.default.set(Config.RESOLUTIONS[4])

        self.drop_down = tk.OptionMenu(self.settings_frame, self.default, *Config.RESOLUTIONS)
        self.drop_down.place(x=self.settings_width*0.5, y=self.settings_height*0.1)

        self.apply_btn = tk.Button(self.settings_frame, text="SAVE CHANGES", command=self.apply_settings)
        self.apply_btn.place(x=self.width*0.9, y=self.height*0.9)
        
        self.drop_down.place(x=int(self.width*0.5), y=int(self.height*0.5))
        self.apply_btn.place(x=int(self.width*0.5), y=int(self.height*0.6))
        self.settings_frame.place(x=0, y=0)

        self.address = tk.StringVar()
        self.address_label = tk.Label(self.lobby_frame, text="Enter the IP Address of the Server: ")
        self.address_label.place()
        self.address_entry = tk.Entry(self.lobby_frame, textvariable=self.address)
        self.address_entry.place()

        self.port = tk.IntVar()
        self.port_label = tk.Label(self.lobby_frame, text="Enter the Port Number of the Server: ")
        self.port_label.place()
        self.port_entry = tk.Entry(self.lobby_frame, textvariable=self.port)
        self.port_entry.place()
        
        self.lobby_count_label = tk.Label(self.lobby_frame, text=f"connect to server to see active players")