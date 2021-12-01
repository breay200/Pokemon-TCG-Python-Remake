from pathlib import PurePosixPath
import tkinter as tk
from tkinter.constants import YES
from tkinter.ttk import *
from PIL import Image, ImageTk
from tkinter import messagebox


def make_active():
    active_card = tk.Button(active, image=deck_img, width=width*0.08, height=height*0.2, bg="blue", borderwidth=0, highlightthickness=0)
    active_card.place(x=0, y=0)
    active.place(x=(width*0.46), y=height*0.015)


def add_to_bench():
    if len(btn_widget_list) < 5:
        button = tk.Button(bench, image=deck_img, width=width*0.08, height=height*0.2, borderwidth=0, highlightthickness=0, command=lambda: make_active())
        btn_widget_list.append(button)
        x_coordinates = 0
        for x in btn_widget_list:
            if btn_widget_list.index(x) == 0:
                pass
            else:
                x_coordinates += (width*0.015)+(width*0.08)
            x.place(x=x_coordinates, y=0)
        bench.place(x=(width*0.02+width*0.2+width*0.03), y=height*0.225)
    else:
        tk.messagebox.showinfo("error", "you cannot add more than 5 cards to the bench")


def load_prize():
    for x in range(6):
        prize_widget_list.append(tk.Button(prize, image=prize_img, width=prize_img_width, height=prize_img_height, borderwidth=0, highlightthickness=0))
    
    for x in prize_widget_list:
        if prize_widget_list.index(x) in [0,2,4]:
            x_coordinates = 0
        elif prize_widget_list.index(x) in [1,3,5]:
            x_coordinates  = prize_img_width
        
        if prize_widget_list.index(x) in [0,1]:
            y_coordinates = 0
        elif prize_widget_list.index(x) in [2,3]:
            y_coordinates = prize_img_height
        elif prize_widget_list.index(x) in [4,5]:
            y_coordinates = prize_img_height*2
        
        x.place(x=x_coordinates, y=y_coordinates)
            

master = tk.Tk()
#master.geometry("1920x1080")
width = master.winfo_screenwidth() * 0.5
height = master.winfo_screenheight() * 0.5
master.geometry(f"{int(width)}x{int(height)}")
master.title("TCG REMAKE")

opponent = tk.Frame(master, width=width, height=height/2, bg="red")
opponent.place(x=0,y=0)

deck_img = Image.open("images/pokemon_back.png").resize((int(width*0.08), int(height*0.2)))
deck_img = ImageTk.PhotoImage(deck_img)

discard_img = Image.open("images/card_space.png").resize((int(width*0.08), int(height*0.2)))
discard_img = ImageTk.PhotoImage(discard_img)

player = tk.Frame(master, width=width, height=height/2, bg="blue")
prize = tk.Frame(player, width=width*0.15, height=height*0.5)
#print(width*0.16, height*0.45)
bench = tk.Frame(player, width=width*0.5, height=height*0.25, highlightthickness=5, highlightbackground="black")
discard = tk.Button(player, image=discard_img, width=width*0.08, height=height*0.2, bg="blue", borderwidth=0, highlightthickness=0)
deck = tk.Button(player, image=deck_img, width=width*0.08, height=height*0.2, bg="blue", borderwidth=0, highlightthickness=0, command=add_to_bench)
active = tk.Frame(player, width=int(width*0.08), height=int(height*0.2), bg="white")
#hand = tk.Frame(master)
w = int(width*0.015)
h = int(height*0.005)
view_hand = tk.Button(player, width=w, height=h, text="View Hand")

prize_img_width = int(width*0.075)
prize_img_height = int(height*0.16666)
prize_img = Image.open("images/pokemon_back.png").resize((prize_img_width, prize_img_height))
prize_img = ImageTk.PhotoImage(prize_img)

btn_widget_list = []
prize_widget_list = []

load_prize()

view_hand.place(x=(width*0.87), y=(height*0.225))
prize.place(x=width*0.02, y=0)
bench.place(x=(width*0.02+width*0.2+width*0.03), y=height*0.225)
discard.place(x=(width*0.02+width*0.2+width*0.03+width*0.5+width*0.02), y=height*0.3)
deck.place(x=(width*0.02+width*0.2+width*0.03+width*0.5+width*0.02), y=height*0.04)
active.place(x=(width*0.46), y=height*0.015)
player.place(x=0,y=height/2)


master.mainloop()