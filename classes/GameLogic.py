from os import stat
import tkinter as tk
from misc_functions import read_file, read_from_received, destroy_widgets
from threading import Thread
from classes.config import Config
import re
from PIL import Image, ImageTk
from tkinter import font


class GameLogic():
    def __init__(self, user, networking) -> None:
        self.user = user
        self.networking = networking
        self.rps_choice = ""
    
    def first_or_second(self, frame, turn, winner):
        def send(data):
            self.networking.send(f"{self.user.username}: {turn},{data}")
            destroy_widgets(hot_frame)
            tk.messagebox.showinfo("Turn Order", f"You chose to take the {data} turn.")
            return data

        if winner == self.user.username:
            hot_frame = tk.Frame(frame)
            label = tk.Label(hot_frame, text="Choose to take the first or second turn.")
            first_btn = tk.Button(hot_frame, text="First", command= lambda: send("first"))
            second_btn = tk.Button(hot_frame, text="Second", command= lambda: send("second"))
            label.grid(column=0, row=0)
            first_btn.grid(column=0, row=1)
            second_btn.grid(column=1, row=1)
            hot_frame.grid(column=0, row=0)
        else:
            infile= f"{self.networking.opponent}: {turn}"
            file_data = read_from_received(infile)
            length = len(self.networking.opponent)+1
            opponent_turn, opponent_choice = file_data[length:].split(',')
            opponent_turn = int(opponent_turn)
            opponent_choice = str(opponent_choice).strip()
            if opponent_choice == "first":
                tk.messagebox.showinfo("Play Order", f"{self.networking.opponent.capitalize()} chose the first turn.\nYou will go second.")
                return "second"
            else:
                tk.messagebox.showinfo("Play Order", f"{self.networking.opponent.capitalize()} chose the second turn.\nYou will go first.")
                return "first"


    def rock_paper_scissors(self, turn):
        """rock_paper_scissors: is called from maingameloop. prompts user to choose one of three buttons. sends data to opponent. waits for opponents data. makes comparison of data."""
        def send(event=None, data=""):
            self.rps_choice = str(data)
            self.rps_choice = self.rps_choice.strip()
            self.networking.send(f"{self.user.username}: {turn},{data}")
            rock.configure(state=tk.DISABLED)
            paper.configure(state=tk.DISABLED)
            scissors.configure(state=tk.DISABLED)

        width, height, _, _ = re.split(r'[x+]', Config.master.winfo_geometry())
        rps_width = int(width)
        rps_height = int(height)
        rps_frame = tk.Frame(Config.master, width=rps_width, height=rps_height)

        font_height = 0 - int(rps_height*0.04)
        txt_label_font = font.Font(family="Courier", size=font_height, weight="bold", underline=1)
        text_label = tk.Label(rps_frame, text="Choose Rock, Paper, or Scissors", font=txt_label_font)
        text_label.place(x=0, y=0)
        
        btn_dimensions = (int(rps_width*0.05), int(rps_height*0.1))
        # btn_width = int(rps_width*0.05)
        # btn_height = int(rps_height*0.1)

        self.rock_img = Image.open("images/rock.png").resize(btn_dimensions)
        self.rock_img = ImageTk.PhotoImage(self.rock_img)

        self.paper_img =  Image.open("images/paper.png").resize(btn_dimensions)
        self.paper_img = ImageTk.PhotoImage(self.paper_img)

        self.scissors_img =  Image.open("images/scissors.png").resize(btn_dimensions)
        self.scissors_img = ImageTk.PhotoImage(self.scissors_img)

        rock = tk.Button(rps_frame, command = lambda: send("rock"), image=self.rock_img)
        paper = tk.Button(rps_frame, command = lambda: send("paper"), image=self.paper_img)
        scissors = tk.Button(rps_frame, command = lambda: send("scissors"), image=self.scissors_img)

        Config.master.bind('1', lambda event: send(event, "rock"))
        Config.master.bind('2', lambda event: send(event, "paper"))
        Config.master.bind('3', lambda event: send(event, "scissors"))

        rock.place(x=(rps_width/2), y=rps_height*0.1, width=btn_dimensions[0], height=btn_dimensions[1])
        paper.place(x=(rps_width/2), y=rps_height*0.3, width=btn_dimensions[0], height=btn_dimensions[1])
        scissors.place(x=(rps_width/2), y=rps_height*0.5, width=btn_dimensions[0], height=btn_dimensions[1])

        rps_frame.place(x=0, y=0)
        
        infile= f"{self.networking.opponent}: {turn}"
        file_data = read_from_received(infile)

        length = len(self.networking.opponent)+1
        opponent_turn, opponent_choice = file_data[length:].split(',')
        opponent_turn = int(opponent_turn)
        opponent_choice = str(opponent_choice)
        opponent_choice = opponent_choice.strip()
        
        winner = ""

        while True:
            if opponent_turn == turn:
                try:
                    if opponent_choice and self.rps_choice:
                        destroy_widgets(rps_frame)
                        if (opponent_choice == self.rps_choice):
                            tk.messagebox.showinfo("Match", f"You both choose {self.rps_choice}. Try again...")
                            break
                        elif (opponent_choice == "rock") and (self.rps_choice == "paper"):
                            tk.messagebox.showinfo("You Won", f"Rock beats Paper. You get to decide heads or tails.")
                            winner = self.user.username
                            break
                        elif (opponent_choice == "paper") and (self.rps_choice == "scissors"):
                            tk.messagebox.showinfo("You Won", f"Scissors beats Paper. You get to decide heads or tails.")
                            winner = self.user.username
                            break
                        elif (opponent_choice == "scissors") and (self.rps_choice == "rock"):
                            tk.messagebox.showinfo("You Won", f"Rock beats Scissors. You get to decide heads or tails.")
                            winner = self.user.username
                            break
                        elif (opponent_choice == "paper") and (self.rps_choice == "rock"):
                            tk.messagebox.showinfo("You Lost", f"Rock beats Paper. {self.networking.opponent.capitalize()} gets to decide heads or tails.")
                            winner = self.networking.opponent
                            break
                        elif (opponent_choice == "scissors") and (self.rps_choice == "paper"):
                            tk.messagebox.showinfo("You Lost", f"Scissors beats Paper. {self.networking.opponent.capitalize()} gets to decide heads or tails.")
                            winner = self.networking.opponent
                            break
                        elif (opponent_choice == "rock") and (self.rps_choice == "scissors"):
                            tk.messagebox.showinfo("You Lost", f"Rock beats Scissors. {self.networking.opponent.capitalize()} gets to decide heads or tails.")
                            winner = self.networking.opponent
                            break
                except Exception as e:
                        print(e)
        return winner