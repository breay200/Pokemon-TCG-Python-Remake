from ctypes import WinDLL
import tkinter as tk
from classes.config import *
from classes.LoginForm import LoginForm
from PIL import Image, ImageTk
from tkinter import font

class MainMenu:
    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.main_frame = tk.Frame(Config.master, width=width, height=height)

        self.title_img = Image.open("images/menu_logo.png").resize((int(width*0.55), int(height*0.55)))
        self.title_img = ImageTk.PhotoImage(self.title_img)

        self.img_label = tk.Label(self.main_frame, image=self.title_img, borderwidth=0, highlightthickness=0, width=int(width*0.55), height=int(height*0.55))
        self.img_label.place(x=int(width*0.225), y=int(height*0.1))

        input_font = font.Font(family="Courier", size=(0 - int(self.height*0.04)), weight="bold")

        btn_width = int((width*0.5)/3)
        btn_x_coordinates = [btn_width*0.5, btn_width*2.5, btn_width*4.5]
        btn_y_coordinates = height*0.75

        self.start_btn = tk.Button(self.main_frame, text="START", font=input_font, fg="white", command=self.start, width=btn_width, bg="red")
        self.start_btn.place(x=btn_x_coordinates[0], y=btn_y_coordinates, width=btn_width)

        self.settings_btn = tk.Button(self.main_frame, text="SETTINGS", font=input_font, fg="white", command=self.settings, width=btn_width, bg="red")
        self.settings_btn.place(x=btn_x_coordinates[1], y=btn_y_coordinates, width=btn_width)
        
        self.quit_btn = tk.Button(self.main_frame, text="QUIT", font=input_font, fg="white", command=self.quit, width=btn_width, bg="red")
        self.quit_btn.place(x=btn_x_coordinates[2], y=btn_y_coordinates, width=btn_width)

        self.main_frame.place(x=0,y=0)

    def quit(self):
        Config.master.destroy()

    def start(self):
        self.main_frame.destroy()
        login_form = LoginForm(self.width, self.height)
    
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
    
    def apply_settings(self):
        result = tk.messagebox.askyesno("Apply Settings", "Would you like to save and apply these settings?")
        if result:
            print("apply settings")