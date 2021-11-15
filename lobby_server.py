from os import error
import socket
import threading
import tkinter as tk
from threading import Thread
from tkinter.constants import E
import select
import queue
global data_dict
data_dict = {}


header_len = 1024

def dataReceived(client_socket):
    count = 0
    trueVar = True
    while trueVar:
        if count < 50:
            try:
                data_header = client_socket.recv(1024)
                data_length = int(data_header.decode('utf-8').strip())
                if data_header and data_length:
                    data = client_socket.recv(data_length)
                    return {"header" : data_header, "data" : data}
                else:
                    count +=1
            except Exception as e:
                print(e)
        else:
            trueVar = False
    return {}


def send_to_client(clients):
    print("clients", clients)
    for x in clients:
        try:
            print("before datareceived")
            data = dataReceived(x)  
            print("after datareceived")

            if not data:
                x.close()
                del clients[x]
                continue

            print(f"Received data: {data['data'].decode('utf-8')}")
            x.send(data['header'] + data['data'])

            x.close()
            del clients[x]
        except Exception as e:
            print(e)



def initiate_server():
    print("started server")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ('127.0.0.1', 65432)

    server.bind(('127.0.0.1', 65432))
    server.listen(4)

    print('connecting to %s port %s', server_address)

    # Sockets from which we expect to read
    inputs = [server]
    
    # Sockets to which we expect to write
    outputs = []

    # Outgoing message queues (socket:Queue)
    data_queue = {}

    while True:
        # Wait for at least one of the sockets to be ready for processing
        readable, writable, exceptional = select.select(inputs, outputs, inputs)
        for s in readable:
            #print(s)
            #print(len(readable))
            if s is server:
                connection, address = s.accept()
                print(f"new connection from {address}")
                connection.setblocking(1) #maybe change to 1
                inputs.append(connection)
                data_queue[connection] = queue.Queue()
            else:
                data = s.recv(1024)
                if data:
                    print(f"received {data.decode('utf-8')} from {s.getpeername()}")
                    data_queue[s].put(data)
                    #name = str(hash(s))
                    #print("connection hash: ", name)
                    #data_dict.update({name:data})
                    #print("data dict in readable", data_dict.get(name))
                    # Add output channel for response
                    if s not in outputs:
                        outputs.append(s)
                else:
                    # Interpret empty result as closed connection
                    print(f"closing {address} after reading no data")
                    # Stop listening for input on the connection
                    if s in outputs:
                        outputs.remove(s)
                    inputs.remove(s)
                    s.close()
                    #del data_queue[s]
                    #name = str(hash(s))
                    #del data_dict[name]
        
        for s in writable:
            #print("type of s: ", type(s))
            #name = str(hash(s))
            #if data_dict[name]:
            #    print("key exisits")
            print("DATA QUEUE", data_queue[s].get())
            try:
                next_msg = data_queue[s].get_nowait()
                #print(len(data_dict.keys()))
                #for key, value in data_dict:
                #    print("heyyyyyy")
                #    print(key, value)
                
                #name = str(hash(s))
                #temp = data_dict.get(name)
                #print("data in writable: ", temp)
            except queue.Empty:
                # No messages waiting so stop checking for writability.
                print(f'output queue for {s.getpeername()} is empty')
                #print(e)
                outputs.remove(s)
            except Exception as e:
                print(e)
            else:
                print(f'sending {next_msg} to {s.getpeername()}')
                s.send(next_msg)
            
            #if temp:
            #    print("sending message")
                #temp = temp.encode('utf-8')
            #    assert s.send(temp)
            #else: # Could use the len(data) and send the header, etc
                #print(f'sending {next_msg} to {s.getpeername()}')
            #    print("something went wrong")


        for s in exceptional:
            print(f'handling exceptional condition for {s.getpeername()}')
            # Stop listening for input on the connection
            inputs.remove(s)
            
            if s in outputs:
                outputs.remove(s)

            s.close()
            #del data_queue[s]
           # name = hash(s)
            #del data_dict[name]





            #clients.add(clientsocket)
            #if clients:
            #    print("we have a client")
            #    send_to_client(clients)
            #else:
            #    print("no clients :(")
        #except Exception as e:
        #    print(e)


#thread = Thread(target = initiate_server, daemon=True)    
#thread.start()
initiate_server()
"""
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

connect_btn = tk.Button(main_frame, text="Start Server", command=initiate_server, width=25)
connect_btn.grid(column=0, row=2)

quit_btn = tk.Button(main_frame, text="Quit", command=lambda: quit(), width=25)
quit_btn.grid(column=1, row=2)

main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(1, weight=1)
main_frame.grid(column=0, row=0)

master.mainloop()
"""