from os import error
import socket
import threading
import tkinter as tk
from threading import Thread
from tkinter.constants import E
import select

from classes.config import Config

global HEADER_LENGTH
HEADER_LENGTH = 1024

def initiate_server():
    print("started server")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ('127.0.0.1', 65432)

    server.bind(server_address)
    server.listen(4)

    print('connecting to %s port %s', server_address)

    inputs = [server]
    
    outputs = []
    data_dict = {}
    data_count = 0

    while True:

        readable, writable, exceptional = select.select(inputs, outputs, inputs)
        for s in readable:

            if s is server:
                connection, address = s.accept()
                print(f"new connection from {address}")
                connection.setblocking(0) #maybe change to 1
                inputs.append(connection)
            else:
                data_header = s.recv(HEADER_LENGTH)

                if not data_header:
                    continue

                data_length = int(data_header.decode('utf-8').strip())
                data = s.recv(data_length)
                print(f"received {data.decode('utf-8')} from {s.getpeername()}")
                data_count += 1
                data_dict[data_count] = {"data": data.decode('utf-8')}
                
                if s not in outputs:
                    outputs.append(s)
 
        for s in writable:
            try:
                for key in data_dict:
                    data = data_dict[key].get("data")
                    #temp = s.getpeername()
                    #data = f"{temp[0]} , {temp[1]} , {data}"
                    data = data.encode('utf-8')
                    data_header = f"{len(data):<{HEADER_LENGTH}}".encode('utf-8')
                    assert s.send(data_header+data)
            except Exception as e:
                print(e)
        
        data_dict = {}
        data_count = 0

initiate_server()

class Server():
    def __init__(self):
        Config.master = tk.Tk()
        width = Config.master.winfo_screenwidth() * 0.75
        height = Config.master.winfo_screenheight() * 0.75
        Config.master.geometry("%dx%d" % (width, height))
        Config.master.title("SERVER")
        self.lobby_frame = tk.Frame(Config.master)
        self.lobby_title = tk.Label(self.lobby_frame, text="LOBBY")
        self.lobby_title.grid(column=0, row=0, sticky="ew")
        self.lobby_count = 0
        self.players_in_lobby_label = tk.Label(self.lobby_frame, text=f"players in lobby: {self.lobby_count}")
        self.players_in_lobby_label.grid(column=0, row=2)
        self.player_names = []
        self.player_frame = tk.Label(self.lobby_frame)
        self.player_frame.grid(column=0, row=3, sticky="ew")
        self.server_address = ('127.0.0.1', 65432)
        self.server_address_label = tk.Label(self.lobby_frame, text=f"server details: {self.server_address}")
        self.server_address_label.grid(column=0 ,row=4, columnspan=3)
        self.start = tk.Button(self.lobby_frame, text="Start Server", command=initiate_server)
        self.start.grid(column=0, row=5, columnspan=3)
        self.lobby_frame.grid(column=0, row=0)
        Config.master.mainloop()

#server = Server()