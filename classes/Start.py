from classes.StartMenu import StartMenu
from classes.config import Config
import tkinter as tk

class Start():
    def __init__(self):
        print("Welcome to Pokemon Trading Card Game - Python Edition!")
        Config.master = tk.Tk()
        width = int(Config.master.winfo_screenwidth() * 0.75)
        height = int(Config.master.winfo_screenheight() * 0.75)
        Config.master.geometry(f"{width}x{height}")
        Config.master.title("TCG REMAKE")
        Config.master.update()
        startmenu = StartMenu()
        Config.master.mainloop()