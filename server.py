from os import error
import socket
import threading
import tkinter as tk
from threading import Thread

HOST = '127.0.0.1' #socket.gethostname()
PORT = 65432
header_len = 10

def initiate_server():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(HOST, PORT)
    #server_address = (ip.get(), int(port.get()))
    #print('connecting to %s port %s' % server_address)
    sock.bind((HOST, PORT))
    sock.listen(3)
    while True:
        clientsocket, address = sock.accept()
        clientsocket.send(f"{address} connected to {HOST}".encode())
        try:
            data = dataReceived(clientsocket)
            print(data.decode('utf-8'))
            if data:
                clientsocket.send(data['header'] + data['data'])
        except Exception as e:
            print(e)

def dataReceived(client_socket):
    try:
        data_header = client_socket.recv(header_len)

        if not len(data_header):
            return False
        
        data_length = int(data_header.decode('utf-8').strip())
        #returns a dict
        return {"header" : data_header, "data" : client_socket.recv(data_length)}
    except:
        print("false")
        return False


thread = Thread(target = initiate_server, daemon=True)    

print("Running Server")
master = tk.Tk()
master.geometry('400x200')
master.title("Server Test")

main_frame = tk.Frame(master)

ip_label = tk.Label(main_frame, text="Server IP Address: ")
ip_label.grid(column=0,row=0)

ip = tk.StringVar()

ip_entry = tk.Entry(main_frame, textvariable=ip)
ip_entry.grid(column=1,row=0, columnspan=2, sticky="ew")

port_label = tk.Label(main_frame, text="Server Port: ")
port_label.grid(column=0,row=1)

port = tk.StringVar()

port_entry = tk.Entry(main_frame, textvariable=port)
port_entry.grid(column=1, row=1, columnspan=2, sticky="ew")

connect_btn = tk.Button(main_frame, text="Start Server", command=lambda: thread.start(), width=25)
connect_btn.grid(column=0, row=2)

quit_btn = tk.Button(main_frame, text="Quit", command=lambda: quit(), width=25)
quit_btn.grid(column=1, row=2)

main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(1, weight=1)
main_frame.grid(column=0, row=0)

master.mainloop()