from os import error
from threading import Thread
import socket

class Networking():
    def __init__(self) -> None:
        self.header_length = 1024
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.status = "not connected"
        self.write_file = "received_data.txt"
        self.server_address = None
        self.players = set()
    
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
                    print("username: ", username)
                    if username not in self.players:
                        self.players.add(username)
                elif 'user2' in data:
                    print("received data from user 2", data)
                    with open("received_data.txt", "a") as file1:
                        file1.write(data + "\n")
                        #no_data = False
                elif 'user1' in data:
                    #print("this is my sent data")
                    pass
            except Exception as e:
                print(e)
    
    def send(self, data):
        """send: sends data to the server with data supplied by the user."""
        try:
            data_header = f"{len(data):<{self.header_length}}".encode('utf-8')
            assert self.sock.send(data_header+data.encode('utf-8'))
        except Exception as e:
            print(f"Exception in send method of networking class: {e}")
