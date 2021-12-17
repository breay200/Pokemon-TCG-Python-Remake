from classes.config import Config
from pathlib import PurePosixPath
import tkinter as tk
from tkinter.constants import YES
from tkinter.ttk import *
from PIL import Image, ImageTk
from tkinter import messagebox

class Gameboard():
    def __init__(self):
        self.width = Config.master.winfo_screenwidth() * 0.8
        self.height = Config.master.winfo_screenheight() * 0.8

        self.opponent = tk.Frame(Config.master, width=self.width, height=self.height/2, bg="red")

        self.deck_img = Image.open("images/pokemon_back.png").resize((int(self.width*0.08), int(self.height*0.2)))
        self.deck_img = ImageTk.PhotoImage(self.deck_img)

        self.discard_img = Image.open("images/card_space.png").resize((int(self.width*0.08), int(self.height*0.2)))
        self.discard_img = ImageTk.PhotoImage(self.discard_img)
        
        self.player_frame = tk.Frame(Config.master, width=self.width, height=self.height/2, bg="blue")
        self.prize_frame = tk.Frame(self.player_frame, width=self.width*0.15, height=self.height*0.5)
        self.active_frame = tk.Frame(self.player_frame, width=int(self.width*0.08), height=int(self.height*0.2))
        self.bench_frame = tk.Frame(self.player_frame, width=self.width*0.5, height=self.height*0.25, highlightthickness=5, highlightbackground="black")
        #self.hand_frame = tk.Frame(Config.master, width=(self.width*0.75), height=(self.height/4), bg="black")
        
        self.discard_btn = tk.Button(self.player_frame, image=self.discard_img, width=(self.width*0.08), height=(self.height*0.2), bg="blue", borderwidth=0, highlightthickness=0)
        self.deck_btn = tk.Button(self.player_frame, image=self.deck_img, width=self.width*0.08, height=self.height*0.2, bg="blue", borderwidth=0, highlightthickness=0, command=self.add_to_bench)
        #self.deck_btn.bind("<Enter>", func=lambda x=None:self.hover_action())
        self.deck_btn.bind("<Enter>", func=lambda e: self.hover_action())
        self.deck_btn.bind("<Leave>", func=lambda e: self.on_hover_leave())

        w = int(self.width*0.015)
        h = int(self.height*0.005)

        #self.view_hand_btn = tk.Button(self.player_frame, width=w, height=h, text="View Hand", command=self.show_hand)

        self.prize_img_width = int(self.width*0.075)
        self.prize_img_height = int(self.height*0.16666)
        self.prize_img = Image.open("images/pokemon_back.png").resize((self.prize_img_width, self.prize_img_height))
        self.prize_img = ImageTk.PhotoImage(self.prize_img)

        self.btn_widget_list = []
        self.prize_widget_list = []

        self.load_prize()

    def place(self):
        self.opponent.place(x=0,y=0)
        #self.view_hand_btn.place(x=(self.width*0.87), y=(self.height*0.225))
        self.prize_frame.place(x=(self.width*0.02), y=0)
        self.bench_frame.place(x=(self.width*0.02+self.width*0.2+self.width*0.03), y=(self.height*0.225))
        self.discard_btn.place(x=(self.width*0.02+self.width*0.2+self.width*0.03+self.width*0.5+self.width*0.02), y=(self.height*0.3))
        self.deck_btn.place(x=(self.width*0.02+self.width*0.2+self.width*0.03+self.width*0.5+self.width*0.02), y=(self.height*0.04))
        self.player_frame.place(x=0,y=(self.height/2))

    def hover_action(self):
        print("hello")
        # print("on enter btn")
        self.hover_frame = tk.Frame(Config.master, width=int(self.width*0.5), height=int(self.height*0.5), bg="yellow")
        self.hover_frame.place(x=0, y=0)
        self.player_frame.update()
        # return
    
    def on_hover_leave(self):
        print("goodbye")
        self.hover_frame.destroy()
        self.player_frame.update()
    # def show_hand(self):
    #     if not self.hand_frame.winfo_ismapped():
    #         self.hand_frame.place(x=(self.width*0.25), y=(self.height*0.2))
    
    def make_active(self):
        self.active_btn = tk.Button(self.active_frame, image=self.deck_img, width=(self.width*0.08), height=(self.height*0.2), borderwidth=0, highlightthickness=0)
        self.active_btn.place(x=0, y=0)


    def add_to_bench(self):
        if len(self.btn_widget_list) < 5:
            button = tk.Button(self.bench_frame, image=self.deck_img, width=(self.width*0.08), height=(self.height*0.2), borderwidth=0, highlightthickness=0, command=self.make_active)
            self.btn_widget_list.append(button)
            x_coordinates = 0
            for x in self.btn_widget_list:
                if self.btn_widget_list.index(x) == 0:
                    pass
                else:
                    x_coordinates += (self.width*0.015)+(self.width*0.08)
                x.place(x=x_coordinates, y=0)
            self.bench_frame.place(x=(self.width*0.02+self.width*0.2+self.width*0.03), y=self.height*0.225)
        else:
            tk.messagebox.showinfo("error", "you cannot add more than 5 cards to the bench")


    def load_prize(self):
        for x in range(6):
            self.prize_widget_list.append(tk.Button(self.prize_frame, image=self.prize_img, width=self.prize_img_width, height=self.prize_img_height, borderwidth=0, highlightthickness=0))
        
        for x in self.prize_widget_list:
            if self.prize_widget_list.index(x) in [0,2,4]:
                x_coordinates = 0
            elif self.prize_widget_list.index(x) in [1,3,5]:
                x_coordinates  = self.prize_img_width
            
            if self.prize_widget_list.index(x) in [0,1]:
                y_coordinates = 0
            elif self.prize_widget_list.index(x) in [2,3]:
                y_coordinates = self.prize_img_height
            elif self.prize_widget_list.index(x) in [4,5]:
                y_coordinates = self.prize_img_height*2
            
            x.place(x=x_coordinates, y=y_coordinates)