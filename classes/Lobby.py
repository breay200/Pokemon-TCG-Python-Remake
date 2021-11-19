from tkinter.constants import DISABLED, NE, NORMAL
from classes.config import Config
from classes.Networking import *
import tkinter as tk

class Lobby():
    def __init__(self):
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
        
        self.lobby_count = 0
        self.lobby_count_label = tk.Label(self.lobby_frame, text=f"number of available players: {self.lobby_count}")
        #self.players_in_lobby_label.grid(column=0, row=2)

        self.player_frame = tk.Label(self.lobby_frame)
        self.player_frame.grid(column=0, row=3, sticky="ew")

        #self.server_address = ('127.0.0.1', 65432)
        #self.server_address_label = tk.Label(self.lobby_frame, text=f"server details: {self.server_address}")
        #self.server_address_label.grid(column=0 ,row=4, columnspan=3)

        self.connect_btn = tk.Button(self.lobby_frame, text="Connect to Server", command=self.connect_to_server)
        self.connect_btn.grid(column=0, row=5, columnspan=3)

        self.lobby_frame.grid(column=0, row=0)
    
    def connect_to_server(self):
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

