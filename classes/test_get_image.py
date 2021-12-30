import tkinter as tk

def hello1(string):
    print(string)

master = tk.Tk()
width = int(master.winfo_screenwidth() * 0.75)
height = int(master.winfo_screenheight() * 0.75)
master.geometry(f"{width}x{height}")
master.title("TCG REMAKE")
button1=tk.Button(master, text="hello")
button2=tk.Button(master, text="hello2")
buttons = [button1, button2]
for btn in buttons:
    print(buttons.index(btn))
    if buttons.index(btn) == 0:
        btn.bind("<Enter>", lambda event: hello1("hello 0"))
        btn.bind("<Leave>", lambda event: hello1("goodbye 0"))
    btn.bind("<Enter>", lambda event: hello1("hello 1"))
    btn.bind("<Leave>", lambda event: hello1("goodbye 1"))
    btn.grid()
# master.update()
master.mainloop()