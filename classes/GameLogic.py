import tkinter as tk
from misc_functions import read_file
from threading import Thread

class GameLogic():
    def __init__(self, user, networking) -> None:
        self.user = user
        self.networking = networking
        self.rps_choice = ""

    def rock_paper_scissors(self, frame, turn):
        """rock_paper_scissors: is called from maingameloop. prompts user to choose one of three buttons. sends data to opponent. waits for opponents data. makes comparison of data."""
        def send(data):
            self.rps_choice = str(data)
            self.rps_choice = self.rps_choice.strip()
            chosen_label.configure(text=f"Your choice: {data}")
            chosen_label.grid(column=0, row=1)
            self.networking.send(f"{self.user.username}: {turn},{data}")

            
        def destroy_widgets():
            for widget in rps_frame.winfo_children():
                widget.destroy()
            rps_frame.destroy()

        rps_frame = tk.Frame(frame)

        chosen_label = tk.Label(rps_frame)
        chosen_label.grid(column=0, row=1)

        opponent_label = tk.Label(rps_frame)
        opponent_label.grid(column=1, row=1)

        rock = tk.Button(rps_frame, text="rock", command = lambda: send("rock"))
        paper = tk.Button(rps_frame, text="paper", command = lambda: send("paper"))
        scissors = tk.Button(rps_frame, text="scissors", command = lambda: send("scissors"))

        rock.grid(column=0, row=2)
        paper.grid(column=1, row=2)
        scissors.grid(column=2, row=2)

        rps_frame.grid(column=0,row=0)
        
        infile= f"{self.networking.opponent}: {turn}"
        
        received = False
        while not received:
            #tries to read received_data.txt for opponents turn
            try:
                file_data = read_file("data/received_data.txt", infile)
            except Exception as e:
                continue
                #print("data not received yet", e)

            if file_data:
                received = True

        length = len(self.networking.opponent)+1
        opponent_turn, opponent_choice = file_data[length:].split(',')
        opponent_choice = str(opponent_choice)
        opponent_choice = opponent_choice.strip()
        
        opponent_label.configure(text=f"{self.networking.opponent} chose {opponent_choice}")
        opponent_label.grid(column=1, row=1)

        wins = False
        winner = ""

        while True:
            if opponent_turn == turn:
                try:
                    if (opponent_choice == self.rps_choice):
                        destroy_widgets()
                        tk.messagebox.showinfo("Match", f"You both choose {self.rps_choice}. Try again...")
                        break
                    elif (opponent_choice == "rock") and (self.rps_choice == "paper"):
                        tk.messagebox.showinfo("You Won", f"Rock beats Paper. You get to decide heads or tails.")
                        destroy_widgets()
                        winner = self.user.username
                        break
                    elif (opponent_choice == "paper") and (self.rps_choice == "scissors"):
                        tk.messagebox.showinfo("You Won", f"Scissors beats Paper. You get to decide heads or tails.")
                        destroy_widgets()
                        winner = self.user.username
                        break
                    elif (opponent_choice == "scissors") and (self.rps_choice == "rock"):
                        tk.messagebox.showinfo("You Won", f"Rock beats Scissors. You get to decide heads or tails.")
                        destroy_widgets()
                        winner = self.user.username
                        break
                    elif (opponent_choice == "paper") and (self.rps_choice == "rock"):
                        tk.messagebox.showinfo("You Lost", f"Rock beats Paper. {self.networking.opponent.capitalize()} gets to decide heads or tails.")
                        destroy_widgets()
                        winner = self.networking.opponent
                        break
                    elif (opponent_choice == "scissors") and (self.rps_choice == "paper"):
                        tk.messagebox.showinfo("You Lost", f"Scissors beats Paper. {self.networking.opponent.capitalize()} gets to decide heads or tails.")
                        destroy_widgets()
                        winner = self.networking.opponent
                        break
                    elif (opponent_choice == "rock") and (self.rps_choice == "scissors"):
                        tk.messagebox.showinfo("You Lost", f"Rock beats Scissors. {self.networking.opponent.capitalize()} gets to decide heads or tails.")
                        destroy_widgets()
                        winner = self.networking.opponent
                        break
                    else:
                        print(f"opponent choice: {hash(opponent_choice)}. my choice: {hash(self.rps_choice)}")
                        print(self.rps_choice is opponent_choice)
                except Exception as e:
                    print(e)
        
        return winner
