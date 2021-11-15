from os import error
import socket
import tkinter as tk
from threading import Thread, stack_size
global HEADER_LENGTH

def receive():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #server_address = (ip.get(), int(port.get()))
    server_address = ('127.0.0.1', 65432)
    print('connecting to %s port %s' % server_address)
    while True:
        try:
            sock.connect(server_address)
            data = sock.recv(1024)
            data = data.decode('utf-8')

            #header = sock.recv(1024)
            #data_length = int(float(header.decode('utf-8').strip()))
            #data = sock.recv(data_length).decode('utf-8')
            if data:
                print("data received: ", data)
                with open("rps.txt", "w") as file1:
                    file1.write("data")
            else:
                print("no data")

            sock.close()
        except Exception as e:
            print(e)

def send(data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #server_address = (ip.get(), int(port.get()))
    server_address = ('127.0.0.1', 65432)

    print('connecting to %s port %s' % server_address)

    try:
        sock.connect(server_address)
        data = data.encode('utf-8')
        #header = f"{len(data):<{1024}}".encode('utf-8')
        #sock.send(header+data)
        sock.send(data)
    except Exception as e:
        print(e)

def rock_paper_scissors():
    def widget_send(data):
        send(data)
    receiving.start()
    for widget in main_frame.winfo_children():
        widget.destroy()
    rock_btn = tk.Button(main_frame, text="rock", command=lambda: widget_send("rock"))
    rock_btn.grid(column=1,row=1)
    paper_btn = tk.Button(main_frame, text="paper", command=lambda: widget_send("paper"))
    paper_btn.grid(column=2, row=1)
    scissor_btn = tk.Button(main_frame, text="scissors", command=lambda: widget_send("scissors"))
    scissor_btn.grid(column=3, row=1)



def encodeAndSend(data, sock):
    data = data.encode('utf-8')
    header = f"{len(data):<{1024}}".encode('utf-8')
    print(header)
    sock.send(header+data)

def decodeData(sock):
    header = sock.recv(1024)
    print(header)
    data_length = int(float(header.decode('utf-8').strip()))
    data = sock.recv(data_length).decode('utf-8')
    print(data)


receiving = Thread(target = receive, daemon=True)
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

send_btn = tk.Button(main_frame, text="Send", command=lambda: rock_paper_scissors(), width=25)
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
