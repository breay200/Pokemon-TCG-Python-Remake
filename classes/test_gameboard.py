import tkinter as tk
from tkinter import Pack, ttk
from tkinter.ttk import *


master = tk.Tk()
#master.geometry("1920x1080")
width = master.winfo_screenwidth() * 0.75
height = master.winfo_screenheight() * 0.75
master.geometry(f"{int(width)}x{int(height)}")
master.title("TCG REMAKE")

opponent = tk.Frame(master, width=width, height=height/2, bg="red")
opponent.place(x=0,y=0)


player = tk.Frame(master, width=width, height=height/2, bg="blue")
prize = tk.Frame(player, width=width*0.2, height=height*0.45, bg="black")
bench = tk.Frame(player, width=width*0.5, height=height*0.17, bg="black")
discard = tk.Frame(player, width=width*0.1, height=height*0.17, bg="black")
deck = tk.Frame(player, width=width*0.1, height=height*0.17, bg="black")
active = tk.Frame(player, width=width*0.1, height=height*0.2, bg="white")

prize.place(x=width*0.02, y=height*0.04)
bench.place(x=(width*0.02+width*0.2+width*0.03), y=height*0.3)
discard.place(x=(width*0.02+width*0.2+width*0.03+width*0.5+width*0.02), y=height*0.3)
deck.place(x=(width*0.02+width*0.2+width*0.03+width*0.5+width*0.02), y=height*0.04)
active.place(x=(width/2), y=height*0.04)
player.place(x=0,y=height/2)


master.mainloop()