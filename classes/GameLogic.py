import tkinter as tk
from misc_functions import read_file

class GameLogic():
    def __init__(self, user, networking) -> None:
        self.user = user
        self.networking = networking
        pass

    def rock_paper_scissors(self, frame):
        def send(data):
            global choice
            choice = data
            chosen_label.configure(text=f"Your choice: {choice}")
            chosen_label.grid(column=0, row=0)
            self.networking.send(f"{self.user.username}: {turn},{choice}")
            get_opponent_choice(f"{self.networking.opponent}: {turn}")

        
        def get_opponent_choice(data):
            while True:
                try:
                    file_data = read_file("data/received_data.txt", data)
                except Exception as e:
                    print(e)
                if file_data:
                    length = len(self.networking.opponent)+1
                    opponent_turn, opponent_choice = file_data[length:].strip(',')
                    opponent_label.configure(text=f"{self.networking.opponent} chose {opponent_choice}")
                    chosen_label.grid(column=0, row=0)
                    if opponent_turn == turn:
                        if opponent_choice == choice:
                            print(f"you both chose {choice}")
                        elif opponent_choice == "rock" and choice == "paper":
                            print("you win")
                        elif opponent_choice == "paper" and choice == "scissors":
                            print("you win")
                        elif opponent_choice == "scissors" and choice == "rock":
                            print("you win")
                        elif opponent_choice == "paper" and choice == "rock":
                            print("you lose")
                        elif opponent_choice == "scissors" and choice == "paper":
                            print("you lose")
                        elif opponent_choice == "rock" and choice == "scissors":
                            print("you lose")
        
        turn = 1

        rps_frame = tk.Frame(frame)

        chosen_label = tk.Label(rps_frame)
        chosen_label.grid(column=0, row=0)

        opponent_label = tk.Label(rps_frame)
        opponent_label.grid(column=1, row=0)

        rock = tk.Button(rps_frame, text="rock", command = lambda: send("rock"))
        paper = tk.Button(rps_frame, text="paper", command = lambda: send("paper"))
        scissors = tk.Button(rps_frame, text="scissors", command = lambda: send("scissors"))

        rock.grid(column=0, row=1)
        paper.grid(column=1, row=1)
        scissors.grid(column=2, row=0)

        rps_frame.grid(column=0,row=0)
        #frame.grid(column=0,row=0)
