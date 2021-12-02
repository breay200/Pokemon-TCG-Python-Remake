import tkinter as tk
from classes.config import *
from classes.LoginForm import LoginForm
from PIL import Image, ImageTk

class MainMenu:
    def __init__(self, width, height):
        print(width, height)


        self.main_frame = tk.Frame(Config.master, width=width, height=height, bg="red")

        self.title_img = Image.open("images/menu_logo.png").resize((int(width), int(height)))
        self.title_img = ImageTk.PhotoImage(self.title_img)

        self.img_label = tk.Label(self.main_frame, image=self.title_img, borderwidth=0, highlightthickness=0, width=width, height=height)
        self.img_label.place(x=0, y=0)

        self.start_button = tk.Button(self.main_frame, text="Start", command=self.start, width=int(width/100), height=int(height/15), bg="blue")
        self.start_button.place(x=(width*0.5), y=(200))
        
        self.quit_button = tk.Button(self.main_frame, text="Quit", command=self.quit, width=int(width/100), height=int(height/100), bg="green")
        self.quit_button.place(x=(width*0.5), y=(height*0.3))

        self.main_frame.place(x=0,y=0)

    def quit(self):
        Config.master.destroy()

    def start(self):
        self.main_frame.destroy()
        login_form = LoginForm()
