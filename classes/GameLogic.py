from os import stat
import tkinter as tk
from misc_functions import read_file, read_from_received, destroy_widgets
from threading import Thread
from classes.config import Config


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


    def rock_paper_scissors(self, frame, turn):
        """rock_paper_scissors: is called from maingameloop. prompts user to choose one of three buttons. sends data to opponent. waits for opponents data. makes comparison of data."""
        def send(event=None, data=""):
            self.rps_choice = str(data)
            self.rps_choice = self.rps_choice.strip()
            chosen_label.configure(text=f"Your choice: {data}")
            chosen_label.grid(column=0, row=1)
            self.networking.send(f"{self.user.username}: {turn},{data}")
            rock.configure(state=tk.DISABLED)
            paper.configure(state=tk.DISABLED)
            scissors.configure(state=tk.DISABLED)
            #rock.grid(column=0, row=2)
            #paper.grid(column=1, row=2)
            #scissors.grid(column=2, row=2)

        rps_frame = tk.Frame(frame)

        chosen_label = tk.Label(rps_frame)
        chosen_label.grid(column=0, row=1)

        opponent_label = tk.Label(rps_frame)
        opponent_label.grid(column=1, row=1)

        rock = tk.Button(rps_frame, text="rock", command = lambda: send("rock"))
        paper = tk.Button(rps_frame, text="paper", command = lambda: send("paper"))
        scissors = tk.Button(rps_frame, text="scissors", command = lambda: send("scissors"))

        Config.master.bind('1', lambda event: send(event, "rock"))
        Config.master.bind('2', lambda event: send(event, "paper"))
        Config.master.bind('3', lambda event: send(event, "scissors"))

        rock.grid(column=0, row=2)
        paper.grid(column=1, row=2)
        scissors.grid(column=2, row=2)

        rps_frame.grid(column=0,row=0)
        
        infile= f"{self.networking.opponent}: {turn}"
        file_data = read_from_received(infile)

        length = len(self.networking.opponent)+1
        opponent_turn, opponent_choice = file_data[length:].split(',')
        opponent_turn = int(opponent_turn)
        opponent_choice = str(opponent_choice)
        opponent_choice = opponent_choice.strip()
        
        #opponent_label.configure(text=f"{self.networking.opponent} chose {opponent_choice}")
        #opponent_label.grid(column=1, row=1)

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