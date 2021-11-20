from tkinter.constants import DISABLED, NE, NORMAL
from classes.config import Config
from classes.Networking import *
from tkinter import messagebox
import tkinter as tk

class Lobby():
    def __init__(self, user):
        self.user = user
        self.connectivity = Networking()

        self.lobby_frame = tk.Frame(Config.master)
        
        self.lobby_title = tk.Label(self.lobby_frame, text="Lobby")
        self.lobby_title.grid(column=0, row=0, sticky="ew")
        
        self.connection_status_label = tk.Label(self.lobby_frame, text=f"connection status: {self.connectivity.status}")
        self.connection_status_label.grid(column=0, row=1)

        self.address = tk.StringVar()
        self.address_label = tk.Label(self.lobby_frame, text="Enter server IP address: ")
        self.address_label.grid(column=0, row=2)
        self.address_entry = tk.Entry(self.lobby_frame, textvariable=self.address)
        self.address_entry.grid(column=1, row=2)

        self.port = tk.IntVar()
        self.port_label = tk.Label(self.lobby_frame, text="Enter server port number: ")
        self.port_label.grid(column=2,row=2)
        self.port_entry = tk.Entry(self.lobby_frame, textvariable=self.port)
        self.port_entry.grid(column=3, row=2)
        
        self.lobby_count_label = tk.Label(self.lobby_frame, text=f"connect to server to see active players")

        self.players_frame = tk.Frame(self.lobby_frame)
        self.players_frame.grid(column=0, row=7, columnspan=3)

        self.player_radiobuttons = []

        #self.server_address = ('127.0.0.1', 65432)
        #self.server_address_label = tk.Label(self.lobby_frame, text=f"server details: {self.server_address}")
        #self.server_address_label.grid(column=0 ,row=4, columnspan=3)

        self.connect_btn = tk.Button(self.lobby_frame, text="Connect to Server", command=self.connect_to_server)
        self.connect_btn.grid(column=0, row=5, columnspan=3)

        self.refresh_btn = tk.Button(self.lobby_frame, text="Refresh Lobby", command=self.refresh_lobby)
        self.refresh_btn.grid(column=0, row=6)

        self.lobby_frame.grid(column=0, row=0)
    
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
        self.connectivity.set_server_address(server_address)
        self.connectivity.connect_to_server()
        self.connectivity.send(f"username: {self.user.username}")

    def refresh_lobby(self):
        self.players = self.connectivity.players
        self.lobby_count_label.configure(text=f"number of available players: {len(self.players)}")
        self.lobby_count_label.grid(column=0, row=7)
        
        for player in self.players:
            self.player_radiobuttons.append(tk.Radiobutton(self.players_frame, text=f"{player}", variable=player, command=lambda: self.prompt_user(player)))
        
        count = 0
        for widget in self.player_radiobuttons:
            widget.grid(column=0, row=count)
            count += 1


    def prompt_user(self, player):
        result = tk.messagebox.askquestion(f"Connect with {player}?", f"Would you like to attempt to connect with {player} and start a match with them?")
        if result == 'yes':
            #do things
            print("doing things")
        else:
            pass