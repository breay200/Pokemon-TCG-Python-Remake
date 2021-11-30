from pathlib import PurePosixPath
import tkinter as tk
from tkinter.constants import YES
from tkinter.ttk import *
from PIL import Image, ImageTk

def add_to_bench():
    btn_widget_list.append(tk.Button(bench, image=deck_img, width=width*0.08, height=height*0.2, borderwidth=0, highlightthickness=0))
    x_coordinates = 0
    for x in btn_widget_list:
        if btn_widget_list.index(x) == 0:
            pass
        else:
            x_coordinates += (width*0.015)+(width*0.08)
        x.place(x=x_coordinates, y=0)
    bench.place(x=(width*0.02+width*0.2+width*0.03), y=height*0.225)

def load_prize():
    for x in range(6):
        prize_widget_list.append(tk.Button(prize, image=deck_img, width=width*0.08, height=height*0.2, borderwidth=0, highlightthickness=0))
    
    for x in prize_widget_list:
        if prize_widget_list.index(x) in [0, 2, 4]:
            x_coordinates = 0
        elif prize_widget_list.index(x) in [1,3,5]:
            x_coordinates  = (width*0.08)
        
        if prize_widget_list.index(x) in [0, 1]:
            y_coordinates = 0
        elif prize_widget_list.index(x) in [2, 3]:
            y_coordinates = height*0.2
        elif prize_widget_list.index(x) in [4, 5]:
            y_coordinates = height*0.4
        
        x.place(x=x_coordinates, y=y_coordinates)
            

master = tk.Tk()
#master.geometry("1920x1080")
width = master.winfo_screenwidth() * 0.8
height = master.winfo_screenheight() * 0.8
master.geometry(f"{int(width)}x{int(height)}")
master.title("TCG REMAKE")

opponent = tk.Frame(master, width=width, height=height/2, bg="red")
opponent.place(x=0,y=0)

deck_img = Image.open("images/pokemon_back.png").resize((int(width*0.08), int(height*0.2)))
deck_img = ImageTk.PhotoImage(deck_img)

discard_img = Image.open("images/card_space.png").resize((int(width*0.08), int(height*0.2)))
discard_img = ImageTk.PhotoImage(discard_img)

player = tk.Frame(master, width=width, height=height/2, bg="blue")
prize = tk.Frame(player, width=width*0.16, height=height*0.45, highlightthickness=5, highlightbackground="black")
bench = tk.Frame(player, width=width*0.5, height=height*0.25, highlightthickness=5, highlightbackground="black")
discard = tk.Button(player, image=discard_img, width=width*0.08, height=height*0.2, bg="blue", borderwidth=0, highlightthickness=0)
deck = tk.Button(player, image=deck_img, width=width*0.08, height=height*0.2, bg="blue", borderwidth=0, highlightthickness=0, command=add_to_bench)
active = tk.Frame(player, width=width*0.1, height=height*0.2, bg="white")

btn_widget_list = []
prize_widget_list = []

load_prize()
"""
for x in range(5):
    btn_widget_list.append(tk.Button(bench, image=deck_img, width=width*0.08, height=height*0.2, borderwidth=0, highlightthickness=0))

x_coordinates = 0
for x in btn_widget_list:
    if btn_widget_list.index(x) == 0:
        pass
    else:
        x_coordinates += (width*0.015)+(width*0.08)
    x.place(x=x_coordinates, y=0)
"""

prize.place(x=width*0.02, y=0)
bench.place(x=(width*0.02+width*0.2+width*0.03), y=height*0.225)
discard.place(x=(width*0.02+width*0.2+width*0.03+width*0.5+width*0.02), y=height*0.3)
deck.place(x=(width*0.02+width*0.2+width*0.03+width*0.5+width*0.02), y=height*0.04)
active.place(x=(width/2), y=height*0.04)
player.place(x=0,y=height/2)


master.mainloop()