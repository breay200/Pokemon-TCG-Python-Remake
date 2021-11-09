from os import error
import socket
import tkinter as tk
from threading import Thread

def connect():
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
            message = sock.recv(1024).decode()
            if len(message)>1:
                print(message)
                sock.close()
                print("closed socket")
                break
        except error:
            print(error)

thread = Thread(target = connect, daemon=True)
    

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

connect_btn = tk.Button(main_frame, text="Connect", command=lambda: thread.start(), width=25)
connect_btn.grid(column=0, row=2)

quit_btn = tk.Button(main_frame, text="Quit", command=lambda: quit(), width=25)
quit_btn.grid(column=1, row=2)

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
