import tkinter as tk
from tkinter.constants import DISABLED, NORMAL
from classes.config import Config
import socket
from threading import Thread

class Lobby():
    def __init__(self):
        self.lobby_frame = tk.Frame(Config.master)
        self.lobby_title = tk.Label(self.lobby_frame, text="LOBBY")
        self.lobby_title.grid(column=0, row=0, sticky="ew")
        self.connection_status = "not connected"
        self.connection_status_label = tk.Label(self.lobby_frame, text=f"status: {self.connection_status}")
        self.connection_status_label.grid(column=0, row=1)
        self.lobby_count = 0
        self.players_in_lobby_label = tk.Label(self.lobby_frame, text=f"players in lobby: {self.lobby_count}")
        self.players_in_lobby_label.grid(column=0, row=2)
        #self.lobby_count_label = tk.Label(self.lobby_frame, text=str(self.lobby_count))
        #self.lobby_count_label.grid(column=1, row=2)
        self.player_names = []
        self.player_frame = tk.Label(self.lobby_frame)
        self.player_frame.grid(column=0, row=3, sticky="ew")
        self.server_address = ('127.0.0.1', 65432)
        self.server_address_label = tk.Label(self.lobby_frame, text=f"server details: {self.server_address}")
        self.server_address_label.grid(column=0 ,row=4, columnspan=3)
        self.connect_btn = tk.Button(self.lobby_frame, text="Connect to Server", command=self.connect_to_server)
        self.connect_btn.grid(column=0, row=5, columnspan=3)
        self.lobby_frame.grid(column=0, row=0)
        self.data = []
    
    def create_thread(self):
        self.lobby_thread = Thread(target=self.connect_to_server, daemon=True)
        self.connect_btn.configure(text="lolololo")
        self.connect_btn.grid(column=0, row=5, columnspan=3)
        self.lobby_frame.grid(column=0, row=0)


    def connect_to_server(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('connecting to %s port %s' % self.server_address)
        try:
            sock.connect(self.server_address)
        except Exception as e:
            print(e)
        while True:
            try:
                message = sock.recv(1024).decode()
                if len(message)>1:
                    self.data.append(message)
                    for x in self.data:
                        print(x)
            except Exception as e:
                print(e)   
