from os import error
from threading import Thread
import socket
import tkinter as tk
from classes.MainGameLoop import *

class Networking():
    def __init__(self, username) -> None:
        self.username = username
        self.header_length = 1024
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.status = "not connected"
        self.write_file = "received_data.txt"
        self.server_address = None
        self.players = set()
        self.opponent = ""
    
    def set_server_address(self, server_address):
        """set_server_address: sets the server address"""
        self.server_address = server_address

    def connect_to_server(self):
        """connect_to_server: connects the socket to the server, then creates and starts the listening thread."""
        print('connecting to %s port %s' % self.server_address)
        self.sock.connect(self.server_address)
        #self.listen_thread = Thread(target = self.listen, args=(self.sock,), daemon=True)
        self.listen_thread = Thread(target = self.listen, daemon=True)
        self.listen_thread.start()

    def listen(self):
        """receive: receives data from the server and writes it to file."""
        while True:
            try:
                data_header = self.sock.recv(self.header_length)
                data_length = int(float(data_header.decode('utf-8').strip()))
                data = self.sock.recv(data_length).decode('utf-8')
                
                if "username:" in data:
                    username = data[9:].strip()
                    print(username)
                    if (username != self.username) and (username not in self.players):
                        self.players.add(username)
                elif "request:" in data:
                    request = data[8:].strip()
                    sender, player = request.split(',')
                    if player == self.username:
                        self.request_pop_up(sender)
                elif "response:" in data:
                    response = data[9:].strip()
                    sender, username, status = response.split(',')
                    if username == self.username:
                        self.response_pop_up(sender, status)
                elif self.opponent in data:
                    with open("data/received_data.txt", "a") as f:
                        f.write(data + "\n")
            except Exception as e:
                print(e)
    
    def send(self, data):
        """send: sends data to the server with data supplied by the user."""
        try:
            data_header = f"{len(data):<{self.header_length}}".encode('utf-8')
            assert self.sock.send(data_header+data.encode('utf-8'))
        except Exception as e:
            print(f"Exception in send method of networking class: {e}")
    
    def match_request(self, sender, player):
        self.send(f"request: {sender},{player}")

    def request_pop_up(self, sender):
        answer = tk.messagebox.askyesno("Battle request", f"{sender.capitalize()} would like to start a battle with you. Accept?")
        if answer:
            print("you accepted the request")
            self.send(f"response: {self.username},{sender},accepted")
            tk.messagebox.showinfo("Match starting", f"Starting battle with {sender}!")
            self.opponent = sender
        else:
            self.send(f"response: {self.username},{sender},refused")
    
    def response_pop_up(self, sender, status):
        if status == "accepted":
            tk.messagebox.showinfo("Request accepted", f"{sender.capitalize()} accepted your battle request!")
            tk.messagebox.showinfo("Match starting", f"Starting battle with {sender}!")
            self.opponent = sender
        elif status == "refused":
            tk.messagebox.showinfo("Request refused", f"{sender.capitalize()} refused your battle request.")