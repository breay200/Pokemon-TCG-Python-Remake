from threading import Condition
from classes.config import Config
from pathlib import PurePosixPath
import tkinter as tk
from tkinter.constants import YES
from tkinter.ttk import *
from PIL import Image, ImageTk
from tkinter import messagebox
import re
from tkinter import font

class Gameboard():
    def __init__(self, maingameloop):
        self.maingameloop = maingameloop
        self.width = Config.master.winfo_screenwidth() * 0.75
        self.height = Config.master.winfo_screenheight() * 0.75

        self.entire_screen_frame = tk.Frame(Config.master, width=self.width, height=self.height)

        self.opponent = tk.Frame(self.entire_screen_frame, width=self.width, height=self.height/2, bg="red")

        self.deck_img = Image.open("images/pokemon_back.png").resize((int(self.width*0.08), int(self.height*0.2)))
        self.deck_img = ImageTk.PhotoImage(self.deck_img)

        self.discard_img = Image.open("images/card_space.png").resize((int(self.width*0.08), int(self.height*0.2)))
        self.discard_img = ImageTk.PhotoImage(self.discard_img)
        
        self.player_frame = tk.Frame(self.entire_screen_frame, width=self.width, height=self.height/2, bg="blue")
        self.prize_frame = tk.Frame(self.player_frame, width=int(self.width*0.15), height=int(self.height*0.5))
        self.active_frame = tk.Frame(self.player_frame, width=int(self.width*0.08), height=int(self.height*0.2))
        self.bench_frame = tk.Frame(self.player_frame, width=int(self.width*0.5), height=int(self.height*0.25), highlightthickness=5, highlightbackground="black")
        
        self.discard_btn = tk.Button(self.player_frame, image=self.discard_img, width=(self.width*0.08), height=(self.height*0.2), bg="blue", borderwidth=0, highlightthickness=0)
        self.deck_btn = tk.Button(self.player_frame, image=self.deck_img, width=self.width*0.08, height=self.height*0.2, bg="blue", borderwidth=0, highlightthickness=0, command=self.add_to_bench)

        w = int(self.width*0.015)
        h = int(self.height*0.005)

        self.hand_frame = None
        self.expanded_card = None
        self.expanded_image = None
        self.options_frame = None

        self.hand_btn = tk.Button(self.player_frame, width=w, height=h, text="View Hand", command=self.show_hand)

        self.prize_img_width = int(self.width*0.075)
        self.prize_img_height = int(self.height*0.16666)
        self.prize_img = Image.open("images/pokemon_back.png").resize((self.prize_img_width, self.prize_img_height))
        self.prize_img = ImageTk.PhotoImage(self.prize_img)
        
        self.card_images = {}
        self.hand_widget_list = []
        self.bench_widget_list = []
        self.prize_widget_list = []
        self.bench = [
            [1, []], [2, []], [3, []], [4, []], [5, []]
        ]
        self.load_prize()
        self.place()
        Config.master.bind("<Escape>", lambda event: self.options_menu(event))

    def place(self):
        self.opponent.place(x=0,y=0)
        self.hand_btn.place(x=(self.width*0.87), y=(self.height*0.225))
        self.prize_frame.place(x=(self.width*0.02), y=0)
        self.bench_frame.place(x=(self.width*0.02+self.width*0.2+self.width*0.03), y=(self.height*0.225))
        self.discard_btn.place(x=(self.width*0.02+self.width*0.2+self.width*0.03+self.width*0.5+self.width*0.02), y=(self.height*0.3))
        self.deck_btn.place(x=(self.width*0.02+self.width*0.2+self.width*0.03+self.width*0.5+self.width*0.02), y=(self.height*0.04))
        self.player_frame.place(x=0,y=(self.height/2))
        self.entire_screen_frame.place(x=0,y=0)

    def options_menu(self, event=None):
        if not self.options_frame:
            options_width = int(self.width*0.4)
            options_height = int(self.height*0.6)
            self.options_frame = tk.Frame(self.entire_screen_frame, width=options_width, height=options_height, bg="white")
            self.btn_font = font.Font(family="Courier", size=(0 - int(self.height*0.04)), weight="bold")
            btn_width = int(self.width*0.2)
            quit_btn = tk.Button(self.options_frame, command=lambda:quit(), text="Quit", bg="red", fg="white", font=self.btn_font)
            btn_coordinates = [(options_width/2)-(btn_width/2), (options_height*0.2)]
            quit_btn.place(x=btn_coordinates[0], y=btn_coordinates[1], width=btn_width)
            self.options_frame.place(x=(self.width/2)-(options_width/2),y=(self.height/2)-(options_height/2))
        else:
            for widget in self.options_frame.winfo_children():
                widget.destroy()
            self.options_frame.destroy()
            self.options_frame = None

    def not_pokemon_card(self):
        tk.messagebox.showinfo("Error", "You can only add Pokemon cards to the bench")

    def show_hand(self):
        self.widgets_cards = {}
        self.coordinate_card_repository = {}

        if not self.hand_frame:
            self.hand_frame = tk.Frame(self.entire_screen_frame, highlightthickness=5, highlightbackground="black", width=int(self.width*0.75), height=int(self.height*0.25))    
            for card in self.maingameloop.hand.current_hand:
                location = card.local_img
                card_img = Image.open(location).resize(((int(self.width*0.08), int(self.height*0.2))))
                card_img = ImageTk.PhotoImage(card_img)
                self.card_images[card] = card_img
                button = tk.Button(self.hand_frame, image=self.card_images[card], width=int((self.width*0.08)), height=int((self.height*0.2)), borderwidth=0, highlightthickness=0)
                self.widgets_cards[button] = card
            
            x_coordinate = 0

            for button, card in self.widgets_cards.items():
                button.bind("<Enter>", lambda event: self.hand_hover_enter(event, Config.master.winfo_pointerx(), self.hand_frame.winfo_rootx()))
                button.bind("<Leave>", lambda event: self.hand_hover_leave(event))
                if card.supertype == "Pokémon":
                    button["command"] = lambda: self.add_to_bench(Config.master.winfo_pointerx(), self.hand_frame.winfo_rootx())
                elif card.supertype in ["Trainer", "Energy"]:
                    button["command"] = self.not_pokemon_card
                if list(self.widgets_cards).index(button) == 0:
                    pass
                else:
                    x_coordinate += (self.width*0.015)+(self.width*0.08)
                button.place(x=x_coordinate, y=0)
    
            self.hand_frame.place(x=(self.width*0.125), y=(self.height*0.225))
            self.hand_frame.update()
            self.entire_screen_frame.update()

            for button, card in self.widgets_cards.items():
                width, _, x, _ = re.split(r'[x+]', button.winfo_geometry())
                key = [int(x),int(x)+int(width)]
                key = str(key)
                self.coordinate_card_repository[key] = card
        
        else:
            for button in self.hand_frame.winfo_children():
                button.destroy()
            self.hand_frame.destroy()
            self.hand_frame = None
            self.entire_screen_frame.update()
    
    def hand_hover_enter(self, event=None, widget_x=0, root_x=0):
        x_coordinate  = widget_x - root_x
        for key, value in self.coordinate_card_repository.items():
            try:
                coords = key
                coords = coords.replace('[','').replace(']','')
                min_x, max_x = coords.split(",")
                min_x = int(min_x)
                max_x = int(max_x)
            except Exception as error:
                print(error)
            # print(x_coordinate, min_x, max_x)
            if min_x <= x_coordinate <= max_x:
                self.hover_card = value
                break
        location = self.hover_card.local_img
        expanded_card_width = int(self.width*0.25)
        expanded_card_height = int(self.height*0.75)
        self.expanded_card = tk.Frame(self.entire_screen_frame, width=expanded_card_width, height=expanded_card_height, bg="white", highlightthickness=3, highlightbackground="black")
        self.expanded_image = Image.open(location).resize((int(expanded_card_width*0.75), int(expanded_card_height*0.75)))
        self.expanded_image = ImageTk.PhotoImage(self.expanded_image)
        label = tk.Label(self.expanded_card, image=self.expanded_image, width=int(expanded_card_width*0.75), height=int(expanded_card_height*0.75), borderwidth=0, highlightthickness=0)
        label.place(x=int(expanded_card_width*0.125), y=int(expanded_card_height*0.125))
        self.expanded_card.place(x=int(self.width*0.375), y=int(self.height*0.5))
        self.entire_screen_frame.update()

    def hand_hover_leave(self, event=None):
        if self.expanded_card:
            self.expanded_card.destroy()
            self.expanded_image = None

    def hover_action(self):
        print("hello")
        # print("on enter btn")
        self.hover_frame = tk.Frame(Config.master, width=int(self.width*0.5), height=int(self.height*0.75), bg="white")
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


    def add_to_bench(self, widget_x=0, root_x=0):
        card = object()
        x_coordinate  = widget_x - root_x
        for key, value in self.coordinate_card_repository.items():
            try:
                coords = key
                coords = coords.replace('[','').replace(']','')
                min_x, max_x = coords.split(",")
                min_x = int(min_x)
                max_x = int(max_x)
            except Exception as error:
                print(error)
            # print(x_coordinate, min_x, max_x)
            if min_x <= x_coordinate <= max_x:
                card = value
                break

        if self.maingameloop.bench.on_bench < 5:
            self.maingameloop.hand.current_hand.remove(card)
            self.hand_hover_leave()
            self.show_hand()
            benched_pokemon = self.maingameloop.bench.add_to_bench(card)
            button = tk.Button(self.bench_frame, image=self.card_images[card], width=(self.width*0.08), height=(self.height*0.2), borderwidth=0, highlightthickness=0, command=self.make_active)
            position = 0
            for pokemon in self.bench:
                if not pokemon[1]:
                    pokemon[1] = [benched_pokemon, button]
                    position = pokemon[0]
                    break
            x_coordinate = (self.width*0.015)+(self.width*0.08)
            if position == 1:
                self.bench[0][1][1].place(x=0, y=0)
            elif position == 2:
                self.bench[1][1][1].place(x=x_coordinate, y=0)
            elif position == 3:
                self.bench[2][1][1].place(x=x_coordinate*2, y=0)
            elif position == 4:
                self.bench[3][1][1].place(x=x_coordinate*3, y=0)
            elif position == 5:
                self.bench[4][1][1].place(x=x_coordinate*4, y=0)
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