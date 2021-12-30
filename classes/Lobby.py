from tkinter.constants import DISABLED, NE, NORMAL
from classes.config import Config
from classes.Networking import Networking
from classes.MainGameLoop import MainGameLoop
from tkinter import messagebox
import tkinter as tk
from threading import Thread

class Lobby():
    def __init__(self, user):
        self.user = user
        self.width = Config.master.winfo_width()
        self.height = Config.master.winfo_height()
        self.networking = Networking(user.username)
        self.lobby_frame = tk.Frame(Config.master, width=self.width, height=self.height, bg="white")
        
        self.lobby_title = tk.Label(self.lobby_frame, text="PLAYERS IN THE LOBBY")
        self.lobby_title.place(x=0, y=0)
        
        self.connection_status_label = tk.Label(self.lobby_frame, text=f"YOUR STATUS: {self.networking.status.capitalize()}")
        self.connection_status_label.place(x=0, y=self.height*0.1)

        self.players_frame = tk.Frame(self.lobby_frame)
        self.players_frame.place(x=0, y=self.height*0.5)

        self.player_radiobuttons = []

        #self.server_address = ('127.0.0.1', 65432)
        #self.server_address_label = tk.Label(self.lobby_frame, text=f"server details: {self.server_address}")
        #self.server_address_label.grid(column=0 ,row=4, columnspan=3)

        self.address = tk.StringVar()
        self.address_label = tk.Label(self.lobby_frame, text="Enter the IP Address of the Server: ")
        self.address_label.place(x=0, y=self.height*0.15)
        self.address_entry = tk.Entry(self.lobby_frame, textvariable=self.address)
        self.address_entry.insert(0, "127.0.0.1")
        self.address_entry.place(x=0, y=self.height*0.2)

        self.port = tk.IntVar()
        self.port_label = tk.Label(self.lobby_frame, text="Enter the Port Number of the Server: ")
        self.port_label.place(x=0, y=self.height*0.25)
        self.port_entry = tk.Entry(self.lobby_frame, textvariable=self.port)
        self.port_entry.insert(0, 65432)
        self.port_entry.place(x=0, y=self.height*0.3)
        
        self.lobby_count_label = tk.Label(self.lobby_frame, text=f"connect to server to see active players")

        self.connect_btn = tk.Button(self.lobby_frame, text="Connect to Server", command=self.connect_to_server)
        self.connect_btn.place(x=0, y=self.height*0.35)

        self.refresh_btn = tk.Button(self.lobby_frame, text="Refresh Lobby", command=self.refresh_lobby)
        self.refresh_btn.place(x=0, y=self.height*0.4)

        self.lobby_frame.place(x=0, y=0)

        self.check_opponent_thread = Thread(target = self.check_opponent)
        self.check_opponent_thread.start()
    
    def check_opponent(self):
        no_opponent = True
        while no_opponent:
            if self.networking.opponent:
                self.lobby_frame.destroy()
                MainGameLoop(self.user, self.networking)
                no_opponent = False
    
    def connect_to_server(self):
        """connect_to_server: gets the variable valyes for address and port, then validates them as string and integer values. A tuple is made containing their values, and this data is passed to the set_server_address() , before calling connect_to_server (from the networking object)"""
        address = self.address.get()
        port = self.port.get()
        try:
            address = str(address)
            port = int(port)
        except Exception as e:
            print("error converting types in connect_to_server method in lobby class", e)
            return
        server_address = (address, port)
        self.networking.set_server_address(server_address)
        self.networking.connect_to_server()
        self.networking.send(f"username: {self.user.username}")

    def refresh_lobby(self):
        """refresh_lobby: when the user presses the refresh button, this method is called."""
        self.networking.send(f"username: {self.user.username}")
        self.players = self.networking.players
        self.lobby_count_label.configure(text=f"number of available players: {len(self.players)}")
        self.lobby_count_label.place(x=0, y=self.height*0.45)

        for widget in self.players_frame.winfo_children():
            widget.destroy()
        
        self.player_radiobuttons = []

        for player in self.players:
            self.player_radiobuttons.append(tk.Radiobutton(self.players_frame, text=f"{player}", variable=player, command=lambda: self.prompt_user(player)))
        
        count = 0
        for widget in self.player_radiobuttons:
            widget.grid(column=0, row=count)
            count += 1

    def prompt_user(self, player):
        """prompt_user: A TkInter askquestion messagebox pops up and asks the user if they would like to start a battle with the opponent"""
        result = tk.messagebox.askquestion(f"Connect with {player}?", f"Would you like to attempt to connect with {player} and start?")
        if result == 'yes':
            self.networking.match_request(self.user.username, player)
        else:
            print(f"you choose not to connect with {player}")