import tkinter as tk
from tkinter import ttk
#from classes.tk_tests import *
import time
from classes.LoginForm import *

class MainApplication:
    def __init__(self, master) -> None:
        self.root = master
        self.main_frame = tk.Frame(master)

        self.start_button = tk.Button(self.main_frame, text="Start Game", command=self.start, width=25)
        self.start_button.grid(column=5, row=2)
        
        self.quit_button = tk.Button(self.main_frame, text="Quit Game", command=quit, width=25)
        self.quit_button.grid(column=2, row=2)
        #self.settings = tk.Button(self.main_frame, text="Settings", width=5)
        #self.settings.pack()
        self.main_frame.grid(column=0, row=0)

        hand = [1, 2, 3, 4, 5, 6, 7]

        buttons=[] 
        for number in hand: 
            card = tk.Button(self.main_frame, text="card", width=20, height=70)
            buttons.append(card)
        
        count=3
        for value in buttons:
            value.grid(column=count, row=3)
            count += 1

    def quit(self):
        self.master.destroy()

    def start(self):
        self.main_frame.destroy()
        login_form = LoginForm(self.root)
        





class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

'''
class Frame():
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title = "Pokemon TCG Remake"
        
        self.mainframe = ttk.Frame(self.root)
        self.mainframe.grid(column=0, row=0)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        
        #get input from user
        feet = StringVar()
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
        feet_entry.grid(column=2, row=1, sticky=(W, E))

        
        meters = StringVar()
        ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
        
        start_button = ttk.Button(self.mainframe, text="Start")
        start_button.grid(column=2, row=2, sticky=(W, E))

        exit_button = ttk.Button(self.mainframe, text="Exit", command=lambda: change_text(exit_button,"Changed the text"))
        exit_button.grid(column=1, row=2, sticky=E)

        settings_button = ttk.Button(self.mainframe, text="Settings")
        settings_button.grid(column=3, row=2, sticky=W)
        
        #self.root.mainloop()
'''
