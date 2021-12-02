from classes.MainMenu import MainMenu
from classes.config import *
import tkinter as tk

class Start():
    def __init__(self):
        print("Welcome to Pokemon Trading Card Game - Python Edition!")
        Config.master = tk.Tk()
        width = int(Config.master.winfo_screenwidth() * 0.75)
        height = int(Config.master.winfo_screenheight() * 0.75)
        Config.master.geometry(f"{width}x{height}")
        Config.master.title("TCG REMAKE")
        mainmenu = MainMenu(width, height)
        Config.master.mainloop()