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

        self.start_button = tk.Button(self.main_frame, text="Start", command=self.start, width=int(width*0.015), height=int(height*0.005), bg="blue")
        self.start_button.place(x=((width*0.5)-(width*0.015)), y=(height*0.6))
        
        self.quit_button = tk.Button(self.main_frame, text="Quit", command=self.quit, width=int(width*0.015), height=int(height*0.005), bg="green")
        self.quit_button.place(x=((width*0.5)-(width*0.015)), y=(height*0.7))

        self.main_frame.place(x=0,y=0)

    def quit(self):
        Config.master.destroy()

    def start(self):
        self.main_frame.destroy()
        login_form = LoginForm(self.width, self.height)
