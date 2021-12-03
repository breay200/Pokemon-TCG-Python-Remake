import tkinter as tk
from classes.config import *
from classes.LoginForm import LoginForm
from PIL import Image, ImageTk

class MainMenu:
    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.main_frame = tk.Frame(Config.master, width=width, height=height)

        self.title_img = Image.open("images/menu_logo.png").resize((int(width*0.8), int(height*0.8)))
        self.title_img = ImageTk.PhotoImage(self.title_img)

        self.img_label = tk.Label(self.main_frame, image=self.title_img, borderwidth=0, highlightthickness=0, width=int(width), height=int(height))
        self.img_label.place(x=0, y=0)

        self.start_btn = tk.Button(self.main_frame, text="Start", command=self.start, width=int(width*0.015), height=int(height*0.005), bg="blue")
        self.start_btn.place(x=((width*0.5)-(width*0.015)), y=(height*0.5))

        self.settings_btn = tk.Button(self.main_frame, text="Settings", command=self.settings, width=int(width*0.015), height=int(height*0.005), bg="silver")
        self.settings_btn.place(x=((width*0.5)-(width*0.015)), y=(height*0.6))
        
        self.quit_btn = tk.Button(self.main_frame, text="Quit", command=self.quit, width=int(width*0.015), height=int(height*0.005), bg="green")
        self.quit_btn.place(x=((width*0.5)-(width*0.015)), y=(height*0.7))

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


