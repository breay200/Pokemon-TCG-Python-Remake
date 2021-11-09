from os import error
import socket
import tkinter as tk
from threading import Thread
global HEADER_LENGTH
HEADER_LENGTH = 1024


def recv():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip.get(), int(port.get()))
    print('connecting to %s port %s' % server_address)
    try:
        sock.connect(server_address)
    except error:
        print(error)
    while True:
        try:
            header = sock.recv(HEADER_LENGTH)
            print(header)
            data_length = int(float(header.decode('utf-8').strip()))
            data = sock.recv(data_length).decode('utf-8')
            print(data)
            if len(data)>1:
                sock.close
            """message = sock.recv(1024).decode()
            if len(message)>1:
                print(message)
                sock.close()
                print("closed socket")
                break"""
        except Exception as e:
            print(e)

def send():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip.get(), int(port.get()))
    print('connecting to %s port %s' % server_address)
    try:
        sock.connect(server_address)
    except error:
        print(error)
    try:
        data = "username: Brandon"
        data = data.encode('utf-8')
        header = f"{len(data):<{HEADER_LENGTH}}".encode('utf-8')
        sock.send(header+data)
        sock.close
        """message = sock.recv(1024).decode()
        if len(message)>1:
            print(message)
            sock.close()
            print("closed socket")
            break"""
    except Exception as e:
        print(e)


def encodeAndSend(data, sock):
    data = data.encode('utf-8')
    header = f"{len(data):<{HEADER_LENGTH}}".encode('utf-8')
    print(header)
    sock.send(header+data)

def decodeData(sock):
    header = sock.recv(HEADER_LENGTH)
    print(header)
    data_length = int(float(header.decode('utf-8').strip()))
    data = sock.recv(data_length).decode('utf-8')
    print(data)


receiving = Thread(target = recv, daemon=True)
sending = Thread(target = send, daemon= True)

print("Client Test")
master = tk.Tk()
master.geometry('400x200')
master.title("Client Test")

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

connect_btn = tk.Button(main_frame, text="Receive", command=lambda: receiving.start(), width=25)
connect_btn.grid(column=0, row=2)

send_btn = tk.Button(main_frame, text="Send", command=lambda: send(), width=25)
send_btn.grid(column=1, row=2)

quit_btn = tk.Button(main_frame, text="Quit", command=lambda: quit(), width=25)
quit_btn.grid(column=2, row=2)

main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(1, weight=1)
main_frame.grid(column=0, row=0)

master.mainloop()

# create an INET, STREAMing socket
#serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
#serversocket.bind((HOST, PORT))
# become a server socket
# 5 dictates how many hosts can conenct before refusing any more
#serversocket.listen(5)

#while True:
    # accept connections from outside
#    (clientsocket, address) = serversocket.accept()
    # now do something with the clientsocket
    # in this case, we'll pretend this is a threaded server
#    ct = client_thread(clientsocket)
#    ct.run(

"""with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)"""
